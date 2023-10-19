e = 1
for a in range(150):
    for b in range(150):
        for c in range(150):
            for d in range(150):
                if (a**5 + b**5 + c**5 + d**5 == e**5):
                    print(a+b+c+d+e)