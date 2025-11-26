input_sentence = input("sentece> ")
words_array = input_sentence.split(" ")
reversed_words = []

for word in words_array:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

final_output = " ".join(reversed_words)
print(f"original: {words_array}")
print(f"reversed: {final_output}")

longest_palindrome = ""

for word in words_array:
    if word == word[::-1]:
        if len(word) > len(longest_palindrome):
            longest_palindrome = word
        
if longest_palindrome:
    print(f"longest palindrome: '{longest_palindrome}' (Length: {len(longest_palindrome)})")
else:
    print("no palindromic word found.")
