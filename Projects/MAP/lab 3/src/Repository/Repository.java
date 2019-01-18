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
    public void addPrg(ProgramState prg) {
        listPrg.add(prg);
    }
    public ProgramState getCurrentPrg() {
        return listPrg.get(current);
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();

        for (ProgramState state : listPrg){
            sb.append(state).append("\n");
        }
        return sb.toString();
    }

    public void logPrgStateExec(String logFilePath)throws IOException{
        PrintWriter logFile =  new PrintWriter(new BufferedWriter(new FileWriter(logFilePath,true)));
        logFile.println(this.getCurrentPrg().toString());
        logFile.println("________________________");
        logFile.close();
    }
}



