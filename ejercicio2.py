matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
matriz[1][3]=sum(matriz[1][:3])
matriz[3][3]=sum(matriz[3][:3])
print(matriz)