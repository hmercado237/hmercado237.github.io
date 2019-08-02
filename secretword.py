import random

# A list of words that
potential_words = ["pulchritudinous", "hippopotomonstrosesquipedaliophobic", "cupidity", "gasconading", "magnanimous"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()
# Make it a list of letters for someone to guess
print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
current_word = ["_ _ _ _ _ _ _ _ _ _ _ _ _ "] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
