# Brick Breaker Game

A classic brick-breaking arcade game built with Python and Turtle graphics. Control a paddle to bounce a ball around the screen, destroy coloured bricks, and earn points while trying to avoid losing all your lives.

## Features

- Control the paddle using the left and right arrow keys.
- Bounce the ball off the paddle and walls.
- Break coloured bricks to earn points, with different brick colours awarding different scores.
- Track your score, remaining lives, and high score.
- Increase the game difficulty as your score progresses.

## Technologies

- Python
- Turtle graphics
- Object-oriented programming

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SinceSlicedBread/brick-breaker-game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd brick-breaker-game
   ```

3. Run the game:

   ```bash
   python main.py
   ```

No external dependencies are required beyond Python's standard library.

## How to Play

- **Left Arrow:** Move the paddle left.
- **Right Arrow:** Move the paddle right.
- Bounce the ball off the paddle to break the bricks.
- Earn points by destroying bricks and try to beat your high score.

## Project Structure

- `main.py` — Initialises the game and manages the main game loop.
- `ball.py` — Handles ball movement, bouncing, and collision detection.
- `paddle.py` — Controls paddle movement.
- `bricks.py` — Defines the bricks and their scoring values.
- `scoreboard.py` — Tracks the score, lives, and high score.

## Purpose

This project demonstrates Python programming fundamentals, object-oriented design, game loops, collision detection, and event-driven keyboard controls.