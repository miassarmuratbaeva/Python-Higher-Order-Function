sentence = "Functional programming in Python is very powerful and elegant"
word = sorted(sentence.split(), key=lambda x: len(x), reverse=True)[:3]
print(word)