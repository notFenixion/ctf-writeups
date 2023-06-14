
#Decompile Me




##1. Decompiling The File

Using [decompyle3](https://github.com/rocky/python-decompile3), we can decompile decompile-me.pyc, and obtain the following:

```
from pwn import xor
with open('flag.txt', 'rb') as f:
    flag = f.read()
a = flag[0:len(flag) // 3]
b = flag[len(flag) // 3:2 * len(flag) // 3]
c = flag[2 * len(flag) // 3:]
a = xor(a, int(str(len(flag))[0]) + int(str(len(flag))[1]))
b = xor(a, b)
c = xor(b, c)
a = xor(c, a)
b = xor(a, b)
c = xor(b, c)
c = xor(c, int(str(len(flag))[0]) * int(str(len(flag))[1]))
enc = a + b + c
with open('output.txt', 'wb') as f:
    f.write(enc)
```


##2. Reverse all the XORs

The output given is **^@l6l;t54L6^?>-"|<^]@bQJ=m>c~?**

Notice that a,b and c should all be the same length.
Hence, a,b,c are simply the 1st 1/3, 2nd 1/3 and 3rd 1/3 of the output respectively.

Using the property that A^A = 0 and A^0 = A,
We can reverse all the XOR operations in the decompiled code.

```
from pwn import xor

with open('output.txt', 'rb') as f:
    enc = f.read()

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

```

We obtain the flag: 
```
SEE{s1mP4l_D3c0mp1l3r_XDXD}
```


