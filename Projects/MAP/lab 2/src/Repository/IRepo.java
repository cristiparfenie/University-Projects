package Repository;

import Model.ProgramState;

import java.io.IOException;

public interface IRepo {
    void addPrg(ProgramState prg);
    ProgramState getCurrentPrg();
    void logPrgStateExec(String LogFilePath) throws IOException;
}