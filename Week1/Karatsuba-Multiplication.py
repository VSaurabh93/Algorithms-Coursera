import math
import time


def recursive_multiply(x, y):

    length_x = len(x)
    length_y = len(y)

    if length_x <= 2 or length_y <= 2:
        return int(x)*int(y)

    a = x[0:int(length_x/2)]
    b = x[int(length_x/2):]
    c = y[0:int(length_y / 2)]
    d = y[int(length_y / 2):]

    ac = recursive_multiply(a, c)
    bd = recursive_multiply(b, d)
    ad = recursive_multiply(a, d)
    bc = recursive_multiply(b, c)

    if (length_x + length_y) % 2 == 0:
        t1 = str(ac) + "0" * int((length_x + length_y) / 2)
    else:
        t1 = str(ac) + "0" * int((length_x + length_y) / 2 + 1)
    if length_x % 2 == 0:
        t2 = str(ad) + "0" * int(length_x/2)
    else:
        t2 = str(ad) + "0" * (int(length_x / 2) + 1)
    if length_y % 2 == 0:
        t3 = str(bc) + "0" * int(length_y/2)
    else:
        t3 = str(bc) + "0" * (int(length_y / 2) + 1)
    t4 = str(bd)

    result = int(t1) + int(t2) + int(t3) + int(t4)

    return result


def karatsuba_multiply(x, y):

    length_x = len(x)
    length_y = len(y)

    base = int(max(length_x / 2, length_y / 2))

    if length_x <= 2 or length_y <= 2:
        return int(x)*int(y)

    a = x[0:base]
    b = x[base:]
    c = y[0:base]
    d = y[base:]

    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    a_plus_b_times_c_plus_d = karatsuba_multiply(str(int(a) + int(b)), str(int(c) + int(d)))
    ad_plus_cb = a_plus_b_times_c_plus_d - ac - bd

    t1 = str(ac) + "0" * (2*base)
    t2 = str(ad_plus_cb) + "0" * base
    t3 = str(bd)

    result = int(t1) + int(t2) + int(t3)

    return result


num1 = 3141592653589793238462643383279502884197169399375105820974944523
num2 = 2718281828459045235360287471352662497757247093699959574966967645

start = time.time()
res1 = recursive_multiply(str(num1), str(num2))
end = time.time()
recursive_time = end - start

start = time.time()
res2 = karatsuba_multiply(str(num1), str(num2))
end = time.time()
karatsuba_time = end - start

start = time.time()
res3 = num1*num2
end = time.time()
traditional_time = end - start

print("traditional method: " + str(res3))
print("recursive method  : " + str(res1))
print("karatsuba method  : " + str(res2))

print("Time elapsed: ")
print("traditional: " + str(traditional_time))
print("recursive  : " + str(recursive_time))
print("karatsuba  : " + str(karatsuba_time))


