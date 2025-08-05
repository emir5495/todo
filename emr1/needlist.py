import json

urunler = []

while True:
    secim = input("\nİşlem seçiniz:\n1- Ürün ekle\n2- Listele\n3- Fiyat hesapla\nQ- Çıkış\n> ").lower()

    if secim == "1":
        while True:
            print("Ürün bilgilerini JSON formatında gir (örn: {\"ad\": \"ekmek\", \"adet\": 2, \"fiyat\": 5.0})")
            girdi = input("Ürün gir (çıkmak için 'q'): ")
            if girdi.lower() == "q":
                break
            try:
                veri = json.loads(girdi)
                if not all(k in veri for k in ("ad", "adet", "fiyat")):
                    print("Eksik bilgi! 'ad', 'adet', 'fiyat' gerekli.")
                    continue
                urunler.append(veri)
            except json.JSONDecodeError:
                print("Geçersiz JSON formatı. Lütfen tekrar deneyin.")

    elif secim == "2":
        if not urunler:
            print("Henüz ürün girilmedi.")
        else:
            print("\n📦 Girilen Ürünler:")
            for urun in urunler:
                print(f"- {urun['adet']} adet {urun['ad']} ({urun['fiyat']} TL)")

    elif secim == "3":
        if not urunler:
            print("Hesaplanacak ürün yok.")
        else:
            toplam = sum(u['adet'] * u['fiyat'] for u in urunler)
            print(f"\n💰 Toplam Fiyat: {toplam:.2f} TL")

    elif secim == "q":
        print("Çıkış yapıldı.")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
