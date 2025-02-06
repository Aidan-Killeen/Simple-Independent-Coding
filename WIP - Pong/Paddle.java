
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
public class Paddle 
{
    static final int PADDLE_WIDTH = 10;
    static final int PADDLE_HEIGHT = 30;
    static int yMaxLimit = Pong.SCREEN_HEIGHT - PADDLE_HEIGHT;
    static int yMinLimit = 0;

    private int xPos;
    private double yPos;

    public int lives = 3;
    public float paddleSpeed = 0;

    Paddle(boolean ai)
    {
        yPos = (double)Pong.SCREEN_HEIGHT/2 - (double)PADDLE_HEIGHT/2;
        if(ai)
            xPos = Pong.SCREEN_WIDTH - Pong.MARGIN - PADDLE_WIDTH;
        else
            xPos = Pong.MARGIN;
    }

    public void update()
    {

    }

    public void draw(Graphics g)
    {
        g.setColor(Color.WHITE);

        g.fillRect(xPos, (int)yPos, PADDLE_WIDTH, PADDLE_HEIGHT);
    }
}
