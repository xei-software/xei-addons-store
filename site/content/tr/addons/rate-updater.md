---
title: SAP Business One için XEI Rate Updater – Döviz kurları
description: SAP Business One'daki döviz kurlarını her gün ECB, İtalya Merkez Bankası veya Open Exchange Rates'in resmi kurlarıyla günceller.
lang: tr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# SAP Business One için XEI Rate Updater

**SAP Business One'daki döviz kurları, kendiliğinden güncellenir.** Program her gün kurları resmi bir kaynaktan alır ve
SAP Business One'a, SAP'nin kullandığı yönde ve ondalık basamak sayısıyla yazar.

## Tanım

Kurları elle güncellemek, her sabah kurları bir web sitesinden SAP'nin kur tablosuna para birimi para birimi kopyalamak
demektir; bir günü unutma veya bir kuru ters girme riski de vardır.

XEI Rate Updater bunu sizin yerinize yapar:

- kurları **Avrupa Merkez Bankası**'ndan (ECB), **İtalya Merkez Bankası**'ndan veya **Open Exchange Rates**'ten alır;
- bir günün kurları için **bir önceki gün** yayınlanan kurları kullanır; hafta sonları ve tatil günlerinde son yayın
  gününü kullanır;
- SAP'ye yalnızca **şirketin yönettiği para birimlerini**, şirketin kullandığı yönde (doğrudan veya dolaylı kur) ve
  altı ondalık basamağa kesilmiş olarak yazar;
- **euro dışında bir yerel para birimiyle** çapraz kurları ona göre hesaplar;
- tarih seçilerek **elle** veya **her gün otomatik olarak** kullanılır;
- her güncellemenin **geçmişini** tutar: kimin yaptığı, kaynak, kurlar ve her para biriminin sonucu.

## Başlıca işlevler

- **Döviz kurları**: kurların tarihi, kaynak ve *SAP'deki kurları güncelle* düğmesi; sonuç her para birimi için doğrudan
  kuru, dolaylı kuru ve SAP'ye yazılıp yazılmadığını gösterir.
- **Geçmiş**: şirketin çalıştırmaları, en yeniden başlayarak; her satır para birimlerini gösterecek şekilde açılır.
- **Otomatik güncelleme**: her gün seçilen saatte veya Windows Görev Zamanlayıcı ile.
- **Kontrol altında hatalar**: bir para birimindeki hata diğerlerini durdurmaz; her çalıştırma neyin yanlış gittiğini
  söyler.
- Herkesin kendi **SAP kullanıcısıyla oturum açma**, kurlar üzerindeki SAP yetkileriyle; yönetici her kullanıcıya
  *Kur güncelleme* ve *Geçmiş* işlevlerini atar.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri, Service Layer ile |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | Windows 10 ve 11, Windows Server 2016 ve üzeri, 64 bit; Microsoft Edge WebView2 Runtime |
| Ağ | seçilen kur kaynağına internet erişimi (ECB, İtalya Merkez Bankası veya kendi API anahtarıyla Open Exchange Rates) |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |
| Kurulum | program klasörü çıkarılır, kurulum gerekmez; .NET dahildir |
| Lisans | XEI lisans kodu; serbest, sunucu başına veya şirket başına (30 gün ücretsiz deneme) |

## Güncel sürüm

**1.0.0** – [sürüm notlarına](../../manuali/tr/rateupdater/note-rilascio-1.0.0.md) ve
[kullanım kılavuzuna](../../manuali/tr/rateupdater/manuale-utente.md) bakın.
