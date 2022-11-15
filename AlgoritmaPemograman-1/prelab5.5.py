# def main():
#     jumlah_mahasiswa = int(input('Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? '))
    
#     with open('nilai_mahasiswa.txt','a') as file_nilai:
#         for i in range(jumlah_mahasiswa):
#             print(f'Masukkan record nilai mahasiswa ke {i+1}')
#             nama = input('Nama: ')
#             nilai = input('Nilai: ')
#             file_nilai.write(f'{nama} \n')
#             file_nilai.write(f'{nilai} \n')
#             print()
            
# main()

# def main():
#     with open('nilai_mahasiswa.txt','r') as nilai_file:
#         baris = 'a'
#         while baris != '':
#             baris = nilai_file.readline()
#             if baris == '':
#                 continue
#             baris = baris.rstrip('\n')
#             print(f'Nama: {baris}')
#             baris = baris.rstrip('\n')
#             baris = nilai_file.readline()
#             print(f'Nilai: {baris}')

# main()