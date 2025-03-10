package pong;

import java.awt.Color;
import java.awt.Graphics;

public class Ball 
{
    static final int RADIUS = 8;

    private double x;
    private double y;

    private double xSpeed;
    private double ySpeed;
    private final int speed;

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
        x = (double)Pong.SCREEN_WIDTH/2;
        y = (double)Pong.SCREEN_HEIGHT/2;

        //choose random xSpeed, xSpeed and ySpeed
        int xDir = (Math.random() < .5)?(1):(-1);
        int yDir = (Math.random() < .5)?(1):(-1);
        
        xSpeed = (double)speed * xDir;
        ySpeed = (double)speed*speedMultiplier*yDir;

        if(playerWon)
            speedMultiplier *=2;
    }

    public void collision(Paddle player)
    {
        if(player.ai)
        {
            if(x-RADIUS <= player.getRight() && x >= player.getLeft() && player.inRange((int)y))
            {
                xSpeed = Math.abs(xSpeed);
                ySpeed = ySpeed + (double)player.paddleSpeed/10;
            }
        }
        else
        {
            if(x+RADIUS >= player.getLeft() && x <= player.getRight() && player.inRange((int)y))
            {
                xSpeed = -Math.abs(xSpeed);
                ySpeed = ySpeed + (double)player.paddleSpeed/10;
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
        g.fillOval((int)x, (int)y, RADIUS, RADIUS);
    }

    public int getX()
    {
        return (int)x;
    }

    public int getY()
    {
        return (int)y;
    }
        
}
