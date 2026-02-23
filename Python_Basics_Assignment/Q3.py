# string manipulator
# takes a sentence from user and shows different things about it

sentence = input("enter a sentence: ")
word_list = sentence.split()

print("your sentence:", sentence)
print("length with spaces:", len(sentence))
print("length without spaces:", len(sentence.replace(" ", "")))
print("number of words:", len(word_list))
print("in uppercase:", sentence.upper())
print("in lowercase:", sentence.lower())
print("title case:", sentence.title())
print("first word:", word_list[0] if word_list else "no words found")
print("last word:", word_list[-1] if word_list else "no words found")
print("reversed sentence:", sentence[::-1])