package com.example.t3.diicandroid;

import android.location.Location;
import android.os.AsyncTask;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class SendLocationTask extends AsyncTask<Location, Void, Void> {

    protected Void doInBackground(Location... location) {
        try {
            String messageStr = location[0].getLatitude() + " " + location[0].getLongitude();
            int server_port = 5500;
            DatagramSocket s = new DatagramSocket();
            InetAddress local = InetAddress.getByName("192.168.1.5");
            int msg_length = messageStr.length();
            byte[] message = messageStr.getBytes();
            DatagramPacket p = new DatagramPacket(message, msg_length, local, server_port);
            s.send(p);
        }
        catch (SocketException se) {
            System.out.println("Socket Exception:");
            se.printStackTrace();
        }
        catch (UnknownHostException uhe) {
            System.out.println("Unknown Host Exception:");
            uhe.printStackTrace();
        }
        catch (IOException ioe) {
            System.out.println("IO Exception:");
            ioe.printStackTrace();
        }
        return null;
    }
}
