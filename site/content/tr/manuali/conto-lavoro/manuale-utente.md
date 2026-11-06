---
title: XEI.ContoLavoro – Kullanım kılavuzu
description: XEI.ContoLavoro ile fason iş emirlerinin, bileşen gönderimlerinin, ürün girişlerinin ve üretim siparişlerinden fason üretimin yönetimi.
lang: tr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Kullanım kılavuzu

Kurulum, lisans ve menüler ayrıca
[kurulum kılavuzunda](installazione.md) anlatılmaktadır.

## 1. Eklenti ne yapar

XEI.ContoLavoro, şirketten bileşen alan, bunları işleyen ve bir mamul veya yarı mamul olarak geri teslim eden
**fasonculara** (dış tedarikçiler) verilen işçilikleri yönetir. Her işçilik için, aşağıdakileri bir arada tutan bir
**fason iş emri** açılır:

- elde edilecek **ürünler** ve ürün ağaçları (gönderilecek bileşenler ve ödenecek işçilikler);
- fasoncuya verilen, fason iş emriyle otomatik olarak uyumlu tutulan **satınalma siparişi**;
- fasoncunun deposuna yapılan **bileşen gönderimleri**, **geri almalar** ve **fireler**;
- ürünlerin **ürün girişi**: ürünlerin ve işçiliklerin mal girişi, tüketilen bileşenlerin mal çıkışı, bir üretim
  siparişinden gelen ürünler için üretimden giriş (bölüm 6);
- gerçek zamanlı durum: ne kadar gönderildiği ve kullanıldığı, fasoncuda ne kaldığı ve ne eksik olduğu.

Tüm ürünler girildiğinde ve fasoncuda bileşen kalmadığında fason iş emri kendiliğinden kapanır.

### Öne çıkanlar

- Stok nakli gibi bir başlık: depolar satırlara aktarılır, fasoncu deposu hareketlerden sonra korunur.
- Partiler ve seri numaraları eklentide seçilir: iş emrinin fasoncudaki partilerinden öneri (izlenebilirlik) ve
  FEFO, elle değiştirilebilir; giren ürünün partisi yapılandırılabilir bir SQL komutuyla; ürün girişi tek bir
  işlemde.
- Tüm bağlı belgelerin gruplanmış ve açılabilir olarak yer aldığı Belgeler sekmesi.
- Ürün maliyetleri her kayıtta yeniden hesaplanır; satınalma siparişi otomatik olarak uyumlu tutulur.
- Üretim siparişlerinden fason iş emirleri, toplu nakil ve iş emirleri arasında nakil, mal girişlerinin toplu
  kapatılması.
- SQL Server ve SAP HANA'da aynı çalışma; çevrilebilir metinler.

## 2. Kurulum ve menüler

### Kurulum

- `XEI.ContoLavoro.zip` paketi SAP Business One'ın Extension Manager'ına içe aktarılır.
- İlk başlatmada eklenti tabloları, alanları, `XEI_CL_COMMESSA` nesnesini (UDO) ve depo üzerinde fasoncu
  tedarikçinin formatlı aramasını oluşturur. SAP *"veritabanı yapısının değiştirildiğini"* onaylamanızı ister:
  yanıtlayın ve istemciyi kullanmadan önce işlemin bitmesini bekleyin.

### Menüler

**Modules › Administration › Add-Ons** (Modüller › Yönetim › Eklentiler) **› XEI-Addon › Fason üretim**:

| Giriş | İşlev |
|---|---|
| Fason iş emri | fason iş emirlerinin açılması, aranması ve oluşturulması |
| Üretim siparişlerinden iş emri oluştur | üretim siparişlerinin dış işçiliklerinden fason iş emirleri (bölüm 6) |
| Fasoncudan teslim alma | fasoncunun birden çok iş emrine ait ürünler içeren bir irsaliyesi: tedarikçi seçilir, iş emirlerinin açık ürünlerinde teslim alınan miktarlar girilir (*Öner* = kalan) ve *Kaydet* ürün girişini iş emri iş emri yapar; ürünlerin girişi ve bileşenlerin çıkışıyla |
| Toplu bileşen nakli | birden çok iş emri için bileşen gönderimi (ilgili seçenekle etkin) |
| İş emirleri arasında bileşen nakli | fasoncuda bulunan stoku bir iş emrinden diğerine taşır |
| Ürün mal girişlerini toplu kapatma | açık kalan ürün mal girişlerini kapatır |
| Fasoncu işçilik fiyatları | tedarikçi ve ürüne göre işçilik fiyatları |
| Yapılandırma | eklentinin seçenekleri |
| Informazioni (Bilgi), Traduzioni (Çeviriler), Licenza (Lisans) | XEI eklentilerinde ortak girişler; Licenza: lisansın durumu ve kodu |

*Yapılandırma*, *Informazioni*, *Traduzioni* ve *Licenza* dışındaki aynı girişler, yapılandırmada seçilen SAP
modülünde de (bölüm 3), seçilen konumda bulunur: **Modules › Purchasing - A/P › Fason üretim** (Modüller ›
Satınalma - Borçlar; varsayılan) veya **Modules › Production › Fason üretim** (Modüller › Üretim).

### Lisans

Eklenti, XEI tarafından verilen bir **lisans kodu** ile çalışır. Deneme talep edildikten sonra e-posta ile, gönderim
tarihinden itibaren 30 gün boyunca herhangi bir şirkette geçerli bir **deneme kodu** alınır; satın almak için
**Licenza** (Lisans) penceresindeki iki kod XEI'ye gönderilir ve lisans kodu alınır.

- Geçerli bir kod olmadan eklenti **kilitlidir**: menüsünde yalnızca *Informazioni* (Bilgi) ve *Licenza* (Lisans)
  kalır ve başlangıçta **Licenza** penceresi durum ve nedenle birlikte kendiliğinden açılır.
- Pencere **şirket kodunu** ve **sunucu kodunu** gösterir: lisansı satın almak için *Copia* (Kopyala) ile bunları
  [license@xeisrl.com](mailto:license@xeisrl.com) adresine gönderin.
- **Süper kullanıcı** olan bir SAP kullanıcısı, alınan kodu *Inserisci un codice di licenza* (Lisans kodu girin)
  alanına yapıştırır ve *Salva codice* (Kodu kaydet) düğmesine basar: eklentinin kilidi SAP yeniden başlatılmadan
  hemen açılır.
- Lisans kodu, şirket (veritabanı) veya gönderilen kodların sunucusu için geçerlidir.
- Aynı pencere *Licenza* menüsünden her zaman açılır: lisansın durumu, bitiş tarihi, numarası ve kapsamı.

## 3. Yapılandırma

Seçenekler sekmeli bir formda ayarlanır (*Partiler* sekmesi bölüm 7'de anlatılmıştır). Seçenekler tüm şirket için
geçerlidir; zaten açık olan formlar bunları yeniden açıldıklarında kullanır.

![Fiyatlar](../../_img/contolavoro/11_config_prezzi.png)

*Fiyatlar*

![Stok](../../_img/contolavoro/12_config_magazzino.png)

*Stok*

| Seçenek | Etki | Varsayılan |
|---|---|---|
| **Genel** | | |
| Kaynak satınalma siparişi | iş emrini doğduğu satınalma siparişine bağlamak için alan | Hayır |
| Kaynak müşteri siparişi | ürün satırlarında müşteri siparişi sütunu | Hayır |
| Ürün ağacı olmayan ürünler | ürün ağacı olmayan ürünlere izin verir: elle oluşturulur | Hayır |
| Ürünün mal girişini kapat | ürün girişinden sonra ürünün mal girişi kapatılır (faturalanmaz) | Hayır |
| Ürün mal girişinin fiyatını yeniden hesapla | işçilik fiyatı değişirse ürünün mal girişini günceller | Hayır |
| Üretim siparişlerinden tedarikçi teklifleri | üretim siparişlerinden oluştururken tedarikçi tekliflerini bağlar | Hayır |
| Toplu nakil | menü girişini etkinleştirir | Hayır |
| Fasoncu ürün ağacı | ürün ağacında "Fasoncu ürün ağacı" sütununu gösterir | Evet |
| Tedarikçi sözleşmeleri | işçilik fiyatları sözleşmelerden (yalnızca SQL Server) | Hayır |
| Varsayılan fiyat listesi | yeni iş emirlerinde önerilen maliyet listesi | – |
| Menü ayrıca SAP modülünde | *Fason üretim* alt menüsünün bulunduğu modül: Purchasing - A/P (Satınalma - Borçlar) veya Production (Üretim) | Purchasing - A/P |
| Modül menüsündeki konum | en sonda, en başta veya modülün bir girişinden sonra | en sonda |
| **Fiyatlar** | | |
| İşçilik / bileşen fiyatı değiştirilebilir | iş emrinin ürün ağacında fiyatlar değiştirilebilir | Hayır |
| İşçilik / bileşen fiyatı ürün ağacından | öncelikle ürün ağacının fiyatı (bileşen: yalnızca üretim siparişleri) | Hayır |
| İşçilik maliyetini dağıt | toplam maliyeti ürünlere dağıtır (yalnızca üretim siparişlerinden) | Hayır |
| Sıfır fiyatlarda engelleme | ürün girişine sıfır fiyatlarla da izin verilir | Hayır |
| Bileşenleri yeniden değerle | üretim çıkışında bileşenlerin yeniden değerlemesi (sürekli envanter) | Hayır |
| **Stok** | | |
| Kalemin varsayılan deposu | bileşen satırları kalemin varsayılan deposundan başlar | Evet |
| Stok = gönderilen | belirtilen bileşenler için fasoncudaki stok gönderilmiş sayılır | Hayır |
| Satır bazında bileşenler | bileşenler ürün bazında ayrı tutulur | Hayır |
| Değişken ihtiyaç | gönderilen miktarı ürünlere dağıtır | Hayır |
| Stok nakli talepleri | stok nakli yerine stok nakli talebiyle bileşen gönderimi | Hayır |
| Toplama listesi | toplama listesini de oluşturur (talepleri etkinleştirir) | Hayır |
| **Seriler ve nedenler** | | |
| Seriler | satınalma siparişi, ürün ve işçilik mal girişleri, nakiller | SAP varsayılanı |
| Sevk nedenleri | nakiller, sipariş, mal girişi, çıkışlar, girişler için (şirket sevk nedenlerini kullanıyorsa) | – |
| **Partiler** | | |
| Giriş partisi komutu | girilen ürünün partisini döndüren, {ItemCode}, {WhsCode}, {DocEntry} içeren SQL (bkz. bölüm 7) | iş emri-sıra numarası |

## 4. Fason iş emri

### Başlık

Başlık, stok naklininki gibi düzenlenmiştir: solda tedarikçi, tedarikçi referansı, proje ve bağlı siparişler; sağda
numaralandırma, durum, tarihler, maliyet listesi ve iki depo.

- **Tedarikçi**: seçildiğinde kullanıcının deposunu ve tedarikçiye bağlı **fasoncu deposunu** (depo ana verilerinin
  *Fornitore terzista* (Fasoncu tedarikçi) alanı) ya da varsayılan olarak işaretlenmiş depoyu önerir.
- **Çıkış deposu**: şirketin deposu; bileşenler buradan çıkar, ürünler buraya geri gelir ve satınalma siparişinin
  satırları bu depo üzerinde oluşur.
- **Fasoncu deposu**: yalnızca iş emrinde bileşen hareketi olmadığı sürece değiştirilebilir; sonrasında alan devre
  dışı kalır ve kayıt değişikliği her durumda reddeder.
- Başlıktaki bir depo değiştirildiğinde, stok naklinde olduğu gibi, bunu ürün ağacının **henüz hareket görmemiş**
  satırlarına aktarmak önerilir.

### Ürünler

Kalem (listeden aynı anda birden çok kalem de) ve üretilecek miktar seçilir: ürün ağacı SAP'den kopyalanır ve bir
adede oranlanır (ürün ağacının temel miktarı dikkate alınarak). Sütunlar üretilecek miktarı, girilen miktarı,
kalanı, bileşenlerin ve işçiliklerin maliyetini gösterir.

### Ürün ağacı

Her ürün için: bileşenler (gönderilecek stok kalemleri) ve işçilikler (fasoncuya ödenen hizmetler). **Ürün ağacını
değiştir** ile henüz hareket görmemiş satırların depoları ve fiyatları değiştirilir; SAP'nin *Satır ekle* / *Satırı sil* komutlarıyla bileşen ve işçilik eklenir ya da hareket görmemiş olanlar kaldırılır. Ürün
satırının bağlam menüsünden: **Yeniden işle** (ürün, yeni işçiliklerle bir bileşen olarak fasoncuya geri gider) ve
**Ürün ağacını yeniden oluştur** (ürün ağacını seçilen bileşenlerle değiştirir).

### Bileşenler

Tüm ürünlerin bileşenleri, kaleme ve depolara göre gruplanmış olarak: ihtiyaç, kullanılan, şirkette kullanılabilir,
fasoncu deposundaki stok, talepler ve toplama listeleri, gönderilen, gönderilecek kalan, iş emrinin fasoncudaki
stoku, geri almalar ve fireler. Hareketler iş emrinin altındaki düğmelerle yapılır: **Bileşenleri gönder** ve **Geri
alma ve fire** (*Bileşenleri fasoncudan geri al*, *Fireyi naklet*, *Fasoncuda fire çıkışı*). Her biri, hareket
ettirilecek miktarların sarı hücrelerde olduğu bir pencere açar: *Öner* bunları doldurur, *Sıfırla* boşaltır ve elle
değiştirilebilirler.

### Belgeler

İş emrine bağlı tüm SAP belgeleri, zaman sırasına göre satır başına bir belge, açmak için bağlantılarıyla; *Göster*
belge türüne göre filtreler. Altta, *Belge satırları* içinde, seçilen belgenin satırları partiler, seri numaraları ve
depo yerleriyle birlikte.

## 5. İş akışı

1. **Fason iş emri**: tedarikçi, depolar, ürünler ve miktarlar; *Ekle*.
2. **Fasoncu siparişi**: *Fasoncu satınalma siparişi* penceresi satınalma siparişini oluşturur; ürün başına bir satır
   ve her işçilik için bir satır ile; sipariş zaten varsa düğme onu açar. İş emrinde sonradan yapılan değişiklikler
   (yeni veya silinmiş ürünler, miktarlar, fiyatlar, tarihler) kayıtta siparişe aktarılır; zaten teslim alınmış
   satırların yalnızca miktarı değişir.
3. **Bileşenleri gönder**: *Bileşen nakli* penceresinde *Gönderilecek* sütunu gönderilecek kalanı önerir (elle
   değiştirilebilir); *Tamam* fasoncunun deposuna stok naklini oluşturur. İlgili seçenekle, toplama listesiyle
   birlikte bir stok nakli talebi oluşturulur.
4. **Ürünleri teslim al**: *Ürün girişi* penceresinde *Girilecek* sütunu kalanı önerir (elle değiştirilebilir) ve
   *Hareket türü* *Ürün girişi ve bileşen çıkışı*, *Yalnızca ürün girişi* ve *Yalnızca bileşen çıkışı* arasında seçim
   yapar; ardından *Tamam*. Şunlar oluşturulur: satınalma siparişinden işçiliklerin ve ürünlerin mal girişi,
   bileşenlerin fasoncu deposundan mal çıkışı, üretim siparişlerinden gelen ürünler için üretimden girişler (bölüm 6).

> Ürün tam maliyetle girer (bileşenler + işçilik); "Ürünün mal girişini kapat" seçeneğiyle mal girişi kapatılır ve
> faturalanmaz: işçilikler faturalanır.

Çıkışı yapılacak bir bileşen iş emrinin fasoncudaki stokunu aşarsa, kalan stokun çıkışının yapılıp yapılmayacağı
sorulur (Evet / Hayır / Tümüne evet).

## 6. Üretim siparişlerinden fason üretim

Bir **üretim siparişinin** bazı aşamaları fasoncularda yapıldığında, eklenti fason iş emirlerini üretim siparişinin
satırlarından oluşturur. Her ürün girişinde fasoncunun tükettiği bileşenleri üretim siparişi için çeker ve tüm dış
işçilikler geri geldiğinde mamulün üretimden girişini kaydeder.

### SAP'de ayarlar

> Dış işçilik, **Conto lavoro** (Fason üretim) alanı = Evet olan bir **stok dışı kalemdir**, bir SAP kaynağı değildir:
> kaynak olarak tanımlanan bir işçilik üretim siparişleri listesinde görünmez.

| Nerede | Ne ayarlanır | Örnekte |
|---|---|---|
| İşçilik kaleminin kalem ana verileri | stok dışı kalem, **Conto lavoro** (Fason üretim) kullanıcı alanı = Evet; **tercih edilen tedarikçi**, listede önerilen fasoncudur | `LAV-SALD` Şasi kaynağı, tedarikçi `F-TER01`; `LAV-MONT` Aks montajı, tedarikçi `F-TER02` |
| Mamulün ürün ağacı | her dış işçilik için adet başına miktarla bir satır; fasoncuya gönderilecek bileşenlerin satırlarında işçiliğin koduyla **Lavorazione terzista** (Fasoncu işçiliği) alanı ve **Manuel** çekme yöntemi | `CMP-01`, `CMP-02` → `LAV-SALD`; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Mamulün ürün ağacı | tüm dış işçilikler geri geldiğinde mamul tamamlanıyorsa **Fasoncu ürün ağacı** = Evet: eklenti üretimden girişi kaydeder. Hayır ile üretimden girişi SAP'de siz kaydedersiniz | `PF-100` = Evet |
| Fasoncu deposunun depo ana verileri | **Fornitore terzista** (Fasoncu tedarikçi) alanı (bölüm 4) | `T-TER01` → `F-TER01`; `T-TER02` → `F-TER02` |
| *Fasoncu işçilik fiyatları* | fasoncu, mamul ve işçiliğe göre fiyat (fiyat arama sırası bölüm 9'da) | `F-TER01` / `PF-100` / `LAV-SALD` 12,00; `F-TER02` / `PF-100` / `LAV-MONT` 3,50 |

İşçiliğe bağlı geriye dönük çekilen bileşenler fasoncuya gönderilmez: bunları üretimden giriş, üretim siparişi
satırının deposundan çeker. Listenin **Neden / uyarılar** sütunu bunu belirtir. Ürün ağacının işçiliği olmayan diğer
bileşenleri her üretim siparişinde olduğu gibi kalır.

> **Ürün ağacı kaydedilirken kontrol.** **Lavorazione terzista** (Fasoncu işçiliği) alanı doldurulmuş bir ürün
> ağacını kaydettiğinizde eklenti girilen kodları kontrol eder. Bir sorun varsa, her durum için bir madde ile
> *"Ürün ağacı PF-100, "Lavorazione terzista" alanı:"* uyarısı görünür; ürün ağacı kayıtlı kalır.
>
> - Kaynak: *"LAV-SALD bir kaynaktır: dış işçilik, "Conto lavoro" = Evet olan stok dışı bir kalem olarak
>   oluşturulmalı ve bileşenler bu koda bağlanmalıdır."*
> - Kalem olmayan kod: *"LAV-SALD bir kalem değil."*
> - Conto lavoro olmayan kalem: *"LAV-SALD kaleminin ana verisinde "Conto lavoro" = Evet değil."*
> - Ürün ağacının satırı olmayan işçilik: *"LAV-SALD ürün ağacının bir satırı değil: üretim siparişinde işçilik
>   satırı olmayacak ve fason iş emri oluşturulamayacak."*
> - Geriye dönük çekilen bileşenler: *"LAV-SALD işçiliğiyle geriye dönük çekilen bileşenler: fasoncuya gönderilmez
>   (manuel çekme yöntemi gerekir)."*

### Adım adım örnek

`PF-100` Araba mamulünün iki dış işçiliği vardır: `F-TER01` «Örnek Fasoncu 1» fasoncusunda şasinin kaynağı ve
`F-TER02` «Örnek Fasoncu 2» fasoncusunda aksların montajı. Her arabada bir şasi ve iki aks vardır. 500 numaralı
üretim siparişi `01` deposunda 100 araba için serbest bırakılmıştır:

| Satır | Kalem | Miktar | Çekme | Lavorazione terzista | Fiyat |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Şasi kaynağı (işçilik) | 100 | | | 12,00 |
| 2 | `CMP-01` Boru (m) | 250 | Manuel | `LAV-SALD` | 4,00 |
| 3 | `CMP-02` Plaka | 400 | Manuel | `LAV-SALD` | 1,50 |
| 4 | `LAV-MONT` Aks montajı (işçilik) | 200 | | | 3,50 |
| 5 | `CMP-03` Tekerlek | 400 | Manuel | `LAV-MONT` | 5,00 |
| 6 | `CMP-04` Pim | 200 | Manuel | `LAV-MONT` | 2,00 |
| 7 | `CMP-05` Vida | 1.600 | geriye dönük | | |

| Adım | Oluşturulan SAP belgesi | Üretim siparişine etkisi |
|---|---|---|
| 1. **Fason üretim › Üretim siparişlerinden iş emri oluştur**: 500 numaralı üretim siparişinin iki satırını seçin ve *İş emri oluştur* düğmesine basın | SAP belgesi yok: 1001 numaralı fason iş emri (`F-TER01`, `01` deposundan `T-TER01` deposuna, ürün `LAV-SALD` 100, ürün ağacı adet başına `CMP-01` 2,5 ve `CMP-02` 4) ve 1002 numaralı iş emri (`F-TER02`, `01` deposundan `T-TER02` deposuna, ürün `LAV-MONT` 200, ürün ağacı adet başına `CMP-03` 2 ve `CMP-04` 1) | yok |
| 2. Her iş emrinde *Fasoncu siparişi* düğmesine basın ve *Fasoncu satınalma siparişi* penceresini onaylayın | `F-TER01` için satınalma siparişi: `LAV-SALD` 100 × 12,00; `F-TER02` için satınalma siparişi: `LAV-MONT` 200 × 3,50 | yok |
| 3. Her iş emrinde *Bileşenleri gönder* düğmesine ve önerilen miktarlarla *Tamam* düğmesine basın | `01` deposundan `T-TER01` deposuna stok nakli: `CMP-01` 250, `CMP-02` 400; `01` deposundan `T-TER02` deposuna: `CMP-03` 400, `CMP-04` 200 | yok |
| 4. 60 şasi geri gelir: 1001 numaralı iş emrinde *Ürünleri teslim al* düğmesine basın, *Ürün girişi* penceresinde *Girilecek* alanına 60 yazın ve *Tamam* düğmesine basın | siparişten mal girişi: `LAV-SALD` 60 × 12,00; `T-TER01` deposundan üretim için çıkış: `CMP-01` 150, `CMP-02` 240 | 2. ve 3. satırların bileşenleri çekilir; giriş yok: akslar eksik ve bir mesaj bunu belirtir (*"Üretim siparişi 500: mamul, LAV-MONT işçiliği de geri geldiğinde stoğa girecek."*) |
| 5. 100 aks geri gelir: 1002 numaralı iş emri, *Ürünleri teslim al*, *Girilecek* alanına 100, *Tamam* | mal girişi `LAV-MONT` 100 × 3,50; `T-TER02` deposundan üretim için çıkış: `CMP-03` 200, `CMP-04` 100; üretimden giriş `PF-100` **50** | 60 şasi ve 100 aks 50 araba için yeterlidir: 50 tamamlanır; SAP `CMP-05` 800 adedi geriye dönük çeker |
| 6. 100 aks daha geri gelir: 1002 numaralı iş emri, *Ürünleri teslim al*, *Girilecek* alanına 100, *Tamam* | mal girişi `LAV-MONT` 100; üretim için çıkış `CMP-03` 200, `CMP-04` 100; üretimden giriş `PF-100` **10** | 60 tamamlanır, diğerleri şasileri bekler (*"Üretim siparişi 500: mamulün 10 adedi stoğa girdi; diğerleri LAV-SALD işçiliği de geri geldiğinde girecek."*); 1002 numaralı iş emri kendiliğinden kapanır |
| 7. Son 40 şasi geri gelir: 1001 numaralı iş emri, *Ürünleri teslim al*, *Girilecek* alanına 40, *Tamam* | mal girişi `LAV-SALD` 40; üretim için çıkış `CMP-01` 100, `CMP-02` 160; üretimden giriş `PF-100` **40** | 100 tamamlanır; 1001 numaralı iş emri kendiliğinden kapanır. Üretim siparişini SAP'de siz kapatırsınız |

> Üretimden giriş, adet başına dış işçiliklerin maliyetiyle değerlenir: her işçilik için bileşenler ve işçilik
> fiyatı, adet başına miktarla çarpılarak. Örnekte bir arabanın değeri
> (2,5 × 4,00 + 4 × 1,50 + 12,00) + 2 × (2 × 5,00 + 1 × 2,00 + 3,50) = 28,00 + 31,00 = **59,00** olur.

### Özel durumlar

- **Birden çok üretim siparişi**: aynı tedarikçiye ve aynı iade deposuna (*İade deposu* sütunu) sahip satırlar aynı
  iş emrine girer, satır başına bir ürün; farklı iade depolarıyla farklı iş emirleri oluşur.
- **Fasoncu hizmetleri**: **Lavorazione terzista** (Fasoncu işçiliği) alanı olan stok dışı bir bileşen (örneğin bir
  test) iş emrinin bir işçiliği olur ve fasoncu siparişinde bir satır daha oluşur.
- **Fasoncu ürün ağacı = Hayır**: eklenti işçiliğin mal girişini ve bileşenlerin çıkışını kaydeder; üretimden girişi,
  örneğin bir iç montajdan sonra, SAP'de siz kaydedersiniz.
- Aynı üretim siparişinde **SAP'de kaydedilmiş üretimden girişler**: eklenti bunları düşer, mamul iki kez girmez.
- **Kesintiye uğrayan iş emri**: bir iş emrini kestiğinizde işçilik listeye geri döner ve başka bir iş emri
  oluşturabilirsiniz.
- **Geriye dönük çekilen bileşenler**: işçiliğe bağlı geriye dönük çekilen bileşenler fasoncuya gönderilmez;
  **Neden / uyarılar** sütunu bunu belirtir.
- **İş emrinin ürün ağacı**: üretim siparişlerinden gelen ürünlerde değiştirilmez; kayıtta fasoncu siparişine
  aktarılan işçilik fiyatını (*İşçilik maliyeti* sütunu) değiştirirsiniz. *İşçilik maliyetini dağıt* seçeneğiyle
  başlıktaki *Toplam işçilik* miktarla orantılı olarak ürünlere bölünür.
- *Ürünün mal girişini kapat* seçeneği üretim siparişlerinden gelen iş emirleri için geçerli değildir: işçiliğin mal
  girişi faturalanmak üzere açık kalır.
- **Tedarikçi teklifleri**: *Üretim siparişlerinden tedarikçi teklifleri* seçeneğiyle *Tedarikçi teklifi* satıra,
  kendi tedarikçisi, fiyatı ve teslimat tarihiyle bir teklif satırı bağlar; seçilmeyen teklif satırları kapatılır.

### Bir üretim siparişi neden listede görünmez

Liste, fason iş emri olmaya hazır işçilikleri gösterir. **Hazır olmayan satırları da göster** seçeneğini açın:
diğerleri de, nedeni ve yapılacak şeyle birlikte **Neden / uyarılar** sütununda görünür. Hazır olmayan satırlar
seçilemez; seçim kutularına tıklarsanız neden durum çubuğunda da görünür.

| Neden (ekrandaki örnek) | Ne yapılmalı |
|---|---|
| Zaten 1001 numaralı fason iş emrinde. | hiçbir şey: iş emrini *İş emri* sütunundan açın |
| LAV-SALD bir kaynaktır: dış işçilik, "Conto lavoro" = Evet olan stok dışı bir kalem olarak oluşturulmalı ve bileşenler bu koda bağlanmalıdır. | işçilik kalemini oluşturun ve kodunu bileşenlerde **Lavorazione terzista** (Fasoncu işçiliği) alanına yazın |
| Bileşenler LAV-SALD işçiliğini gösteriyor, ancak bu bir kalem değil. | bileşenlerde **Lavorazione terzista** alanını düzeltin veya kalemi oluşturun |
| LAV-SALD kaleminin ana verisinde "Conto lavoro" = Evet değil. | kalem ana verilerinde **Conto lavoro** (Fason üretim) = Evet olarak ayarlayın |
| Üretim siparişinde LAV-SALD işçiliği için satır yok: üretim siparişine (veya ürünün ürün ağacına) ekleyin. | satırı üretim siparişine veya sonraki üretim siparişleri için ürün ağacına ekleyin |
| Gönderilecek bileşen yok: bileşen satırlarında "Lavorazione terzista" = LAV-SALD ve manuel çekme yöntemini girin. | gönderilecek bileşenleri Manuel çekme yöntemiyle doldurun |
| Üretim siparişi serbest bırakılmadı: SAP içinde serbest bırakın. | üretim siparişini serbest bırakın |

SAP kaynağı olarak tanımlanmış bir işçilik sık görülen bir nedendir: dış işçilik, **Conto lavoro** (Fason üretim) =
Evet olan stok dışı bir kalem olarak oluşturulmalıdır.

Hazır satırlarda aynı sütun, seçimi engellemeyen uyarıları verir:

| Uyarı | Ne yapılmalı |
|---|---|
| Bu işçilikle geriye dönük çekilen bileşenler: fasoncuya gönderilmez (manuel çekme yöntemi gerekir). | gönderilmeleri gerekiyorsa Manuel çekme yöntemini ayarlayın |
| Tedarikçiyi girin. | *Tedarikçi* sütununda tedarikçiyi seçin |
| Tedarikçi F-TER01 için bağlı fasoncu deposu yok. | fasoncunun deposunu tedarikçiye bağlayın (**Fornitore terzista** (Fasoncu tedarikçi) alanı): bu olmadan iş emri oluşturulmaz |

## 7. Partiler, seri numaraları ve depo yerleri

Nakiller, geri almalar, fireler ve ürün girişindeki bileşen çıkışı için partiler ve seri numaraları, belgeler
oluşturulmadan **önce** eklentinin bir penceresinde seçilir. Ardından tüm belgeler tek bir işlemde oluşturulur.

- **Otomatik öneri**: fasoncunun deposundan (bileşen çıkışı, geri alma, fire) önce **o iş emrine gönderilmiş**
  partiler (SAP'nin parti hareket günlüğünden alınan "İş emrine ait" sütunu), sonra son kullanma tarihine göre
  (FEFO); şirketin deposundan son kullanma tarihine göre (FEFO).
- **Elle seçim**: "Kullanılacak" sütunu değiştirilebilir; miktar, partinin stokuyla (aynı partideki diğer satırlar
  düşülerek) ve seri numaraları için 1 ile sınırlıdır. *Öner* öneriyi yeniden yapar, *Sıfırla* her şeyi boşaltır.
  Onay yalnızca her satırda tam olarak talep edilen miktar olduğunda mümkündür.
- Yalnızca **serbest bırakılmış** partiler ve seri numaraları önerilir (engellenmiş veya erişilemez olmayanlar).
- Stok nakli talepleri parti hareketi yapmaz: bunlar için seçim penceresi açılmaz.

### Giren ürünün partisi

Girilen ürünün partisi, yapılandırılabilir bir **SQL komutuyla** (Yapılandırma › Partiler) üç sabit parametreyle
hesaplanır: `{ItemCode}` kalem, `{WhsCode}` giriş deposu, `{DocEntry}` fason iş emri. Varsayılan komut iş emri
numarası + sıra numarası döndürür (örn. `20160256-1`); *Doğrula* komutu test verileriyle çalıştırır. Oluşturulan parti
ürün girişinin sonundaki mesajda görünür.

![Giren ürünün parti komutu](../../_img/contolavoro/19_config_lotti.png)

*Giren ürünün parti komutu*

### Taslak belgeler

Belge; **depo yerleri** olan depolarda, **seri numaralı** giren ürünlerde, parti komutu boş olduğunda veya sonuç
vermediğinde ve toplu nakilde, SAP formunda tamamlanmak üzere taslak olarak oluşturulur. Belgeyi tamamlayıp *Ekle*
düğmesine basarsınız: eklenti taslağı siler ve devam eder.

## 8. Geri almalar ve fireler

- **Geri alma ve fire › Bileşenleri fasoncudan geri al**: *Geri alınacak* sütununa miktar (*Öner* = iş emrinin
  fasoncudaki stoku), ardından *Tamam*: fasoncunun deposundan şirketin deposuna nakil.
- **Geri alma ve fire › Fireyi naklet**: *Fire verilecek* sütununa miktar; fireleri fasoncudan seçilen bir depoya
  taşır.
- **Geri alma ve fire › Fasoncuda fire çıkışı**: *Fire çıkışı* penceresinde, firelerin doğrudan fasoncunun deposundan
  mal çıkışı.

Fire verilen bileşenler gönderilecek kalana geri döner.

## 9. Yardımcı işlevler

### Üretim siparişlerinden iş emirleri

Serbest bırakılmış üretim siparişlerinin iş emri olmaya hazır dış işçiliklerini listeler ve **tedarikçi ve iade
deposu başına bir iş emri** oluşturur. *Hazır olmayan satırları da göster* ile bir işçiliğin neden hazır olmadığını
açıklar. Ayarlar, tam örnek ve özel durumlar bölüm 6'dadır.

### Toplu bileşen nakli

Açık iş emirlerini analiz eder (tarih, tedarikçi, bileşen filtreleri) ve gönderilecek kalanı olan bileşenleri önerir;
şirket negatif stoku engelliyorsa iş emirleri arasında paylaşılan kullanılabilirliğe uyar. Tedarikçi başına bir nakil
oluşturur (parti veya depo yeri gerekiyorsa taslak olarak). Fasoncu deposu eksik olan veya çıkış deposuyla aynı olan
satırlar hariç tutulur ve bildirilir.

### İş emirleri arasında bileşen nakli

Fasoncuda bulunan stoku stok hareketi olmadan (yalnızca kayıt) bir iş emrinden diğerine taşır. Bu nedenle yalnızca
**aynı fasoncu deposuna** sahip **açık** iş emirleri arasında mümkündür: liste yalnızca bunları önerir; farklı
depolarda işlem engellenir ve mal geri alınıp yeniden gönderilmelidir. Stok, onay anında yeniden okunur.

### Ürün mal girişlerini toplu kapatma ve işçilik fiyatları

*Ürün mal girişlerini toplu kapatma* hâlâ açık olan ürün mal girişlerini listeler ve seçilenleri kapatır. *Fasoncu
işçilik fiyatları*, fasoncu ve ürüne göre işçilik fiyatlarının tablosudur.

Bir işçiliğin fiyatının arama sırası: tedarikçi sözleşmeleri (seçenek, yalnızca SQL Server), fasoncuya göre fiyatlar,
ürün ağacı (seçenek), SAP tedarikçi fiyatı, iş emrinin fiyat listesi.

## 10. Veriler, alanlar ve hareket türleri

| Tablo | İçerik |
|---|---|
| `@XEI_CL_OCNT` | iş emri başlığı (UDO `XEI_CL_COMMESSA`, serili) |
| `@XEI_CL_CNT1` | ürünler |
| `@XEI_CL_CNT2` | ürün ağacı (bileşenler ve işçilikler) |
| `@XEI_CL_PRZLAV` | fasoncu ve ürüne göre işçilik fiyatları |
| `@XEI_CL_TRCOMM` | iş emirleri arasında nakiller |

SAP tablolarındaki alanlar (`XEI_CL_` öneki):

| Alan | Tablolar | İçerik |
|---|---|---|
| `U_XEI_CL_ENTRY` | belge satırları | fason iş emri (DocEntry) |
| `U_XEI_CL_LINENUM` | belge satırları | ürün veya ürün ağacı satırı |
| `U_XEI_CL_TYPE` | belge satırları | hareket türü (aşağıdaki tablo) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | belge satırları | metin, referans kalem ve üretim siparişi, kullanılabilir teklifler |
| `U_XEI_CL_ICNT` | kalemler | fason üretim kalemi |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | depolar | deponun fasoncu tedarikçisi, varsayılan fasoncu deposu |
| `U_XEI_CL_DISTTERZ` | ürün ağaçları | fasoncu ürün ağacı (üretim siparişlerinden üretimden giriş) |
| `U_XEI_CL_ILAV` | ürün ağacı ve üretim siparişi satırları | bileşenin ait olduğu işçilik |

Şirket bunları kullanıyorsa eklenti belgelerin ticari kodunu, sevk nedenini, navlun koşulunu ve taşıyıcısını da
doldurur.

| Tür | Belge | Anlamı |
|---|---|---|
| EMP | satınalma siparişi, mal girişi | ürün |
| OAL | satınalma siparişi, mal girişi | işçilik |
| UMC | mal çıkışı (üretim siparişinden geliyorsa üretim için çıkış) | tüketilen bileşenler |
| TSO | stok nakli veya talep | fasoncuya gönderilen bileşenler |
| TSI | stok nakli | bileşen geri alma |
| TSS | stok nakli | fire nakli |
| UMR | mal çıkışı | fasoncudaki fireler |
| EPR | üretimden giriş | üretim siparişinin mamulü (bölüm 6) |

Hesaplamalarda iptal edilmiş belgeler hariç tutulur ve iadeler satır satır düşülür.

## 11. Diller

Eklenti SAP istemcisinin dilini izler. **İtalyanca** (temel dil), **İngilizce**, **Almanca**, **Fransızca**,
**İspanyolca** ve **Türkçe** kullanılabilir: menüler, formlar, sütunlar, düğmeler, mesajlar ve oluşturulan
belgelerin açıklamaları. Öngörülmeyen bir dilde İtalyanca kullanılır.

| SAP dili | Eklentinin metinleri | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | İtalyanca | Commessa terzista | terzista |
| English (United States / United Kingdom) | İngilizce | Subcontracting Job | subcontractor |
| German | Almanca | Lohnfertigungsauftrag | Lohnfertiger |
| French | Fransızca | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | İspanyolca | Orden de subcontratación | subcontratista |
| Turkish | Türkçe | Fason iş emri | fasoncu |

Terimler aynı dildeki SAP Business One terimlerini izler (örneğin İngilizcede *Vendor*, *Posting Date*, *Inventory
Transfer*, *Bill of Materials*, *Batch*; Türkçede *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün ağacı*, *Parti*).

### Dili değiştirme

1. **Administration › Setup › General › Users** (Yönetim › Ayarlar › Genel › Kullanıcılar), *Display* (Görüntüleme)
   sekmesi, *Language* (Dil) alanı, ardından *Update* (Güncelle).
2. SAP tüm açık pencerelerin kapatılacağını bildirir: *Evet* yanıtını verin.
3. Eklenti metinleri kendiliğinden yeniden yükler ve menüleri yeni dilde yeniden oluşturur: yeniden başlatmak
   gerekmez.

### Metinleri özelleştirme

Her metin, eklentinin **Traduzioni** (Çeviriler) menüsünden veya formlarda sağ tıklayarak (*Modifica testo…* (Metni
düzenle…), *Testi di questa form…* (Bu formun metinleri…)) tek bir müşteri için değiştirilebilir. `XEI_TEXTS` yetkisi
gerekir (süper kullanıcılarda her zaman vardır). Özelleştirmeler eklenti güncellemelerinde korunur.

SAP'nin veritabanına kaydettiği metinler İtalyanca kalır, örneğin kullanıcı alanlarının tanımları ve *Prezzi
lavorazioni terzisti* (Fasoncu işçilik fiyatları) tablosunun başlığı. Çerçevenin *Informazioni*, *Traduzioni* ve
*Licenza* girişleri pencereleriyle birlikte tüm dillerde İtalyancadır.
