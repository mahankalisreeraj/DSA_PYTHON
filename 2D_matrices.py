#creating a 3X3 matrix and storing elements from 1 to 9

mat = []
t1 = []
for i in range(1,10):
    t1.append(i)
    
    if i % 3 == 0:
        mat.append(t1)
        t1 = []
        
for i in mat:
    for j in i:
        print(j,end = " ")
    print()
    
#Change the center element to 0 and print

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m,n = len(matrix)//2,len(matrix[0])//2
matrix[m][n] = 0

for i in matrix:
    for j in i:
        print(j,end = " ")
    print()


# row and column sum
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
row,col = [],[]
for i in matrix:
    row.append(sum(i))
    
for i in range(len(matrix[0])):
    s1 = 0
    for j in range(len(matrix)):
        s1 += matrix[j][i]
    col.append(s1)

print("Row Sum : ",row)
print("Column Sum : ",col)


# boudary checking
def check_boundary(mat, i, j):
    return 0 <= i < len(mat) and 0 <= j < len(mat[0])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(check_boundary(matrix,1,2))
print(check_boundary(matrix,4,1))

#matrix search
def search(mat,tgt):
    for i in mat:
        if tgt in i:
            return True 
    return False

matrix = [
    [1, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
]
print(search(matrix,7))


#diagonals sum
matrix = [
    [2, 5, 7],
    [4, 6, 8],
    [1, 3, 9]
]
primary,secondary = 0,0
m = len(matrix)
for i in range(m):
    primary += matrix[i][i]
    secondary += matrix[i][m - i - 1]
print(primary,secondary)