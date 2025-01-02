import re

with open("the-verdict.txt", "r") as file:
    raw_text = file.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print("preprocessed:", preprocessed[:10])
print("len(preprocessed):", len(preprocessed))

all_words = sorted(list(set(preprocessed)))
print("len(all_words):", len(all_words))

# creating vocabulary
