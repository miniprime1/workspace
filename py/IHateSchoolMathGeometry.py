def surfaceSquare(x, y, z):
    S = 2*x*y + 2*(x+y)*z
    return S

print(surfaceSquare(1, 1, 216))
print(surfaceSquare(2, 2, 54))
print(surfaceSquare(3, 6, 12))
print(surfaceSquare(4, 6, 9))
print(surfaceSquare(6, 6, 6))
print(surfaceSquare(9, 6, 4))
print(surfaceSquare(12, 9, 2))