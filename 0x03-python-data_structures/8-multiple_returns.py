#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
    x = len(sentence)
    else:
        x = 0
    return (x, sentence if not sentence else sentence[:1])
