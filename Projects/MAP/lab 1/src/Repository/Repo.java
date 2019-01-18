package Repository;

import Model.*;

public class Repo implements Repository{
    Objects elems[];
    Integer len;
    Integer cap;

    public Integer getLen(){return len;}
    public Integer getCap(){return cap;}
    public Repo(Integer c){
        cap=c;
        len=0;
        elems=new Objects[cap];
    }
    @Override
    public Objects get(Integer pos){return elems[pos];}
    public void add(Objects e){
        try{elems[len]=e;
            len++;}
        catch (Exception ex){
            this.resize();
            this.add(e);
        }

    }
    public void remove(Integer pos){
        for(Integer i=pos;i<len-1;i++){
            elems[i]=elems[i+1];
        }
        len--;
    }
    public Repository getByKg(){
        Repository r=new Repo(cap);
        for(Integer i=0;i<len;i++){
            if(elems[i].getKg()>0.2){
                r.add(elems[i]);
            }
        }
        return r;
    }

    public void resize(){
        Objects s[]=new Objects[cap*2];
        for(Integer i=0;i<this.len;i++)
        {
            s[i]=elems[i];
        }
        this.elems=new Objects[cap*2];
        elems=s;
        cap=cap*2;
    }
}

