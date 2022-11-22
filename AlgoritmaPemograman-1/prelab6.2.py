# def kali(x, y, z = 0):
#     if y < 1:
#         return z
    
#     return kali(x,y-1,z = z+x)

# def maksimum_rekursif(data,res = 0, index = 0):
#     if len(data) <= index:
#         return res
    
#     if res < data[index]:
#         res = data[index]
#         return maksimum_rekursif(data, res, index+1)
    
#     return maksimum_rekursif(data, res, index+1)