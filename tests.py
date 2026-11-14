
import unittest
from sahne_hesaplayici import sahne_hesapla


class TestSahneHesapla(unittest.TestCase):

    def test_kisa_sahne(self):
        sonuc = sahne_hesapla("Giriş", 3, 24)
        self.assertEqual(sonuc["kare"], 72)
        self.assertEqual(sonuc["sinif"], "Kısa")

    def test_orta_sahne(self):
        sonuc = sahne_hesapla("Orta", 10, 24)
        self.assertEqual(sonuc["kare"], 240)
        self.assertEqual(sonuc["sinif"], "Orta")

    def test_uzun_sahne(self):
        sonuc = sahne_hesapla("Final", 20, 30)
        self.assertEqual(sonuc["kare"], 600)
        self.assertEqual(sonuc["sinif"], "Uzun")

    def test_calisma_gunu(self):
        sonuc = sahne_hesapla("Test", 10, 24)
        self.assertEqual(sonuc["gun"], 10.0)

    def test_farkli_fps(self):
        sonuc = sahne_hesapla("Test", 5, 30)
        self.assertEqual(sonuc["kare"], 150)


if __name__ == "__main__":
    unittest.main()