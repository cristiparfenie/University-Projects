package Model.Expressions;

import Model.Utilities.IDictionary;

import Exception.InvalidOperator;

public class BooleanExpr implements IExpr {
    private IExpr l, r;
    private String o;

    public BooleanExpr(IExpr le, IExpr ra, String op){
        l=le;
        r=ra;
        o=op;
    }

    @Override
    public int evaluate(IDictionary<String, Integer> dic, IDictionary<Integer,Integer>heap){
        int left = this.l.evaluate(dic,heap);
        int right = this.r.evaluate(dic,heap);

        switch (o){
            case("<"):
                if(left<right)
                    return 1;
                else
                    return 0;

            case("<="):
                if(left<=right)
                    return 1;
                else
                    return 0;

            case("=="):
                if(left==right)
                    return 1;
                else
                    return 0;

            case("!="):
                if(left!=right)
                    return 1;
                else
                    return 0;

            case(">"):
                if(left>right)
                    return 1;
                else
                    return 0;

            case(">="):
                if(left>=right)
                    return 1;
                else
                    return 0;

        }
        throw new InvalidOperator("Error! Invalid Operator!");
    }
}
