values = [True, False]
print('X | Y | Z | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
for x in values:
    for y in values:
        for z in values:
            resultLeft = not(x or y or z)
            resultRight = not x and not y and not z
            result = resultLeft == resultRight
            print(f'{int(x)} | {int(y)} | {int(z)} | {int(result)}')