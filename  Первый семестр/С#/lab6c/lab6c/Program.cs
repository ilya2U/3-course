
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace Lab6c_
{
    internal class Program
    {
        public static String filters(String str)
        {
            Console.WriteLine(str + "\nХотите ли вы изменить символ в этой строке?\n1)yes\n2)no\nВаш ответ: ");
            if(Console.ReadLine() == "1")
            {
                Console.Write("Введите символ, который вы хотите заменить:");
                String n1 = Console.ReadLine();
                Console.Write("Введите символ, на который вы хотите заменить:");
                String n2 = Console.ReadLine();
                str = str.Replace(n1, n2);
            }
            return str;
        }

        public static int checkLength(string path)
        {
            int length = 0;
            foreach(string line in System.IO.File.ReadLines(path))
            {
                length = length + line.Length;
            }

            return length;
        }

        public static void task1(StreamWriter writer, string path)
        {
            char[] mas = new char[checkLength(path)];
            string str = "";
            foreach (string line in System.IO.File.ReadLines(path))
            {
                str += line;
            }
            // filters(str);
            mas = str.ToCharArray();
            for(int i = 0; i < mas.Length; i++)
            {
                writer.Write(mas[i] + " ");
            }
        }

        public static void task2(StreamWriter writer, string path)
        {
            foreach (string line in System.IO.File.ReadLines(path))
            {
//              filters(line);
                writer.WriteLine(line);
            }
        }


        static void Main(string[] args)
        {
            String path = "/Users/androsovilya/Desktop/С#/lab6c/lab6c/input.txt";
            StreamWriter streamWriter = new StreamWriter("/Users/androsovilya/Desktop/С#/lab6c/lab6c/output.txt");
            Console.WriteLine("Как будет скопирован текст? \n1) Посимвольно \n2) Построчно \nВаш ответ: ");
            int otv = Convert.ToInt32(Console.ReadLine());
            if (otv == 1)
            {
                task1(streamWriter, path);
            } else
            {
                task2(streamWriter, path);
            }
            streamWriter.Close();
        }
    }
}
