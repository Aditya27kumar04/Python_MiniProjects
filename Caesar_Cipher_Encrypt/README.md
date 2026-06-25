# 🔐 Caesar Cipher Encrypt & Decrypt

A simple command-line Python application that encrypts and decrypts messages using the classic **Caesar Cipher** encryption technique.

The program allows users to repeatedly encode or decode messages by providing a shift value, while preserving spaces, numbers, and special characters.

---

## 📌 Features

- 🔒 Encrypt any text using the Caesar Cipher
- 🔓 Decrypt encrypted messages
- 🔁 Run the program multiple times without restarting
- 🔤 Supports both uppercase and lowercase input
- 📝 Preserves spaces, punctuation, and numbers
- 🧮 Handles shift values greater than 26 using modulo arithmetic
- 🎨 Displays a custom ASCII art logo

---

## 🛠️ Technologies Used

- Python 3
- Functions
- Loops
- Lists
- Conditional Statements
- String Manipulation

---

## 📂 Project Structure

```
Caesar_Cipher_Encrypt/
│
├── Caesar_Cipher.py      # Main program
├── art.py                # ASCII logo
└── README.md             # Project documentation
```

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/Python_MiniProjects.git
```

2. Navigate to the project folder:

```bash
cd Python_MiniProjects/Caesar_Cipher_Encrypt
```

3. Run the program:

```bash
python Caesar_Cipher.py
```

---

## 💻 Example

```
Type 'encode' to encrypt or 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here is the encoded result:
mjqqt btwqi

Type 'yes' if you want to go again. Otherwise type 'no':
yes
```

---

## 📖 How Caesar Cipher Works

Each letter in the message is shifted forward (or backward) by a fixed number of positions in the alphabet.

Example (Shift = 3)

```
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

For decryption, the same shift is applied in the opposite direction.

---

## 🎯 Concepts Practiced

- Function Creation
- Parameter Passing
- While Loops
- List Indexing
- Modulo Operator (`%`)
- String Traversal
- Conditional Logic
- Python Modules (`import`)

---

## 🚀 Future Improvements

- Add support for custom alphabets
- Preserve original letter casing
- Add file encryption/decryption
- Build a GUI version using Tkinter
- Support multiple encryption algorithms

---

## 👨‍💻 Author

**Aditya Kumar**

Learning Python by building real-world mini projects 🚀