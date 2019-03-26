def buatNol(m, n):
    x = [[0 for i in range(m)] for j in range(n)]
    return x 

def buatNol(m):
    x = [[0 for i in range(m)] for j in range(m)]
    return x

def buatIdentitas(m):
    x = [[0 for i in range(m)] for j in range(m)]
    for k in range(int(len(x))):
        x[k][k] = 1
    return x
            

