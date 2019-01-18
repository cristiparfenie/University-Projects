package Repository;

import Model.ProgramState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepo {
    private List<ProgramState> listPrg = new ArrayList<>();
    private int current = 0;


    @Override
    public List<ProgramState> getPrgList(){return listPrg;}
    public void setPrgList(List<ProgramState> list){this.listPrg=list;}
    public void addPrg(ProgramState prg) {
        listPrg.add(prg);}

    public String toString(){
        StringBuilder sb = new StringBuilder();

        for (ProgramState state : listPrg){
            sb.append(state).append("\n");
        }
        return sb.toString();
    }

    public void logPrgStateExec(ProgramState state)throws IOException{
        String logFilePath="log";
        PrintWriter logFile =  new PrintWriter(new BufferedWriter(new FileWriter(logFilePath,true)));
        logFile.println(state.toString());
        logFile.println("________________________");
        logFile.close();
    }
}



