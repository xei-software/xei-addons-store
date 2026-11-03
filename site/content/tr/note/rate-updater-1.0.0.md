---
title: SAP Business One için XEI Rate Updater 1.0.0 – Sürüm notları
lang: tr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# SAP Business One için XEI Rate Updater 1.0.0 – Sürüm notları

## Bu sürümün işlevleri

- Avrupa Merkez Bankası, İtalya Merkez Bankası veya Open Exchange Rates kurlarıyla **SAP Business One'da döviz
  kurları**: bir günün kurları için bir önceki gün yayınlanan kurlar geçerlidir.
- **Yalnızca şirketin para birimleri**, şirketin yönünde (doğrudan veya dolaylı kur), altı ondalık basamağa kesilmiş
  olarak.
- **Euro dışında yerel para birimi**: yerel para birimine göre çapraz kurlar.
- Döviz kurları sayfasından her para biriminin sonucuyla **elle güncelleme**.
- Her gün seçilen saatte veya `XEI.RateUpdater.exe aggiorna` komutuyla Windows Görev Zamanlayıcı'dan **otomatik
  güncelleme**.
- Her şirketin çalıştırmalarının, her para biriminin kurları ve sonucuyla birlikte **geçmişi**.
- Serbest, sunucu başına veya şirket başına **XEI lisansı**; 30 günlük ücretsiz deneme.
- **Programın dilleri**: İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca ve Türkçe.

## Kurulum

- Windows 10 ve 11 ile Windows Server 2016 ve üzeri, 64 bit için program: zip dosyasındaki klasör çıkarılır ve
  `XEI.RateUpdater.exe` başlatılır; .NET dahildir.
- Genellikle zaten yüklü olan Microsoft Edge WebView2 Runtime ve SAP Business One 10.0 veya üzerinin Service Layer'ı
  gerekir.
