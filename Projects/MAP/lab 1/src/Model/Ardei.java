package Model;

public class Ardei implements Objects{
    public Float kg;

    public Ardei(Float k){this.kg=k;}

    @Override
    public Float getKg(){
        return this.kg;
    }
    public void setKg(Float k){
        this.kg=k;
    }
    public String toString() {
        String s=new String();
        s+="Ardei cu greutatea de "+Float.toString(kg)+" kg.";
        return s;
    }
}
