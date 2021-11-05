# Iterasi Gauss Seidel

# Definisikan Persamaan yang akan diselesaikan
# Dalam bentuk dominan secara diagonal
def f1(x, y, z): return (-4-3*y+z)/4
def f2(x, y, z): return (40+2*x-5*z)/-4
def f3(x, y, z): return (14-x-2*y)/6

# Nama: Muchammad Prasetyo
# NPM: 202110717001
# Kelas: TF3A4


# Inisial Awal
x0 = 2
y0 = -8
z0 = 2
step = 1

# Input nilai galat/error
e = float(input('Input Toleransi error : '))

# Implementasi iterasi Gauss Seidel
print('\nStep\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (step, x1, y1, z1))
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)

    step += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e
print('\nSolusi : x = %0.3f, y = %0.3f and z = %0.3f\n' % (x1, y1, z1))
