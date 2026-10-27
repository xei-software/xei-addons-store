---
title: XEI.CommissionManagement – Kurulum, lisans, menüler ve yetkiler
description: XEI.CommissionManagement'ın nasıl kurulacağı, lisansın nasıl etkinleştirileceği, menülerin nerede bulunacağı ve yetkilerin nasıl atanacağı.
lang: tr
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement – Kurulum, lisans, menüler ve yetkiler

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Program dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |
| E-posta | erişilebilir bir SMTP posta sunucusu; yalnızca dökümleri temsilcilere e-posta ile göndermek için (Yapılandırma › E-posta) |

## Kurulum

1. `XEI.CommissionManagement.zip` paketini indirin.
2. SAP Business One'da **Extension Manager**'ı açın, paketi içe aktarın ve şirkete atayın.
3. İlk açılışta eklenti alanları, tabloları, dizinleri ve yetkileri oluşturur. Belge satırlarındaki alanların
   oluşturulması **birkaç dakika** sürer: SAP birkaç kez *"Database structure has been modified... all open windows
   will be closed. Continue?"* (Veritabanı yapısı değiştirildi... tüm açık pencereler kapatılacak. Devam edilsin
   mi?) mesajını gösterir: **Yes** (Evet) yanıtını verin.

Eklentinin her güncellemesi aynı şekilde kurulur.

Kurulumdan sonra: önce **Yapılandırma**'yı, sonra **Temsilciler**'i (roller, üstler, yüzdeler), sonra **Kuralları**
doldurun. Belgeler yüzdeleri ancak bundan sonra alır. Süper kullanıcı olmayan kullanıcılara **yetkiler** verilmelidir
(aşağıda).

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

Öğeler **XEI-Addon › Komisyonlar** altındadır.

| Öğe | İşlev |
|---|---|
| Yapılandırma | seçenekler (altı sekme) ve kuralların arama sırası (kullanım kılavuzu, bölüm 5) |
| Temsilciler | rol, üstler, varsayılan %, faturada %, ödeme, satıcı, SAP kullanıcısı (bölüm 6) |
| Yüzde kuralları | müşteri, müşteri grubu, kalem, kalem grubu, fiyat listesi başına % (bölüm 7) |
| Kademeler ve primler | yıllık satış üzerinden primler, Yapılandırma'da etkinse (bölüm 15) |
| % kontrolü ve ataması | belgelerin kurallarla karşılaştırılması ve toplu düzeltme (bölüm 9) |
| Komisyon hesaplama | faturalar, peşinat faturaları ve alacak dekontları üzerinde hesaplama (bölüm 10) |
| Hesaplanan komisyonlar | görüntüleme, düzeltme, yeniden hesaplama, silme (bölüm 11) |
| Ödeme | ödenecek tahsil edilmiş paylar, ters kaydedilecek ödenmemişler (bölüm 12) |
| Düzeltmeler | temsilci ve ay başına elle tutarlar, temsilci fatura taslakları (bölüm 13) |
| Komisyon ekstresi | hesaplanan, ödenecek, ödenen ve düzeltmeler; CSV, yazdırma/PDF, e-posta (bölüm 14) |
| Kontroller | kontrol edilecek sorunlar (bölüm 16) |
| Informazioni (Bilgi), Traduzioni (Çeviriler), Licenza (Lisans) | XEI eklentilerinin ortak öğeleri; Licenza: durum ve lisans kodu |

## Yetkiler

Eklenti SAP'nin *General Authorizations* (Genel yetkiler) penceresinde (*Administration* › *System Initialization* ›
*Authorizations* (Yönetim › Sistem başlatma › Yetkiler)) *User Authorization* (Kullanıcı yetkisi) altında beş alt
öğeli **Provvigioni** (Komisyonlar) öğesini oluşturur. Süper kullanıcılar her zaman her şeye sahiptir; diğer
kullanıcılara her öğe için *No Authorization* (Yetki yok), *Read Only* (Yalnızca okuma) veya *Full Authorization*
(Tam yetki) atanır.

![Genel yetkiler](../../_img/commissionmanagement/autorizzazioni.png)

*Genel yetkiler: yetkisi olmayan bir kullanıcı için beş alt öğeli Provvigioni (Komisyonlar) öğesi.*

| Yetki | Yalnızca okuma | Tam |
|---|---|---|
| Configurazione (Yapılandırma) | – | Yapılandırma'yı açmak ve kaydetmek |
| Agenti, regole e scaglioni (Temsilciler, kurallar ve kademeler) | görüntülemek | temsilcileri, kuralları ve kademeleri kaydetmek |
| Controllo, calcolo e verifiche (Kontrol, hesaplama ve kontroller) | Kontrol, Hesaplama, Hesaplanan komisyonlar, Kontroller'i görüntülemek | %'leri uygulamak, hesaplamak, yeniden hesaplamak, payları kaydetmek, silmek |
| Liquidazione, conguagli e bozze fatture (Ödeme, düzeltmeler ve fatura taslakları) | Ödeme ve Düzeltmeler'i görüntülemek | ödemeleri onaylamak, düzeltmeleri kaydetmek, primleri kaydetmek, taslak oluşturmak |
| Estratto di tutti gli agenti (Tüm temsilcilerin ekstresi) | tüm temsilcilerin ekstresini görmek (olmadan: yalnızca kendininkiler) | e-postayla gönderim de |

Yetki olmadan menü öğesi durum çubuğunda *"İşleve izin verilmiyor: «…» yetkisi gerekir (Genel yetkiler >
Provvigioni)"* yanıtını verir; yalnızca okuma yetkisiyle pencere açılır, ama değişiklik yapan düğmeler *"İşleme izin
verilmiyor: «…» üzerinde tam yetki gerekir (Genel yetkiler > Provvigioni)"* yanıtını verir.

## Destek

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com). Destek için:
[info@xeisrl.com](mailto:info@xeisrl.com). Talebinizde eklentinin sürümünü (*Informazioni* (Bilgi) menüsü) ve
sorunun bir açıklamasını belirtin.
