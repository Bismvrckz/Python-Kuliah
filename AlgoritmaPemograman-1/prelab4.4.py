
# def cari_ruby(input_list):
#     count = 0
    
#     for i in range(len(input_list)):
#         if input_list[i] == 'Ruby':
#             count += 1
    
    
#     return count



# def get_score():
#     score = 1
#     score_list = []
    
#     while score >= 0:
#          score = int(input('Masukkan skor (masukkan angka negatif untuk menyudahi): '))
           
#          if score >= 0:
#             score_list.append(score)
#          else:
#             break
        
#     return score_list


# def banyak_huruf_besar(input_string):
#     huruf_besar = 0
    
#     for i in range(len(input_string)):
        
#         if input_string[i].isupper():
#             huruf_besar += 1
#         else:
#             continue

    
#     return huruf_besar

# def jumlah_list(input_list):
# 	jumlah_index_ganjil=0
# 	jumlah_index_genap=0

# 	for i in range(len(input_list)):
# 		if i == 0:
# 			jumlah_index_genap += input_list[i]
# 			continue
		
# 		if i % 2 == 0:
# 			jumlah_index_genap += input_list[i]
# 		else:
# 			jumlah_index_ganjil += input_list[i]
# 	print(f'Total elemen indeks ganjil:  {jumlah_index_ganjil}')
# 	print(f'Total elemen indeks genap:  {jumlah_index_genap}')

# def kuadrat_list(input_list):
#     output_list = []

#     for i in range(len(input_list)):
#         output_list.append(input_list[i]**2)
    
#     return output_list