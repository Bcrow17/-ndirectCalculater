def emsal_hesapla(emsaller, yuzde ):
    # Verilen sayıların ortalamasını hesapla
    ortalama = sum(emsaller) / len(emsaller)
    print(f"Ortalama: {ortalama}")

    # Yüzde aralığı kontrolü
    alt_limit = ortalama - (ortalama * yuzde / 100)
    ust_limit = ortalama + (ortalama * yuzde / 100)

    # Yüzde aralığına uymayan değerleri filtrele
    emsaller = [sayi for sayi in emsaller if alt_limit <= sayi <= ust_limit]

    # Yeni ortalamayı hesapla
    yeni_ortalama = sum(emsaller) / len(emsaller)
    print(f"Yeni Ortalama: {yeni_ortalama}")

    return yeni_ortalama

# Kullanıcıdan sayıları ve yüzde aralığını al
sayi_listesi = [float(x) for x in input("Sayıları arasına virgül koyarak girin: ").split(',')]
yuzde = float(input("Yüzde aralığını girin: "))

# Fonksiyonu çağır
sonuc = emsal_hesapla(sayi_listesi, yuzde)
print(f"Yeni Ortalama: {sonuc}")

# Maksimum Minimum aralığını yazdır
print(f"Maksimum: {sonuc*(1+(yuzde/100))}")
print(f"Minimum: {sonuc*(1-(yuzde/100))}")

maksimum_limit=sonuc*(1+(yuzde/100))
minimum_limit=sonuc*(1-(yuzde/100))

#if emsal>maksimum_limit:
 #   print(f"{emsal} atılmıştır")
#elif emsal<minimum_limit:
 #   print(f"{emsal} atılmıştır")
#else:
 #   print(f"Kullanılan Emsaler {emsal}")