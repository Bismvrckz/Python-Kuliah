class Burung:
    def __init__(self,__spesies):
        self.__spesies = __spesies
    
    def tampilkan_spesies(self):
        print(f'Saya adalah seekor {self.__spesies}')
    
    def buat_suara(self):
        print('Ciut... Ciut...')

class Ayam(Burung):
    def __init__(self):
        Burung.__init__(self,'ayam')
        
    
    def buat_suara(self):
        print('Kukuruyuuuk...')

class Bebek(Burung):
    def __init__(self):
        Burung.__init__(self,'bebek')
    
    def buat_suara(self):
        print('Kwek! Kwek!')