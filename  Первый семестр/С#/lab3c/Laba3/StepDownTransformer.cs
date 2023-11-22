namespace Laba3;

public class StepDownTransformer : IElectricAppliance, IElectricSource
{
    public string Name { get; set; }
    public int InputPower { get; set; }
    public List<IElectricAppliance> Appliances { get; set; }
}