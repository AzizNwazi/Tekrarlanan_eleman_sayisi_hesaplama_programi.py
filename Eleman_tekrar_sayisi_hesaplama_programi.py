liste = [1,2,3,3,4,6,8,9,8,1,2,5,4,3]


yeni_liste = [] #tekrar eden elemanları bir kere tutmak için yeni listemizi oluştur
tekrar_edenler = []#aksi durumda sadece tekrar edenleri tutumak için listemizi oluştur

#elemanları for döngüsünde tek tek geziyoruz
for i in liste:
    if i not in yeni_liste: #eğer gezdiğin eleman yeni listede tekrar geçmediyse eyni listeye ekle
        yeni_liste.append(i)
    else:                    # geçtiyse de tekrar edenler listesine ekle
        tekrar_edenler.append(i)
    liste.count(i)

#tekrar eden elemanın kaç kes geçtiğini sayan ve yazdıran döngümüz
for eleman in tekrar_edenler:
    tekrar_sayisi = liste.count(eleman)
    print(eleman,"elemani",tekrar_sayisi,"kez tekrar ediyor")

#asıl listemizi yazdır
print("\nAsil liste: ",liste)
#tekrar edilenleri silmeden önce yazdır
print("\nTekrar eden elemanlar:",tekrar_edenler)
#yeni listeyi yazdır
print("\nYeni liste:",yeni_liste)