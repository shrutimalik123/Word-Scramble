import random

def word_scramble():
    # 1. Setup the Word Bank
    words = ["python", "coding", "jupiter", "galaxy", "keyboard", "science"]
    target_word = random.choice(words)
    
    # 2. Scramble the Word
    # Convert string to list so we can shuffle it
    scrambled = list(target_word)
    random.shuffle(scrambled)
    # Join the list back into a string
    display_scramble = "".join(scrambled)

    attempts = 3
    print("--- 🔀 Word Scramble 🔀 ---")
    print(f"Unscramble the letters to find the word: **{display_scramble}**")

    # 3. Game Loop
    while attempts > 0:
        guess = input(f"\nYour guess ({attempts} left): ").lower().strip()

        if guess == target_word:
            print("🎉 **Correct!** You're a word master!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("❌ Not quite! Try again.")
            else:
                print(f"💀 Out of turns! The word was: **{target_word}**")

# Start the game
word_scramble()
