from math import *

def make_fourier_matrix(n):
    w = complex(cos(2 * pi / n), sin(2 * pi / n))

    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[-1].append(w**(i*j))
    return result

def main():
    print(make_fourier_matrix(4))

main()
