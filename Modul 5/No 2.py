class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku
    def __str__(self):
        p = self.nama + ' | ' + str(self.nim) + ' | ' + self.kota + ' | ' + str(self.uangsaku)
        return p

class my_Array(object):
    internal_data = 11 * [None]

    def __getitem__(self, item):
        return self.internal_data[item]

    def __setitem__(self, key, value):
        self.internal_data[key] = value

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

c0 = MhsTIF('ika', 10, 'sukoharjo', 240000)
c1 = MhsTIF('budi', 51, 'klaten', 230000)
c2 = MhsTIF('ahmad', 2, 'surakarta', 250000)
c3 = MhsTIF('chandra', 18, 'surakarta', 235000)
c4 = MhsTIF('eka', 4, 'boyolali', 240000)
c5 = MhsTIF('fandi', 31, 'salatiga', 250000)
c6 = MhsTIF('deni', 13, 'klaten', 245000)
c7 = MhsTIF('galuh', 5, 'wonogiri', 245000)
c8 = MhsTIF('janto', 23, 'klaten', 245000)
c9 = MhsTIF('hasan', 64, 'karanganyar', 270000)
c10 = MhsTIF('khalid', 29, 'purwodadi', 265000)

c = my_Array()
c[0] = c0.nim
c[1] = c1.nim
c[2] = c2.nim
c[3] = c3.nim
c[4] = c4.nim
c[5] = c5.nim
c[6] = c6.nim
c[7] = c7.nim
c[8] = c8.nim
c[9] = c9.nim
c[10] = c10.nim

list1 = [c[2], c[4], c[7], c[0], c[6], c[3]]
list2 = [c[8], c[10], c[5], c[1], c[9]]

list11 = [1, 3, 4, 6, 10, 11]
list22 = [2, 5, 7]

def gabung_list(A, B):
    l1 = len(A)
    l2 = len(B)
    c = list()
    i = 0
    j = 0
    while i < l1 and j < l2:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < l1:
        c.append(A[i])
        i += 1
    while j > l2:
        c.append(B[j])
        j + 1
    return c

print(gabung_list(list11, list22))

