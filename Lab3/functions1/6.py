def invert_sent(s):
    words = s.split()
    inverted_sent = " ".join(reversed(words))
    return inverted_sent

s = "We are ready"
print(invert_sent(s))