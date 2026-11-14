# Sahne Kare Hesaplayıcı (Scene Frame Calculator)

## 1. Proje Hakkında

Sahne Kare Hesaplayıcı, animasyon öğrencilerinin sahne sürelerine ve FPS (Frame Per Second) değerlerine göre ihtiyaç duydukları toplam kare sayısını hesaplamalarını sağlayan bir Python programıdır.

Kullanıcıdan sahne adı, sahne süresi ve FPS bilgisi alınır. Program bu bilgiler doğrultusunda toplam kare sayısını hesaplar ve sahne hakkında ek bilgiler sunar.

## 2. Programın Özellikleri

- Yeni sahne ekleme.
- Sahne süresi ve FPS değerine göre toplam kare sayısını hesaplama.
- Sahneleri kısa, orta ve uzun olarak sınıflandırma.
- Eklenen tüm sahneleri listeleme.
- Toplam kare sayısını görüntüleme.
- Sahne bilgilerini CSV dosyasına kaydetme.
- Hatalı veya geçersiz kullanıcı girişlerini kontrol etme.
- Menü üzerinden programı yönetme.

## 3. Kullanılan Teknolojiler

- Python 3
- CSV modülü
- Unittest modülü

Programda harici bir Python kütüphanesi kullanılmamıştır.

## 4. Kurulum ve Çalıştırma

Programı çalıştırmak için bilgisayarda Python 3 kurulu olmalıdır.

1. Proje klasörünü açın.
2. Terminali proje klasöründe başlatın.
3. Aşağıdaki komutu çalıştırın:

   `python sahne_hesaplayici.py`

4. Ekrandaki menü üzerinden yapmak istediğiniz işlemi seçin.

## 5. Menü Seçenekleri

| Seçim | İşlev |
|---|---|
| 1 | Yeni sahne ekleme |
| 2 | Eklenen sahneleri listeleme |
| 3 | Sahne bilgilerini CSV dosyasına kaydetme |
| 4 | Programdan çıkış |

## 6. Örnek Hesaplama

Örnek giriş:

- Sahne adı: Giriş
- Süre: 10 saniye
- FPS: 24

Hesaplama:

10 × 24 = 240 kare

Sonuç: 240 kare

## 7. Otomatik Testleri Çalıştırma

Programın hesaplama fonksiyonunu test etmek için terminalde şu komut çalıştırılır:

`python tests.py`

Otomatik testlerde kısa, orta ve uzun sahneler, çalışma günü hesaplaması ve farklı FPS değerleri kontrol edilmektedir.

Son test sonucunda 5 testin tamamı başarılı olmuştur.

## 8. Proje Dosyaları

| Dosya | Açıklama |
|---|---|
| `sahne_hesaplayici.py` | Programın ana Python kodu |
| `tests.py` | Otomatik test kodları |
| `TEST_RESULTS.md` | Manuel ve otomatik test sonuçları |
| `README.md` | Proje tanıtımı ve kullanım kılavuzu |
| `AI_LOG.md` | Yapay zekâ kullanım günlüğü |
| `reflection.md` | Proje değerlendirme raporu |
