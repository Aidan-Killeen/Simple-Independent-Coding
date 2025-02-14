import java.awt.Color;
import java.awt.Graphics;

public class Ball 
{
    static final int RADIUS = 8;
    private int x, y;
    private int xSpeed, ySpeed;
    private int speed;

    private int speedMultiplier = 1;

    double yMax = Pong.SCREEN_HEIGHT - RADIUS;
    double yMin = RADIUS;

    Ball(int speed)
    {
        this.speed = speed;
        reset(false);
    }

    public void reset(boolean playerWon)
    {
        x = Pong.SCREEN_WIDTH/2;
        y = Pong.SCREEN_HEIGHT/2;

        //choose random xSpeed, xSpeed and ySpeed
        int xDir = (Math.random() < .5)?(1):(-1);
        int yDir = (Math.random() < .5)?(1):(-1);
        
        xSpeed = speed * xDir;
        ySpeed = speed*speedMultiplier*yDir;

        if(playerWon)
            speedMultiplier *=2;
    }

    public void collision(Paddle player)
    {
        if(player.ai)
        {
            if(x-RADIUS <= player.getX() && player.inRange(y))
            {
                xSpeed = -xSpeed;
            }
        }
        else
        {
            if(x+RADIUS >= player.getX() && player.inRange(y))
            {
                xSpeed = -xSpeed;
            }
        }
    }

    public void update()
    {
        x = x + xSpeed;
        y = y + ySpeed;

        if (y <= yMin || y >= yMax)
            ySpeed = -ySpeed;
    }

    public void draw(Graphics g)
    {
        g.setColor(Color.WHITE);
        g.fillOval(x, y, RADIUS, RADIUS);
    }

    public int getX()
    {
        return x;
    }

    public int getY()
    {
        return y;
    }
        
}
