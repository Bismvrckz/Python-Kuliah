# soal 4
# Tuliskan fungsi Anda di bawah
def hitung_imt(b, t):
  return   b / (t**2)


#soal 5
# Fungsi konversi_ke_km
# [1] Tambahkan parameter yang diperlukan
def konversi_ke_km(mil):
    # [2] Konversi argumen ke km dan kembalikan hasilnya.
    return mil * 1.6

# Fungsi main
def main():
    # [3] Minta pengguna memasukkan jarak dalam mil dalam tipe floating point
    mil = float(input('Masukkan jarak dalam mil: '))

    # [4] Panggil fungsi konversi_ke_km
    hasil = konversi_ke_km(mil)
    
    # [5] Tampilkan hasil konversi
    print(f"Jarak dalam km = {hasil:.2f}")

    
main()



