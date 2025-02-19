
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
public class Paddle 
{
    static final int PADDLE_WIDTH = 10;
    static final int PADDLE_HEIGHT = 60;//Pong.SCREEN_HEIGHT;//30;
    static int yMaxLimit = Pong.SCREEN_HEIGHT - PADDLE_HEIGHT;
    static int yMinLimit = 0;

    private int xPos;
    private int yPos;
    private int base_speed = 2;

    public int lives = 3;
    public float paddleSpeed = 0;

    public boolean ai;

    Paddle(boolean ai)
    {
        this.ai = ai;
        yPos = Pong.SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2;
        if(ai)
            xPos = Pong.MARGIN;
        else
            xPos = Pong.SCREEN_WIDTH - Pong.MARGIN - PADDLE_WIDTH;
    }

    public void update(Ball ball, Controls controls)
    {
        //AI Controls
        if(ai)
        {
            yPos = ball.getY() - PADDLE_HEIGHT/2;
        }
        else
        {
            if(controls.up)
                yPos -= base_speed;
            if(controls.down)
                yPos += base_speed;
        }

        //
        //Keeping paddle in range
        if(yPos < 0)
        {
            yPos = 0;
        }
        if(yPos + PADDLE_HEIGHT > Pong.SCREEN_HEIGHT)
        {
            yPos = Pong.SCREEN_HEIGHT - PADDLE_HEIGHT;
        }
    }


    public void lostLife()
    {
        lives--;
    }

    public void draw(Graphics g)
    {
        g.setColor(Color.WHITE);

        g.fillRect(xPos, yPos, PADDLE_WIDTH, PADDLE_HEIGHT);
    }

    public int getLeft()
    {
        return xPos;
    }

    public int getRight()
    {
        return xPos+PADDLE_WIDTH;
    }

    public boolean inRange(int y)
    {
        return y >= yPos && y <= yPos + PADDLE_HEIGHT;
    }

}
