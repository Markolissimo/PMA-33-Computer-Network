using System.Net;
using System.Net.Sockets;
using System.Text;

namespace CLIENT
{
    public partial class Form1 : Form
    {
        Socket s1;
        IPAddress adr;
        IPEndPoint ipEnd;
        public Form1()
        {
            InitializeComponent();
            s1 = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            adr = Dns.Resolve("localhost").AddressList[1];
            ipEnd = new IPEndPoint(adr, 8086);
            s1.Connect(ipEnd);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string word = textBox1.Text;
                bool check = word.All(Char.IsLetter);
                if (check)
                {
                    byte[] msg = Encoding.ASCII.GetBytes(word);
                    s1.Send(msg);
                    byte[] R = new byte[1024];
                    int bytesRec = s1.Receive(R);
                    textBox2.Text = $"У введеному слові {R[0]} лiтер";

                }
                else
                    throw new FormatException("Ви ввели не слово.");
            }
            catch (FormatException ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox1.Clear();
            }

        }
    }
}