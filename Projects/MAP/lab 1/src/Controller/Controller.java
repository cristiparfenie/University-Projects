package Controller;
import Repository.*;
import Model.*;

public interface Controller {
    Repository getRepo();
    Boolean addRepo(Objects e);
    Boolean removeRepo(Integer pos);
    Repository getByKg() throws Exception;
}
