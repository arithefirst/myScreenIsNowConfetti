# MY SCREEN IS NOW CONFETTI! 🎉

A fast-paced survival game built with Pygame where you dodge enemies while collecting power-ups to stay alive!

## 🎮 Gameplay

Survive waves of enemies that spawn from the edges of the screen and move towards the center. Collect health power-ups to restore your health and see how long you can last as the difficulty increases!

### Features
- **Dynamic Difficulty**: Enemies spawn faster and move quicker as you progress through stages
- **Power-ups**: Health restoration items and time slow effects spawn randomly to help you survive
- **Particle Effects**: Explosion effects when enemies are destroyed or power-ups are collected
- **Stage Progression**: Multiple background themes that change as you advance
- **Score System**: Earn points for surviving and lose points for taking damage

## 🎯 Controls

- **Movement**: WASD or Arrow Keys
- **Precision Mode**: Hold Shift to move at half speed
- **Start Game**: Space (on start screen)
- **Restart**: R (on game over screen)

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Pygame library

### Installation

1. Clone or download this repository
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## 🎵 Audio Credits

Background music: ["Strawberry Cake" by nobonoko](https://www.youtube.com/watch?v=S_kxr-erXB8&pp=ygUdIlN0cmF3YmVycnkgQ2FrZSIgYnkgbm9ib25va28%3D)


## 🎯 Game Mechanics

### Health System
- Start with 3 health points
- Lose 1 health when touching an enemy
- Collect health power-ups to restore health (max 3)
- Game ends when health reaches 0

### Power-up System
- **Health Power-up** (Red Heart): Restores 1 health point (up to maximum of 3)
- **Time Slow Power-up** (Hourglass): Slows down all enemy movement by 50% for 4.5 seconds
- Power-ups spawn randomly every 5-7 seconds
- Health power-ups only work if you're below maximum health
- Time slow effect doesn't stack - collecting another while active has no effect

### Scoring
- +10 points for each enemy that self-destructs
- -25 points for taking damage (minimum score: 0)

### Stage Progression
The game features 6 stages (0-5) plus an endless mode:
- Enemy spawn rate increases each stage
- Enemy movement speed increases
- Background themes change
- Stage 6+ becomes "ENDLESS" mode