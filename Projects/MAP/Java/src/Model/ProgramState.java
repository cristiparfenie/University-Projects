package Model;

import Model.Utilities.*;
import  Model.Statements.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import Exception.EmptyStack;

public class ProgramState {
    private IStack<IStmt> stack;
    private IDictionary<String, Integer> SymTable;
    private IList<Integer> list;
    private IDictionary<Integer, BufferedReader> FileTable;
    private IDictionary<Integer, Integer> heap;
    private Integer id;


    public ProgramState(IStack<IStmt> stack, IDictionary<String, Integer> symTable, IList<Integer> list,IDictionary<Integer,BufferedReader> ft, IDictionary<Integer, Integer>h) {
        this.stack = stack;
        this.SymTable = symTable;
        this.list = list;
        this.FileTable=ft;
        this.heap=h;
        this.id=1;
    }

    public IStack<IStmt> getStack() {
        return stack;
    }

    public Integer getID(){return id;}

    public void setID(Integer i){id=i;}

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

    public void clearFileFromSym() {this.SymTable.setMap(SymTable.getMap().entrySet().stream().filter(e-> FileTable.getMap().containsKey(e)).collect(Collectors.toMap(Map.Entry::getKey,Map.Entry::getValue)));}

    public void clearFileTable() {this.FileTable.clear();}

    public Boolean isNotCompleted(){return !this.stack.isEmpty();}

    public ProgramState oneStep() throws IOException{
        if(stack.isEmpty()) throw new EmptyStack("Stack is empty!");
        IStmt crtStmt = stack.pop();
        return crtStmt.execute(this);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\nProgram State ID: "+id+"\n");

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
