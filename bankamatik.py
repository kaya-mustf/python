SadikHesap = {
    "ad":"sadık turan",
    "HesapNo": "12345678",
    "bakiye": 3000,
    "ekhesap":2000
}



alikHesap = {
    "ad":"ali yıldırım",
    "HesapNo": "987654321",
    "bakiye": 5000,
    "ekhesap":1000
}




def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam= hesap['bakiye'] + hesap['ekhesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanılsınmı (E/H")

            if ekHesapKullanimi == "E":
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap["ekhasap"] -= ekHesapKullanilacakMiktar

                print("paranızı alabilirsiniz.")
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("üzgünüz bakiye yetersiz")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['bakiye']} TL Bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']}TL bulunmaktadır.")




paraCek(SadikHesap,3000)


print("***************")

paraCek(SadikHesap,2000)


