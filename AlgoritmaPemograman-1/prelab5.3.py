# import random
# def main():
#     with open('daftar_angka.txt', 'a') as file_angka:
#         for i in range(0,100):
#             file_angka.write(str(random.randint(1,100)) + "\n")       
# main()

# def main():
#     angka_total = 0
#     baris_total = 0
    
#     with open('sales.txt','r') as file:
#         baris = file.readline()
        
#         while baris != '':
#             angka = float(baris)
#             angka_total = angka_total + angka
#             baris_total += 1
#             baris = file.readline()
    
#     rata2 = angka_total / baris_total
#     print(f'Rata-rata penjualan: {rata2:,.2f}')
# main()

# def main():
#     angka_total = 0
#     baris_total = 0
    
#     with open('sales.txt','r') as file:
        
#         for baris in file:
#             angka = float(baris)
#             angka_total = angka_total + angka
#             baris_total += 1
    
#     rata2 = angka_total / baris_total
#     print(f'Rata-rata penjualan: {rata2:,.2f}')
# main()
