---
title: XEI.ContoLavoro – Kurulum, lisans ve menüler
description: XEI.ContoLavoro'nun nasıl kurulacağı, lisansın nasıl etkinleştirileceği ve menülerin nerede bulunacağı.
lang: tr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Kurulum, lisans ve menüler

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Program dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |

## Kurulum

1. `XEI.ContoLavoro.zip` paketini indirin.
2. SAP Business One'da **Extension Manager**'ı açın, paketi içe aktarın ve şirkete atayın.
3. İlk açılışta eklenti tabloları, alanları, fason iş emri nesnesini ve depodaki fasoncu tedarikçinin formatlı
   aramasını oluşturur. SAP *"Database structure has been modified..."* (Veritabanı yapısı değiştirildi...) mesajını
   gösterir: **Yes** (Evet) yanıtını verin ve istemciyi kullanmadan önce işlemin bitmesini bekleyin.

Eklentinin her güncellemesi aynı şekilde kurulur.

Kurulumdan sonra: **Yapılandırma**'yı doldurun, ardından SAP'de fasoncunun her deposuna tedarikçisini bağlayın
(depo ana verilerindeki *Fornitore terzista* (Fasoncu tedarikçi) alanı) ve fason üretim kalemlerini işaretleyin
(kullanım kılavuzu, bölüm 3 ve 6).

## Lisans

Eklenti, XEI tarafından verilen bir **lisans kodu** ile çalışır.

- **Deneme**: denemeyi talep ettikten sonra e-posta ile, gönderimden itibaren 30 gün boyunca her şirkette geçerli bir
  **deneme kodu** alırsınız.
- **Satın alma**: **Licenza** (Lisans) penceresindeki iki kodu XEI'ye gönderir ve lisans kodunu alırsınız.

**Licenza** (Lisans) penceresi:

- Geçerli bir kod olmadan eklenti **kilitlidir**: menüsünde yalnızca *Informazioni* (Bilgi) ve *Licenza* (Lisans)
  kalır ve başlangıçta durumu ve nedeni gösteren **Licenza** penceresi kendiliğinden açılır.
- Pencere **şirket kodunu** ve **sunucu kodunu** gösterir: lisansı satın almak için bunları *Copia* (Kopyala) ile
  [license@xeisrl.com](mailto:license@xeisrl.com) adresine gönderin.
- Bir SAP **süper kullanıcısı**, alınan kodu *Inserisci un codice di licenza* (Lisans kodu girin) alanına yapıştırır
  ve *Salva codice* (Kodu kaydet) düğmesine basar: eklentinin kilidi, SAP yeniden başlatılmadan hemen açılır.
- Deneme kodu her şirkette geçerlidir. Lisans kodu, gönderilen kodların şirketi (veritabanı) veya sunucusu için
  geçerlidir.
- Aynı pencere istenildiği zaman *Licenza* (Lisans) menüsünden açılır: lisansın durumu, bitiş tarihi, numarası ve
  kapsamı.

## Menüler

Öğeler **XEI-Addon › Fason üretim** altındadır. **Fason üretim** alt menüsü, Yapılandırma'da seçilen SAP modülünde de
görünür (*Purchasing - A/P* (Satınalma - Borçlar) veya *Production* (Üretim)).

| Öğe | İşlev |
|---|---|
| Fason iş emri | fason iş emirlerini açma, arama ve oluşturma (kullanım kılavuzu, bölüm 4 ve 5) |
| Üretim siparişlerinden iş emri oluştur | üretim siparişlerinin dış işçiliklerinden fason iş emirleri (bölüm 6) |
| Fasoncudan teslim alma | fasoncunun bir irsaliyesindeki ürünlerin birden fazla fason iş emrine girişi (ürünlerin girişi ve bileşenlerin çıkışı) |
| Toplu bileşen nakli | Yapılandırma'da etkinse, birden fazla fason iş emri için bileşenlerin gönderilmesi (bölüm 9) |
| İş emirleri arasında bileşen nakli | fasoncuda bulunan stoku bir fason iş emrinden diğerine taşır (bölüm 9) |
| Ürün mal girişlerini toplu kapatma | ürünlerin açık kalan mal girişlerini kapatır (bölüm 9) |
| Fasoncu işçilik fiyatları | fasoncu ve ürün bazında işçilik fiyatları (bölüm 9) |
| Yapılandırma | eklentinin seçenekleri (bölüm 3) |
| Informazioni (Bilgi), Traduzioni (Çeviriler), Licenza (Lisans) | XEI eklentilerinin ortak öğeleri; Licenza: durum ve lisans kodu |
