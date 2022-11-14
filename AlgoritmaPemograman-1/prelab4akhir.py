# def main():
#     jumlah_mahasiswa = int(input('Masukkan jumlah mahasiswa: '))

#     list_nilai = []

#     for i in range(jumlah_mahasiswa):
#         total_ujian = 0
#         print('==================================================')
#         print(f'Masukkan nilai ujian untuk mahasiswa {i+1}')
#         print('--------------------------------------------------')
#         total_ujian += float(input('Masukkan nilai ujian ke-1: '))
#         total_ujian += float(input('Masukkan nilai ujian ke-2: '))
#         total_ujian += float(input('Masukkan nilai ujian ke-3: '))
#         list_nilai.append(total_ujian/3)

#     print('==================================================')
#     for i in range(jumlah_mahasiswa):
#         print(f'Rata-rata ujian mahasiswa {i+1}: {list_nilai[i]:.2f}')


    
    
# main()

# def main():
#     text = input('Masukkan sebuah teks: ')

#     char_list = []
#     index_list = []

#     for i in range(len(text)):
#         if len(char_list) == 0:
#             char_list.append([text[i]])
#             continue

#         isPushed = False
        
#         for x in range(len(char_list)):
#             if char_list[x][0].upper() == text[i].upper():
#                 char_list[x].append(text[i])
#                 isPushed = True
#                 break
#             elif  x + 1 == len(char_list) and isPushed == False:
#                 char_list.append([text[i]])
#                 break
    
#     for index in range(len(char_list)):
#         index_list.append([index, len(char_list[index])])
    
#     def sortFunc(x):
#         return x[1]
    

#     index_list.sort(reverse=True, key=sortFunc)
    
#     print(f'Karakter terbanyak:  {char_list[index_list[0][0]][0].lower()}')



# main()


