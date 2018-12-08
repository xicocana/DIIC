package com.example.t3.diicandroid;

import android.content.Context;
import android.location.Location;
import android.os.AsyncTask;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

import twitter4j.StatusUpdate;
import twitter4j.TwitterException;

public class SendLocationTask extends AsyncTask<Context, Void, Void> {

    protected Void doInBackground(Context... params) {
        try {
            Context context = params[0];

            MainActivity mainActivity = (MainActivity) context;
            if (mainActivity == null) return null;

            String messageStr = mainActivity.lastLocation.getLatitude() + " " + mainActivity.lastLocation.getLongitude();
            /*
            int server_port = 5500;
            DatagramSocket s = new DatagramSocket();
            InetAddress local = InetAddress.getByName("192.168.1.5");
            int msg_length = messageStr.length();
            byte[] message = messageStr.getBytes();
            DatagramPacket p = new DatagramPacket(message, msg_length, local, server_port);
            s.send(p);
            */
            mainActivity.twitter.updateStatus(messageStr);
        }
        catch (TwitterException te) {
            te.printStackTrace();
        }
        /*
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
        return null;
    }
}
