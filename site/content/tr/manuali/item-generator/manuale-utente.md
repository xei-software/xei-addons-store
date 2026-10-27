---
title: XEI.ItemGenerator – Kullanım kılavuzu
description: XEI.ItemGenerator ile tabanların, değerlerin ve varyantların nasıl yapılandırılacağı ve kalemlerin nasıl oluşturulacağı.
lang: tr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Kullanım kılavuzu

Programın arayüzü İngilizce görünür: menü, pencere ve alan adları ekranda göründükleri şekliyle İngilizce verilmiş, yanlarına Türkçe karşılıkları eklenmiştir.

Kurulum, lisans, menüler ve yetkiler
[kurulum kılavuzunda](installazione.md) anlatılmaktadır.

## 1. Eklenti ne yapar

XEI.ItemGenerator, kodları düzey düzey değerler seçilerek **oluşturulan** kalemleri kalem ana
verilerinde oluşturur: ürün tipi, ölçü, malzeme... Seçim ağacı bir kez tanımlanır; ardından kodları
ve tanımları elle uydurmak yerine bunlar bir pencerede derlenir: eklenti kodu, tanımı, fiyatı,
ağırlığı, ölçüleri, grubu, özellikleri ve ürün ağacını hesaplar ve kalemleri bir şablon kalemi
kopyalayarak oluşturur.

- **Tutarlı kodlar**: kod "anlamlıdır" (ör. `PE090` = 90'lık üst dolap) ve varyantları (renk,
  kulp...) ayırt eden bir sıra numarası içerir.
- **Mükerrer kayıt yok**: aynı bileşim her zaman aynı kalemi oluşturur; kalem zaten varsa eklenti
  onu bulur.
- **Tek seferde çok sayıda kalem**: birden fazla ölçü ve seçenek tüm kombinasyonları verir.
- **Eksiksiz kalemler**: tanımlar (yabancı dilde de), kalem ana verileri, fiyat listesindeki fiyat
  ve ürün ağacı yapılandırmadan gelir.
- **Belgeden**: satış tekliflerinde ve satış siparişlerinde satırın kalemi belgeden çıkmadan
  yapılandırılır.

### Öne çıkanlar

- SAP'nin üzerinde, boyutu değiştirilebilen bir pencerede oluşturma: onay kutulu kod ağacı ve varyant
  ağacı (farklı dallarda da), arama, durum, fiyat ve sonuç bilgisiyle kalem listesi; SAP kullanılmaya
  devam edilebilir. SAP istemcisinin görünümü, aynı tarzda mesajlar, sağ tıklama ile
  değiştirilebilen metinler.
- Değerlerden ve seçeneklerden derlenen fiyat, ağırlık, ölçüler, gruplar, özellikler, yabancı ad ve
  ürün ağacı.
- Kodlar, seçenekler ve isteğe bağlı bölümler içeren tanım formülü.
- Satış tekliflerinden ve satış siparişlerinden kalemi yapılandırma; oluşturulmuş bir kalemden benzer
  kalemler oluşturma.
- Düzeltilecek ana veriyi açan yapılandırma kontrolü; Excel ile içe/dışa aktarma; çoğaltma.
- İşleve göre SAP yetkileri; beş dilde metinler.

## 2. Kavramlar: tabanlar, değerler, varyantlar ve yapılar

Bir kalemin kodu **nötr kod** + **sonek**ten oluşur:

- **nötr kod** anlamlı bölümdür: düzey düzey seçilen **değerlerin** kodlarının birleşimidir. Her düzey
  sabit bir uzunluğa ve kendi değerlerine sahip bir **tabandır** (ör. *Tipo mobile* (Mobilya tipi),
  *Larghezza* (Genişlik)); her değer bir sonraki **alt düzeye** götürür ya da son değerdir;
- **sonek**, aynı nötr koda ve farklı **varyantlara** sahip kalemleri ayırt eden N basamaklı bir sıra
  numarasıdır (yapılandırma); 0 basamakla kod, nötr kodun kendisidir;
- bir **varyantın** (ör. *Colore* (Renk)) **seçenekleri** vardır (ör. beyaz, meşe). Bir değer için
  sorulacak varyantlar, değere bağlı bir **varyant yapısında** toplanır.

Kılavuzun tamamında, *Excel Import / Export* (Excel İçe / Dışa Aktarma) ile içe aktarılacak
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx) dosyasında bulunan bu örnek
kullanılmaktadır:

```
Tipo mobile cucina (CU, 2 caratteri)          struttura CUSC: Colore
├── BA Mobile base     → Larghezza
└── PE Mobile pensile  → Larghezza
Larghezza (CL, 3 caratteri)                   struttura CUSM: Colore anta + Maniglia, eredita varianti
├── 060 Larghezza 60 cm
└── 090 Larghezza 90 cm
Colore (CUCOL)     BI Bianco · RO Rovere
Maniglia (CUMAN)   AL Maniglia alluminio · NE Maniglia nera
```

Alüminyum kulplu 90'lık üst dolabın nötr kodu `PE090`'dır; beyaz ve meşe birlikte, 3 basamaklı bir
sonekle oluşturulduğunda beyaz (BI, RO'dan önce gelir) `PE090001`, meşe ise `PE090002` olur.

**Bileşim** (her düzeyin değerleri + seçilen seçenekler) kalemi tanımlar: aynı bileşim yeniden
oluşturulduğunda eklenti yeni bir kalem oluşturmak yerine mevcut kalemi bulur.

## 3. Yapılandırma

![Yapılandırma](../../_img/itemgenerator/02_configurazione.png)

*Yapılandırma penceresi.*

| Seçenek | Etkisi | Varsayılan |
|---|---|---|
| Suffix digits (Sonek basamakları) | nötr koddan sonraki sıra numarası (0-10); 0 = kod nötr koda eşit (nötr kod başına tek kalem) | 0 |
| Description formula (Tanım formülü) | tanımın nasıl oluşturulacağı (bölüm 8); boş = düzeylerin tanımları sırayla | boş |
| Descriptions in upper case (Büyük harfle tanımlar) | tanım, genişletilmiş tanım ve yabancı ad büyük harfle | Hayır |
| Price list (Fiyat listesi) | kalemin fiyatının (değerlerin ve seçeneklerin fiyatlarının toplamı) yerel para biriminde yazılacağı fiyat listesi | yok |
| Length unit (Uzunluk birimi) | değerlerin ve kalemlerin ölçülerinin (uzunluk, genişlik, yükseklik) birimi; boş = ölçüler aktarılmaz | yok |
| Weight unit (Ağırlık birimi) | değerlerin ve seçeneklerin ağırlık birimi; boş = ağırlık aktarılmaz | yok |
| Bill of Materials (Ürün ağacı) | bileşenlerle oluşturulan ürün ağacının tipi: None (Yok), Production (Üretim), Sales (Satış), Assembly (Montaj), Template (Şablon) | Production |
| Menu after creation (Oluşturma sonrası menü) | oluşturulan her kalem için çalıştırılacak menü (diğer eklentilerle entegrasyon, bölüm 14) | boş |
| Picture thumbnail in Item Master Data (Kalem ana verilerinde resim küçük resmi) | kalem ana verilerinin başlığında kalemin resmi (bölüm 14) | Hayır |
| Add to list clears the list of items to generate first (last selection only) (Listeye ekle önce listeyi boşaltır) | oluşturmada *Add to list* (Listeye ekle) listeyi son seçimle değiştirir; bu seçenek olmadan kalemler birikir ve *Clear list* (Listeyi boşalt) ile kaldırılır (bölüm 9) | Evet |
| Window theme (Pencere teması) | eklenti pencerelerinin (oluşturma) renkleri, SAP istemcisinin iki teması gibi: **SAP SQL** (koyu başlık, altın sarısı düğmeler) veya **SAP HANA** (mavi başlık, açık mavi düğmeler). Şirketin tüm XEI eklentileri için geçerlidir; açık pencereler hemen değişir | veritabanına göre |

Seçenekler tüm şirket için geçerlidir; oluşturma penceresi zaten açıksa bunları yeniden açıldığında
kullanır.

## 4. Varyantlar ve varyant yapıları

### Varyantların ve seçeneklerin tanımı

Bir varyantın bir kodu, bir tanımı ve **seçenekleri** (*Options* (Seçenekler) sekmesi) vardır.
Başlıkta, tabanlarda olduğu gibi, bir **User table** (Kullanıcı tablosu) ve bir **Item user field**
(Kalem kullanıcı alanı) belirtilebilir: kalem oluşturulurken seçilen seçenek tabloya eklenir (yoksa)
ve kodu kalemin kullanıcı alanına yazılır (bölüm 6).

![Seçenekleriyle Colore varyantı](../../_img/itemgenerator/03_varianti.png)

*Seçenekleriyle Colore (Renk) varyantı.*

| Sütun | Kullanım |
|---|---|
| Option, Description (Seçenek, Tanım) | seçeneğin kodu ve tanımı; tanım, kalemin tanımındaki seçenek metnidir |
| Foreign desc. (Yabancı tanım) | yabancı addaki seçenek metni (boş = İtalyanca metin) |
| Alias (Takma ad) | serbest metin |
| Price (Fiyat) | kalemin fiyatına katkı |
| Weight (Ağırlık) | kalemin ağırlığına katkı |
| Properties (Özellikler) | etkinleştirilecek kalem özellikleri: virgülle ayrılmış 1 ile 64 arası sayılar (ör. `2, 12`) |
| Active (Etkin) | devre dışı bırakılan seçenekler oluşturmada görünmez |

*Components* (Bileşenler) sekmesinde seçeneklerin getirdiği ürün ağacı bileşenleri belirtilir
(bölüm 7).

![Seçeneklerin bileşenleri](../../_img/itemgenerator/04_varianti_componenti.png)

*Kulp seçeneklerinin bileşenleri: 01 deposundan iki kulp.*

### Varyant yapıları

Bir yapı, bir taban değeri için sorulacak varyantları **Position** (Konum) (oluşturmadaki sıra; hepsi
farklı) ve **Desc. position** (Tanım konumu) (seçilen seçeneğin tanımın sonundaki sırası; 0 = sona
eklenmez) ile birlikte toplar. Satırın tanımı, belirtilmişse varyantın tanımının yerine geçer (ör.
"Colore anta" (Kapak rengi)).

![Varyant yapısı](../../_img/itemgenerator/05_strutture.png)

*CUSM yapısı: kapak rengi ve kulp.*

Bir yapı tarafından kullanılan bir varyant ve bir taban tarafından kullanılan bir yapı silinemez.

## 5. Tabanlar ve değerler

Tabanın başlığı: kod, tanım, **Code length** (Kod uzunluğu) (tüm değerler bu uzunluktadır),
Classification (Sınıflandırma), User table (Kullanıcı tablosu) ve Item user field (Kalem kullanıcı
alanı). *Values* (Değerler) sekmesinde her değer için bir satır bulunur:

![Değerleriyle taban](../../_img/itemgenerator/06_basi_valori.png)

*Değerleriyle CU tabanı: tanımlar, alt düzey, varyant yapısı.*

![Değerlerin sütunları](../../_img/itemgenerator/06b_basi_valori.png)

*Sonraki sütunlar: kalem için veriler (grup, özellikler, fiyat, ölçüler, ağırlık).*

Sütun sayısı fazladır: **pencere ekranı kaplayacak şekilde büyütüldüğünde** tablo genişler ve tüm
sütunlar görünür.

| Sütun | Kullanım |
|---|---|
| Code, Description (Kod, Tanım) | değerin kodu (tam olarak tabanda belirtilen uzunlukta) ve tanımı |
| Item desc. (Kalem tanımı) | kalemin tanımındaki değer metni |
| Foreign desc. (Yabancı tanım) | kalemin yabancı adındaki değer metni (boş = İtalyanca metin) |
| Sub-level (Alt düzey) | bir sonraki düzeyin tabanı (seçim listesi; ok tabanı açar); boş = son düzey |
| Variant structure (Varyant yapısı) | değer için sorulacak varyantlar (ok yapıyı açar) |
| Inherit variants (Varyantları devral) | önceki bir düzeyde zaten bulunan varyantlar orada seçilen seçeneklerle, **öneri olarak** başlar: değer üzerinde değiştirilebilirler (önerilenlere dönmek için oluşturmada sağ tıklama). Öneriyi izledikleri sürece seçenek yalnızca bir kez sayılır |
| Force inheritance (Devralmayı zorla) | Inherit variants ile birlikte: önceki düzeyin seçimi geçerlidir ve değer üzerinde değiştirilemez (varyant kendi düzeyinde görünmez) |
| Active (Etkin) | devre dışı bırakılan değerler oluşturmada görünmez |
| Inventory UoM / Purchasing UoM / Sales UoM (Stok / Satın alma / Satış ölçü birimi) | kalemin metin olarak ölçü birimleri |
| Item group, UoM group (Kalem grubu, Ölçü birimi grubu) | kalemin kalem grubu ve ölçü birimi grubu |
| Properties (Özellikler) | etkinleştirilecek kalem özellikleri (1-64) |
| Price, Weight (Fiyat, Ağırlık) | kalemin fiyatına ve ağırlığına katkılar |
| Length, Width, Height (Uzunluk, Genişlik, Yükseklik) | kalemin ölçüleri |

Bu verilerin kalem için nasıl kullanıldığı bölüm 6'da açıklanmaktadır. *Components* (Bileşenler)
sekmesinde değerlerin getirdiği ürün ağacı bileşenleri belirtilir:

![Değerlerin bileşenleri](../../_img/itemgenerator/07_basi_componenti.png)

*Üst dolap iki dirsek getirir.*

- **User table** (Kullanıcı tablosu) (nesnesi olmayan bir kullanıcı tablosu, örneğin bir renk
  tablosu): kalem oluşturulurken seçilen değer, yoksa tabloya eklenir (kod ve tanım).
- **Item user field** (Kalem kullanıcı alanı) (örneğin kalem ana verilerinde bir *Renk* alanı):
  oluşturma sırasında seçilen değerin kodu bu alana yazılır.
- **Birinci düzey** tabanlar, hiçbir değerin alt düzeyi olmayan tabanlardır.

Kaydederken eklenti uzunlukları, tekrarlanan kodları, alt düzeyin tabanın kendisinden farklı olmasını,
özellikleri ve bileşenleri kontrol eder; bir hatanın nedeni durum çubuğunda görünür ve kaydetme
yapılmaz. Oluşturulmuş kalemlerde kullanılan veya başka bir tabanın alt düzeyi olan bir taban
silinemez.

> **Duplicate** (Çoğalt) (tabanlarda, varyantlarda ve yapılarda): açık bir kayıtla, aynı verilere ve
> tüm satırlara sahip yeni bir kayıt hazırlar; yeni kodu yazıp *Add* (Ekle) düğmesine basarsınız.
> Benzer tabanlar için kullanışlıdır (ör. başka bir ölçü yelpazesi).

## 6. Oluşturulan kalemin verileri

Kalemin her verisi, bileşimin değerlerinden ve seçilen seçeneklerden iki kurala göre gelir:

- **veriyi belirten son düzey geçerlidir**: sonraki bir düzey önceki düzeylerin verisini yeniden
  tanımlar; boş veya sıfır bir veri önceki düzeyin verisini silmez;
- **toplanır**: tüm değerler ve seçilen seçenekler katkıda bulunur. Devralınan bir seçenek, onu
  devralan düzey onu izlediği sürece yalnızca bir kez, seçildiği düzeyde sayılır; o düzeydeki kendi
  seçimi orada da sayılır (aynı seçenek olsa bile).

| Kalemin verisi | Kaynak | Kural |
|---|---|---|
| Kod | değerlerin kodları | nötr kod + sonek (en fazla 50 karakter) |
| Tanım, genişletilmiş tanım | değerlerin kalem tanımı, seçeneklerin tanımları | formül (bölüm 8); tanım 200 karakterde kesilir, genişletilmiş tanım *Extended description* (Genişletilmiş tanım) alanında eksiksizdir |
| Yabancı ad | değerlerin ve seçeneklerin yabancı tanımı | aynı formül; hiçbirinde yabancı tanım yoksa boş |
| Notlar | bileşim | değerler ve seçilen seçeneklerle ağaç |
| Kalem grubu | değerler | son düzey; yoksa şablonunki |
| Ölçü birimi grubu | değerler | son düzey; bir grup varsa metin olarak ölçü birimleri kullanılmaz |
| Stok / satın alma / satış ölçü birimi | değerler | son düzey, her biri ayrı ayrı |
| Özellikler | değerler ve seçenekler | toplanır: hepsi etkinleştirilir |
| Uzunluk, genişlik, yükseklik | değerler | son düzey, her biri ayrı ayrı; satın almada ve satışta |
| Ağırlık | değerler ve seçenekler | toplanır; satın almada ve satışta |
| Fiyat | değerlerin ve seçeneklerin fiyatı | toplanır; yapılandırmadaki fiyat listesinde |
| Ürün ağacı | değerlerin ve seçeneklerin bileşenleri | toplanır (bölüm 7) |

Örnek: alüminyum kulplu, meşe 90'lık üst dolap (renk 1. düzeyde seçilir ve 090 tarafından
devralınır).

| Düzey | Seçim | Fiyat | Ağırlık | Ölçüler | Grup | Özellikler |
|---|---|---|---|---|---|---|
| 1 Tip | PE Pensile | 100 | 10 | genişlik 350, yükseklik 720 | 101 | 1, 3 |
| 1 Renk | RO Rovere | 30 | 1,5 | | | 2 |
| 2 Genişlik | 090 L90 | 40 | 3 | uzunluk 900 | | 5 |
| 2 Kulp | AL Alluminio | 5 | 0,2 | | | |
| **Kalem PE090002** | | **175** | **14,7** | **900 × 350 × 720** | **101** | **1, 2, 3, 5** |

Geri kalan her şey (hesaplar, planlama verileri, tedarikçi, depolar...) oluşturmada seçilen **şablon
kalemden** gelir: yeni kalemler onun verilerini stoklar, fiyatlar, barkodlar, ürün ağacı, son fiyatlar
ve yabancı ad olmadan kopyalar.

![Oluşturulan kalem](../../_img/itemgenerator/12_articolo.png)

*Oluşturulan kalem: tanım, yabancı ad, grup, fiyat listesindeki fiyat.*

![Özellikler](../../_img/itemgenerator/13_articolo_proprieta.png)

*Değerler ve seçenekler tarafından etkinleştirilen özellikler.*

![Ölçüler ve ağırlık](../../_img/itemgenerator/14_articolo_misure.png)

*Satış verilerinde ölçüler ve ağırlık.*

## 7. Ürün ağacı

Her taban değeri ve her varyant seçeneği **bileşenlere** sahip olabilir (iki ana verinin
*Components* (Bileşenler) sekmesi): bileşen kalem, oluşturulan kalemin **bir birimi için miktar** ve
isteğe bağlı olarak çekişin yapılacağı **depo** (boş = bileşenin varsayılan deposu). Oluşturma
sırasında eklenti, kalemin ürün ağacını tüm bileşimin bileşenleriyle oluşturur:

1. her düzey için, birinciden sonuncuya, seçilen değerin bileşenleri ve ardından seçilen seçeneklerin
   bileşenleri;
2. **devralınan** seçenekler bileşenlerini yeniden getirmez;
3. **aynı depoya sahip aynı kalem**, miktarları toplanmış tek bir satır olur;
4. ürün ağacının miktarı 1'dir ve **tipi** yapılandırmadaki tiptir (üretim, satış, montaj, şablon);
   *None* (Yok) ile veya bileşimde bileşen yoksa ürün ağacı oluşturulmaz;
5. kalem ve ürün ağacı birlikte kaydedilir: ürün ağacı oluşturulamazsa kalem de kalmaz ve neden,
   oluşturma penceresinin *Result* (Sonuç) sütunundadır.

> SAP her ürün ağacı tipini yalnızca uygun kalemlerde kabul eder (örneğin üretim ürün ağacını bir
> stok kaleminde, satış ve montaj ürün ağaçlarını stok kalemi olmayan bir satış kaleminde): şablon
> kalem, yapılandırmada seçilen tip için doğru özelliklere sahip olmalıdır.

Örnekte üst dolap 2 dirsek, meşe seçeneği 1 kapak, alüminyum kulp ise 01 deposundan 2 kulp getirir.
Alüminyum kulplu, meşe 90'lık üst dolabın ürün ağacı şöyledir:

![Ürün ağacı](../../_img/itemgenerator/15_distinta.png)

*Kalemle birlikte oluşturulan ürün ağacı.*

Oluşturma penceresinde listenin *Components* (Bileşenler) sütunu ürün ağacının kaç satırı olacağını
gösterir; oluşturmadan sonra sonuç "With bill of materials (n components)." (Ürün ağacıyla (n
bileşen)) der. Yapılandırma kontrolü var olmayan, miktarı sıfır olan veya var olmayan depolara sahip
bileşenleri bildirir.

## 8. Tanım formülü

Formül (yapılandırma) tanımın, genişletilmiş tanımın ve yabancı adın nasıl oluşturulacağını belirler.

| Yer tutucu | Dönüştüğü değer |
|---|---|
| `{1}`, `{2}`... | 1., 2.... düzeyde seçilen değerin *Item desc.* (Kalem tanımı) metni |
| `{C:1}`, `{N:1}` | 1. düzeyde seçilen değerin kodu ve tanımı |
| `{V:CUCOL}` | `CUCOL` varyantı için seçilen seçeneğin tanımı |
| `{VC:CUCOL}` | `CUCOL` varyantı için seçilen seçeneğin kodu |
| `{NEUTRO}` | nötr kod |
| `[ ... ]` | isteğe bağlı bölüm: yalnızca içerdiği tüm yer tutucuların bir değeri varsa görünür |

- **Boş formül**: düzeylerin kalem tanımları sırayla.
- **Sona**, formül varyantlarını `{V:...}` veya `{VC:...}` ile zaten anmıyorsa, tanım konumu sıfırdan
  büyük olan seçeneklerin tanımları bu sırayla eklenir.
- Değeri olmayan bir yer tutucu boş olur; `[ ]` içinde ise ayırıcılar dahil tüm bölümü kaldırır.
- Çift boşluklar kaldırılır; *Descriptions in upper case* (Büyük harfle tanımlar) ile her şey büyük
  harftir; yer tutucularda büyük/küçük harf fark etmez.
- **Yabancı ad**: yabancı tanımlarla aynı formül (eksik olduğu yerlerde İtalyanca tanımlar); hiçbir
  değerde ve hiçbir seçenekte yabancı tanım yoksa boş.
- Tanınmayan bir yer tutucu, görünsün diye metinde kalır; yapılandırma kontrolü, kapatılmamış veya iç
  içe köşeli parantezler gibi bunu da bildirir.

Alüminyum kulplu, meşe 60'lık üst dolap ile örnekler:

| Formül | Tanım |
|---|---|
| *(boş)* | `Pensile L60 Rovere Maniglia alluminio` |
| `{1} {V:CUCOL} {2}` | `Pensile Rovere L60 Maniglia alluminio` |
| `{N:1} {C:2} - {NEUTRO}` | `Mobile pensile 060 - PE060 Rovere Maniglia alluminio` |
| `{1} {2}[ con {V:CUMAN}]` | `Pensile L60 con Maniglia alluminio Rovere`; kulpsuz: `Pensile L60 Rovere` |
| *(boş)*, büyük harf | `PENSILE L60 ROVERE MANIGLIA ALLUMINIO` |
| *(boş)*, yabancı ad | `Wall unit L60 Oak Maniglia alluminio` |

## 9. Kalemlerin oluşturulması

Oluşturma, **SAP'nin üzerinde ayrı bir penceredir**: her Windows penceresi gibi büyütülür, simge
durumuna küçültülür ve yeniden boyutlandırılır (bölmeler uyum sağlar; bölmeler arasındaki ayırıcılar
sürüklenir). Konum, boyutlar, ayırıcılar ve sütun genişlikleri kullanıcı başına hatırlanır; ilk seferde
tam ekran açılır. Pencere açıkken, kalemler oluşturulurken bile SAP kullanılmaya devam edilebilir.
Renkler yapılandırmadaki **Window theme** (Pencere teması) ayarını izler (bölüm 3): başlıkta kodun
biçimi, altında ise oluşturmanın nereden açıldığını (bir belgenin satırı, benzer kalem) veya neyin
yolunda gitmediğini belirten bir bölme bulunur.

Uzun işlemler (çok sayıda düzeyi açma, arama, tüm bir dalı işaretleme, çok sayıda kalem ekleme veya
oluşturma) pencerenin altında **ne yaptıklarını gösterir** (ilerleme mesajı, çubuk) ve *Stop*
(Durdur) ile durdurulur; bu sırada komutlar kilitlidir ve pencere etkin kalır. Sonuçlar altta bir
simgeyle (yeşil, turuncu, kırmızı) okunur. Beklenmeyen bir hata bir mesajda gösterilir ve pencere
kullanılabilir kalır.

![Varyantlarla oluşturma](../../_img/itemgenerator/09_genera_varianti.png)

*Alt dolabın ve üst dolabın 060 ve 090 genişlikleri işaretli (iki dalda), beyaz ve meşe renk,
alüminyum ve siyah kulp: derlenecek 16 kalem.*

1. **Template item** (Şablon kalem) (üstte, isteğe bağlı, oturumlar arasında hatırlanır): yeni
   kalemler onun verilerini kopyalar (bölüm 6). *...* düğmesi (veya F2) kalemi koda veya tanıma göre
   arar; kodun yanında tanım veya *Item not found in Item Master Data.* (Kalem, kalem ana verilerinde
   bulunamadı.) görünür. Şablon olmadan kalemler yalnızca yapılandırma verileriyle oluşturulur.
2. **Code tree** (Kod ağacı) (solda): birinci düzey tabanlar ve değerleri; **+** işareti bir değerin
   alt düzeyini açar. Varyantı olan değerler mavidir; fare bir değerin üzerine getirildiğinde kalem
   tanımı, varyantlar ve alt düzey görünür. **Son düzeyin değerleri işaretlenir** (onay kutusu olan
   tek değerler), birden fazla da olabilir ve **farklı dallarda da** olabilir: dalların yanında altta
   kaç değerin işaretli olduğu (*✓ 2*), ağacın altında ise bunların nötr kodları görünür.
   - **Find** (Bul): tam bir nötr kod (ör. `PE090`) doğrudan değerine götürür; aksi halde kodunda veya
     tanımında metni içeren bir sonraki değere götürür (sonraki için Enter, aramaya dönmek için
     Ctrl+F). Arama henüz açılmamış düzeyler için de geçerlidir.
   - **Expand all** (Tümünü genişlet), **Collapse** (Daralt), **Uncheck all** (Tüm işaretleri kaldır);
     **Neutral code** (Nötr kod) her değerin yanında nötr kodu gösterir.
   - Bir dalda sağ tıklama: *Check the last-level values below* (Alttaki son düzey değerlerini
     işaretle), *Uncheck below* (Alttaki işaretleri kaldır), *Expand below* (Altını genişlet). Son
     düzeydeki bir değere çift tıklama veya boşluk tuşu: işaretler veya işareti kaldırır.
3. **Variants and options** (Varyantlar ve seçenekler) (sağda): ağaçta **seçili değerin yapısı** (tıklama
   veya ok tuşları), yapıdaki sırasıyla varyantları, işaretlenecek seçenekler ve fiyata katkıları;
   başlık hangi değer olduğunu belirtir. Devralınan bir varyant bunu adının yanında belirtir:
   *proposed by level 1, Tipo: editable* (1. düzey, Tipo tarafından önerildi: değiştirilebilir)
   (yukarıda yapılan seçimi izler), *own choice, different from level 1* (kendi seçim, 1. düzeyden
   farklı) (sağ tıklama ile *Back to the proposed options* (Önerilen seçeneklere dön)), *same as level
   1: forced inheritance* (1. düzeyle aynı: zorunlu devralma) (bölüm 5). Aynı düzeydeki aynı varyant,
   işaretli tüm değerler için **yalnızca bir kez** seçilir. *All variants of the checked values, by
   level* (İşaretli değerlerin tüm varyantları, düzeye göre) onay kutusu ise işaretli değerlerin tüm
   varyantlarını düzeye göre gruplanmış olarak gösterir; bir varyant yalnızca bazı değerleri
   ilgilendiriyorsa *only for 060* (yalnızca 060 için) yazar. Aynı varyantın birden fazla seçeneği
   birden fazla kalem verir; işaretli seçeneği olmayan bir varyant bileşime girmez. Sağ tıklama:
   *Check all options* (Tüm seçenekleri işaretle) / *Uncheck all options* (Tüm seçeneklerin
   işaretini kaldır). Altta kaç kalemin derleneceği görünür.
4. **Add to list** (Listeye ekle): tüm kombinasyonları alttaki listede kod, tanım, fiyat, ürün ağacı
   bileşen sayısı ve durumla derler. Varsayılan olarak (*Add to list clears the list of items to
   generate first* (Listeye ekle önce listeyi boşaltır) seçeneği, bölüm 3) liste boşaltılır ve yalnızca
   son seçimi içerir; seçenek devre dışıyken kalemler birikir ve listede zaten bulunanlar tekrarlanmaz.
   Değerlerin ve seçeneklerin işaretleri kalır (*Uncheck all* (Tüm işaretleri kaldır) ile kaldırılır):
   bir seçenek veya değer değiştirilip yeniden eklenir.
5. **Generate Items (n)** (Kalemleri Oluştur (n)): listenin işaretli kalemlerini (n düğmenin
   üzerindedir) teker teker, satır satır sonuç ve ilerleme çubuğuyla oluşturur. *Stop* (Durdur),
   oluşturmayı işlemdeki kalemden sonra durdurur. Sonunda, pencerenin altında özet bulunur: *Items
   created: n.* (Oluşturulan kalemler: n.), ardından yalnızca varsa, bu arada başka bir kullanıcının
   zaten oluşturduğu kalemler ve hatalı olanlar; liste oluşturulan ilk kaleme konumlanır.

![Derlenen kalemlerin listesi](../../_img/itemgenerator/08_genera.png)

*Derlenen 16 kalem (listenin sonu): 15'i kalem ana verilerinde zaten var (sarı) ve biri, PE060004,
fiyatı ve bileşen sayısıyla oluşturulacak.*

| Durum | Anlamı |
|---|---|
| To create (Oluşturulacak) | kod = nötr kod + ilk boş sonek (ne kalem ana verilerinde ne de listede bulunan) |
| Already exists (Zaten var) | aynı bileşim kalem ana verilerinde zaten var: kod mevcut kalemin kodudur (sarı) |
| Created (Oluşturuldu) | kalem oluşturuldu (yeşil); sonuç ürün ağacı olup olmadığını belirtir |
| Error (Hata) | neden *Result* (Sonuç) sütunundadır (kırmızı): kod zaten kullanılıyor, sonekler tükendi, kod çok uzun, SAP hatası. Düzeltip yeniden oluşturabilirsiniz |

![Oluşturmanın sonucu](../../_img/itemgenerator/11_genera_esito.png)

*Oluşturmanın sonucu: beyaz 60'lık ve 90'lık alt dolaplar oluşturuldu (yeşil) ve altta özet;
bileşenleri olmadığı için ürün ağaçları yok (bileşenlerle sonuç "With bill of materials" (Ürün
ağacıyla) der).*

Listede onay kutusu (yalnızca oluşturulacak veya hatalı kalemlerde) hangi kalemlerin oluşturulacağını
belirler. Oluşturulmuş veya zaten var olan bir kaleme **çift tıklama** (veya Enter) onu SAP'nin kalem
ana verilerinde açar (oluşturma penceresi simge durumuna küçülür ve görev çubuğundan yeniden açılır).
Henüz oluşturulmamış bir kalem hiçbir şey açmaz: pencerenin altında *Item ... is not in Item Master
Data yet.* (Kalem ... henüz kalem ana verilerinde değil.) okunur; kalem bu arada SAP'de silindiyse de
aynısı olur. Sağ tıklama: *Open in Item Master Data* (Kalem ana verilerinde aç), *Copy code* (Kodu
kopyala), *Remove from list* (Listeden kaldır), *Check all* (Tümünü işaretle), *Uncheck all* (Tüm
işaretleri kaldır); Del seçili satırları kaldırır, Ctrl+C kodlarını kopyalar. *Clear list* (Listeyi
boşalt) sıfırdan başlatır. Listede henüz oluşturulmamış kalemler varsa, kapatma veya boşaltma onay
ister.

### Pencerenin mesajları ve metinleri

Oluşturma penceresinin soruları ve mesajları (örneğin *Create 2 items in Item Master Data?* (Kalem
ana verilerinde 2 kalem oluşturulsun mu?)) pencereyle aynı görünüme sahiptir: Enter vurgulanan düğmeyi
seçer, Esc Hayır yanıtını verir. **Modifica testi add-on XEI** (XEI eklenti metinlerini değiştirme)
yetkisine sahip olan kullanıcı, pencerenin metinlerini SAP pencerelerinde olduğu gibi
değiştirebilir: bir etiket, bir düğme, bir bölme başlığı, bir sütun başlığı veya bir mesajın metni
üzerinde sağ tıklama, ardından **Modifica testo...** (Metni düzenle); **Testi di questa finestra...** (Bu
pencerenin metinleri) (ağaçların ve listenin menülerinin sonunda da bulunur) hepsini listeler.
Özelleştirilmiş metin, kullanılan dilde tüm kullanıcılar için geçerlidir ve hemen görünür.

![Oluşturmadan önceki soru](../../_img/itemgenerator/25_messaggio.png)

*Pencerenin tarzıyla, oluşturmadan önceki soru.*

![Modifica testo](../../_img/itemgenerator/26_modifica_testo.png)

*Find (Bul) düğmesine sağ tıklayarak Modifica testo (Metni düzenle): başlangıç metni ve özelleştirilmiş
metin.*

Her kalemi oluşturmadan önce eklenti, bu arada kimsenin aynı bileşimi oluşturmadığını veya kodu
kullanmadığını yeniden kontrol eder. Her kalem tek bir işlemde oluşturulur (kalem, ürün ağacı,
kullanıcı tabloları, bileşim): bir hata yarım kalmış veri bırakmaz.

## 10. Satış tekliflerinden ve satış siparişlerinden kalemler

**Satış tekliflerinde** ve **satış siparişlerinde** bir satırda sağ tıklama › **Configure Item...**
(Kalemi Yapılandır...):

![Satırdan kalemi yapılandırma](../../_img/itemgenerator/17_ordine_menu.png)

*Sipariş satırından Configure Item (Kalemi Yapılandır).*

Oluşturma penceresi o satır için açılır (bunu pencerenin başlığı ve üstteki bölme belirtir). Kalem
her zamanki gibi derlenir ve oluşturulur; ardından **Use in row** (Satırda kullan), listede seçili
kalemi (oluşturulmuş veya zaten var olan; listede yalnızca bir kalem varsa seçmek gerekmez) belgenin
satırına koyar, oluşturma penceresini kapatır ve belgeyi yeniden öne getirir. SAP satırı, kod elle
yazılmış gibi doldurur: tanım, müşterinin fiyat listesindeki fiyat, depo.

![Satırdan açılan oluşturma](../../_img/itemgenerator/18_genera_documento.png)

*Siparişin 2. satırından açılan oluşturma: yeni oluşturulan kalem seçili ve "Use in row" (Satırda
kullan).*

![Satırdaki kalem](../../_img/itemgenerator/19_ordine_riga.png)

*Sipariş satırındaki kalem.*

- Satırda yapılandırıcı tarafından oluşturulmuş bir kalem zaten varsa, oluşturma onun
  yapılandırmasından başlar: doğru varyantı elde etmek için bir seçeneği değiştirmek yeterlidir.
- Oluşturma penceresi zaten açıksa yeni satıra geçer; liste kalır, böylece daha önce derlenmiş bir
  kalem yeniden kullanılabilir.
- Belge açık kalmalıdır; kapalı veya değiştirilemeyen bir belge değişmez (neden pencerenin altında
  görünür).

## 11. Benzer kalemler

Yapılandırıcı tarafından oluşturulmuş bir kalemin ana verilerinde sağ tıklama › **Generate Similar
Items...** (Benzer Kalemler Oluştur...): oluşturma penceresi, kalemin yapılandırması önceden
ayarlanmış olarak (son değeri ağaçta işaretli, ona kadar açılmış, ve seçilen seçenekler) ve şablon
olarak kalemin kendisiyle açılır. Değerler ve seçenekler değiştirilir ve kalemler listeye eklenir.
Oluşturma penceresi zaten açıksa (simge durumunda bile) kalemin yapılandırmasıyla öne gelir; liste
kalır.

![Oluşturulmuş bir kalemde sağ tıklama](../../_img/itemgenerator/16_simili_menu.png)

*Oluşturulmuş bir kalemde sağ tıklama.*

![Benzer kalemlerin oluşturulması](../../_img/itemgenerator/20_simili.png)

*PE090002'nin yapılandırmasından oluşturma (SAP HANA teması): 90'lık üst dolap, meşe ve alüminyum kulp
zaten işaretli; şablon kalemin kendisi.*

Bu arada yapılandırma değiştiyse (kaldırılan veya devre dışı bırakılan değerler, farklı alt düzeyler)
oluşturma bir uyarıyla sıfırdan başlar; artık var olmayan seçenekler yok sayılır.

## 12. Yapılandırma kontrolü

Tüm yapılandırmayı (devre dışı bırakılan değerler ve seçenekler dahil) kontrol eder ve sorunları önce
hatalar, sonra uyarılar olarak gösterir. Bir satıra **çift tıklama** düzeltilecek ana veriyi kayıtta
açar; *Check again* (Yeniden kontrol et) düzeltmelerden sonra kontrolü tekrarlar. Pencere büyütüldüğünde
(tam ekran da olabilir) sorun listesi onu izler.

![Yapılandırma kontrolü](../../_img/itemgenerator/21_verifica.png)

*Kontrol: var olmayan bir varyant yapısı ve devralınacak varyantı olmadan devralan bir değer.*

| Tip | Kontrol |
|---|---|
| Hata | uzunluğu olmayan taban; tabandan farklı uzunlukta kod; tekrarlanan kod |
| Hata | var olmayan alt düzey, varyant yapısı, kalem grubu, ölçü birimi grubu; geçersiz özellikler |
| Hata | bir yapıda var olmayan varyant; tekrarlanan seçenek |
| Hata | kalemi olmayan, kalemi veya deposu var olmayan, miktarı sıfır olan, var olmayan bir değer veya seçenek için bileşen |
| Hata | kendisinin alt düzeyi olan taban (yol ile birlikte döngü); birinci düzey taban yok |
| Uyarı | etkin değeri olmayan taban; varyantı olmayan yapı; etkin seçeneği olmayan varyant |
| Uyarı | birinci düzeyden ulaşılamayan taban (yalnızca devre dışı değerlerin alt düzeyi) |
| Uyarı | sonek dahil 50 karakterden uzun kodlar veren yol |
| Uyarı | önceki düzeylerde aynı varyantlar olmadan varyantları devralan değer; Inherit variants (Varyantları devral) olmadan Force inheritance (Devralmayı zorla) |
| Uyarı | tanınmayan yer tutucular veya hatalı köşeli parantezler içeren formül |

## 13. Excel ile içe ve dışa aktarma

![Excel'den içe aktarma](../../_img/itemgenerator/22_excel.png)

*Örnek dosyanın başarılı içe aktarımı.*

**Export...** (Dışa aktar...) nereye kaydedileceğini sorar ve tüm yapılandırmayı bir .xlsx dosyasına,
ana veri başına bir sayfa olacak şekilde, kalın ve sabitlenmiş başlıkla yazar. **Import** (İçe aktar)
belirtilen dosyayı okur (*Browse...* (Gözat...)). Pencere büyütüldüğünde dosya adı ve sonuç listesi
genişler.

| Sayfa | Her satır | Sütunlar |
|---|---|---|
| Basi | değer (tabanın verileri tekrarlanır) | Base, Descrizione base, Lunghezza, Classificazione, Tabella utente, Campo utente, Codice, Descrizione, Desc. articolo, Desc. straniera, Sotto livello, Struttura varianti, Eredita varianti, Forza ereditarietà, Attivo, UM magazzino, UM acquisti, UM vendite, Valore, Dim. 1, Dim. 2, Dim. 3, Peso, Gruppo articoli, Gruppo UM, Proprietà, Note |
| Componenti basi | bileşen | Base, Valore, Componente, Descrizione, Quantità, Magazzino, Note |
| Varianti | seçenek | Variante, Descrizione variante, Tabella utente, Campo utente, Opzione, Descrizione, Desc. straniera, Alias, Valore, Peso, Proprietà, Note, Attivo |
| Componenti varianti | bileşen | Variante, Opzione, Componente, Descrizione, Quantità, Magazzino, Note |
| Strutture | varyant | Struttura, Descrizione struttura, Variante, Descrizione variante, Posizione, Pos. descrizione |

- Sütunlar **başlıklarından** tanınır: sıra önemli değildir ve bilinmeyen sütunlar yok sayılır. Dosya
  sayfaların yalnızca bir kısmını da içerebilir.
- İtalyan biçiminde (`1.234,5`) veya İngiliz biçiminde (`1234.5`) sayılar; evet/hayır için Y, S, Sì,
  X, 1, Vero.
- Başında sıfır olan kodlar (`060`) metin olarak yazılmalıdır (Excel'de kesme işaretiyle: `'060`),
  aksi halde Excel bunları sayıya dönüştürür.
- İçe aktarma **önce dosyanın tamamını kontrol eder**: bir hata varsa hiçbir şey yazmaz ve liste her
  hatanın sayfasını, satırını ve nedenini gösterir.
- Ardından her şeyi birlikte yazar: dosyadaki her taban, varyant veya yapı eklenir ya da güncellenir ve
  satırları mevcut satırların **yerine geçer**; bileşenler yalnızca bileşen sayfalarında bulunan
  tabanlar ve varyantlar için değişir; dosyada olmayanlar olduğu gibi kalır.

Tipik kullanımlar: dışa aktarmak, Excel'de değiştirmek (yeni değerler, güncel fiyatlar) ve yeniden içe
aktarmak; yapılandırmayı başka bir şirkete kopyalamak;
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx) gibi bir örnekten başlamak.

## 14. Kalem ana verileri, tutarlılık kontrolü, diğer eklentiler

### Resmin küçük resmi

*Picture thumbnail in Item Master Data* (Kalem ana verilerinde resim küçük resmi) seçeneğiyle kalem
ana verileri, kalemin resmini (Picture (Resim) alanı, SAP'nin resim klasöründe) başlığın boş
alanında, Inventory Item/Sales Item/Purchasing Item (Stok kalemi/Satış kalemi/Satın alma kalemi) onay
kutularının solunda gösterir. Çerçeve resmin oranlarını alır ve kalemin resmi yoksa gizlenir. Kalem
ana verileri yavaşlamaz.

![Kalem ana verilerinde küçük resim](../../_img/itemgenerator/24_miniatura.png)

*Kalem ana verilerinde küçük resim.*

### Tutarlılık kontrolü

Oluşturulan tüm kalemlerin bileşimini yeniden hesaplar. Yapılandırma verileri eklentinin dışında
değiştirildiyse kullanışlıdır; SAP'den silinen kalemlerin bileşimlerini de kaldırır.

### Diğer eklentilerle entegrasyon

Yapılandırmada bir *Menu after creation* (Oluşturma sonrası menü) ile eklenti, oluşturulan her kalem
için kodunu XEI tablosu `@XEI_IG_EVENTS`'e kaydettikten sonra o menüyü çalıştırır: o menüyü dinleyen
başka bir eklenti kalemi tamamlayabilir.
