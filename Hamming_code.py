def hamming_encode(data):
    m = len(data)
    r = 0

    while 2**r < m+r+1:
        r += 1

    codeword = [None] * (m+r)

    j = 0
    for i in range(1,m+r+1):
        if not (i&(i-1)):
            continue
        codeword[i-1] = data[j]
        j += 1