namespace Laba3;

public class HighLine : IElectricWire
{
    public string Name { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
    public List<IElectricSource> Sources { get; set; }
}