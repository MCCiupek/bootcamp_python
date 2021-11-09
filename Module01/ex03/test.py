from generator import generator

text = "Le Lorem Ipsum est simplement du faux texte."

print("--- NO OPT ---")
for word in generator(text, sep=" "):
    print(word)

print("--- UNIQUE ---")
for word in generator(text, sep=" ", option="unique"):
    print(word)

print("--- SHUFFLE ---")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("--- ORDERED ---")
for word in generator(text, sep=" ", option="ordered"):
    print(word)

print("--- UNKNOWN ---")
for word in generator(text, sep=" ", option="unknown"):
    print(word)

print("--- NOT STR ---")
for word in generator(1.0, sep=" ", option="unknown"):
    print(word)