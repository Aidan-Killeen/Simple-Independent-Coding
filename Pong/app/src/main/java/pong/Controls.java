package pong;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Controls extends KeyAdapter
{
    Paddle player;
    boolean launched = false;
    boolean up = false;
    boolean down = false;

    Controls(Paddle player)
    {
        this.player = player;
    }

    @Override
    public void keyPressed(KeyEvent e)
    {
        //System.out.println("Key pressed");
        int key = e.getKeyCode();
        if(key == KeyEvent.VK_ENTER)
        {
            launched = true;
        }
        if(key == KeyEvent.VK_W)
            up = true;
        else if(key == KeyEvent.VK_S)
            down = true;
    }

    @Override
    public void keyReleased(KeyEvent e)
    {
        int key = e.getKeyCode();

        if(key == KeyEvent.VK_W)
            up = false;
        else if(key == KeyEvent.VK_S)
            down = false;
    }
}
