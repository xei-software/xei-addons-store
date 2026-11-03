---
title: SAP Business One için XEI Rate Updater – Kullanım kılavuzu
description: "SAP Business One'da döviz kurları: kurulum, ilk başlatma, elle ve otomatik güncelleme, geçmiş ve lisans."
lang: tr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# SAP Business One için XEI Rate Updater – Kullanım kılavuzu

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri, Service Layer ile |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | Windows 10 ve 11, Windows Server 2016 ve üzeri, 64 bit; Microsoft Edge WebView2 Runtime |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |

## 1. Programın işlevi

SAP Business One için XEI Rate Updater, SAP Business One'daki **döviz kurlarını** resmi bir kaynağın yayınladığı
kurlarla günceller:

1. seçilen **kaynağın** istenen tarihe ait kurlarını alır;
2. SAP şirketinden **yerel para birimini** ve kurların **yönünü** okur: doğrudan kur (bir birim yabancı para birimi
   karşılığında yerel para birimi) veya dolaylı kur (bir birim yerel para birimi karşılığında yabancı para birimi);
3. yerel para birimi euro değilse **çapraz kurları** ona göre hesaplar;
4. **şirketin yönettiği her para birimi** için SAP'ye o tarihteki kuru, şirketin yönünde ve altı ondalık basamağa
   kesilmiş olarak yazar;
5. çalıştırmayı **geçmişe** kaydeder.

Bir para birimindeki hata diğerlerini durdurmaz.

### Kurların tarihi

Bir günün kurları gün sonunda yayınlanır. Bu nedenle SAP'de bir günün kurları için **bir önceki gün** yayınlanan kurlar
kullanılır. Yayın olmayan günlerde (hafta sonları, tatil günleri) bundan önceki son yayın günü geçerlidir.

*Örnek*: 24 Şubat 2025 Pazartesi gününün kurları, 21 Şubat Cuma gününün kurlarıdır. Kurların tarihi gelecekte olamaz.

### Kur kaynakları

| Kaynak | Notlar |
|---|---|
| Avrupa Merkez Bankası (ECB) | varsayılan, ücretsiz, anahtar gerekmez |
| İtalya Merkez Bankası | İtalya'nın resmi kurları, çok sayıda para birimi |
| Open Exchange Rates | bir Open Exchange Rates API anahtarı gerekir (Ayarlar › Döviz kurları) |

Tüm kaynaklar kurları euroya göre yayınlar. Euro dışında bir yerel para biriminde kaynak onu kote etmelidir.

### Para birimleri

Program para birimlerini **ISO kodundan** tanır (örneğin `USD`, `CHF`). SAP'de yabancı para birimlerinin kodu ISO kodu
olmalıdır. Yerel para biriminin SAP'de başka bir kodu varsa (örneğin euro için «Eu» veya «€»), ISO kodu
*Ayarlar › Döviz kurları* bölümünde belirtilir.

## 2. Kurulum

1. Zip dosyasındaki klasörü bilgisayara çıkarın, örneğin `C:\XEI\RateUpdater` klasörüne.
2. **XEI.RateUpdater.exe** dosyasını başlatın. Program .NET'i zaten içerir. **Microsoft Edge WebView2 Runtime**
   gerekir; genellikle zaten yüklüdür: yoksa program bunu bildirir ve indirmeyi önerir.

Programın kurulumu yoktur. Ayarlar ve geçmiş, bilgisayarın tüm kullanıcılarına ait Windows veri klasöründe bulunur;
bu nedenle o bilgisayarda programı kullanan herkes ve zamanlanmış güncelleme için geçerlidir.

## 3. İlk başlatma

İlk açılışta program **İlk başlatma** sayfasını gösterir: henüz SAP'ye bağlı değildir. İlk başlatma kodu zaten
yazılıdır.

1. **SAP bağlantısı**:
   - *Service Layer adresi*;
   - *SAP şirketleri*: girişte seçilebilen veritabanları;
   - **Bağlantıyı dene**.
2. **Giriş ve ilk yönetici**:
   - *Operatör girişi*: **Herkesin kendi SAP kullanıcısı** (herkes kendi SAP kullanıcısıyla oturum açar) veya
     **Kendi kullanıcılar ve teknik SAP kullanıcısı**;
   - *İlk yöneticinin SAP kullanıcısı* (örneğin `manager`);
   - *Teknik SAP kullanıcısı* ve parolası: **otomatik güncelleme** için gerekir. Yalnızca kurları yazma yetkisi olan
     ayrı bir kullanıcı tercih edin.
3. **Kaydet ve yeniden başlat**: program giriş sayfasında yeniden açılır.

Aynı ayarlar daha sonra **Ayarlar › SAP** bölümünde değiştirilir.

![İlk başlatma](../../_img/rateupdater/00b-primo-avvio.png)

*İlk başlatma: SAP bağlantısı, lisans kapsamı ve ilk yönetici.*

![Ayarlar › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Ayarlar › SAP: Service Layer adresi, şirketler ve operatör girişi.*

## 4. Oturum açma

**SAP Business One kullanıcısı** ve parolasıyla oturum açılır. Sağ üstte kullanıcı ve şirket görünür.

![Oturum açma](../../_img/rateupdater/00-accesso.png)

*SAP Business One kullanıcısıyla oturum açma.*

*Herkesin kendi SAP kullanıcısı* seçeneğinde program kurları çalışan kişinin kullanıcısıyla yazar: o kişinin kurlar
üzerindeki SAP yetkileri geçerlidir.

### Kullanıcıların işlevleri

Bir yönetici, menüdeki **Kullanıcılar** sayfasından her kullanıcıya işlevleri atar; sayfa SAP kullanıcıları ve kendi
kullanıcılar için aynıdır:

| İşlev | Neye izin verir |
|---|---|
| Kur güncelleme | Döviz kurları sayfasından SAP'deki kurları güncellemeye |
| Geçmiş | elle ve otomatik güncelleme çalıştırmalarını görmeye |

Yönetici tüm işlevlere sahiptir. İlk yönetici, İlk başlatma sırasında belirtilen SAP kullanıcısıdır.

## 5. Döviz kurları

**Döviz kurları** menüsü.

1. **SAP'deki kurların tarihi**: başlangıçta bugündür, gelecekte olamaz. Altında hangi kurların kullanıldığı ve
   ayarlanan kaynak yazılıdır.
2. **SAP'deki kurları güncelle** düğmesine basın.
3. **Sonuç** tarihi, kaynağı, kurların gününü, kaç para biriminin yazıldığını ve yerel para birimini gösterir. Tablo,
   kaynaktaki her para birimi için şunları gösterir:

| Sütun | Ne gösterir |
|---|---|
| Para birimi | ISO kodu |
| Doğrudan kur | bir birim yabancı para birimi karşılığında yerel para birimi |
| Dolaylı kur | bir birim yerel para birimi karşılığında yabancı para birimi |
| Sonuç | **SAP'ye yazıldı**, **yönetilmiyor** (şirket bu para birimini kullanmıyor) veya SAP hatasıyla birlikte reddedildi |

Altında, son çalıştırmayla birlikte **otomatik güncellemenin** durumu bulunur.

![Döviz kurları](../../_img/rateupdater/01-cambi.png)

*Döviz kurları: tarih, kaynak ve otomatik güncellemenin durumu.*

![Güncellemenin sonucu](../../_img/rateupdater/02-cambi-esito.png)

*Sonuç: kaynağın kurları, SAP'ye yazılan para birimleri ve şirketin yönetmediği para birimleri.*

## 6. Geçmiş

**Geçmiş** menüsü: şirketin çalıştırmaları, en yeniden başlayarak.

| Sütun | Ne gösterir |
|---|---|
| Başlangıç | çalıştırmanın tarihi ve saati |
| Başlatan | kullanıcı veya *otomatik* |
| Kur tarihi | SAP'deki kurların tarihi |
| Kaynak | kurların kaynağı |
| Kurların yayın tarihi | kullanılan kurların günü |
| Yazılan para birimleri | SAP'ye kaç para biriminin yazıldığı |
| Sonuç | **başarılı** veya **başarısız** |

Bir satır, her birinin kurları ve sonucuyla birlikte para birimlerini gösterecek şekilde açılır. Geçmiş son
çalıştırmaları tutar (başlangıçta 100, *Ayarlar › Döviz kurları* bölümünde).

![Geçmiş](../../_img/rateupdater/03-storico.png)

*Geçmiş: şirketin elle ve otomatik güncellemeleri.*

![Para birimleriyle geçmiş](../../_img/rateupdater/03b-storico-valute.png)

*Açılmış bir satır: her para biriminin kurları ve sonucu.*

## 7. Ayarlar › Döviz kurları

Yalnızca yöneticiler için. Değişikliklerden sonra **Ayarları kaydet** düğmesine basın.

| Ayar | İşlevi |
|---|---|
| Kur kaynağı | Avrupa Merkez Bankası (varsayılan), İtalya Merkez Bankası veya Open Exchange Rates |
| Yerel para biriminin ISO kodu | yalnızca SAP'de yerel para biriminin kodu ISO kodundan farklıysa; boş = SAP'den alınır |
| Open Exchange Rates API anahtarı | yalnızca Open Exchange Rates kaynağıyla; şifrelenmiş olarak kaydedilir |
| Otomatik güncelleme | program her gün bugünün kurlarını her şirkette teknik SAP kullanıcısıyla kendiliğinden günceller |
| Otomatik güncelleme saati | SS:dd biçiminde (varsayılan 07:00) |
| Geçmişteki çalıştırmalar | her şirket için kaç çalıştırma tutulacağı, 10 ile 1000 arası (varsayılan 100) |

![Ayarlar › Döviz kurları](../../_img/rateupdater/04-impostazioni-cambi.png)

*Ayarlar › Döviz kurları: kaynak, yerel para birimi, otomatik güncelleme ve geçmiş.*

## 8. Otomatik güncelleme

Bugünün kurları her gün iki şekilde güncellenir.

### Program açıkken

**Otomatik güncelleme** açıkken, ayarlanan saat geçtikten sonra program bugünün kurlarını her şirkette teknik SAP
kullanıcısıyla günceller ve çalıştırmayı geçmişe kaydeder (*Başlatan*: otomatik). Program belirlenen saatte kapalıysa,
yeniden açılır açılmaz günceller. Kaynak veya SAP yanıt vermezse kısa bir süre sonra yeniden dener.

### Windows Görev Zamanlayıcı ile

Böylece kurlar program açılmadan da güncellenir.

1. İlk başlatmayı yapın ve **teknik SAP kullanıcısını** ayarlayın (Ayarlar › SAP).

   ![Teknik SAP kullanıcısı](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *Ayarlar › SAP bölümünde teknik SAP kullanıcısı.*

2. Windows'ta **Görev Zamanlayıcı**'yı açın ve bir temel görev oluşturun, örneğin her gün saat 7:00'de.
3. Eylem olarak **Program başlat** seçeneğini seçin:
   - program: program klasöründeki `XEI.RateUpdater.exe`;
   - bağımsız değişkenler: `aggiorna`.
4. Görevin özelliklerinde, bilgisayarın bir Windows kullanıcısıyla **Kullanıcının oturum açıp açmadığına bakılmaksızın
   çalıştır** seçeneğini seçin.

Komut bugünün kurlarını teknik SAP kullanıcısıyla günceller ve pencere açmadan kapanır. Programla aynı ayarları ve aynı
geçmişi kullanır. İsteğe bağlı bağımsız değişkenler:

| Bağımsız değişken | Anlamı |
|---|---|
| `--societa <SAP veritabanı>` | güncellenecek şirket; yalnızca bir şirket yapılandırılmışsa gerekmez |
| `--data aaaa-mm-gg` | bugün değilse kurların tarihi (yıl-ay-gün) |

Görev Zamanlayıcı sonucu alır: **0** başarılı, **1** başarısız veya reddedilen bir para birimiyle, **2** hatalı
bağımsız değişkenler. Ayrıntılar geçmiştedir. Komut bugünün kurlarını zaten güncellediyse, açık program bunları
yeniden güncellemez.

## 9. Lisans

Program, XEI tarafından verilen bir **lisans kodu** ile çalışır; üç kapsam vardır:

| Kapsam | Geçerli olduğu yer |
|---|---|
| Tek şirket | bir SAP veritabanı |
| Sunucu | SQL Server veya SAP HANA örneğinin tüm şirketleri |
| Serbest | bir veritabanına bağlı değildir |

**Ücretsiz deneme** 30 gün sürer ve serbesttir.

![Lisans](../../_img/rateupdater/06-licenza.png)

*Lisans sayfası: durum, son kullanma tarihi, kapsam ve kod alanı.*

![Ayarlar › Lisans](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Ayarlar › Lisans: lisansın üç kapsamı.*

**Lisans** menüsü: lisansın durumu, son kullanma tarihi ve kapsamı. XEI'den alınan kod **Lisans kodu girin** alanına
yapıştırılır ve yeniden başlatmadan hemen geçerli olur. Şirket veya sunucu başına bir lisans için programın lisans
veritabanına salt okunur olarak bağlı olması gerekir (*Ayarlar › Lisans*, **Bağlantıyı test et**): XEI'ye
gönderilecek şirket ve sunucu kodları orada ve Lisans sayfasında görünür.

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Sık sorulan sorular ve sorunlar

| Ne görüyorsunuz | Neden | Ne yapmalı |
|---|---|---|
| Bir para birimi *yönetilmiyor* | SAP şirketi bu para birimini kullanmıyor | Hiçbir şey: yalnızca şirketin para birimleri yazılır |
| Şirketin bir para birimi güncellenmiyor | SAP'de para biriminin kodu ISO kodu değil | SAP'de ISO kodunu kullanın (örneğin `USD`) |
| Çalıştırma, yerel para birimiyle ilgili bir hatayla hemen duruyor | Kaynak yerel para birimini kote etmiyor veya SAP'de kodu ISO değil | ISO kodunu *Ayarlar › Döviz kurları* bölümünde girin veya başka bir kaynak seçin |
| Bir para biriminin sonucu bir SAP hatası | SAP kuru reddetti (örneğin kullanıcının yetkileri nedeniyle) | Hatayı okuyun; kullanıcının kurlar üzerindeki SAP yetkilerini kontrol edin |
| Otomatik güncelleme başlamıyor | Kapalı veya teknik SAP kullanıcısı eksik | *Ayarlar › Döviz kurları* bölümünde açın ve teknik kullanıcıyı *Ayarlar › SAP* bölümünde ayarlayın |
| Program WebView2'yi yüklemeyi istiyor | Microsoft Edge WebView2 Runtime eksik | Önerilen indirmeyi kabul edin veya Microsoft'un sitesinden yükleyin |

## 11. Destek

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com). Destek için:
[info@xeisrl.com](mailto:info@xeisrl.com). Talebinizde programın sürümünü (*Bilgi* menüsü) ve sorunun bir açıklamasını
belirtin.
