package task3;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.util.Arrays;


public class JavaUdpServer {

    public static void main(String args[])
    {
        System.out.println("JAVA UDP SERVER");
        DatagramSocket socket = null;
        int portNumber = 9008;

        try{
            socket = new DatagramSocket(portNumber);
            byte[] receiveBuffer = new byte[1024];

            while(true) {
                //Arrays.fill(receiveBuffer, (byte)0);
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);
                byte[] msg = receivePacket.getData();
                msg = Arrays.copyOfRange(msg, 0, 4);
                for(byte b : msg){
                    System.out.println(b);
                }
                System.out.println();
                int nb = ByteBuffer.wrap(msg).getInt();
                System.out.println(nb);
                System.out.println("ok");

                InetAddress address = receivePacket.getAddress();
                int port = receivePacket.getPort();
                byte[] sendBuffer =  ByteBuffer.allocate(4).putInt(nb+1).array();

                DatagramPacket packet = new DatagramPacket(sendBuffer, sendBuffer.length, address, port);
                socket.send(packet);
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}
