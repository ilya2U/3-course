namespace Laba3;

public interface IElectricSource
{
    public string Name { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
}