package pong;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;

public class Pong extends Canvas implements Runnable
{
    public static final int SCREEN_WIDTH = 900;    //Change this to be package visable only
    public static final int SCREEN_HEIGHT = 800;
    public static final int MARGIN = 10;

    private Paddle player;
    private Paddle ai;
    private Ball ball;

    private Thread gameThread;
    private boolean running;
    private boolean gameEnd;

    private Controls controls;

    private void draw() 
    {
        //creating screen
        BufferStrategy buffer = this.getBufferStrategy();
        if(buffer == null)
        {
            this.createBufferStrategy(3);
            return;
        }

        Graphics g = buffer.getDrawGraphics();

        g.setColor(Color.BLACK);
        g.fillRect(0, 0, SCREEN_WIDTH , SCREEN_HEIGHT);

        //Draw Gameplay elements
        if(!gameEnd)
        {
            //Ball
            if(controls.launched)
                ball.update();
            ball.draw(g);
            checkIfScored();

            //Player Paddle
            player.update(ball, controls);
            player.draw(g);
            ball.collision(player);

            //AI Paddle
            ai.update(ball, controls);
            ai.draw(g);
            ball.collision(ai);
        }
        //Game has ended
        else
        {
            //Show Outcome of the game
            g.setColor(Color.WHITE);
            g.setFont(new Font("TimesRoman", Font.PLAIN, 80)); 
            String outcome = "You Won!";
            if(player.lostGame())
            {
                outcome = "You Lost.";
            }

            int offsetX = g.getFontMetrics().stringWidth(outcome)/2;
            g.drawString(outcome, SCREEN_WIDTH/2-offsetX, SCREEN_HEIGHT/2);

            //Instructions to Continue playing
            g.setFont(new Font("TimesRoman", Font.PLAIN, 40));
            String newGame = "Press Enter to start a new game.";
            offsetX = g.getFontMetrics().stringWidth(newGame)/2;
            g.drawString(newGame, SCREEN_WIDTH/2-offsetX, SCREEN_HEIGHT/2+80);

        }
        g.dispose();
        buffer.show();

    }

    public void checkIfScored()
    {
        if(ball.getX() < 0)
        {
            controls.launched = false;
            ai.lostLife();
            ball.reset(true);
        }
        else if(ball.getX() > SCREEN_WIDTH)
        {
            controls.launched = false;
            player.lostLife();
            ball.reset(false);
        }
        if(player.lostGame() || ai.lostGame())
        {
            gameEnd = true;
        }
        

    }

    public boolean getGameEnd()
    {
        return gameEnd;
    }

    public void setGameEnd(boolean end)
    {
        gameEnd = end;
    }

    @Override
    public void run()
    {
        this.requestFocus();
        while(running)
        {
            draw();
        }
        draw();
    }

    public void start()
    {
        gameThread = new Thread(this);
        gameThread.start();

        running = true;
        gameEnd = false;
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
        controls = new Controls(player, ai);
        this.addKeyListener(controls);
        this.setFocusable(true);

    }

   
    public static Pong p;
    
    public static void main(String[] args)
    {
        p = new Pong();
        //System.out.println("Working");
    }
}