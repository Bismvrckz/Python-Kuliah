# def sortir(data):
#     data.sort()
#     return data

# def median(data):
#     sorted_data = sortir(data)
    
#     if len(sorted_data) % 2 == 0:
#         return float(sorted_data[int(len(sorted_data)/2-1)]) + 0.5
#     else:
#         return sorted_data[int((len(sorted_data)-1)/2)]

# def indeks_minimum(data):
#     return data
    
# def selection_sort_rekursif(data, sorted=[]):
#     if len(data) == 1 or len(data) == 0:
#         return data
#     elif len(data) == len(sorted):
#         return sorted
    
    
#     data.sort(reverse=True)
    
#     if len(sorted) == 0:
#         sorted.append(data[-1])
#         return selection_sort_rekursif(data, sorted)
#     else:
#         sorted.append(data[-(len(sorted)+1)])
#         return selection_sort_rekursif(data, sorted)