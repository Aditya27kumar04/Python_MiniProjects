# ☕ Coffee Machine Simulator

A command-line Python application that simulates a coffee vending machine. Users can order coffee, insert coins, receive change, and the machine automatically manages its available resources.

---

## 📌 Features

* ☕ Order **Espresso**, **Latte**, or **Cappuccino**
* 💰 Coin-based payment system
* 💵 Calculates and returns change
* 📦 Tracks available resources (water, milk, and coffee)
* 📊 Displays the current machine report
* 🚫 Prevents orders when resources are insufficient
* 🔴 Turn the machine off using the `off` command

---

## 🛠️ Technologies Used

* Python 3
* Functions
* Dictionaries
* Loops
* Conditional Statements
* User Input Handling

---

## 📂 Project Structure

```text
Coffee_Machine/
├── Coffee_Machine_main.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Python_MiniProjects.git
```

2. Navigate to the project folder:

```bash
cd Python_MiniProjects/Coffee_Machine
```

3. Run the program:

```bash
python Coffee_Machine_main.py
```

---

## ☕ Available Drinks

| Drink      |  Cost |
| :--------- | ----: |
| Espresso   | $1.50 |
| Latte      | $2.50 |
| Cappuccino | $3.00 |

---

## 💰 Accepted Coins

* Quarter = **$0.25**
* Dime = **$0.10**
* Nickel = **$0.05**
* Penny = **$0.01**

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

This project helped me strengthen my understanding of Python fundamentals by combining functions, dictionaries, loops, conditional statements, and user input handling to build a real-world command-line coffee vending machine simulation.
