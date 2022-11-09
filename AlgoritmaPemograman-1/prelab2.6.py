import math


def hitung_populasi(pop, waktu):
    return math.e * pop ** 0.1 * waktu
    
    
    
    

def main():
    populasi = int(input('Masukkan populasi awal: '))
    
    waktu = int(input('Masukkan waktu dalam tahun: '))
    
    pop_akhir = hitung_populasi(populasi,waktu)
    print(f'Populasi akhir = {int(pop_akhir)}')


    
    
    
main()