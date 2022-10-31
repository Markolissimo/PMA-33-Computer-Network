import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class ClientSocket {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("127.0.0.1",6667);
        PrintWriter out = new PrintWriter(socket.getOutputStream());
        Scanner in = new Scanner(System.in);
        System.out.println("Client start working...");
        System.out.println("Write line for capitalize:");
        String line= in.nextLine();
        System.out.println("Client finish working...");
        out.println(line);
        out.close();
        socket.close();

    }
}
