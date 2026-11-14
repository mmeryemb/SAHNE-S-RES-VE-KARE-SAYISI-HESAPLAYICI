"""Animasyon Sahne Süresi ve Kare Hesaplayıcı
GEP1316 Ara Değerlendirme Ödevi 1

Sahne adı, süre (sn) ve fps girilir; program toplam kare sayısını ve
tahmini çalışma gününü hesaplar, sonuçları ekrana yazar ve CSV'ye kaydeder.
"""

import csv

# Varsayım: bir animatör günde ortalama bu kadar kare üretir (değiştirilebilir)
GUNLUK_KARE = 24
DOSYA_ADI = "sahneler.csv"


def sayi_al(mesaj, tur=float):
    """Kullanıcıdan pozitif sayı alır; hatalı girdide tekrar sorar."""
    while True:
        giris = input(mesaj).strip().replace(",", ".")
        try:
            deger = tur(giris)
        except ValueError:
            print("Uyarı: Lütfen geçerli bir sayı girin.")
            continue
        if deger <= 0:
            print("Uyarı: Değer 0'dan büyük olmalı.")
            continue
        return deger


def ad_al():
    """Boş olmayan bir sahne adı alır."""
    while True:
        ad = input("Sahne adı: ").strip()
        if ad:
            return ad
        print("Uyarı: Sahne adı boş olamaz.")


def sahne_hesapla(ad, sure, fps):
    """Sahne bilgilerinden bir sözlük üretir."""
    kare = round(sure * fps)
    gun = kare / GUNLUK_KARE

    # Karar yapısı 1: sahne uzunluğu sınıfı
    if sure < 5:
        sinif = "Kısa"
    elif sure < 15:
        sinif = "Orta"
    else:
        sinif = "Uzun"

    return {"ad": ad, "sure": sure, "fps": fps,
            "kare": kare, "gun": round(gun, 1), "sinif": sinif}


def sahne_ekle(sahneler):
    """3 girdi alır, doğrular ve sahneyi listeye ekler."""
    ad = ad_al()
    sure = sayi_al("Süre (saniye): ")
    fps = sayi_al("FPS (örn. 12, 24, 30): ", int)

    # Karar yapısı 2: alışılmadık fps uyarısı
    if fps not in (12, 24, 25, 30, 60):
        print("Not: Bu fps değeri yaygın değil, yine de kaydedildi.")
    elif fps == 60:
        print("Not: 60 fps çok yüksek kare sayısı üretir.")

    sahne = sahne_hesapla(ad, sure, fps)
    sahneler.append(sahne)
    print(f"Eklendi: {ad} -> {sahne['kare']} kare")


def listele(sahneler):
    """Sahneleri biçimli tablo olarak yazdırır."""
    if not sahneler:
        print("Henüz sahne yok.")
        return
    print(f"\n{'Sahne':<15}{'Süre':>7}{'FPS':>6}{'Kare':>8}{'Gün':>7}  Sınıf")
    print("-" * 52)
    for s in sahneler:
        print(f"{s['ad']:<15}{s['sure']:>7.1f}{s['fps']:>6}"
              f"{s['kare']:>8}{s['gun']:>7}  {s['sinif']}")
    toplam_kare = sum(s["kare"] for s in sahneler)
    toplam_sure = sum(s["sure"] for s in sahneler)
    print("-" * 52)
    print(f"Toplam: {toplam_sure:.1f} sn, {toplam_kare} kare, "
          f"~{toplam_kare / GUNLUK_KARE:.1f} iş günü\n")


def kaydet(sahneler):
    """Sahneleri CSV dosyasına yazar."""
    if not sahneler:
        print("Kaydedilecek sahne yok.")
        return
    with open(DOSYA_ADI, "w", newline="", encoding="utf-8-sig") as f:
        yazici = csv.DictWriter(
            f, fieldnames=["ad", "sure", "fps", "kare", "gun", "sinif"])
        yazici.writeheader()
        yazici.writerows(sahneler)
    print(f"{len(sahneler)} sahne {DOSYA_ADI} dosyasına kaydedildi.")


def menu():
    """Ana menü döngüsü."""
    sahneler = []
    while True:
        print("1-Sahne ekle  2-Listele  3-CSV'ye kaydet  4-Çıkış")
        secim = input("Seçiminiz: ").strip()
        if secim == "1":
            sahne_ekle(sahneler)
        elif secim == "2":
            listele(sahneler)
        elif secim == "3":
            kaydet(sahneler)
        elif secim == "4":
            print("Çıkılıyor.")
            break
        else:
            print("Uyarı: 1-4 arasında bir seçim yapın.")


if __name__ == "__main__":
    menu()
