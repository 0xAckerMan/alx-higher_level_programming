#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        y = None
    else:
        y = sentence[0]
    return (x, y)


if __name__ == "__main__":
    sentence = ""
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
