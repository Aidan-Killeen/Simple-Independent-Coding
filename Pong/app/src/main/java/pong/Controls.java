package pong;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Controls extends KeyAdapter
{
    Paddle player, ai;
    boolean launched = false;
    boolean up = false;
    boolean down = false;

    Controls(Paddle player, Paddle ai)
    {
        this.player = player;
        this.ai = ai;
    }

    @Override
    public void keyPressed(KeyEvent e)
    {
        //System.out.println("Key pressed");
        int key = e.getKeyCode();
        if(key == KeyEvent.VK_ENTER)
        {
            if(!Pong.gameEnd)
                launched = true;
            else
            {
                player.reset();
                ai.reset();
                Pong.gameEnd = false;
            }
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
