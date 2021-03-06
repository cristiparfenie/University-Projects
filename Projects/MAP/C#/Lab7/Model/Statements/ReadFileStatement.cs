﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using Lab7.Model.Expressions;
namespace Lab7.Model.Statements
{
    public class ReadFileStatement : Statement
    {
        private Expression expr;
        private string varName;

        public ReadFileStatement(Expression e, string var)
        {
            this.expr = e;
            this.varName = var;
        }

        public PrgState Execute(PrgState p)
        {
            int res = this.expr.Eval(p.Dict);
            if (!p.FileTable.Contains(res))
                throw new SystemException("File not found");
            FileData fd = p.FileTable.GetValue(res);
            StreamReader head = fd.Header;
            string line = head.ReadLine();
            Expression val;
            if (line == null)
                val = new ConstantExpression(0);
            else
                val = new ConstantExpression(Int32.Parse(line));
            Statement st = new AssignStatement(this.varName, val);
            st.Execute(p);
            return p;

        }
        public override string ToString()
        {
            return "Read(" + this.varName + "," + this.expr + ")";
        }
    }
}
