import cmath
#input the complex number
z = complex(raw_input())
x = z.real
y = z.imag

r = abs(z)
theta = cmath.phase(z)

print r
print theta

