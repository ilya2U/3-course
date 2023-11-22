namespace Laba3;

public class SolarBattery : IElectricSource
{
    public string Name { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
}