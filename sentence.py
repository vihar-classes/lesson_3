input_sentence = input("sentece> ")
words_array = input_sentence.split(" ")
reversed_words = []

for word in words_array:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

final_output = " ".join(reversed_words)
print(f"original: {words_array}")
print(f"reversed: {final_output}")
