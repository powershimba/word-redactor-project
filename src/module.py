import random
import string

def count_char(words):
    cnt_list = [0, 0]
    for word in words:
        for char in word:
            if char.isupper():
                cnt_list[0] += 1
            elif char.islower():
                cnt_list[1] += 1
    return cnt_list

def generate_word(words):
    cnt_list = count_char(words)
    word = ''
    for i in range(cnt_list[0]):
        word += "R"
    for i in range(cnt_list[1]):
        word += "r"
    return word