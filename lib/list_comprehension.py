#!/usr/bin/env python3

def return_evens(num_list):
    even = [num for num in num_list if num%2==0]
    return even
    


def make_exclamation(sentence_list):
    return ([sent+'!' for sent in sentence_list])