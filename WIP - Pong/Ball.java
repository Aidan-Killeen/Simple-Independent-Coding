import java.awt.Color;
import java.awt.Graphics;

public class Ball 
{
    static final int radius = 8;
    private int x, y;
    private int xDir, yDir;
    private int speed;

    private double speedRandMax = 2;
    private double speedRandMin = -2;

    double yMax = Pong.SCREEN_HEIGHT - radius;
    double yMin = radius;

    Ball(int speed)
    {
        this.speed = speed;
        reset();
    }

    public void reset()
    {
        x = Pong.SCREEN_WIDTH/2;
        y = Pong.SCREEN_HEIGHT/2;

        xDir = (int)(Math.random() * (speedRandMin+speedRandMax+1) + speedRandMin);
        yDir = 2*speed;

    }

    public void update()
    {
        x = x + xDir;
        y = y + yDir;
    }

    public void draw(Graphics g)
    {
        g.setColor(Color.WHITE);
        g.fillOval(x, y, radius, radius);
    }
}
