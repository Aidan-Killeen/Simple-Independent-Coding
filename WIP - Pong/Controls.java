import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Controls extends KeyAdapter
{
    Paddle player;
    boolean launched = false;

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
    }
}
