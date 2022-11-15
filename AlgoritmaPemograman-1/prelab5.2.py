# def main():    
#     angka1 = float(input("Masukkan sebuah angka desimal: "))
#     angka2 = float(input("Masukkan sebuah angka desimal lainnya: "))
#     angka3 = float(input("Masukkan sebuah angka desimal lainnya: "))
#     with open('angka.txt','a') as file:
#         file.write(str(angka1))
#         file.write(f'\n{angka2}')
#         file.write(f'\n{angka3}')
#     print("Data telah berhasil disimpan dalam file angka.txt.")
# main()

# def main():
#     with open('angka_float.txt','r') as file:
#         float1 = float(file.readline())
#         float2 = float(file.readline())
#     hasil = float1 * float2
#     print(f'Baris 1 file angka_float.txt berisi: {float1}')
#     print(f'Baris 2 file angka_float.txt berisi: {float2}')
#     print(f'Hasil kali baris 1 dan baris 2 = {hasil:.2f}')
# main()