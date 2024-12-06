import random

# ElGamal Signature implementation
def gen_keys():
    p = 23 # prime number, in reality this should be much larger
    g = 5  # some root modulo p
    x = random.randint(1, p-2) # private key
    y = pow(g, x, p) # public key

    return (p, g, y), x

def elgamal_sign(M, p, g, x):
    k = random.randint(1, p-2)
    while gcd(k, p-1) != 1:
        k = random.randint(1, p-2)
    r = pow(g, k, p)
    k_inv = pow(k, -1, p-1)
    s = (M - x*r) * k_inv % (p-1)
    return r, s

def elgamal_verify(M, r, s, p, g, y):
    is_equal = pow(g, M, p) == (pow(y, r, p) * pow(r, s, p)) % p
    print("Verification using Elgamal:")
    print(is_equal)
    return is_equal

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
