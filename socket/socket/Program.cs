using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace socket
{
    class Program
    {
        static void Main(string[] args)
        {
            IPAddress ipAddress = System.Net.IPAddress.Parse("127.0.0.1");
            IPEndPoint ipEndPoint = new IPEndPoint(ipAddress, 6667);
            using Socket client = new Socket(
            ipEndPoint.AddressFamily,
            SocketType.Stream,
            ProtocolType.Tcp);

            client.Connect(ipEndPoint);
            while (true)
            {
                // Send message.
                var message = "Слава Українi!<|EOM|>";
                var messageBytes = Encoding.UTF32.GetBytes(message);
                _ = client.Send(messageBytes, SocketFlags.None);
                Console.WriteLine($"Socket client sent message: \"{message}\"");

                // Receive ack.
                var buffer = new byte[1_024];
                var received = client.Receive(buffer, SocketFlags.None);
                var response = Encoding.UTF32.GetString(buffer, 0, received);
                if (response.Contains("<|ACK|>"))
                {
                    Console.WriteLine(
                        $"Socket client received acknowledgment: \"{response.Split("<|")[0]}\"");
                    break;
                }
                // Sample output:
                //     Socket client sent message: "Hi friends 👋!<|EOM|>"
                //     Socket client received acknowledgment: "<|ACK|>"
            }

            client.Shutdown(SocketShutdown.Both);
        }
    }
}
