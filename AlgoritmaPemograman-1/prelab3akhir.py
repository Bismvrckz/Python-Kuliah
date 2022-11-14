# import math

# def main():
#     detikTotal = int(input('Masukkan jumlah detik: '))
#     hari = math.floor(detikTotal / 60 / 60 / 24)
#     jam = math.floor(detikTotal / 60 / 60 % 24)
#     menit = math.floor(detikTotal / 60 % 60 )
#     detik = math.floor(detikTotal % 60 % 60 )

#     if hari:
#         print('{0} hari {1} jam {2} menit {3} detik'.format(hari,jam,menit,detik))
#     elif jam:
#         print('{0} jam {1} menit {2} detik'.format(jam,menit,detik))
#     elif menit:
#         print('{0} menit {1} detik'.format(menit,detik))
#     else:
#         print('{0} detik'.format(detik))
# main()







# def main():
#     lanjut = 'y'

#     while lanjut == 'y':
#         angka1 = int(input('Masukkan angka 1: '))
#         angka2 = int(input('Masukkan angka 2: '))
#         jumlah = angka1 + angka2
#         print(f'Jumlah = {jumlah}')
#         lanjut = input('Masukkan y untuk melanjutkan: ')
    
# main()