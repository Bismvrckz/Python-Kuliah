class Orang:
    def __init__(self,__nama,__umur):
        self.__nama = __nama
        self.__umur = __umur
    
    def tampilkan_nama(self):
        print(f'Nama saya adalah {self.__nama}')
    
    def tampilkan_umur(self):
        print(f'Umur saya adalah {self.__umur}')

class Siswa(Orang):
    def __init__(self,__nama,__umur,__tingkat):
        Orang.__init__(self,__nama,__umur)
        self.__tingkat = __tingkat
    
    def tampilkan_tingkat(self):
        print(f'Saya tingkat {self.__tingkat}')

class Pekerja(Orang):
    def __init__(self,__nama,__umur,__pekerjaan):
        Orang.__init__(self,__nama,__umur)
        self.__pekerjaan = __pekerjaan
    
    def tampilkan_pekerjaan(self):
        print(f'Pekerjaan saya {self.__pekerjaan}')