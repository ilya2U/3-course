using UAParser;
using System.Threading;
using System.IO;

internal class Program
{

  private static ManualResetEvent doneEvent = new ManualResetEvent(false);
  private static Dictionary<string, IReport1> info = new Dictionary<string, IReport1>(){};
  private static Dictionary<DateTime, IReport2> info2 = new Dictionary<DateTime, IReport2>(){};
  private static Dictionary<string, IReport3> info3 = new Dictionary<string, IReport3>(){};
  private static string[] files = Directory.GetFiles("access-log", "*.txt");
  private static int tasks = 0;
  private static void Main(string[] args)
  {
    string dateStart = "10/Feb/2023";
    string dateEnd = "17/Feb/2023";
    tasks = files.Length * 3;
    foreach(string file in files) {
      ThreadPool.QueueUserWorkItem(new WaitCallback(firstReport), new ReportProps(file, dateStart, dateEnd)); 
    }

    foreach(string file in files) {
      ThreadPool.QueueUserWorkItem(new WaitCallback(secondReport), new ReportProps(file, dateStart, dateEnd)); 
    }

    foreach(string file in files) {
      ThreadPool.QueueUserWorkItem(new WaitCallback(thirdReport), new ReportProps(file, dateStart, dateEnd)); 
    }

    WaitHandle.WaitAll(new WaitHandle[] { doneEvent  });
  }

  private static void firstReport(object state) {
    ReportProps wrapper = state as ReportProps;
    DateTime d1 = DateTime.Parse(wrapper.startDate);
    DateTime d2 = DateTime.Parse(wrapper.endDate);
    Console.WriteLine(Thread.CurrentThread.ManagedThreadId);
    var totalDays = (d2 - d1).TotalDays;
    using (StreamReader fs = new StreamReader(wrapper.path))
    {
        while (true)
        {
            string temp = fs.ReadLine();
            if(temp == null) break;
            MyParser data = new MyParser(temp);
            if(data.TimeStamp < d1) continue;
            if(data.TimeStamp > d2) break;
            lock(info) {
              if(info.ContainsKey(data.IpAddress)) {
                info[data.IpAddress].requestCount += 1;
                info[data.IpAddress].traficCount += data.ResponseSize;
              }

              else {
                info.Add(data.IpAddress, new IReport1(data.ResponseSize));
              }
            }
        }
      if (Interlocked.Decrement(ref tasks) == 0)
      {
        foreach(KeyValuePair<string, IReport1> entry in info)
        {
          info[entry.Key].averageRequest = info[entry.Key].traficCount / totalDays;      
        }

        File.WriteAllLines("report1.txt",
        info.Select(x =>  x.Key + " " + x.Value.requestCount + " " + x.Value.traficCount + " " + x.Value.averageRequest));

        File.WriteAllLines("report2.txt",
        info2.Select(x =>  x.Key + " " + x.Value.traficCount + " " + x.Value.maxDomain + " " + x.Value.maxIp));

        File.WriteAllLines("report3.txt",
        info3.Select(x =>  x.Key + " " + x.Value.getMaxBrowsers() + " " +  x.Value.getMaxIps()));
        doneEvent.Set();
      }
     }
  }

    private static void secondReport(object state) {
    ReportProps wrapper = state as ReportProps;
    DateTime d1 = DateTime.Parse(wrapper.startDate);
    DateTime d2 = DateTime.Parse(wrapper.endDate);
    var totalDays = (d2 - d1).TotalDays;
    using (StreamReader fs = new StreamReader(wrapper.path))
    {
        while (true)
        {
            string temp = fs.ReadLine();
            if(temp == null) break;
            MyParser data = new MyParser(temp);
            if(data.TimeStamp < d1) continue;
            if(data.TimeStamp > d2) break;
            lock(info2) {
              if(info2.ContainsKey(data.TimeStamp)) {
                info2[data.TimeStamp].traficCount += data.ResponseSize;
                if(data.ResponseSize > info2[data.TimeStamp].maxTrafic) {
                  info2[data.TimeStamp].maxTrafic = data.ResponseSize;
                  info2[data.TimeStamp].maxDomain = data.Domen;
                  info2[data.TimeStamp].maxIp = data.IpAddress;
                }
              }
              else {
                info2.Add(data.TimeStamp, new IReport2(data.ResponseSize, data.Domen, data.ResponseSize, data.IpAddress));
              }
            }
        }
     }

    if (Interlocked.Decrement(ref tasks) == 0)
    {
      foreach(KeyValuePair<string, IReport1> entry in info)
      {
        info[entry.Key].averageRequest = info[entry.Key].traficCount / totalDays;      
      }

      File.WriteAllLines("report1.txt",
      info.Select(x =>  x.Key + " " + x.Value.requestCount + " " + x.Value.traficCount + " " + x.Value.averageRequest));

      File.WriteAllLines("report2.txt",
      info2.Select(x =>  x.Key + " " + x.Value.traficCount + " " + x.Value.maxDomain + " " + x.Value.maxIp));

      File.WriteAllLines("report3.txt",
      info3.Select(x =>  x.Key + " " + x.Value.getMaxBrowsers() + " " +  x.Value.getMaxIps()));
      doneEvent.Set();
    }
  }

  private static void thirdReport(object state) {
    ReportProps wrapper = state as ReportProps;
    DateTime d1 = DateTime.Parse(wrapper.startDate);
    DateTime d2 = DateTime.Parse(wrapper.endDate);
    var totalDays = (d2 - d1).TotalDays;
    using (StreamReader fs = new StreamReader(wrapper.path))
    {
        while (true)
        {
            string temp = fs.ReadLine();
            if(temp == null) break;
            MyParser data = new MyParser(temp);
            if(data.TimeStamp < d1) continue;
            if(data.TimeStamp > d2) break;
            lock(info3) {
              if(info3.ContainsKey(data.Domen)) {
                info3[data.Domen].traficCount += data.ResponseSize;
                if(info3[data.Domen].browsers.ContainsKey(data.Browser)) {
                  info3[data.Domen].browsers[data.Browser] += 1;
                }
                else {
                  info3[data.Domen].browsers.Add(data.Browser, 1);
                }

                if(!info3[data.Domen].ips.ContainsKey(data.IpAddress)) {
                  info3[data.Domen].ips.Add(data.IpAddress, data.ResponseSize);
                }
                else {
                  info3[data.Domen].ips[data.IpAddress] += data.ResponseSize;
                }
              }
              else {
                info3.Add(data.Domen, new IReport3(data.ResponseSize));
              }
            }
        }
     }

    if (Interlocked.Decrement(ref tasks) == 0)
    {
      foreach(KeyValuePair<string, IReport1> entry in info)
      {
        info[entry.Key].averageRequest = info[entry.Key].traficCount / totalDays;      
      }

      File.WriteAllLines("report1.txt",
      info.Select(x =>  x.Key + " " + x.Value.requestCount + " " + x.Value.traficCount + " " + x.Value.averageRequest));

      File.WriteAllLines("report2.txt",
      info2.Select(x =>  x.Key + " " + x.Value.traficCount + " " + x.Value.maxDomain + " " + x.Value.maxIp));

      File.WriteAllLines("report3.txt",
      info3.Select(x =>  x.Key + " " + x.Value.getMaxBrowsers() + " " +  x.Value.getMaxIps()));
      doneEvent.Set();
    }
  }      
}



class IReport1 {
  public IReport1(long currentTrafficCount) {
    this.requestCount = 1;
    this.traficCount = currentTrafficCount;
    this.averageRequest = 0;
  }
  
  public int requestCount{ get; set; }
  public long traficCount{ get; set; }
  public double averageRequest{ get; set; }
}

class IReport2 {
  public IReport2(long currentTrafficCount, string currentMaxDomain, long currentMaxIpTrafic, string currentMaxIp) {
    this.traficCount = currentTrafficCount;
    this.maxDomain = currentMaxDomain;
    this.maxTrafic = currentMaxIpTrafic;
    this.maxIp = currentMaxIp;
  }
  
  public long traficCount{ get; set; }
  public string maxDomain{ get; set; }
  public long maxTrafic{ get; set; }
  public string maxIp{ get; set; }
}

class IReport3 {
  public IReport3(long currentTrafficCount) {
    this.traficCount = currentTrafficCount;
    this.browsers = new Dictionary<string, long>(){};
    this.ips = new Dictionary<string, long>(){};
  }
  
  public long traficCount{ get; set; }
  public Dictionary<string, long> browsers{ get; set; }
  public Dictionary<string, long> ips{ get; set; }

  public string getMaxBrowsers() {
    string first = "";
    string second = "";
    string third = "";
    foreach(KeyValuePair<string, long> entry in browsers)
    {
      if(first == "") {
        first = entry.Key;
      }
      else if(entry.Value > browsers[first]) {
        third = second;
        second = first;
        first = entry.Key;
      }
      else if(second == "") {
        second = entry.Key;
      }
      else if(entry.Value > browsers[second]) {
        third = second;
        second = entry.Key;
      }
      else if(third == "") {
        third = entry.Key;
      }
      else if(entry.Value > browsers[third]) {
        third = entry.Key;
      }
    }
    return first + " " + second + " " + third;
  }

    public string getMaxIps() {
    string first = "";
    string second = "";
    string third = "";
    foreach(KeyValuePair<string, long> entry in ips)
    {
      if(first == "") {
        first = entry.Key;
      }
      else if(entry.Value > ips[first]) {
        third = second;
        second = first;
        first = entry.Key;
      }
      else if(second == "") {
        second = entry.Key;
      }
      else if(entry.Value > ips[second]) {
        third = second;
        second = entry.Key;
      }
      else if(third == "") {
        third = entry.Key;
      }
      else if(entry.Value > ips[third]) {
        third = entry.Key;
      }
    }
    return first + " " + second + " " + third;
  }
}

class ReportProps {
  public ReportProps(string currentPath, string currentStartDate, string currentEndDate) {
    this.path = currentPath;
    this.startDate = currentStartDate;
    this.endDate = currentEndDate;
  }
  public string path { get; set; }
  public string startDate { get; set; }
  public string endDate { get; set; }
}

class MyParser {
  public string IpAddress { get; set; }
  public DateTime TimeStamp { get; set; }
  public string RequestMethod { get; set; }
  public string RequestUri { get; set; }
  public string Domen { get; set; }
  public int StatusCode { get; set; }
  public long ResponseSize { get; set; }
  public string UserAgent { get; set; }
  public string Browser { get; set; }
  public MyParser(string data) {
    string[] splitData = data.Split(' ');
    this.IpAddress = splitData[0];
    string[] parseDate = splitData[3].Substring(1).Split(':');
    this.TimeStamp = DateTime.Parse(parseDate[0] + " " + parseDate[1] + ":00:00");
    this.RequestMethod = splitData[5].Substring(1);
    this.RequestUri = splitData[6];
    this.Domen = RequestUri.Split('/')[2];
    this.StatusCode = Int32.Parse(splitData[8]);
    this.ResponseSize = Int32.Parse(splitData[9].Substring(0, splitData[9].Length));
    this.UserAgent = String.Join(" ", splitData.Skip(10));
    var uaParser = Parser.GetDefault();
    ClientInfo userAgent = uaParser.Parse(UserAgent);
    this.Browser = userAgent.UA.Family;
  }

  public void printAll() {
    Console.WriteLine(this.IpAddress);
    Console.WriteLine(this.TimeStamp);
    Console.WriteLine(this.RequestMethod);
    Console.WriteLine(this.RequestUri);
    Console.WriteLine(this.Domen);
    Console.WriteLine(this.StatusCode);
    Console.WriteLine(this.ResponseSize);
    Console.WriteLine(this.UserAgent);
    Console.WriteLine(this.Browser);
  }
}
