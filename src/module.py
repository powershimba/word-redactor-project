import random

def generate_word(words):
    return "".join(random.choice(['r', 'R']) for _ in range(len(words)))