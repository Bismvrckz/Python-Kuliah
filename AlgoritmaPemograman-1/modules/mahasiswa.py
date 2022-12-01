class Mahasiswa:
    def __init__(self,__nama, __npm,__jurusan,__no_telepon):
        self.__nama = __nama
        self.__npm = __npm
        self.__jurusan = __jurusan
        self.__no_telepon = __no_telepon
    
    def set_nama(self,__nama):
        self.__nama = __nama
    
    def set_npm(self,__npm):
        self.__npm = __npm
    
    def set_jurusan(self,__jurusan):
        self.__jurusan = __jurusan
    
    def set_no_telepon(self,__no_telepon):
        self.__no_telepon = __no_telepon
    
    def get_nama(self):
        return self.__nama
    
    def get_npm(self):
        return self.__npm
    
    def get_jurusan(self):
        return self.__jurusan
    
    def get_no_telepon(self):
        return self.__no_telepon

def tampilkan_mahasiswa(class_object):
    print(f'Nama: {class_object.get_nama()}')
    print(f'NPM: {class_object.get_npm()}')
    print(f'Jurusan: {class_object.get_jurusan()}')
    print(f'Nomor Telepon: {class_object.get_no_telepon()}')
    print('')