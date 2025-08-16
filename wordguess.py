import random

user = input("Enter your name: ")
print(f"Welcome {user} to the Word Guessing Game!")

words = [
    "python", "java", "scratch", "algebra", "javascript", "html", "csharp", "kotlin", "ruby", "swift",
    "binary", "matrix", "function", "variable", "operator", "loop", "recursion", "pointer", "compile", "debug",
    "science", "physics", "chemistry", "biology", "atom", "neutron", "proton", "gravity", "energy", "force",
    "math", "geometry", "calculus", "trigonometry", "probability", "theorem", "algebraic", "integral", "vector", "logic",
    "computer", "hardware", "software", "network", "server", "database", "algorithm", "machine", "learning", "neuron"
]

word = random.choice(words)
guessed_letters = ""
turns = 10

while turns > 0:
    failed = 0

    # Show the word progress
    for char in word:
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()  # newline after showing word progress

    # Win check
    if failed == 0:
        print(f"\n Congratulations {user}! You've guessed the word '{word}' correctly!")
        break

    # Player input
    guess = input("\nGuess a letter or the full word: ").lower()

    # If player guessed the whole word
    if guess == word:
        print(f"\n Congratulations {user}! You guessed the whole word '{word}' directly!")
        break

    # If it's a single character
    elif len(guess) == 1:
        if guess in guessed_letters:
            print(f" You've already guessed '{guess}'. Try a different letter.")
        else:
            guessed_letters += guess
            if guess not in word:
                turns -= 1
                print(f" Sorry {user}, '{guess}' is not in the word.")
                print(f"You have {turns} turns left.")
    else:
        print(" Please enter either a single letter or the full word.")

    # Game over check
    if turns == 0:
        print(f"\n Game Over {user}! The word was '{word}'.")
