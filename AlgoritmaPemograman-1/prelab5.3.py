# def main():
#     with open('angka_float.txt','r') as file:
#         float1 = float(file.readline())
#         float2 = float(file.readline())
#     hasil = float1 * float2
#     print(f'Baris 1 file angka_float.txt berisi: {float1}')
#     print(f'Baris 2 file angka_float.txt berisi: {float2}')
#     print(f'Hasil kali baris 1 dan baris 2 = {hasil:.2f}')
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
