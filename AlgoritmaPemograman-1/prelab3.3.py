def main():
    pembelian = int(input('Masukkan banyak pembelian: '))
    
    if pembelian > 99:
        diskon = 0.5
    elif pembelian > 49:
        diskon = 0.4
    elif pembelian > 19:
        diskon = 0.3
    elif pembelian > 10:
        diskon = 0.2
    else:
        diskon = 0
    
    if diskon != 0:
        print('Diskon = Rp.{0:,.2f}'.format(pembelian*diskon*990000))
        print('Total = Rp.{0:,.2f}'.format(pembelian*990000-pembelian*diskon*990000))
    else:
        print('Total = Rp.{0:,.2f}'.format(pembelian*990000))

main()