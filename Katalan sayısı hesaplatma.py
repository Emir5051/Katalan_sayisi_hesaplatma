i = int(0)
eksilen_sayi= int(0)
def fonksiyonel(sayi):
    sayi=int(sayi)
    fsayi=int(1)
    eksilen_sayi = int(sayi)
    eksilen_sayi += int(1)
    for i in range(sayi):
        eksilen_sayi-=1
        fsayi*=eksilen_sayi
    return fsayi
def katalan(asilsayi):
    asilsayi=int(asilsayi)
    ikisayi=fonksiyonel(asilsayi*2)
    artisayi=fonksiyonel(asilsayi+1)
    if ikisayi/(artisayi+fonksiyonel(asilsayi)) == asilsayi:
        return "Bu bir Katalan Sayısıdır"
    else:
        return "Bu bir Katalan Sayısı Değildir"
sorusayi = input("Sayı gir lan merzifon eşeği:")
print(katalan(sorusayi))