#!/usr/bin/env python3
from matplotlib import pyplot
import numpy as np


def Iy(q,l,E,u):
    numerator = 5 * q * np.power(l,4)
    print("Iy numerator",numerator)
    quotient = 384 * E * u
    print("Iy quotient",quotient)
    ret = numerator/quotient
    print("Iy is finally",ret)
    return ret

def thickness(h,b,_Iy):
    term1 = 0.5 * h
    print("term1",term1)
    tmp1 = np.power(b,3) * np.power(h,2)
    print("tmp1",tmp1)
    tmp2 = -12 * np.power(b,2)*_Iy
    print("tmp2",tmp2)
    term2 = np.power(tmp1+tmp2,1/3)
    print("term2",term2)
    t = term1 + term2
    print("t is finally",t)
    return t

def main():
    q = np.array([5*28.5])
    print("q",q)
    _Iy = Iy(q,
    _t = thickness(300,5000,_Iy)

if __name__ == "__main__":
    main()
