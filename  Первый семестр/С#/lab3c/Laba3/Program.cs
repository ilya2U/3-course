// List<Student> students = new List<Student>();
// Student student = new Student
// {
//     Name = "Mike",
//     Address = "Main St"
// }; 
// students.Add(Student);           

using Laba3;

Kettle Kettle1 = new Kettle
{
    Name = "Bork 3000",
    InputPower = 2
};

Refrigerator Rf1 = new Refrigerator
{
    Name = "Samsung 3000",
    InputPower = 6
};

DieselGenerator Diesel = new DieselGenerator
{
    Name = "dg",
    Appliances = new List<IElectricAppliance>()
};

Diesel.Appliances.Add(Kettle1);
Diesel.Appliances.Add(Rf1);


Console.WriteLine("Приборы подключенные к дизельному генератору");
foreach(var app in Diesel.Appliances) {
    Console.WriteLine($"{app.Name}");
}
Console.WriteLine("");

ElectricPowerStrip Strip = new ElectricPowerStrip
{
    Name = "220V strip",
    Appliances = new List<IElectricAppliance>(),
    Sources = new List<IElectricSource>()
};

Strip.Appliances.Add(Kettle1);
Strip.Appliances.Add(Rf1);
Strip.Sources.Add(Diesel);

Console.WriteLine($"Приборы и источники подключенные к {Strip.Name}");
Console.WriteLine("Источники: ");
foreach(var src in Strip.Sources) 
{
    Console.WriteLine($"{src.Name}");
}
Console.WriteLine("Приборы: ");
foreach(var app in Strip.Appliances) 
{
    Console.WriteLine($"{app.Name}");
}
Console.WriteLine("");

StepDownTransformer TR = new StepDownTransformer
{
    Name = "High voltage transformer",
    Appliances = new List<IElectricAppliance>(),
    InputPower = 5000
};

TR.Appliances.Add(Kettle1);
TR.Appliances.Add(Rf1);

Console.WriteLine($"Приборы подключенные к {TR.Name} с мощностью {TR.InputPower / 1000} тВт");
Console.WriteLine($"Приборы: ");
foreach(var app in TR.Appliances) 
{
    Console.WriteLine($"{app.Name}");
}
Console.WriteLine("");
