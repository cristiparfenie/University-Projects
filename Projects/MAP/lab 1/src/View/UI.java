package View;
import Controller.*;
import Model.*;
import Repository.*;

public class UI {
    Controller contro;
    Repository r;
    public UI(){contro=new Contro(r=new Repo(100));}

    public void printRepo(Repository r){
     for(int i=0;i<r.getLen();i++){
         System.out.print(r.get(i).toString()+'\n');
     }
    }

    public void start(){
            Objects o1=new Rosii(20.f);
            Objects o2=new Vinete(30.f);
            Objects o3=new Ardei((float)0.1);
            Objects o4=new Rosii((float)0.3);
            Objects o5=new Vinete(400.f);
            Objects o6=new Ardei((float)0.01);

            contro.addRepo(o1);
            contro.addRepo(o2);
            contro.addRepo(o3);
            contro.addRepo(o4);
            contro.addRepo(o5);
            contro.addRepo(o6);

            this.printRepo(contro.getRepo());


            System.out.println();
            System.out.print("The new repository: ");
            System.out.println();

            //contro.removeRepo(2);
            //contro.removeRepo(0);

            try{this.printRepo(contro.getByKg());}
            catch (Exception ex){
                System.out.print(ex.getMessage());
            }

    }
}
