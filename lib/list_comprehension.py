#!/usr/bin/env python3

def return_evens(num_list):
    evens = [x for x in num_list if x%2 == 0]
    return evens

def make_exclamation(sentence_list):
    exclamations =[sentence + '!' for sentence in sentence_list]
    return exclamations





input_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = return_evens(input_sequence)
print(result)

input_sentences = ["Hello", "How are you", "Python is fun"]
result4 = make_exclamation(input_sentences)
print(result4)