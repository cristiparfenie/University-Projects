package Model;


public class Rosii implements Objects{
    public Float kg;

    public Rosii(Float k){this.kg=k;}
    @Override
    public Float getKg(){
        return this.kg;
    }
    public void setKg(Float k){
        this.kg=k;
    }
    public String toString(){
        String s=new String();
        s+="Rosie cu greutatea de " + Float.toString(kg)+" kg. ";
        return s;
    }
}
