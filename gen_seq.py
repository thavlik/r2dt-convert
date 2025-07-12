import random

def gen_rand_sequence(len=100):
    """Generate a random sequence of DNA."""
    return ''.join(random.choice('ACGU') for _ in range(len))

print('>random_sequence')
print(gen_rand_sequence())
