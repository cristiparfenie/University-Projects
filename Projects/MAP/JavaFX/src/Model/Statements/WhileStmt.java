package Model.Statements;

import Model.Expressions.IExpr;
import Model.ProgramState;
import Model.Utilities.IDictionary;
import Model.Utilities.IStack;

import java.io.IOException;
import java.time.chrono.IsoChronology;

public class WhileStmt implements IStmt{
    private IExpr expr;
    private IStmt stmt;

    public WhileStmt(IExpr e, IStmt s){
        expr=e;
        stmt=s;
    }

    @Override
    public ProgramState execute (ProgramState state)throws IOException {
        IDictionary<String,Integer> dic=state.getSymTable();
        IDictionary<Integer,Integer> heap=state.getHeap();
        IStack<IStmt> stack=state.getStack();

        if(expr.evaluate(dic,heap)!=0){
            stack.add(this);
            stack.add(stmt);
        }
        return null;
    }


    public String toString(){ return "while("+expr+") "+stmt; }
}
