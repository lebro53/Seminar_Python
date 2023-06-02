def arithmetic_progression() -> list:
    a1 = int(input('VVedite pervoe chislo: '))
    n = int(input('VVedite raznostb: '))
    b = int(input('VVedite kolichestvo elementov: '))
    ap = []
    # ap.append(a1)
    for i in range(1, b+1):
        x = a1 + (i-1)*n
        ap.append(x)
    return ap

print(arithmetic_progression())