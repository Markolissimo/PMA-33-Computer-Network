import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server {
    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(6667);
        Socket input = serverSocket.accept();
        Scanner in = new Scanner(input.getInputStream());
        System.out.println("Server Start...");
        String lineCapitalize = "";
        lineCapitalize += in.nextLine().toUpperCase();
        System.out.println("Result is:"+lineCapitalize);
        System.out.println("Server Finish...");

        in.close();
        input.close();
        serverSocket.close();
    }
}
