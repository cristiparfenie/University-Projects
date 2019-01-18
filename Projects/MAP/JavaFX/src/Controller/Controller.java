package Controller;

import Model.ProgramState;
import Model.Statements.IStmt;
import Model.Utilities.IStack;
import Repository.IRepo;
import Exception.EmptyStack;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    private IRepo repo;
    private ExecutorService executor;

    public Controller(IRepo repo) {
        this.repo = repo;
    }

    public void setExecutor(ExecutorService e){executor=e;}
    public void setPrgList(List<ProgramState> l){repo.setPrgList(l);}

    public ProgramState oneStep(ProgramState state){
        try {
            IStack<IStmt> stack = state.getStack();
            if (stack.isEmpty())
                throw new EmptyStack("The stack is empty!");
            IStmt currentStmt = stack.pop();
            return currentStmt.execute(state);
        }
        catch (IOException e){
            System.out.println((e.getMessage()));
            System.exit(0);
        }
        return null;
    }

    public ProgramState getByID(List<ProgramState> prgList,Integer id){
        for(ProgramState p:prgList){
            if(p.getID()==id)
                return p;
        }
        return null;
    }

    public Integer addProc(List<ProgramState> inPrgList,Integer sum){
        inPrgList.stream()
                .filter(p -> !p.isNotCompleted())
                .collect(Collectors.toList());
        sum+=inPrgList.size();
        return sum;
    }

    public void ExecutorShutdown(){executor.shutdownNow();}

    public void oneStepForAllPrg(List<ProgramState> prgList){
        try{

            List<Callable<ProgramState>> callList = prgList.stream()
                    .map((ProgramState p) -> (Callable<ProgramState>)(() -> {return p.oneStep();}))
                    .collect(Collectors.toList());
            List<ProgramState> newPrgList = executor.invokeAll(callList). stream()
                    . map(future -> { try { return future.get();} catch(Exception e) { System.out.println(e.getMessage()); return null;}})
                    .filter(p -> p!=null).collect(Collectors.toList());
            prgList.addAll(newPrgList);
            prgList.forEach(prg ->{try{repo.logPrgStateExec(prg);}catch(IOException e){System.out.println(e.getMessage());}});
            repo.setPrgList(prgList);
        }
        catch(Exception e){System.out.println(e.getMessage());}
    }

    public void allStep() {
        executor = Executors.newFixedThreadPool(2);
        List<ProgramState> prgList=removeCompletedPrg(repo.getPrgList());
        while(prgList.size() > 0){
            prgList.stream().forEach(e->e.setHeapMap(conservativeGarbageCollector(e.getSymTable().getValues(),e.getHeap().getMap())));
            oneStepForAllPrg(prgList);
            prgList.stream().forEach(e->{System.out.println("--------------------");System.out.println(e);});
            prgList=removeCompletedPrg(repo.getPrgList());
        }
        executor.shutdownNow();
        List<ProgramState> temp=repo.getPrgList();
        temp.stream().forEach(e->{CloseAllOpenFiles(e);System.out.println("--------------------");System.out.println(e);
            try{repo.logPrgStateExec(e);}catch(IOException ex){System.out.println(ex.getMessage());}});
        repo.setPrgList(prgList);
    }

    public List<ProgramState> removeCompletedPrg(List<ProgramState> inPrgList){
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public Map<Integer,Integer> conservativeGarbageCollector(List<Integer> symTableValues,
                                                             Map<Integer,Integer> heap){
        return heap.entrySet().stream()
                .filter(e->symTableValues.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));}


    public ProgramState CloseAllOpenFiles(ProgramState prog){
        prog.clearFileFromSym();
        List<BufferedReader> myList=prog.getFileTable().getValues();
        myList.stream().forEach(el->{try{el.close();}catch (IOException e){System.out.println(e.getMessage());}});
        prog.clearFileFromSym();
        return prog;
    }

    @Override
    public String toString(){
        return "Controller: " + repo.toString();
    }
}
