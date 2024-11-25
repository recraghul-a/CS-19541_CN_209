def hamming_encode(data):
    m = len(data)  # Number of data bits
    r = 1
    while 2 ** r < m + r + 1:
        r += 1

    # Calculate the positions of parity bits
    parity_positions = [2 ** i for i in range(r)]

    # Create the encoded string with parity bits
    encoded_data = ['0'] * (m + r)

    # Assign data bits to their positions
    j = 0
    for i in range(1, m + r + 1):
        if i not in parity_positions:
            encoded_data[i - 1] = data[j]
            j += 1

    # Calculate parity bits
    for p in parity_positions:
        parity_sum = 0
        for i in range(1, m + r + 1):
            if i & p:
                parity_sum ^= int(encoded_data[i - 1])
        encoded_data[p - 1] = str(parity_sum)

    return ''.join(encoded_data)


# Example usage:
data = input()
encoded_data = hamming_encode(data)
print(encoded_data)