public interface IEnumerable {
    IEnumerator GetEnumerator();
}
public interface IEnumerator {
    object Current { get; }
    bool MoveNext();
    void Reset();
}

class Primes : IEnumerable, IEnumerator
{
    int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
        251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
        457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541 };
    int index = -1;

    // Реализуем интерфейс IEnumerable
    public IEnumerator GetEnumerator()
    {
        return this;
    }

    // Реализуем интерфейс IEnumerator
    public bool MoveNext()
    {
        if (index == primes.Length - 1)
        {
            Reset();
            return false;
        }

        index++;
        return true;
    }

    public void Reset()
    {
        index = -1;
    }

    public object Current
    {
        get
        {
            return primes[index];
        }
    }
}

class Program
{
    static void Main()
    {
        Primes pr = new Primes();

        foreach (int p in pr)
            Console.Write(p+"\t");
    }
}

// static IEnumerable<int> PrimeNumbers(int numPrimes)
// {
//     yield return 2; // first prime number
//     for(int n=1, p = 3; n < numPrimes; p+=2)
//     {
//         if (!checkIfPrime(p)) continue;                                
//         n++;
//         yield return p;              
//     }
// }
//
// // p > 2, odd
// static bool checkIfPrime(int p)
// {
//     for (int t = 3; t <= Math.Sqrt(p); t += 2)
//     {
//         if (p % t == 0) return false;              
//     }
//     return true;
// }
//
// int i = 0;
// foreach(int p in PrimeNumbers(100))
// {
//     Console.Write("{0}, ", p);                    
//}