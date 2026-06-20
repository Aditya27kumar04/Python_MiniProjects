# 🃏 Blackjack Game

A simple command-line Python application that simulates the classic **Blackjack (21)** card game. Play against the computer, draw cards strategically, and try to get as close to 21 as possible without going over.

---

## 📌 Features

* Random card dealing
* Automatic Blackjack detection
* Ace value adjusts from **11** to **1** when necessary
* Computer dealer follows standard Blackjack rules
* Play multiple rounds without restarting the program
* Clean and modular code using functions

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
Blackjack_Game/
│
├── main.py
├── Art.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd Blackjack_Game
```

3. Run the program:

```bash
python main.py
```

---

## 📖 How It Works

1. The player and the computer are each dealt two cards.
2. The player's current score and one of the computer's cards are displayed.
3. The player chooses whether to draw another card or pass.
4. If the player's score exceeds 21, they lose immediately.
5. The computer continues drawing cards until its score reaches at least 17.
6. The final scores are compared, and the winner is announced.

---

## 🎯 Concepts Practiced

* Functions
* Lists
* Loops
* Conditional Statements
* Random Module
* Game Logic
* Modular Programming

---

## 💡 Sample Output

```text
Your cards: [10, 7], current score: 17
Computer's first card: 9

Type 'yes' to get another card, type 'no' to pass:
no

===== FINAL RESULT =====
Your final hand: [10, 7], final score: 17
Computer's final hand: [9, 8], final score: 17

Draw
```

---

## 👨‍💻 Author

**Aditya Kumar**
