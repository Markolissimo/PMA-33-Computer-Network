using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace SERVER
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Socket Listener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            IPAddress adr = Dns.Resolve("localhost").AddressList[1];
            //var test = Dns.Resolve("localhost").AddressList;

            IPEndPoint ipEnd = new IPEndPoint(adr, 8086);

            Listener.Bind(ipEnd);
            Listener.Listen(10);

            Console.WriteLine("Очiкую на з'єднання...");
            Socket s = Listener.Accept();

            byte[] bufR = new byte[1024];
            string data = null;
            while (true)
            {
                int bytesRec = s.Receive(bufR);
                data = Encoding.ASCII.GetString(bufR, 0, bytesRec).Replace("\0", "");
                Console.WriteLine($"Слово {data}");


                int res = data.Distinct().Count();

                byte[] r = new byte[1];
                r[0] = Convert.ToByte(res);
                s.Send(r);
                Console.WriteLine($"Результат {res.ToString()} вiдправлено.\n");
            }
        }
    }
}