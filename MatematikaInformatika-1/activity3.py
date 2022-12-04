# # Definisi fungsi f
# def f(x):
#     return (2*x)+1                                           


# S = {-1,0,2,4,7                                        } # Domain

# # Buat tabel pemetaan
# print(f'| {"x":^5s} | {"f(x)":^5s} |')
# for x in sorted(S):
#     y = f(x)                                              
#     print(f'| {x:5d} | {y:5d} |')

# print()

# import sympy

# # Tetapkan x sebagai sebuah simbol
# x = sympy.Symbol('x')

# # Definisikan f dengan formula yang mengandung simbol x
# f = x**2 + 1                                          

# # Tetapkan Domain
# A = {2,4,6,8,10                                        }

# # Print nilai-nilai f
# for i in A:
# #Mensubtitusi simbol x pada fungsi f dengan nilai i dan mengevaluasi f
#     y = f.subs(x,i)                                       
#     print(f'f({i}) = {y}')

# print()

# import sympy

# # Tetapkan x , y sebagai sebuah simbol
# x, y = sympy.symbols("x y")                              

# # Gunakan fungsi solve pada modul sympy untuk mencari fungsi invers dari suatu fungsi
# print(sympy.solve(2*x - y)                              )

# import sympy

# # Tetapkan x sebagai sebuah simbol
# x = sympy.symbols('x')                                

# # Definisikan fungsi f dan g
# f = (x**2) +1                                         
# g = x + 2                                             

# # Gunakan fungsi compose pada modul sympy untuk mencari komposisi dari 2 buah fungsi
# print("f o g = ", sympy.compose(f,g)                                )    
# print("g o f = ", sympy.compose(g,f)                                )    
