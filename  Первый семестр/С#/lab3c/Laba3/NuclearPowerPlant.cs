namespace Laba3;

public class NuclearPowerPlant : IElectricSource
{
    public string Name { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
}