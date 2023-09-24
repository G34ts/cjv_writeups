h = open("qr_code.txt", "r")

h = h.read()

for i in h.split():
    binn = bin(int(i))[2:].zfill(29)
    print(binn)