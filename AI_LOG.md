1. How I Used AI

I used ChatGPT as an assistant during the development of my Scene Frame Calculator project. I mainly used it to understand Python concepts, organize the project, improve testing, and troubleshoot errors.

AI was used as a learning and debugging assistant. I reviewed the suggestions and tested the program myself.

2. Prompts and AI Assistance

The following are summaries of the prompts and questions I used during the project:1

How can I test whether my scene calculator works correctly?

Suggested manual test cases for normal and invalid inputs.

2

Which file should I use to document my test results?

Explained the purpose of a separate TEST_RESULTS.md file.

3
Why does running python tests.py ask me to enter an FPS value?

Helped me investigate an unexpected program execution issue.

4

How can I check whether my calculation function works independently?

Suggested testing the function through a Python import command.

5

How can I run automated tests using Python unittest?

Explained how to run the test file and interpret the results.

3. Critical Evaluation of AI Suggestions

AI suggestions were useful, especially when organizing the project and identifying possible errors. However, I did not assume that every suggestion was automatically correct.

For example, when I ran the automated tests, the program unexpectedly asked me to enter an FPS value. Instead of immediately changing the code, I investigated the issue by checking the main Python file and testing the calculation function separately.

I also ran the automated tests again after troubleshooting. The final result was five successful tests and zero failures.

This process helped me understand that AI-generated suggestions should always be checked by running and testing the actual program.

4. What I Learned

Through this process, I learned how to:

Use Python's unittest module.

Test functions independently.

Identify and investigate unexpected program behavior.

Validate user inputs.

Document manual and automated test results.

Evaluate AI suggestions instead of accepting them without checking.

5. Conclusion

AI helped me during the development process, but I was responsible for reviewing the code, running the program, testing its functionality, and evaluating the results.
# Yapay Zekâ Kullanım Günlüğü

## 1. Yapay Zekâyı Nasıl Kullandım?

Scene Frame Calculator projesini geliştirirken ChatGPT'den yardımcı bir araç olarak yararlandım. Özellikle Python kavramlarını anlamak, proje dosyalarını düzenlemek, test sürecini geliştirmek ve karşılaştığım hataları çözmek için kullandım.

Yapay zekâyı öğrenme ve hata ayıklama sürecinde bir yardımcı olarak kullandım. Verilen önerileri kendim kontrol ettim ve programı çalıştırarak test ettim.

## 2. Yapay Zekâya Sorduğum Sorular ve Aldığım Yardımlar

| No. | Sorduğum Sorunun Özeti | Aldığım Yardım |
|---|---|---|
| 1 | Sahne hesaplama programımın doğru çalışıp çalışmadığını nasıl test edebilirim? | Normal ve hatalı girişler için manuel test senaryoları önerdi. |
| 2 | Test sonuçlarımı hangi dosyada tutmalıyım? | Test sonuçları için ayrı bir TEST_RESULTS.md dosyası oluşturmamı önerdi. |
| 3 | `python tests.py` komutunu çalıştırdığımda program neden FPS değeri istiyor? | Beklenmeyen program davranışının nedenini araştırmama yardımcı oldu. |
| 4 | Hesaplama fonksiyonumun bağımsız çalıştığını nasıl kontrol edebilirim? | Fonksiyonu Python üzerinden ayrı olarak çalıştırmamı önerdi. |
| 5 | Python unittest kullanarak otomatik testleri nasıl çalıştırabilirim? | Test dosyasını çalıştırmayı ve sonuçları yorumlamayı açıkladı. |

## 3. Yapay Zekâ Önerilerinin Eleştirel Değerlendirilmesi

Yapay zekâdan aldığım öneriler özellikle proje düzenleme ve hata tespit etme aşamalarında faydalı oldu. Ancak verilen her önerinin doğrudan doğru olduğunu varsaymadım.

Örneğin, otomatik testleri çalıştırdığımda program beklenmedik şekilde FPS değeri girmemi istedi. Kodu hemen değiştirmek yerine ana Python dosyasını kontrol ettim ve hesaplama fonksiyonunu ayrı olarak çalıştırarak sorunu araştırdım.

Daha sonra otomatik testleri tekrar çalıştırdım. Sonuç olarak beş testin tamamı başarılı oldu ve hiçbir test başarısız olmadı.

Bu süreç bana yapay zekâ tarafından verilen önerilerin gerçek program üzerinde çalıştırılarak ve test edilerek kontrol edilmesi gerektiğini gösterdi.

## 4. Bu Süreçte Neler Öğrendim?

Proje sürecinde:

- Python'da unittest modülünü kullanmayı,
- Fonksiyonları birbirinden bağımsız test etmeyi,
- Beklenmeyen program davranışlarını araştırmayı,
- Kullanıcı girişlerini doğrulamayı,
- Manuel ve otomatik test sonuçlarını belgelemeyi,
- Yapay zekâ önerilerini kontrol ederek değerlendirmeyi öğrendim.

## 5. Sonuç

Yapay zekâ proje geliştirme sürecinde bana yardımcı oldu. Ancak kodları incelemek, programı çalıştırmak, işlevleri test etmek ve sonuçları değerlendirmek benim sorumluluğumdaydı. Bu proje sayesinde hem Python bilgimi geliştirdim hem de hata ayıklama ve test süreçleri hakkında deneyim kazandım.