# 🎯 Number Guessing Game

A simple command-line Number Guessing Game built with Python. The computer randomly generates a number between **1 and 100**, and your goal is to guess it within a limited number of attempts. Choose between **Easy** and **Hard** difficulty levels and use the hints to find the correct number.

---

## 📌 Features

* 🎲 Random number generation
* 🎮 Two difficulty levels

  * **Easy:** 10 attempts
  * **Hard:** 5 attempts
* 📉 Hints after every guess

  * Too High
  * Too Low
* 🏆 Win message when the correct number is guessed
* ❌ Game Over message when all attempts are used
* 🎨 ASCII art welcome screen

---

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── Guessing_Main.py      # Main game logic
├── Art.py                # ASCII art/logo
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system

### Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Number-Guessing-Game.git
```

2. Navigate to the project directory

```bash
cd Number-Guessing-Game
```

3. Run the game

```bash
python Guessing_Main.py
```

---

## 🎮 How to Play

1. Run the program.
2. Choose a difficulty level:

   * **Easy** → 10 attempts
   * **Hard** → 5 attempts
3. Enter your guess.
4. The game will tell you whether your guess is:

   * **Too High**
   * **Too Low**
5. Continue guessing until you find the correct number or run out of attempts.

---

## 💻 Sample Output

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Choose a difficulty level. Type 'easy' or 'hard': easy

You have 10 attempts remaining.
Make a guess: 50

Too High!
Guess again.

You have 9 attempts remaining.
Make a guess: 25

Too Low!
Guess again.

You got it! The answer was 37.
```

---

## 🛠️ Technologies Used

* Python 3
* Random Module

---

## 📚 Concepts Practiced

* Functions
* Loops
* Conditional Statements
* User Input
* Variables
* Random Number Generation
* Modular Programming

---

## 🔮 Future Improvements

* Add a replay option
* Validate invalid user input
* Add score tracking
* Multiple difficulty levels
* Leaderboard
* GUI version using Tkinter or Pygame

---

## 👨‍💻 Author

**Aditya Kumar**

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
