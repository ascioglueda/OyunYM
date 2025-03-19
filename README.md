# Oyun Alani Yonetim Sistemi

Bu proje, bir oyun alanini yonetmek icin tasarlanmis bir Python uygulamasidir. Abonelik yonetimi, oyun alani verileri, personel yonetimi, raporlama, yogunluk tahmini ve muhasebe modullerini icerir.

## Moduller
- `entry_management.py`: Abonelik ve giris yonetimi (QR kod dogrulama, sure hatirlatma)
- `game_area.py`: Oyun alani verileri ve yas profiline gore ozellestirme
- `staff_management.py`: Personel yonetimi (nobet cizelgesi, maas, izinler)
- `reporting.py`: Gunluk ve haftalik raporlar
- `density_prediction.py`: Yogunluk tahmini
- `accounting.py`: Muhasebe (kar/zarar, harcamalar)

## Kurulum
1. Python 3.x'i yukleyin.
2. Proje klasorune gidin ve asagidaki komutu calistirin:
   ```bash
   python main.py