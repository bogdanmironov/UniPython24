mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

def kWeakestRows(mat, k):
    enumerated = list(enumerate(mat))
    enumerated.sort(key=lambda x: x[1])
    print(enumerated)
    return [element[0] for element in enumerated[:k]]

print(kWeakestRows(mat, 3))