﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab7.Model
{
    public class NextNumber
    {
        private static int count = 1;
        public static int Generate()
        {
            return count++;
        }
    }
}
