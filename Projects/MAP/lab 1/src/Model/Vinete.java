package Model;

public class Vinete implements Objects{
    public Float kg;

    public Vinete(Float k){this.kg=k;}

    @Override
    public Float getKg(){
        return this.kg;
    }
    public void setKg(Float k){
        this.kg=k;
    }
    public String toString(){
        String s=new String();
        s+="Vanata cu greutatea de "+Float.toString(kg)+" kg. ";
        return s;
    }
}
