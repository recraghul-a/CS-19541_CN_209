import random
import time

def sender(window_size):
    seq_num = 0
    base = 0  # Index of the oldest unacknowledged packet
    while True:
        # Send packets within the window
        for i in range(base, base + window_size):
            print(f"Sending packet {i}")
            # Simulate packet loss or delay
            if random.randint(1, 10) > 8:
                print("Packet lost!")
            else:
                time.sleep(1)  # Simulate transmission delay

        # Wait for acknowledgment
        while base < seq_num:
            if receive_ack(base):  # Check if acknowledgment is received
                base += 1
                print(f"Acknowledgment received for packet {base - 1}")

def receive_ack(seq_num):
    # Simulate acknowledgment reception
    if random.randint(1, 10) > 7:  # Simulate acknowledgment loss
        print("Acknowledgment lost!")
        return False
    else:
        time.sleep(1)  # Simulate acknowledgment delay
        print(f"Received acknowledgment for packet {seq_num}")
        return True

# Example usage:
window_size = 5
sender(window_size)