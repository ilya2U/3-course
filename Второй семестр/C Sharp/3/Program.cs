using System;
using System.Net.Http.Headers;
using System.Xml.Serialization;

namespace Laba3
{
    public class AccesData
    {
        public List<string> levels = new List<string> { "Совершенно секретно", "Секретно", "Открытые данные" };
        public List<DataObject> objects;
        public List<User> users;
        public AccesData(int u_count, int o_count)
        {
            objects = new List<DataObject>();
            users = new List<User>();
            int iter = 0;
            while (iter < o_count)
            {
                objects.Add(new DataObject($"Object{iter}", levels[GetRandom()]));
                iter++;
            }
            iter = 0;
            while (iter < u_count)
            {
                users.Add(new User($"User{iter}", levels[GetRandom()]));
                iter++;
            }

        }
        public int GetRandom()
        {
            Random rnd = new Random();
            return rnd.Next(0, 3);
        }
        public void PrintUsers()
        {
            Console.WriteLine("----------Users:----------");
            foreach(var user in users) { user.Print(); }
            Console.WriteLine("--------------------------");
        }
        public void PrintObjects()
        {
            Console.WriteLine("---------Objects:---------");
            Console.WriteLine("Objects: ");
            foreach (var obj in objects) { obj.Print(); }
            Console.WriteLine("--------------------------");
        }
    }

    public class Session
    {
        string current_user;
        string current_acces_level;
        List<int> objects_inds;
        AccesData data; 
        public Session(AccesData _data)
        {
            data = _data;
        }
        public void Login()
        {
            Console.WriteLine("Вход: ");
            for (int i = 0; i < data.users.Count; i++) { Console.WriteLine($"{i}) {data.users[i].name}"); }
            int u_select = -1;
            while(u_select<0 || u_select > data.users.Count) { u_select = Convert.ToInt32(Console.ReadLine()); }
            current_user = data.users[u_select].name;
            current_acces_level = data.users[u_select].acces_level;
            Console.WriteLine($"Добро пожаловать, {current_user}. Уровень  доступа - {current_acces_level}");
        }
        public void PrintObjectts(string acces_level) 
        {
            objects_inds = new List<int>();
            int pos_user = GetIndex(data.levels, current_acces_level);
            
            Console.WriteLine("Доступные объекты: ");
            for (int i = 0; i < data.objects.Count; i++)
            {
                int pos_obj = GetIndex(data.levels, data.objects[i].acces_level);
                if (pos_user <= pos_obj) { data.objects[i].Print(); objects_inds.Add(i); }
            }
        }

        public int Request()
        {
            Console.WriteLine("Запрашиваемый объект");
            for(int i = 0; i< objects_inds.Count; i++)
            {
                Console.WriteLine($"{i}) {data.objects[objects_inds[i]].name}");
            }
            int select = -1;
            while(select<0 || select > objects_inds.Count)
            {
                select = Convert.ToInt32(Console.ReadLine());
            }

            return objects_inds[select];
        }
        public void CheckAcces(int obj_ind)
        {
            int pos_user = GetIndex(data.levels, current_acces_level);
            int pos_obj = GetIndex(data.levels, data.objects[obj_ind].acces_level);

            if (pos_user <= pos_obj) { Console.WriteLine("Доступ получен"); return; }
            else if (pos_user > pos_obj) { Console.WriteLine("Доступ ограничен"); return; }
        }

        public int GetIndex(List<string> list, string val)
        {
            for (int i = 0; i < list.Count; i++) { if (val == list[i]) { return i; } }
            return -1;
        }

        public void Menu()
        {
            data.PrintUsers();
            Login();
            int choise = -1;
            while (choise != 0)
            {
                choise = -1;
                Console.WriteLine("Выбор опции:");
                Console.WriteLine("0) Выход; \n1) Доступные файлы; \n2) Запрос; \n3) Сменить пользователя; \n4) Объекты. ");
                while(choise<0 || choise > 4)
                {
                    choise = Convert.ToInt32(Console.ReadLine());
                }
                switch (choise)
                {
                    case 0: return;
                    case 1: PrintObjectts(current_acces_level); break;
                    case 2: CheckAcces(Request()); break;
                    case 3: Login(); break;
                    case 4: data.PrintObjects(); break;
                }
            }
        }
    }

    public class DataObject
    {
        public DataObject(string _name, string _acces_level)
        {
            name = _name;
            acces_level = _acces_level;
        }
        public string name { get; set; }
        public string acces_level { get; set; }
        public void Print() => Console.WriteLine($"{name} - {acces_level}");
    }
    public class User
    {
        public User(string _name, string _acces_level)
        {
            name = _name;
            acces_level = _acces_level;
        }
        public string name { get; set; }
        public string acces_level { get; set; }
        public void Print() => Console.WriteLine($"{name} - {acces_level}");
    }
    class Program
    {
        public static void Main(string[] args)
        {
            AccesData data = new AccesData(4,9);
            Session session = new Session(data);
            session.Menu();
        }
    }
}