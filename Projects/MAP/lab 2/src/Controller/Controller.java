package Controller;

import Model.ProgramState;
import Model.Statements.IStmt;
import Model.Utilities.IStack;
import Repository.IRepo;
import Exception.EmptyStack;

import java.io.File;
import java.io.IOException;

public class Controller {
    private IRepo repo;

    public Controller(IRepo repo) {
        this.repo = repo;
    }

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

    public void allSteps(){
        ProgramState prg = repo.getCurrentPrg();
        File f = new File("D:\\FACULTATE\\MAP\\lab 3\\log");
        if(f.exists()){
            f.delete();
            try {
                f.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        try {
            while (!prg.getStack().isEmpty()) {
                oneStep(prg);
                repo.logPrgStateExec("D:\\FACULTATE\\MAP\\lab 3\\log");
                System.out.println("______________________");
                System.out.println(prg);
            }
        }
        catch(IOException e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public String toString(){
        return "Controller: " + repo.toString();
    }
}
