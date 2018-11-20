import ctypes as C
math=C.CDLL('./libmymath.so')

m=8
n=3

math.add_float.argtypes = [C.c_float, C.c_float]
math.add_float.restype = C.c_float

suma=math.add_float(m,n)

print("Según add_float, {} + {} = {}".format(m, n, suma))

math.add_int.argtypes = [C.c_int, C.c_int]
math.add_float.restype = C.c_int

suma=math.add_int(m,n)

print("En cambio, según add_int, {} + {} = {}".format(m, n, suma))

sumando1 = C.c_float(m)
sumando2 = C.c_float(n)
suma = C.c_float()

math.add_float_ref(C.byref(sumando1), C.byref(sumando2), C.byref(suma))

print ("Add_float_ref dice que {} + {} = {}".format(sumando1.value, sumando2.value, suma.value))

sumando1 = C.c_int(m)
sumando2 = C.c_int(n)
suma = C.c_int()

math.add_int_ref(C.byref(sumando1), C.byref(sumando2), C.byref(suma))

print ("A lo que add_int_ref contesta {} + {} = {}".format(sumando1.value, sumando2.value, suma.value))

vector1 = (C.c_int * 3) (1, 1, 1)
vector2 = (C.c_int * 3) (1, 0, 0)
suma = (C.c_int * 3) ()

math.add_int_array(C.byref(vector1), C.byref(vector2), C.byref(suma), 3)

a = [vector1[0], vector1[1], vector1[2]]
b = [vector2[0], vector2[1], vector2[2]]
c = [suma[0], suma[1], suma[2]]

print("La función add_int_array dice que {} + {} = {}".format(a,b,c))

vector1 = (C.c_float * 3) (1, 1, 1)
vector2 = (C.c_float * 3) (1, 0, 0)

math.dot_product.restype = C.c_float

producto = math.dot_product(C.byref(vector1), C.byref(vector2), 3)

a = [vector1[0], vector1[1], vector1[2]]
b = [vector2[0], vector2[1], vector2[2]]

print("Y la función dot_product agrega finalmente {} · {} = {}".format(a, b, producto))
