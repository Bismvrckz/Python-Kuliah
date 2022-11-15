# def main():
#     angka = [234, 694, 123, 789, 923, 674, 534]
#     with open('list_angka.txt','w') as file:
#         for num in angka:
#             file.write(f'{num}\n')
# main()

# from statistics import mean 
# def main():
    
#     rata_rata = 0.0
#     nilai_tertinggi = 0.0
#     nilai_terendah = 0.0
#     total_nilai = 0.0
#     list_nilai = []
    
#     with open('daftar_nilai.txt','r') as file:
#         for nilai in file:
#             list_nilai.append(float(nilai))
    
#     for nilai in list_nilai:
#         total_nilai += nilai
        
#     rata_rata = mean(list_nilai)
#     nilai_tertinggi = max(list_nilai)
#     nilai_terendah = min(list_nilai)
    
#     print(f'Rata-rata nilai ujian:  {rata_rata:.2f}')
#     print(f'Nilai ujian tertinggi:  {nilai_tertinggi:.2f}')
#     print(f'Nilai ujian terendah:  {nilai_terendah:.2f}')
        
# main()