def binery_search(kumpulan, target) :
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        tengah = (kiri + kanan) // 2

        if kumpulan[tengah] == target :
            return tengah

        elif kumpulan[tengah] < target :
            kiri = tengah + 1

        else :
            kanan = tengah - 1

    return -1

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
