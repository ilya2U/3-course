using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Reflection;
using System.Runtime.Intrinsics.X86;
using System.Text.RegularExpressions;
using static Lab1.Program;

namespace Lab1
{
    internal class Program
    {
        static Robot robot = new Robot(20, "TSP-15");
        static Dictionary<String, Variable> variables = new Dictionary<String, Variable>();
        public class Robot
        {
            public int energy { get; set; }
            public String name { get; set; }
            public Robot(int energy, string name)
            {
                this.energy = energy;
                this.name = name;
            }
            public void sayHello()
            {
                Console.WriteLine("Hello, my name is: " + name);
            }
            public int charge(int energy)
            {
                this.energy += energy;
                Console.WriteLine("Recharged " + energy + " energy. Now: " + this.energy);
                return this.energy;
            }
            public void action()
            {
                if (this.energy < 10)
                {
                    Console.WriteLine("Not enough energy. Current: " + this.energy + ". Required: 10");
                }
                else
                {
                    this.energy -= 10;
                    Console.WriteLine("Performing action. Remaining energy is " + this.energy);
                }
            }
            public object this[string name]
            {
                get
                {
                    return this.GetType().GetProperty(name).GetValue(this);
                }
                set
                {
                    this.GetType().GetProperty(name).SetValue(this, value, null);
                }
            }
        }
        public class Variable
        {
            public string type { get; set; }
            public object value { get; set; }
            public Variable(string type, object value)
            {
                this.type = type;
                this.value = value;
            }   
        }
        public static Variable checkType(object var)
        {
            if (var.GetType().ToString() == "System.String")
            {
                String str = (string)var;
                double d;
                int n;
                if(double.TryParse(str, out d))
                {
                    if(int.TryParse(str, out n))
                    {
                        return new Variable("System.Int32", n);
                    }
                    return new Variable("System.Double", d);
                }
                return new Variable("System.String", var.ToString().Replace("\"", ""));
            }
            return new Variable(var.GetType().ToString(), var);
        }
        public static void addOrUpdateVar(String name, Variable v)
        {
            if (variables.ContainsKey(name))
            {
                variables.Remove(name);
            }
            variables.Add(name, v);
        }
        public static void logVars()
        {
            foreach (var key in variables.Keys)
            {
                Console.WriteLine("key: " + key + ". Value: " + variables[key].value);
            }
        }
        public static void doAction(String action)
        {
            if (Regex.IsMatch(action, @"\(.*\)"))
            {
                String methodFullname;

                if (action.Contains("="))
                {
                    var parsed = action.Split(" ");
                    methodFullname = parsed[2].Split(".")[1];
                }
                else
                {
                    methodFullname = action.Split(".")[1];
                    
                }
                var methodName = methodFullname.Substring(0, methodFullname.IndexOf("("));

                Type t = typeof(Robot);
                var availableMethods = t.GetMethods();

                var hasMethod = false;
                foreach(var m in availableMethods)
                {
                    
                    if (m.Name.Contains(methodName))
                    {
                        hasMethod = true;
                    }
                }
                if (!hasMethod) throw new InvalidOperationException("robot doesn't have method: " + methodFullname);

                //System.Collections.Generic.List<object> args = new System.Collections.Generic.List<object>();
                //var result = typeof(Robot).GetMethod(methodName).Invoke(robot, args.Cast<object>().ToArray());
                object result;

                if(methodName == "sayHello")
                {
                    result = typeof(Robot).GetMethod(methodName).Invoke(robot, null);
                }
                else if(methodName == "charge")
                {
                    var start = methodFullname.IndexOf("(") + 1;
                    var length = methodFullname.IndexOf(")") - start;
                    object energy = int.Parse(methodFullname.Substring(start, length));
                    result = typeof(Robot).GetMethod(methodName).Invoke(robot, new[] { energy } );

                    if (action.Contains("="))
                    {
                        var parsed = action.Split(" ");
                        var varName = parsed[0];
                        addOrUpdateVar(varName, checkType(result));
                    }
                }
                if (methodName == "action")
                {
                    result = typeof(Robot).GetMethod(methodName).Invoke(robot, null);
                }
            }
            else
            {
                var parsed = action.Split(" ");
                var left = parsed[0];
                var right = parsed[2];
                if (right.Contains("."))
                {
                    // assigning {variable} = {robot.attr}
                    var attrName = right.Split(".")[1];
                    addOrUpdateVar(left, checkType(robot[attrName]));
                   
                }
                else if (left.Contains("."))
                {
                    if (Regex.IsMatch(right, @""".*"""))
                    {
                        // assigning {robot.attr} = {"string"}
                        var attrName = left.Split(".")[1];
                        if (checkType(robot[attrName]).type != checkType(right).type)
                        {
                            throw new InvalidOperationException("types aren't equal");
                        }
                        robot[attrName] = checkType(right).value;
                    }
                    else
                    {
                        // assigning {robot.attr} = {variable}
                        var variable = variables[right];
                        var attrName = left.Split(".")[1];
                        if (checkType(robot[attrName]).type != variable.type)
                        {
                            throw new InvalidOperationException("types aren't equal");
                        }
                        robot[attrName] = variable.value;
                    }
                }
            }
        } 
        static void Main(string[] args)
        {
            //robot.sayHello();
            //doAction("newname = robot.name");
            //doAction("robot.name = \"MREA-100\"");
            //robot.sayHello();
            //doAction("robot.name = newname");
            //robot.sayHello();
            doAction("robot.sayHello()");
            doAction("robot.action()");
            doAction("robot.action()");
            doAction("varia = robot.charge(30)");
            doAction("robot.action()");
            doAction("robot.charge(5000)");
            logVars();
            doAction("robot.energy = varia");
            doAction("robot.action()");

        }
    }
}
