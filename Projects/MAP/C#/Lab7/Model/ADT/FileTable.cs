﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
namespace Lab7.Model.ADT
{
    public class FileTable<K, V> : IFileTable<K, V>
    {
       
    
        private Dictionary<K, V> dict = new Dictionary<K, V>();

        public void AddValue(K key, V value)
        {
            this.dict.Add(key, value);
        }

        public void UpdateValue(K key, V value)
        {
            this.dict[key] = value;
        }
        public void Remove(K key)
        {
            this.dict.Remove(key);
        }
        public bool Contains(K key)
        {
            return this.dict.ContainsKey(key);
        }
        public V GetValue(K key)
        {
            return this.dict[key];
        }
        public IEnumerator GetEnumerator()
        {
            return dict.GetEnumerator();
        }
        public override string ToString()
        {
            StringBuilder buff = new StringBuilder();
            foreach (KeyValuePair<K, V> pair in this.dict)
            {
                buff.Append(pair.Key);
                buff.Append(" : ");
                buff.Append(pair.Value);
                buff.Append("\n");
            }
            buff.Append("\n");
            return buff.ToString();
        }


    }
}
