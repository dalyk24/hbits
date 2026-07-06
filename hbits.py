posi = [0, 2, 2, 3]

bits = [1, 0, 1, 0]

addressCheck = ((posi[0] % 2) == 0 and (posi[1] % 2) == 0)

if addressCheck:
    result = (bits[posi[0]] == bits[posi[1]])
else:
    result = -1

print(result)
