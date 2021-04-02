# penggunaan if untuk tiga kasus dan selebihnya
# inputkan bilangan
print('Masukkan koordinat!')
x = int(input('Masukkan nilai x: '))
y = int(input('Masukkan nilai y: '))
Info = 'Koordinat (' + str(x) + ',' + str(y) + ') berada pada kuadran '
#memeriksa nilai x dan y
if x > 0 and y > 0:
    print(Info + 'I')
elif x < 0 and y > 0:
    print(Info + 'II')
elif x < 0 and y < 0:
    print(Info + 'III')
elif x > 0 and y > 0:
    print(Info + 'IV')
else:
    pass
print()