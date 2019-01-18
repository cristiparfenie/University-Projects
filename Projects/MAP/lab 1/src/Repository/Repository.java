package Repository;
import Model.*;

public interface Repository {
    Objects get(Integer pos);
    void add(Objects e);
    void remove(Integer pos);
    void resize();
    Repository getByKg();
    public Integer getLen();
    public Integer getCap();
}
