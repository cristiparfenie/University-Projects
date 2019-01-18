package Model;

import Model.Utilities.*;
import  Model.Statements.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.Map;

public class ProgramState {
    private IStack<IStmt> stack;
    private IDictionary<String, Integer> SymTable;
    private IList<Integer> list;
    private IDictionary<Integer, BufferedReader> FileTable;
    private IDictionary<Integer, Integer> heap;


    public ProgramState(IStack<IStmt> stack, IDictionary<String, Integer> symTable, IList<Integer> list,IDictionary<Integer,BufferedReader> ft, IDictionary<Integer, Integer>h) {
        this.stack = stack;
        this.SymTable = symTable;
        this.list = list;
        this.FileTable=ft;
        this.heap=h;
    }

    public IStack<IStmt> getStack() {
        return stack;
    }

    public void setStack(IStack<IStmt> stack) {
        this.stack = stack;
    }

    public IDictionary<String, Integer> getSymTable() {
        return SymTable;
    }

    public void setSymTable(IDictionary<String, Integer> symTable) {
        SymTable = symTable;
    }

    public IDictionary<Integer, BufferedReader> getFileTable() {
        return FileTable;
    }

    public void setFileTable(IDictionary<Integer, BufferedReader> FileTable) {
        this.FileTable = FileTable;
    }

    public void setHeapMap(Map<Integer, Integer> h) {
        this.heap.setMap(h);
    }

    public IDictionary<Integer, Integer> getHeap() {
        return heap;
    }

    public void setHeap(IDictionary<Integer, Integer> heap) {
        this.heap = heap;
    }

    public IList<Integer> getList() {
        return list;
    }

    public void setList(IList<Integer> list) {
        this.list = list;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("\nExeStack:\n");
        for(IStmt s : stack.getElements()) {
            sb.append(s.toString()).append("\n");
        }

        sb.append("\nSymTable:\n");
        for(String key : SymTable.getElements()){
            sb.append(key).append(" : ").append(SymTable.getValue(key)).append("\n");
        }

        sb.append("\nOut:\n");
        for(Integer i : list.getElements()){
            sb.append(i).append("\n");
        }

        sb.append("\nHeap:\n");
        for(int key : heap.getElements()) {
            sb.append(key).append(" : ").append(heap.getValue(key)).append("\n");
        }

        return sb.toString();
    }
}
