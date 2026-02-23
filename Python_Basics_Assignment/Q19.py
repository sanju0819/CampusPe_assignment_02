# Text Analysis Program
# contains multiple text processing functions

# 1. count words
def count_words(text):
    words = text.split()   # split text by spaces
    return len(words)


# 2. count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# 3. count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        # check alphabet and not vowel
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# 4. reverse text
def reverse_text(text):
    return text[::-1]   # slicing method


# 5. check palindrome
def is_palindrome(text):
    # remove spaces and make lowercase for proper check
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# 6. remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result


# 7. word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        # remove punctuation from word
        word = word.strip(".,!?;:")
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


# 8. longest word
def longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        clean_word = word.strip(".,!?;:")
        if len(clean_word) > len(longest):
            longest = clean_word

    return longest


# 9. main analysis function
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    long_word = longest_word(text)
    print(f"Longest word: {long_word} ({len(long_word)} letters)")

    freq = word_frequency(text)
    print("Word Frequency:", end=" ")

    # printing dictionary in required format
    freq_list = []
    for key in freq:
        freq_list.append(f"{key}: {freq[key]}")
    print(", ".join(freq_list))


#  main execution 

user_text = input("Enter text: ")

# check empty input
if user_text.strip() == "":
    print("Text cannot be empty.")
else:
    analyze_text(user_text)