package Model.Expressions;

import Model.Utilities.IDictionary;
import Exception.*;

public class ArithmExpr implements IExpr {

    private IExpr left, right;
    private String operator;

    public ArithmExpr(String op, IExpr l, IExpr r){
        operator = op;
        left = l;
        right = r;
    }

    @Override
    public int evaluate(IDictionary<String, Integer> dic) {
        int left = this.left.evaluate(dic);
        int right = this.right.evaluate(dic);

        switch (operator){
            case "+":
                return left + right;
            case "-":
                return left - right;
            case "*":
                return left * right;
            case "/":
                if(right == 0)
                        throw new DivisionByZero("Division by 0 ERROR!");
                return left/right;
        }
        throw new InvalidOperator("Invalid operator ERROR!");
    }

    public String toString(){
        return "" + left + operator + right;
    }
}
