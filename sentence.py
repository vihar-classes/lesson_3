def remove_adjacent_duplicates(s):
    result = []
    i = 0
    while i < len(s):
        if not result or s[i] != result[-1]:
            result.append(s[i])
            i += 1
        else:
            result.pop()
            i += 1
            
    final_string = "".join(result)
    if final_string != s:
        return remove_adjacent_duplicates(final_string)
    else:
        return final_string


def find_longest_palindrome(words):
    longest_palindrome = ""
    for word in words:
        if word == word[::-1]:
            if len(word) > len(longest_palindrome):
                longest_palindrome = word
    return longest_palindrome


input_sentence = input("sentece> ")
processed_sentence = remove_adjacent_duplicates(input_sentence)
words_array = processed_sentence.split(" ")
reversed_words = []

for word in words_array:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

final_output = " ".join(reversed_words)
longest_palindrome = find_longest_palindrome(words_array)

print(f"cleaned string: {processed_sentence}")
print(f"original words: {input_sentence.split(' ')}")
print(f"words after cleaning: {words_array}")
print(f"reversed words: {final_output}")

if longest_palindrome:
    print(f"longest palindrome: '{longest_palindrome}' (Length: {len(longest_palindrome)})")
else:
    print("no palindromic word found.")
