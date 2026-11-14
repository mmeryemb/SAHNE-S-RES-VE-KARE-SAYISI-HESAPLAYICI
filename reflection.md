# Proje Değerlendirme Raporu (Reflection)

## 1. Projenin Amacı

Bu projede animasyon öğrencilerinin sahne sürelerine ve FPS değerlerine göre toplam kare sayılarını hesaplayabilmelerini sağlayan bir Python programı geliştirdim.

Programın temel amacı, animasyon üretim sürecinde ihtiyaç duyulan kare sayısı hesaplamalarını kolaylaştırmak ve sahnelerin sürelerini daha düzenli takip edebilmektir.

## 2. Proje Sürecinde Öğrendiklerim

Bu projeyi geliştirirken Python programlama dilinin temel yapılarını uygulamalı olarak öğrenme fırsatı buldum.

Özellikle:
- Değişkenler ve veri türlerini kullanmayı,
- Kullanıcıdan veri almayı ve girişleri doğrulamayı,
- Koşullu ifadelerle karar yapıları oluşturmayı,
- Döngüler kullanarak menü sistemini yönetmeyi,
- Fonksiyonlar oluşturarak kodu bölümlere ayırmayı,
- Listeler ve sözlüklerle verileri saklamayı,
- CSV dosyalarına veri kaydetmeyi,
- Otomatik testler yazmayı ve çalıştırmayı öğrendim.

## 3. Karşılaştığım Zorluklar

Proje sırasında en çok zorlandığım konulardan biri kullanıcıdan alınan verilerin kontrol edilmesiydi. Örneğin, süre veya FPS alanına sayı yerine metin girildiğinde ya da negatif bir değer yazıldığında programın hata vermeden çalışmaya devam etmesini sağlamam gerekiyordu.

Bir diğer zorluk ise otomatik testleri çalıştırma aşamasında karşılaştığım beklenmedik davranıştı. Testleri başlattığımda programın FPS değeri istemesi üzerine ana dosyanın çalışma yapısını kontrol ettim. Hesaplama fonksiyonunu bağımsız olarak çalıştırarak sorunu araştırdım ve ardından testleri tekrar çalıştırdım.

## 4. Yapay Zekâ Kullanımı

Proje sürecinde Claude ve ChatGPT'den Python kodlarını anlamak, karşılaştığım hataları araştırmak ve test sürecini düzenlemek için yardım aldım.

Ancak verilen önerileri doğrudan uygulamak yerine kodun nasıl çalıştığını anlamaya ve sonuçları kendim kontrol etmeye çalıştım. Özellikle test aşamasında programı farklı girişlerle manuel olarak deneyerek önerilerin doğruluğunu kontrol ettim.

## 5. Projenin Güçlü Yönleri

- Kullanımı kolay bir menü sistemine sahip olması.
- Farklı sahnelerin ayrı ayrı eklenebilmesi.
- Süre ve FPS değerlerine göre kare sayısını otomatik hesaplaması.
- Hatalı kullanıcı girişlerini kontrol etmesi.
- Sahne bilgilerinin CSV dosyasına kaydedilebilmesi.
- Otomatik testlerle temel hesaplama işlemlerinin kontrol edilmesi.

## 6. Geliştirilebilecek Yönler

Program gelecekte daha fazla özellikle geliştirilebilir. Örneğin:
- Mevcut sahneleri düzenleme ve silme özelliği eklenebilir.
- Daha gelişmiş bir grafik arayüz hazırlanabilir.
- Farklı projeler için ayrı sahne listeleri oluşturulabilir.
- Sahne süreleri ve toplam kare sayıları üzerinden daha ayrıntılı raporlar hazırlanabilir.
Ayrıca varsayım olarak günlük 24 frame yapılacak şeklinde alınd ama her sahnenin yükü farklı olduğu için bazı detaylar eklenebilir.

## 7. Genel Değerlendirme

Bu proje, Python programlama dilini teorik olarak öğrenmenin yanında gerçek bir ihtiyaca yönelik uygulama geliştirmemi sağladı.

Animasyon alanında eğitim aldığım için programın doğrudan sahne süreleri ve kare hesaplamalarıyla ilgili olması benim için ayrıca faydalıydı. Projeyi geliştirirken programlama mantığını, hata kontrolünü ve test süreçlerini daha iyi anlamaya başladım.

Sonuç olarak bu çalışma, hem kodlama bilgimi geliştirmeme hem de öğrendiğim konuları kendi alanımla ilişkilendirmeme yardımcı oldu.