def differanse(tall1: float, tall2: float):
    diff = tall1 - tall2

    if diff < 0:
        diff *= -1
    
    return diff

print(differanse(6,2))
print(differanse(1, 100))