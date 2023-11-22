namespace Laba3;

public class DieselGenerator : IElectricSource
{
    public string Name { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
}