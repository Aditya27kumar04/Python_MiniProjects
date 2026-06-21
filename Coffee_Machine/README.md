# ☕ Coffee Machine Simulator

A command-line Python application that simulates a coffee vending machine. Users can choose a drink, insert coins, and receive coffee if there are enough resources and payment is successful.

---

## 📌 Features

* ☕ Order **Espresso**, **Latte**, or **Cappuccino**
* 💰 Coin-based payment system
* 💵 Calculates and returns change
* 📦 Tracks available resources (water, milk, coffee)
* 📊 Displays machine report
* 🚫 Prevents orders when resources are insufficient
* 🔴 Allows the machine to be turned off

---

## 🛠️ Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* Conditional Statements

---

## 📂 Project Structure

```text
CoffeeMachine/
│── main.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd CoffeeMachine
```

3. Run the program:

```bash
python main.py
```

---

## ☕ Available Drinks

| Drink      |  Cost |
| ---------- | ----: |
| Espresso   | $1.50 |
| Latte      | $2.50 |
| Cappuccino | $3.00 |

---

## 💰 Accepted Coins

* Quarter = $0.25
* Dime = $0.10
* Nickel = $0.05
* Penny = $0.01

---

## 📷 Sample Output

```text
☕ What would you like? (espresso/latte/cappuccino): latte

💰 Please insert coins.
How many quarters?: 12
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

💵 Here is $0.50 in change.
☕ Here is your latte. Enjoy! 😊
```

---

## 📚 Concepts Practiced

* Functions
* Dictionaries
* Nested Dictionaries
* Loops
* Conditional Logic
* Variable Scope (`global`)
* Resource Management
* User Input Handling

---

## 🎯 Learning Outcome

This project strengthened my understanding of Python fundamentals by combining functions, dictionaries, loops, and conditional statements to build a real-world command-line application that simulates a coffee vending machine.
