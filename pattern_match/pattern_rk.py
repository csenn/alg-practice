# Rabin-Karp

d = 256

def search(pattern, text, q):
    pattern_len = len(pattern)
    text_len = len(text)
    i = 0
    j = 0
    pattern_hash = 0    # hash value for pattern
    text_hash = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    h = pow(d, pattern_len-1) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in xrange(pattern_len):
        print pattern_hash
        pattern_hash = (d * pattern_hash + ord(pat[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in xrange(text_len - pattern_len + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if pattern_hash == text_hash:
            # Check for characters one by one
            for j in xrange(pattern_len):
                if text[i+j] != pattern[j]:
                    break
            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == pattern_len:
                print "Pattern found at index " + str(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < text_len - pattern_len:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i+pattern_len])) % q

            # We might get negative values of t, converting it to
            # positive
            if text_hash < 0:
                text_hash = text_hash + q

# Driver program to test the above function
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 # A prime number
search(pat,txt,q)