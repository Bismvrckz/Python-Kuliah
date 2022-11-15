# try:
#     x = float('abc123')
#     print('Konversi berhasil.')
# except IOError:
#     print('Kode ini menyebabkan IOError.')
# except ValueError:    
#     print('Kode ini menyebabkan ValueError.') <-- Jawaban 1

# try:
#     y = int('x1010')
#     print(y)
# except IOError:
#     print('Kode ini menyebabkan IOError.')
# except ZeroDivisionError:
#     print('Kode ini menyebabkan ZeroDivisionError.')
# except:
#     print('Sebuah error terjadi.') <-- Jawaban 2

# def main():
#     try:
#         angka_yang_dibagi = int(input('Masukkan sebuah angka yang akan dibagi: '))
#         angka_pembagi = int(input('Masukkan sebuah angka pembagi: '))
#         angka_hasil = angka_yang_dibagi / angka_pembagi
#         print(f'{angka_yang_dibagi} dibagi dengan {angka_pembagi} sama dengan {angka_hasil:.1f}')
#     except ValueError:
#         print('Nilai yang diinput salah.')
#     except ZeroDivisionError:
#         print('Tidak dapat membagi dengan nol.')
# main()

# from statistics import mean 
# def main():
#     try:
#         list_angka = []
#         nama_file = input('Masukkan nama file: ')
    
#         rata_rata = 0.0
#         nilai_tertinggi = 0.0
#         nilai_terendah = 0.0
#         total_nilai = 0.0
#         list_nilai = []
        
#         with open(f'{nama_file}','r') as file:
#             for nilai in file:
#                 list_nilai.append(float(nilai))
    
#         for nilai in list_nilai:
#             total_nilai += nilai
        
#         rata_rata = mean(list_nilai)
#         nilai_tertinggi = max(list_nilai)
#         nilai_terendah = min(list_nilai)
        
#         print(f'Rata-rata nilai: {rata_rata:.2f}')
#         print(f'Nilai tertinggi: {nilai_tertinggi:.2f}')
#         print(f'Nilai terendah: {nilai_terendah:.2f}')
#     except FileNotFoundError:
#         print('File tidak ditemukan.')
#     except ValueError:
#         print('Terdapat data non numerik dalam file.')

# main()