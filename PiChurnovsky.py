from decimal import *

def calculate_pi(digits):
    getcontext().prec = digits + 1
    a = Decimal(13591409)
    b = Decimal(545140134)
    c = Decimal(-640320)
    d = Decimal(100100025)
    e = Decimal(327843840)
    f = Decimal(53360)
    k = 1
    pi = Decimal(0)

    while True:
        ak = Decimal(6 * k - 5)
        bk = Decimal(2 * k - 1)
        ck = Decimal(1)
        dk = Decimal(1)
        ek = Decimal(2 * k - 1)
        fk = Decimal(1)

        if k == 1:
            term = Decimal(1)
        else:
            term = Decimal(ak * b * ck * dk * ek * fk) / Decimal(k * k * k * c * c * c)

        pi += term

        if abs(term) < 1e-100:
            break

        k += 1
 
    pi = pi * Decimal(d) / Decimal(e)
    pi = pi.sqrt()
    pi = Decimal(426880) * pi

    return str(pi)[:digits+2]

print("Calculating PI up to 100 digits")
print(calculate_pi(100))
