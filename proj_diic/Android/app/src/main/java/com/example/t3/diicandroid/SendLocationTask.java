package com.example.t3.diicandroid;

import android.location.Location;
import android.os.AsyncTask;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.HttpURLConnection;
import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.net.URL;
import java.net.UnknownHostException;

public class SendLocationTask extends AsyncTask<Location, Void, Void> {

    protected Void doInBackground(Location... location) {
        /*
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
        */
        try {
            URL url = new URL("http://urldeexemplo.com/");
            HttpURLConnection client = (HttpURLConnection) url.openConnection();
            String messageStr = "location=" + location[0].getLatitude() + ";" + location[0].getLongitude();

            client.setRequestMethod("POST");
            client.setDoOutput(true);

            OutputStream os = client.getOutputStream();
            os.write(messageStr.getBytes());
            os.flush();
        }
        catch(MalformedURLException error) {
            error.printStackTrace();
        }
        catch(SocketTimeoutException error) {
            error.printStackTrace();
        }
        catch (IOException error) {
            error.printStackTrace();
        }

        return null;
    }
}
