package Controller;

import Model.*;
import Repository.*;

public class Contro implements Controller{
    Repository repo;
    public Contro(Repository r){
        repo=r;
    }
    @Override
    public Boolean addRepo(Objects e){
        try{
            repo.add(e);
        }catch(Exception a){
            return false;
        }
        return true;
    }
    public Boolean removeRepo(Integer pos){
        try{
            repo.remove(pos);
        }catch(Exception e){
            return false;
        }
        return true;
    }
    public Repository getRepo(){return repo;}
    public Repository getByKg() throws Exception{
        Repository r=repo.getByKg();
        if(repo.getLen()==0)
            throw new Exception("The Repository is empty! ");
        return r;
    }
}
