# Percobaan 3: Pengulangan for
# alpro403.py

awal=int(input('Set Nilai Awal = '))
akhir=int(input('Set Nilai Akhir = '))

count=0
summ=0

print('Bilangan antara %d dan %d' % (awal,akhir))
# kurang dari (<)
for i in range(awal,akhir+1): #secara default 1
    print(i, end=' ')
    count=count+1
    summ=summ+i

print('Bilangan di atas %d bilangan' %count)
print('Jumlah semua bilangan adalah %d' %summ)
'''
i = 0
while i < 7:
    i = i + 1
0 1 2 3 4 5 6
for i in range(7):
'''
