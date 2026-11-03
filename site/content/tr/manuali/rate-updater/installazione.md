---
title: SAP Business One için XEI Rate Updater – Kurulum, ilk başlatma, lisans ve zamanlanmış güncelleme
description: SAP Business One için XEI Rate Updater'ın nasıl kurulacağı, SAP Business One'a nasıl bağlanacağı, lisansın nasıl etkinleştirileceği ve kurların günlük güncellemesinin nasıl zamanlanacağı.
lang: tr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# SAP Business One için XEI Rate Updater – Kurulum, ilk başlatma, lisans ve zamanlanmış güncelleme

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri, Service Layer ile |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | Windows 10 ve 11, Windows Server 2016 ve üzeri, 64 bit; Microsoft Edge WebView2 Runtime |
| Ağ | seçilen kur kaynağına internet erişimi |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |

## Kurulum

1. Programın zip dosyasını indirme sayfasından indirin.
2. Zip dosyasındaki klasörü bilgisayara çıkarın, örneğin `C:\XEI\RateUpdater` klasörüne.
3. **XEI.RateUpdater.exe** dosyasını başlatın. Program .NET'i zaten içerir. **Microsoft Edge WebView2 Runtime**
   gerekir; genellikle zaten yüklüdür: yoksa program bunu bildirir ve indirmeyi önerir.

Programın kurulumu yoktur. Ayarlar ve geçmiş, bilgisayarın tüm kullanıcılarında ortak olan Windows veri klasöründe
bulunur. Programı güncellemek için klasör yenisiyle değiştirilir: ayarlar ve geçmiş korunur.

## İlk başlatma

İlk açılışta, ilk başlatma kodu zaten yazılı olarak **İlk başlatma** sayfası açılır.

1. **SAP bağlantısı**: *Service Layer adresi* ve *SAP şirketleri*; ardından **Bağlantıyı dene**.
2. **Giriş ve ilk yönetici**:
   - *Operatör girişi*: **Herkesin kendi SAP kullanıcısı** veya **Kendi kullanıcılar ve teknik SAP kullanıcısı**;
   - *İlk yöneticinin SAP kullanıcısı* (örneğin `manager`);
   - *Teknik SAP kullanıcısı* ve parolası: otomatik güncelleme için gerekir. Yalnızca kurları yazma yetkisi olan ayrı
     bir kullanıcı tercih edin.
3. **Kaydet ve yeniden başlat**.

Daha sonra aynı ayarlar **Ayarlar › SAP** bölümündedir. Kur kaynağı ve otomatik güncelleme **Ayarlar › Döviz kurları**
bölümündedir.

## Lisans

Program, XEI tarafından verilen bir **lisans kodu** ile çalışır.

| Kapsam | Geçerli olduğu yer |
|---|---|
| Tek şirket | bir SAP veritabanı |
| Sunucu | SQL Server veya SAP HANA örneğinin tüm şirketleri |
| Serbest | bir veritabanına bağlı değildir |

- **Deneme**: 30 gün, serbest.
- **Lisans** menüsü: durum, son kullanma tarihi ve kapsam. XEI'den alınan kod **Lisans kodu girin** alanına
  yapıştırılır ve yeniden başlatmadan hemen geçerli olur.
- Şirket veya sunucu başına bir lisans için programın lisans veritabanına salt okunur olarak bağlı olması gerekir
  (*Ayarlar › Lisans*, **Bağlantıyı test et**): orada ve Lisans sayfasında şirket ve sunucu kodları görünür; bunları
  [license@xeisrl.com](mailto:license@xeisrl.com) adresine gönderin.

## Windows ile zamanlanmış güncelleme

Böylece kurlar program kapalıyken de her gün güncellenir.

1. **Teknik SAP kullanıcısını** ayarlayın (Ayarlar › SAP).
2. Windows'ta **Görev Zamanlayıcı**'yı açın ve bir temel görev oluşturun, örneğin her gün saat 7:00'de.
3. **Program başlat** eylemi: program klasöründeki `XEI.RateUpdater.exe`, `aggiorna` bağımsız değişkeniyle.
4. Görevin özelliklerinde **Kullanıcının oturum açıp açmadığına bakılmaksızın çalıştır** seçeneğini seçin.

Komut bugünün kurlarını günceller ve pencere açmadan kapanır; çalıştırma **Geçmiş** sayfasında görünür. Birden fazla
şirketle `--societa <SAP veritabanı>` eklenir; her şirket için bir görev oluşturulur. Görev Zamanlayıcı için sonuç:
**0** başarılı, **1** başarısız veya reddedilen bir para birimiyle, **2** hatalı bağımsız değişkenler.

Alternatif olarak, program açıkken *Ayarlar › Döviz kurları* bölümünde **Otomatik güncelleme**'yi açmak yeterlidir.

## Destek

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com). Destek için:
[info@xeisrl.com](mailto:info@xeisrl.com). Talebinizde programın sürümünü (*Bilgi* menüsü) ve sorunun bir açıklamasını
belirtin.
