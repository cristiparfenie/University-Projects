using Lab7.Model.ADT;
using Lab7.Model.Statements;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab7.Model
{
    public class PrgState
    {
        private ADT.IDictionary<string, int> symbolTable;
        private IOutput<int> output;
        private IExeStack<Statement> exeStack;
        private IFileTable<int, FileData> filetable;

        public PrgState(ADT.IDictionary<string, int> s, IExeStack<Statement> exe, IOutput<int> o, IFileTable<int, FileData> ft)
        {
            this.symbolTable = s;
            this.exeStack = exe;
            this.output = o;
            this.filetable = ft;
        }

        public ADT.IDictionary<string, int> Dict
        {
            get { return this.symbolTable; }
            set { this.symbolTable = value; }
        }

        public IExeStack<Statement> Stack
        {
            get { return this.exeStack; }
            set { this.exeStack = value; }
        }

        public IOutput<int> Messages
        {
            get { return this.output; }
            set { this.output = value; }
        }
        public IFileTable<int, FileData> FileTable
        {
            get { return this.filetable; }
            set { this.filetable = value; }
        }
        public override string ToString()
        {
            StringBuilder buff = new StringBuilder();
            buff.Append("Stack:\n");
            buff.Append(this.exeStack);
            buff.Append("\nSymbolTable:\n");
            buff.Append(this.symbolTable);
            buff.Append("\nList:\n");
            buff.Append(this.output);
            buff.Append("\nFileTable:\n");
            buff.Append(this.filetable);
            buff.Append("\n-----------\n");
            return buff.ToString();
        }
    }
}
