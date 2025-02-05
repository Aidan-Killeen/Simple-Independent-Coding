import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Pong extends Canvas implements Runnable
{
    private static final int SCREEN_WIDTH = 400;
    private static final int SCREEN_HEIGHT = 400;

    private Paddle player;
    private Paddle ai;
    private Ball ball;

    private Thread gameThread;
    private boolean running;

    boolean launched = false;

    private void draw() 
    {
        BufferStrategy buffer = this.getBufferStrategy();
        if(buffer == null)
        {
            this.createBufferStrategy(3);
            return;
        }

        Graphics g = buffer.getDrawGraphics();

        g.setColor(Color.BLACK);
        g.fillRect(0, 0, SCREEN_WIDTH , SCREEN_HEIGHT);

        //Ball
        if(launched)
            ball.update();
        ball.draw();

        //Paddle
        player.update();
        player.draw();

        ai.update();
        ai.draw();

        g.dispose();
        buffer.show();

    }
    @Override
    public void run()
    {
        this.requestFocus();
        while(running)
        {
            draw();
        }
    }

    public void start()
    {
        gameThread = new Thread(this);
        gameThread.start();

        running = true;
    }

    private void stop()
    {
        try
        {
            gameThread.join();
            running = false;
        }
        catch(InterruptedException e)
        {
            e.printStackTrace();
        }
    }

    Pong()
    {
        //Setup Canvas
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
		this.setMaximumSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
		this.setMinimumSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));

        //new game setup
        ball = new Ball();
        player = new Paddle(false);
        ai = new Paddle(true);

        //Window
        JFrame frame = new JFrame("Pong");
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
		
		frame.add(this);
		frame.pack();
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
		
		this.start();

        this.setFocusable(true);

    }

   

    public static void main(String[] args)
    {
        new Pong();
        //System.out.println("Working");
    }
}