# def validasi_password(passwd):
#     spesial_karakter = ['$', '@', '#', '%']
    
#     def contains_number(value):
#         for character in value:
#             if character.isdigit():
#                 return True
#         return False

#     panjang_benar = False
#     ada_digit = False
#     ada_huruf_besar = False
#     ada_huruf_kecil = False
#     ada_spesial_karakter = False
    
#     panjang_passwd = len(passwd)

#     if panjang_passwd > 6 and panjang_passwd < 20 :
#         panjang_benar =  True

#     if contains_number(passwd):
#         ada_digit = True
    
#     for i in range(panjang_passwd):

#         if passwd[i].isupper():
#             ada_huruf_besar = True
#         else:
#             ada_huruf_kecil = True
        
#         if ada_huruf_besar and ada_huruf_kecil:
#             break

#     for i in range(len(spesial_karakter)):
#         if spesial_karakter[i] in passwd:
#             ada_spesial_karakter =  True

#     if panjang_benar and ada_digit and ada_huruf_besar and ada_huruf_kecil and ada_spesial_karakter:
#         return True
#     else:
#         return False




# def main():
#     nama_lengkap = input('Masukkan nama: ')

#     split = nama_lengkap.split(' ')

#     print(f'Inisial nama Anda: {split[0][0]}. {split[1][0]}.')
   
# main()

def main():
    format_tanggal = input('Masukkan tanggal dalam format hh/bb/tttt: ')
    split_tanggal = format_tanggal.split('/')

    bulan_lookup =['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

    i_bulan = split_tanggal[1]

    if i_bulan[0] == '0':
        i_bulan = int(i_bulan[1:])
    else:
        i_bulan = int(i_bulan)

    if split_tanggal[0][0] == "0":
        split_tanggal[0] = int(split_tanggal[0][1:])

    if i_bulan < 1 or i_bulan > 12:
        print('Anda tidak memasukkan tanggal yang benar.')
        return

    print(split_tanggal[0], bulan_lookup[i_bulan-1], split_tanggal[2])



main()