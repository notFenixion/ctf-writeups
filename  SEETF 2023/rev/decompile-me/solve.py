
with open('output.txt', 'rb') as f:
    enc = f.read()


from pwn import xor

# enc = '^@l6l;t54L6^?>-"|<^]@bQJ=m>c~?'
a = enc[0:len(enc) // 3]
b = enc[len(enc) // 3:2 * len(enc) // 3]
c = enc[2 * len(enc) // 3:]

c = xor(c, int(str(len(enc))[0]) * int(str(len(enc))[1]))
c = xor(b, c)
b = xor(a, b)
a = xor(c, a)
c = xor(b, c)
b = xor(a, b)
a = xor(a, int(str(len(enc))[0]) + int(str(len(enc))[1]))
flag = a + b + c

print(flag)
