using System;
using System.Drawing;
using System.Globalization;

class Lab1
{
    static void Main(String[] args)
    {
        // zad1();
        // zad2();
        // zad3();
        dopzad();
    }

    static void zad1()
    {
        int a;
        Console.WriteLine("Введите колличество элементов массива: ");
        a = int.Parse(Console.ReadLine());
        int[] array = new Int32[a];
        bool affff = false;
        do
        {
            try
            {
                Console.WriteLine("Введите элементы:");
                string str = Console.ReadLine();

                array = str.Split(" ").Select(x => int.Parse(x)).ToArray();
                int c = 0;
                affff = true;
            }
            catch
            {
                Console.WriteLine("Повторите попытку");
            }
        } while (!affff);

        for (int i = 0; i < array.Length; i++)
        {
            Console.Write(array[i] + " ");
        }

        sort(array);
        Console.WriteLine("Самая длинная последовательность: " + f1(array));

    }

    static void sort(int[] arr)
    {
        Console.WriteLine();
        for (int i = 1; i < arr.Length; i++)
        {
            Console.WriteLine("Итерация " + i);
            int value = arr[i];
            int index = i;
            while ((index > 0) && (arr[index - 1] > value))
            {
                arr[index] = arr[index - 1];
                index--;
            }

            arr[index] = value;
            Console.WriteLine("________________________________");
            for (int i1 = 0; i1 < arr.Length; i1++)
            {
                Console.Write(arr[i1] + " ");
                Console.WriteLine();
            }

            Console.WriteLine("________________________________");
        }
    }

    static int f1(int[] arr)
    {
        int x = arr[0];
        int max = -1;
        int count = 0;

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] == x)
                count++;
            else
            {
                if (count > max)
                    max = count;
                count = 1;
                x = arr[i];
            }
        }

        if (count > max)
            max = count;
        return max;
    }

    
    
    // 1   2   3   4 
    // 5   6   7   8
    // 9  10   11  12
    
    static void zad2()
    {
        Console.WriteLine("Введите колличество строк: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите колличество столбцов: ");
        int b = int.Parse(Console.ReadLine());
        int[,] array = new int[a, b];
        Console.WriteLine("Введите элементы:");
        string str = Console.ReadLine();
        Console.WriteLine();
        int[] array1 = str.Split(" ").Select(x => int.Parse(x)).ToArray();
        for (int i = 0; i < a; i++)
        for (int j = 0; j < b; j++)
        {
            array[i, j] = array1[j + i * b];
        }

        Console.WriteLine("Матрица: ");
        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
                Console.Write(array[i, j] + " ");
            Console.WriteLine();
        }

        Console.WriteLine();
        for (int i = 0; i < a; i++)
        {
            int sum1 = 0;
            for (int j = 0; j < b; j++)
            {
                sum1 += array[i, j];
            }

            Console.WriteLine("Сумма " + (i + 1) + " строки = " + sum1);
        }

        Console.WriteLine();
        for (int j = 0; j < b; j++)
        {
            int sum1 = 0;
            for (int i = 0; i < a; i++)
            {
                sum1 += array[i, j];
            }

            Console.WriteLine("Сумма " + (j + 1) + " столбца = " + sum1);
        }

        Console.WriteLine();
        int sum = 0;
        for (int i = 0; i < a; i++)
        {
            int j = i;
            sum += array[i, j];
        }

        Console.WriteLine("Сумма главной диагонали = " + sum);
        sum = 0;
        for (int i = 0; i < a; i++)
        {
            int j = b - i - 1;
            sum += array[i, j];
        }

        Console.WriteLine("Сумма побочной диагонали = " + sum);
    }
    
    

    static void zad3()
    {
        Console.WriteLine("Введите колличество строк: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите колличество столбцов: ");
        int b = int.Parse(Console.ReadLine());
        int[,] array = new int[a, b];
        Console.WriteLine("Введите элементы:");
        string str = Console.ReadLine();
        Console.WriteLine();
        int[] arr = str.Split(" ").Select(x => int.Parse(x)).ToArray();

        for (int i = 0; i < a; i++)
        for (int j = 0; j < b; j++)
        {
            array[i, j] = arr[j + i * b];
        }

        Console.WriteLine("Первая матрица: ");
        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
                Console.Write(array[i, j] + " ");
            Console.WriteLine();
        }

        Console.WriteLine("Введите колличество строк: ");
        int c = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите колличество столбцов: ");
        int d = int.Parse(Console.ReadLine());
        int[,] array1 = new int[c, d];
        Console.WriteLine("Введите элементы:");
        string str1 = Console.ReadLine();
        Console.WriteLine();
        int[] arr1 = str1.Split(" ").Select(x => int.Parse(x)).ToArray();

        for (int i = 0; i < c; i++)
        for (int j = 0; j < d; j++)
        {
            array1[i, j] = arr1[j + i * d];
        }

        Console.WriteLine("Вторая матрица: ");
        for (int i = 0; i < c; i++)
        {
            for (int j = 0; j < d; j++)
                Console.Write(array1[i, j] + " ");
            Console.WriteLine();
        }

        Console.WriteLine();
        bool tf = ContainsMatrix(array, array1);

        
        
        if (tf == true)
            Console.WriteLine("Первая матрица содержит структуру второй матрицы");
        else
            Console.WriteLine("Первая матрица не содержит структуру второй матрицы");

    }

    static bool ContainsMatrix(int[,] big, int[,] small)
    {
        int smallWidth = small.GetLength(0);
        Console.Write(small.GetLength(0)+ " ");
        int smallHeight = small.GetLength(0);
        Console.Write(small.GetLength(0)+ " ");
        int bigWidth = big.GetLength(1);
        Console.Write(big.GetLength(1)+ " ");
        int bigHeight = big.GetLength(0);

        if (smallHeight > bigHeight || smallWidth > bigWidth)
            return false;

        for (int i = 0; i < bigHeight - smallHeight + 1; i++)
        {
            for (int j = 0; j < bigWidth - smallWidth + 1; j++)
            {
                if (Compare(big, small, i, j))
                    return true;
            }
        }

        return false;
    }

    static bool Compare(int[,] big, int[,] small, int rowOffset, int colOffset)
    {
        for (int i = 0; i < small.GetLength(0); i++)
        {
            for (int j = 0; j < small.GetLength(1); j++)
            {
                if (small[i, j] != big[i + rowOffset, j + colOffset])
                    return false;
            }
        }

        return true;
    }
    
    static void dopzad()
    {
        Console.WriteLine("Введите колличество строк первой матрицы: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите колличество столбцов первой матрицы: ");
        int b = int.Parse(Console.ReadLine());
        Console.WriteLine();
        Console.WriteLine("Введите колличество строк второй матрицы: ");
        int c = int.Parse(Console.ReadLine());
        Console.WriteLine("Введите колличество столбцов второй матрицы: ");
        int d = int.Parse(Console.ReadLine());
        int[,] array1 = new int[a, b];
        int[,] array2 = new int[c, d];
        Random random = new Random();
        for (int i = 0; i < a; i++)
            for (int j = 0; j < b; j++)
                array1[i, j] = random.Next(1, 4);
        for (int i = 0; i < c; i++)
            for (int j = 0; j < d; j++)
                array2[i, j] = random.Next(1, 4);
        Console.WriteLine("\n\nПервая матрица:");
        for (int i = 0; i < a; i++)
        {
            for (int j = 0; j < b; j++)
                Console.Write(array1[i, j] + " ");
            Console.WriteLine();
        }
        Console.WriteLine("\n\nВторая матрица:");
        for (int i = 0; i < c; i++)
        {
            for (int j = 0; j < d; j++)
                Console.Write(array2[i, j] + " ");
            Console.WriteLine();
        }
        if (b!=c) throw new Exception("Матрицы нельзя перемножить");
        {
            int[,] r = new int[array1.GetLength(0), array2.GetLength(1)];
            for (int i = 0; i < array1.GetLength(0); i++)
            {
                for (int j = 0; j < array2.GetLength(1); j++)
                {
                    for (int k = 0; k < array2.GetLength(0); k++)
                    {
                        r[i, j] += array1[i, k] * array2[k, j];
                    }
                }
            }
            Console.ReadLine();
            Console.WriteLine("Результат: ");
            for (int i = 0; i < r.GetLength(0); i++)
            {
                for (int j = 0; j < r.GetLength(1); j++)
                {
                    Console.Write(r[i,j]+" ");
                }
                Console.WriteLine();
                
            }
        }
    }
}

   