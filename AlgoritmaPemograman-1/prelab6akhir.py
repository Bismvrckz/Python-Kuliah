import statistik
import statistics 

def main():
    try:
        nama_file = input('Masukkan nama file: ')
        data = []
        with open(nama_file,'r') as file:
            for i in file:
                data.append(float(i.rstrip('\n')))
        
        mean = statistik.mean(data)
        var = statistik.var(data,mean)
        std = statistik.std(var)
        med = statistik.median(data)
        print(f'Mean dari data: {mean:.2f}')
        print(f'Variansi dari data: {var:.2f}')
        print(f'Standar Deviasi dari data: {std:.2f}')
        print(f'Median dari data: {med:.2f}')
    except FileNotFoundError:
        print(f'File {nama_file} tidak ditemukan.')
    except ValueError:
        print(f'File {nama_file} berisi data non-numerik.')
main()