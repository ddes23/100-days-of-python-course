#Dictionary Comprehension
import random

names = ["Marty", "Doc", "Biff", "George", "Lorraine"]

scores = {character:random.randint(1,100) for character in names}

passed = {character:score for (character, score) in scores.items() if score >= 60}
print(scores)
print(passed)