# File Encryption / Decryption Tool

A simple Python project that can **encrypt** and **decrypt** both text and files.

This is a college project I built while learning the basics of how encryption
works in Python. The goal was to take something I read about (keeping data
private) and actually turn it into a small working program.

## What does this project do?

In simple words, **encryption** means scrambling a message so that nobody can
read it unless they have the secret "key". **Decryption** is the opposite —
turning the scrambled message back into the normal readable one.

This matters in real life. Businesses store a lot of private information like
customer details, passwords and documents. If those files ever get stolen,
encryption makes sure the thief just sees random characters instead of the real
data. That is the practical idea I wanted to explore with this tool.

So this program lets you:

- Encrypt and decrypt **plain text** that you type in
- Encrypt and decrypt **files** stored on your computer
- Choose between **two different methods** (explained below)

## How I am approaching it (two methods)

While learning, I found there are very simple ciphers and there are proper
secure ones. I decided to include both, because comparing them helped me
understand *why* the simple ones are not safe.

### 1. Caesar Cipher (the "learning" method)

This is one of the oldest and simplest ciphers. It works by shifting every
letter in the alphabet by a fixed number (the key). For example, with a shift
of 3, the letter `A` becomes `D`, `B` becomes `E`, and so on.

I am writing this one **from scratch** myself, because it shows how a cipher
actually works step by step.

> ⚠️ Note: The Caesar Cipher is **not secure** at all and should never be used
> for real data. It is only here to learn the concept.

### 2. Fernet encryption (the "proper" method)

For real, strong encryption I am using Python's `cryptography` library, which
gives us something called **Fernet**. Fernet uses a strong, well-tested
encryption method (AES) and handles all the difficult maths for us.

With this method, a secret **key** is generated and you need that same key to
decrypt the data again. This is much closer to how encryption is actually used
in the real world.

## Tools and technology used

- **Python 3**
- **cryptography** library (for the Fernet method)

## Planned project structure

```
encryption-decprytion-tool/
├── README.md          # this file
├── requirements.txt   # libraries the project needs
├── caesar_cipher.py   # the simple Caesar Cipher (text + files)
├── fernet_cipher.py   # the secure Fernet method (text + files)
└── main.py            # the menu that runs everything
```

## How it will be used

The plan is to run one file (`main.py`) which shows a simple menu in the
terminal, something like:

```
1. Encrypt text
2. Decrypt text
3. Encrypt a file
4. Decrypt a file
5. Exit
```

You pick an option, choose the method, and the program does the rest.

## Project steps (my plan)

1. Set up the project and write this README ✅ (this commit)
2. Build the Caesar Cipher for text and files
3. Build the Fernet method for text and files
4. Create the menu in `main.py` to connect everything
5. Test everything and finish the usage notes

## What I hope to learn

- How encryption and decryption actually work
- The difference between a weak cipher and a strong one
- How to use a real Python library to protect data
- How to organise a small project into separate files
