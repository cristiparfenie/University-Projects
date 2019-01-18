package Repository;

import Model.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepo {
    void addPrg(ProgramState prg);
    void logPrgStateExec(ProgramState state) throws IOException;
    List<ProgramState> getPrgList();
    void setPrgList(List<ProgramState> list);
}