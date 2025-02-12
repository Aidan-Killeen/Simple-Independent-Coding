import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Pong extends Canvas implements Runnable
{
    public static final int SCREEN_WIDTH = 800;    //Change this to be package visable only
    public static final int SCREEN_HEIGHT = 800;
    public static final int MARGIN = 10;

    private Paddle player;
    private Paddle ai;
    private Ball ball;

    private Thread gameThread;
    private boolean running;

    Controls controls;

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
        if(controls.launched)
            ball.update();
        ball.draw(g);

        //Paddle
        player.update();
        player.draw(g);

        ai.update();
        ai.draw(g);

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
        ball = new Ball(1);
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
        controls = new Controls(player);
        this.addKeyListener(controls);
        this.setFocusable(true);

    }

   

    public static void main(String[] args)
    {
        new Pong();
        //System.out.println("Working");
    }
}