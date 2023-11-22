using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab2_Net_
{
    internal class Program
    {
        class Animals
        {
            private int countLegs 
            {
                get; set;
            }
            public Animals(int countLegs)
            {
                this.countLegs = countLegs;
            }
            public virtual void print()
            {
                Console.WriteLine("Количество ног: " + countLegs);
            }
        }

        class Mammals : Animals
        {
            private bool isFriendly { get; set; }
            
            public Mammals(int countLegs, bool isFriendly)
                : base(countLegs)
            {
                this.isFriendly = isFriendly;
            }
        }

        class Insects : Animals
        {
            private bool isFly { get; set; }
            
            public Insects(int countLegs, bool isFly)
                : base(countLegs)
            {
                this.isFly = isFly;
            }
        }

        class Horse : Mammals
        {
            private string breed { get; set; }
            
            public Horse(bool isFriendly, int countLegs, string breed)
                : base(countLegs, isFriendly)
            {
                this.breed = breed; 
            }
        }

        class Spiders : Insects
        {
            private string type { get; set; }

            public Spiders(int countLegs, string type, bool isFly)
                : base(countLegs, isFly)
            {
                this.type = type;
            }
            
        }

        class Dogs : Mammals
        {
            private int age { get; set; }
            
            public Dogs(bool isFriendly, int countLegs, int age)
                : base(countLegs, isFriendly)
            {
                this.age = age; 
            }
        }

        class Crocodile
        {
            private string gender;

            public Crocodile(string gender)
            {
                this.gender = gender;
            }
        }
        
        class Fish
        {
            private bool isSea { get; set; }

            public Fish (bool isSea)
            {
                this.isSea = isSea;
            }
        }

        static void Main(string[] args)
        {
            Dogs sam = new Dogs(true, 4, 41);
            sam.print();
            Spiders lopy = new Spiders(8, "tarantula", false);
            lopy.print();

        }
    }
}
