# Test Results

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| Normal input | Scene added successfully, 240 frames calculated | Worked correctly | PASS |
| Text input (abc) | Warning and asks for input again | Worked correctly | PASS |
| Negative duration (-5) | Warning and asks for input again | Worked correctly | PASS |
| Zero FPS (0) | Warning and asks for input again | Worked correctly | PASS |
| Scene listing | Displays added scenes | Worked correctly | PASS |
| CSV saving | Saves scene data to CSV file | Worked correctly | PASS |
| Menu exit | Closes the program | Worked correctly | PASS |

## Bugs Found
No major bugs were found during manual testing.

## Corrections Made
Input validation successfully prevented invalid values from being accepted. The program continued running and requested valid input.
Test

Result

test_kisa_sahne

PASS

test_orta_sahne

PASS

test_uzun_sahne

PASS

test_calisma_gunu

PASS

test_farkli_fps

PASS
#
Girdi
Beklenen
Gerçek
Sonuç


1
Ad: Giriş, süre: 10, fps: 24
240 kare, 10.0 gün, sınıf Orta
240 kare, 10.0 gün, Orta
✔
2
Süre: abc
Uyarı verir, tekrar sorar
“Lütfen geçerli bir sayı girin.” yazdı, tekrar sordu
✔
3
Süre: -5
“0'dan büyük olmalı” uyarısı
“Değer 0'dan büyük olmalı.” yazdı
✔


4 Süre (saniye): 4        Eklendi: test -> 48 kare   Eklendi: test -> 48 kare                    ✔
FPS : 12


1-Sahne ekle  2-Listele  3-CSV'ye kaydet  4-Çıkış
Seçiminiz: 4
Çıkılıyor.
PS C:\Users\MERYEM\Desktop\scene-frame-calculator>
 
1-Sahne ekle  2-Listele  3-CSV'ye kaydet  4-Çıkış
Seçiminiz: test
Uyarı: 1-4 arasında bir seçim yapın.
1-Sahne ekle  2-Listele  3-CSV'ye kaydet  4-Çıkış
Seçiminiz: 1
Sahne adı: test
Süre (saniye): abc
Uyarı: Lütfen geçerli bir sayı girin.
Süre (saniye): -5
Uyarı: Değer 0'dan büyük olmalı.
Süre (saniye): 4
FPS (örn. 12, 24, 30): 12
Eklendi: test -> 48 kare
 


Total: 5 tests
Passed: 5
Failed: 0

All automated tests passed successfully.
