import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;


public class Pong extends Canvas implements Runnable
{
    private static final int SCREEN_WIDTH = 400;
    private static final int SCREEN_HEIGHT = 400;
    private void draw() 
    {
        return;
    }
    @Override
    public void run()
    {
        return;
    }

    Pong()
    {
        //Setup Canvas
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
		this.setMaximumSize(new Dimension(WIDTH, HEIGHT));
		this.setMinimumSize(new Dimension(WIDTH, HEIGHT));
    }

    public static void main(String[] args)
    {
        new Pong();
    }
}