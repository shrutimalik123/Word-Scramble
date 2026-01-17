# 🔀 Word Scramble - Text Puzzle Game

A fun word-puzzle game where players must unscramble a randomly shuffled word. This project is a great way to learn how to manipulate strings and utilize Python's built-in randomization tools.

This project focuses on teaching:
* **Immutability vs Mutability:** Understanding why we must convert strings to lists to change them.
* **The `.join()` Method:** Learning how to combine list elements into a single string.
* **Random Shuffling:** Using `random.shuffle()` to reorganize data.
* **Basic Game State:** Managing a "lives" or "attempts" system.

---

## ✨ Features

* **Dynamic Scrambling:** Every time you play, the word is shuffled differently.
* **Word Bank:** Easily expandable list of hidden words.
* **Limited Attempts:** Players have 3 chances to guess the word before the game ends.
* **Case Insensitivity:** Automatically handles uppercase or lowercase guesses.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `word_scramble.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python word_scramble.py
    ```

### 3. Gameplay Instructions
1.  Look at the scrambled letters provided (e.g., `o-p-y-h-t-n`).
2.  Type your best guess of what the original word is.
3.  You have **3 attempts** to get it right!

---

## 🧠 Code Structure Highlights

### Converting Strings for Shuffling
In Python, strings cannot be changed once created (**immutable**). To scramble a word, we have to convert it into a list, shuffle it, and then "glue" it back together into a string.



```python
scrambled = list(target_word) # Convert to list
random.shuffle(scrambled)     # Shuffle the items
display_scramble = "".join(scrambled) # Join back to string

