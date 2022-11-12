def balik_string(input_string):
    string_akhir = ''

    for i in range(len(input_string)):
        string_akhir += input_string[-(i+1)]
    
    print(string_akhir)