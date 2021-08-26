import random

# Open the txt file
# TODO REPLACE THIS WITH YOUR FILE PATH
f = open('words.txt', 'r')

# Set what length of word you want to work with
word_len = 4

# Set how many words an ending needs to have to be included
num_words = 30

# Store each line to a list of words
unprocessed_words = f.readlines()



# Create a list for the useable words
words = []

for word in unprocessed_words:
    # Convert the word to lowercase and clean it
    word = word.lower().strip()

    # Ignore words containing an apostrophe
    if "'" in word:
        continue

    # If the word is 4 letters long, add it to our new list of words to use
    if len(word) == word_len:
        # Only add it if it's not already in the list, so we get each word once
        if word not in words:
            words.append(word)

# Print the number of unique four letter words
print(f'There are {len(words)} unique, {word_len} letter words in the text file\n')



# Create a dictionary for the word endings
word_endings = {}

# To calculate how many words each ending has
for word in words:
    # Extract the last two letters of the word
    word_end = word[-2:]

    # If the ending isn't in the dictionary, add it and give a value of 1
    if word_endings.get(word_end) is None:
        word_endings[word_end] = [word]

    # If it is in the list, increase its dictionary entry value by 1
    else:
        word_endings[word_end].append(word)


# Create a dictionary with the ending and length of its list of words
# This gives a dict with the freqency of each ending
ending_freq = {k:len(v) for (k,v) in word_endings.items()}

# Sort that dictionary by the number of words
# So the ending with the most words will be at the top
ending_freq = dict(sorted(ending_freq.items(), key=lambda item: item[1], reverse=True))


# Create a list for the popular word endings
popular_endings = []

# Print a title for the ending frequencies
print('| Ending | Frequency |')

# Run through the dictionary and extract the ending and its frequency
for end, freq in ending_freq.items():
    # If that frequency is 30 or over
    if freq >= num_words:
        # Print the ending and the frequency for the user
        print(f'|{end:^8}|{freq:^11}|')

        # Add the ending to a list of only our popular endings
        popular_endings.append(end)



# Create a list for our final words
final_words = []

# We want to pick a word for each ending in our popular endings list
for ending in popular_endings:

    # For each ending, take one of it's words randomly from the endings dictionary
    # and add it to a variable
    chosen_word = random.choice(word_endings[ending])

    # Add this word to our final list of words
    final_words.append(chosen_word)


# We print the length of the list
print(f'\nThere are {len(final_words)} words in our stimuli list:', end=' ')
# And its contents
for word in final_words:
    print(f'{word},', end=' ')

# Close the text file
f.close()
