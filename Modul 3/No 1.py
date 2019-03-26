matrix = [[1,2,3], [4,5,4], [7,8,9]]
math = [[2,3,6], [1,7,3], [3,4,6]]

s = len(matrix)

def konsisten():
    for i in range(s):
        bb = len(matrix[i])
        count = i + 1
        if bb == s:
            i += 1
        elif bb != s:
            break
    if count == s:
        print("Matriks Sudah Konsisten!")
    else:
        print("Matriks tidak konsisten, tolong dicek ulang...")

def ukuran():
    for i in range(s):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = ' ')
        print("\n")
    print("Ukuran matrix adalah = ", "(", len(matrix), " X ",  len(matrix[0]), ")")

def jumlah():
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            hasil = matrix[i][j] + math[i][j]
            print(hasil, end = ' ')
        print("\n")

def kali():
    final = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix[0])):
            total = 0
            for k in range(len(matrix[0])):
                total = total + (matrix[i][j] + math[i][j])
            row.append(total)
        final.append(row)
    for i in range(len(final)):
        for j in range(len(final[0])):
            print(final[i][j], end = ' ')
        print("\n")

def determinan(l):
    n = len(l)
    if n > 2:
        i = 1
        t = 0
        sum = 0
        while t <= n - 1:
            d = {}
            t1 = 1
            while t1 <= n - 1:
                m = 0
                d[t1] = []
                while m <= n - 1:
                    if m == t:
                        u = 0
                    else:
                        d[t1].append(l[t1][m])
                    m += 1
                t1 += 1
            l1 = [d[x] for x in d]
            sum = sum + i * (l[0][t]) * (determinan(l1))
            i = i * (-1)
            t += 1
        return sum
    else:
        return l[0][0] * l[1][1] - l[0][1] * l[1][0]
    
    
    
            
