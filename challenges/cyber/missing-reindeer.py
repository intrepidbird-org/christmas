#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

e = 3
d = -1

while d == -1:
    p = getPrime(1024)
    q = getPrime(1024)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

n = p * q

message = b"🎅 [CENSORED] 🎅"
holly = bytes_to_long(message)
jolly = pow(holly, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"jolly = {jolly}")
