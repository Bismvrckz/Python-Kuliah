# def main():
#     found = False
#     try:
#         fileName = input('Masukkan nama file: ')
#         list_nilai = []
        
#         with open(fileName,'r') as file:
#             print(f'File {fileName} berhasil dibuka.')
#             print('')
#             nama_target = input('Masukkan nama mahasiswa yang ingin dicari: ')
#             for lines in file:
#                 list_nilai.append(lines.rstrip('\n'))
#             target = list_nilai.index(nama_target)
#             print(f'Nama Mahasiswa: {nama_target}')
#             print(f'Nilai: {list_nilai[target+1]}')
#     except FileNotFoundError:
#         print(f'File {fileName} tidak ditemukan.')
#     except ValueError:
#         print(f'Nama {nama_target} tidak ditemukan.')
# main()