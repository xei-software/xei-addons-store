---
title: XEI.CommissionManagement – Kullanım kılavuzu
description: "SAP Business One'da satış temsilcilerinin komisyonları: yapılandırma, kurallar, hesaplama, ödeme, düzeltmeler ve ekstreler."
lang: tr
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Kullanım kılavuzu

| | |
|---|---|
| SAP Business One | 10.0 veya üstü |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir deneme yapılması önerilir) |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |

## 1. Eklentinin işlevi

XEI.CommissionManagement, SAP Business One belgelerinden yola çıkarak **satış temsilcilerinin komisyonlarını**
hesaplar ve öder. Her fatura satırı (ve peşinat faturası veya alacak dekontu satırı) en fazla dört yüzde içerir:
biri belgenin **temsilcisi** için, birer tane de onun üstlerinin her biri için: **bölge sorumlusu**, **alan
sorumlusu** ve **müdür**. Eklenti:

- belgeler doldurulurken **yüzdeleri satırlara atar**; müşteri, müşteri grubu, kalem, kalem grubu, fiyat listesi,
  dönem ve iskontoya göre kurallar temelinde (veya temsilcinin varsayılan yüzdelerine göre);
- bir dönemin belgelerinin komisyonlarını **hesaplar** ve bunları **paylara** böler: bir kısmı faturada, kalanı
  tahsilatta tahakkuk eder (taksit taksit veya belgenin tamamı tahsil edildiğinde);
- SAP tahsilatları kaydettikçe payları **öder** ve tahsil edilemeyen taksitlerin paylarını **ters kaydeder**;
- her temsilci için hesaplanan tutarın, ödenecek kalanın ve dönemde hak ettiği tutarın (ödenen artı elle girilen
  **düzeltmeler**) **ekstresini** üretir; ekstre Excel için CSV olarak dışa aktarılabilir, PDF olarak
  yazdırılabilir ve her temsilciye e-postayla gönderilebilir;
- isteğe bağlı olarak (Yapılandırma'daki seçenekler): bir belge kaydedildiğinde komisyonu tahmin eder, faturaları
  kaydedilir kaydedilmez kendiliğinden hesaplar, elle düzeltilen yüzdeleri korur, kısmi tahsilatları öder, teslim
  edilmiş dönemleri kapatır, yıllık satış üzerinden **primleri** hesaplar, temsilcilerin **fatura taslaklarını**
  hazırlar ve sorunları bildirir (**Kontroller**).

Her şey SAP içindedir: satış çalışanlarında ve belge satırlarında kullanıcı alanları, kurallar, komisyonlar ve
düzeltmeler için kullanıcı tabloları; harici veritabanı yoktur. Microsoft SQL Server ve SAP HANA'da aynı şekilde çalışır; SAP HANA'da kurulum sırasında bir deneme yapılması önerilir.

## 2. Kavramlar: hak sahipleri, yüzdeler, paylar, ödeme

### Komisyonu kim alır (hak sahipleri)

Belgenin *Sales Employee* (satış çalışanı) alanındaki kişi temsilcidir. Temsilciler kartında ona bir **bölge
sorumlusu**, bir **alan sorumlusu** ve bir **müdür** atanabilir: bunlar onun belgelerinin diğer hak sahipleridir.
Her birinin her satırda kendi yüzdesi vardır (dört sütun: *Provv. % agente / capo zona / capo area / direttore*
(Komisyon % temsilci / bölge sorumlusu / alan sorumlusu / müdür)).

- Bir satış çalışanı yalnızca bir **rolü** varsa (Temsilci, Bölge sorumlusu, Alan sorumlusu, Müdür) komisyon alır.
  Rolü olmayan bir satış çalışanı "yönetilmiyor" durumundadır: belgeleri komisyon oluşturmaz ve birinin üstü olarak
  belirtilmişse onun payı hesaplanmaz.
- "Temsilci" rolü belgelerde satış çalışanı olarak görünenler içindir; "Bölge sorumlusu", "Alan sorumlusu" ve
  "Müdür" ise bir satış çalışanının üst olarak seçilebildiği unvanlardır. Üst rolü olan biri yine de kendi
  belgelerine sahip olabilir: o belgelerde temsilci odur.

### Yüzdeler

Bir satırın yüzdeleri **kurallardan** (bölüm 7) veya hiçbir kural uygulanmıyorsa belgenin temsilcisinin
**varsayılan yüzdelerinden** (bölüm 6) gelir. Belge doldurulurken kendiliğinden atanır (bölüm 8), elle
düzeltilebilir ve hesaplamadan önce toplu olarak kontrol edilip düzeltilebilir (bölüm 9).

### Paylar: faturada ve tahsilatta

Bir belgenin komisyonunun tamamı hemen hak edilmez. Eklenti her hak sahibi için komisyonu paylara böler:

- **faturada** tahakkuk eden pay (taksit 0), satış çalışanının "Faturada %" değerine eşittir ve belgenin kayıt
  tarihinde tahakkuk eder;
- kalanı **tahsilatta** tahakkuk eder: **taksitle** ödemede belgenin her taksiti için taksitle orantılı bir pay
  oluşur ve o taksit tahsil edildiğinde ödenebilir; **toplam üzerinden** ödemede tek bir pay oluşur (taksit -1) ve
  tüm taksitler tahsil edildiğinde ödenebilir.

Örnek: 1.350 matrahlı fatura, %5 komisyon = 63,00; temsilcinin %30'u faturada ve ödemesi taksitle, belge %50'lik
iki taksitte: pay 0 = kayıtta 18,90, taksit 1 = 22,05 ve taksit 2 = 22,05 ilgili vade tarihlerinde.

### Ödeme

Bir payı ödemek, onu bir ödeme tarihiyle temsilciye tanımak demektir. Eklenti SAP tahsilatlarını (ödemeler,
kambiyo senetleri, mutabakatlar, alacak dekontları) okuyarak ödenecek payları önerir ve taksitleri kapalı
görünmeyen (ödenmemiş) ödenmiş payların **ters kaydını** önerir. **Kesinleşmiş** bir pay kesindir: ters
kaydedilmez ve komisyon yeniden hesaplanmaz.

## 3. Kurulum ve ilk açılış

- Extension Manager paketi: `XEI.CommissionManagement.zip`, XEI sitesinin indirme sayfasından. SAP Business
  One'da **Extension Manager** açılır, paket içe aktarılır ve şirkete atanır.
- İlk açılışta eklenti alanları, tabloları, dizinleri ve yetkileri oluşturur. Belge satırlarındaki alanların oluşturulması **birkaç
  dakika** sürer: SAP birkaç kez *"Database structure has been modified... all open windows will be closed.
  Continue?"* (Veritabanı yapısı değiştirildi... tüm açık pencereler kapatılacak. Devam edilsin mi?) mesajını
  gösterir: **Yes** (Evet) yanıtını verin.
- Menü **XEI-Addon › Komisyonlar** altındadır:

    Komisyonlar
      Yapılandırma                      seçenekler (altı sekme) ve kuralların arama sırası
      Temsilciler                       rol, üstler, varsayılan %, faturada %, ödeme, satıcı, SAP kullanıcısı
      Yüzde kuralları                   müşteri / grup / kalem / kalem grubu / fiyat listesi başına %
      Kademeler ve primler              yıllık satış üzerinden primler (Yapılandırma'da etkinse)
      % kontrolü ve ataması             belgeler / kurallar karşılaştırması ve toplu düzeltme
      Komisyon hesaplama                faturalar, peşinatlar ve alacak dekontları üzerinde hesaplama
      Hesaplanan komisyonlar            görüntüleme, düzeltme, yeniden hesaplama, silme
      Ödeme                             ödenecek tahsil edilmiş paylar, ters kaydedilecek ödenmemişler
      Düzeltmeler                       temsilci ve ay başına elle tutarlar, temsilci fatura taslakları
      Komisyon ekstresi                 hesaplanan, ödenecek, ödenen + düzeltmeler; CSV, yazdırma/PDF, e-posta
      Kontroller                        kontrol edilecek sorunlar
      Informazioni, Traduzioni, Licenza (Bilgi, Çeviriler, Lisans: XEI eklentilerinin ortak öğeleri)

> Kurulumdan sonra: önce **Yapılandırma**'yı, sonra **Temsilciler**'i (roller, üstler,
> yüzdeler), sonra **Kuralları** doldurun. Belgeler yüzdeleri ancak bundan sonra alır. Süper
> kullanıcı olmayan kullanıcılara **yetkiler** verilmelidir (bölüm 17).

### Lisans

Eklenti, XEI tarafından verilen bir **lisans kodu** ile çalışır.

- **Deneme**: sitede denemeyi talep ettikten sonra e-posta ile, gönderimden itibaren 30 gün boyunca her
  şirkette geçerli bir **deneme kodu** alırsınız.
- **Satın alma**: **Licenza** (Lisans) penceresindeki iki kodu (şirket kodu ve sunucu kodu, *Copia* (Kopyala)
  ile) XEI'ye gönderir ve o kodların şirketi veya sunucusu için geçerli olan lisans kodunu alırsınız.
- Geçerli bir kod olmadan eklenti **kilitlidir**: menüsünde yalnızca *Informazioni* (Bilgi) ve *Licenza*
  (Lisans) kalır ve başlangıçta durumu ve nedeni gösteren **Licenza** penceresi kendiliğinden açılır.
- Bir SAP **süper kullanıcısı** kodu *Inserisci un codice di licenza* (Lisans kodu girin) alanına yapıştırır ve
  *Salva codice* (Kodu kaydet) düğmesine basar: eklentinin kilidi, SAP yeniden başlatılmadan hemen açılır.

### Diller

Eklenti SAP istemcisinin dilini kullanır (SAP'de: *Users - Setup* (Kullanıcılar - Ayarlar) \> *Display*
(Görüntüleme) \> *Language* (Dil)): İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca veya Türkçe; diğer
dillerde İtalyanca kalır. Dil değiştiğinde SAP açık pencereleri kapatır ve eklenti kendiliğinden yeniden başlar.
Tek tek metinler **Komisyonlar \> Traduzioni** (Çeviriler) menüsünden uyarlanabilir. SAP'nin veritabanına bir kez
kaydettiği metinler tüm dillerde İtalyanca kalır: yetkilerin adları (*General Authorizations* (Genel yetkiler) \>
Provvigioni (Komisyonlar)) ve belgelere ve satış çalışanlarına eklenen alanların başlıkları (örn. "Provv. %
manuali" (Komisyon elle %), "% agente" (temsilci %)); mesajlar bunları bu adlarla anar, böylece SAP'de
bulunabilirler.

## 4. Her ayın işi, kısaca

1.  **Ay boyunca** belgeler yüzdeleri kendiliğinden alır; belgeyi giren kişi bunları düzeltebilir.
2.  Ayın faturaları üzerinde **% kontrolü ve ataması**: yüzdeleri kurallarla uyuşmayan satırlar görülür ve toplu
    olarak düzeltilir (isteğe bağlı ama önerilir).
3.  Ayın **Komisyon hesaplama** işlemi: faturalar, peşinat faturaları, alacak dekontları.
4.  **Hesaplanan komisyonlar**: örnekleme kontrolü, tek tek komisyonların düzeltilmesi.
5.  Son tarihi ay sonu olan **Ödeme**: tahsil edilmiş payların ve olası ters kayıtların onaylanması.
6.  Ayın **Düzeltmeler**'i (primler, geri alımlar, elle düzeltmeler) ve etkinse temsilcilerin **fatura
    taslakları**.
7.  Ayın "ödenen komisyonlar ve düzeltmeler" **Komisyon ekstresi**: her temsilciye tanınacak tutardır; Excel için
    CSV, yazdırma/PDF veya her temsilciye e-posta.
8.  Ekstreler teslim edildiğinde, ay sonuna kadar **kapalı dönem** (seçenek kullanılıyorsa).

**Kontroller** (bölüm 16) her an, hesaplamadan veya ekstrelerden önce çalıştırılabilir; hesaplanmamış belgeleri,
değişen temsilcileri, yüzdesi olmayan satırları, ödenmemiş tahsilatları bulur. Yıl sonunda **Kademeler ve
primler** (bölüm 15) satış primlerini aralık ayı düzeltmeleri olarak kaydeder.

## 5. Yapılandırma

Yapılandırmanın altı sekmesi vardır. **Genel** sekmesi temel seçenekleri ve kuralların sırasını içerir; diğerleri
(**Belgeler**, **Ödeme**, **Temsilciler**, **E-posta**, **Uyarılar**) ek işlevleri içerir ve bunların hepsi
başlangıçta **kapalıdır**: her birinin altında bir açıklama ve bir örnek vardır, gerektiğinde işaretlenerek
etkinleştirilir. «Configurazione» (Yapılandırma) yetkisi gerekir (bölüm 17).

![Yapılandırma, Genel sekmesi](../../_img/commissionmanagement/cfg.png)

*Komisyon yapılandırması, Genel sekmesi*

### Genel sekmesi

Yüzdeleri satış belgelerinin satırlarına girilirken ata  
Otomatik atamayı etkinleştirir (bölüm 8). Kapatılırsa yüzdeler elle veya Kontrol ile yazılır.

Kuralların kullandığı satır iskontosu  
Kuralların kendi "asgari iskontoları" ile karşılaştırdığı iskonto: satırın *Satır iskontosu %* değeri veya
satırların yüzde türünde bir kullanıcı alanı (örneğin başka bir eklentinin hesapladığı "fiili" iskonto).

Net fiyatlar  
İskonto belirtmeden net fiyatla satanlar için: satırda iskonto yoksa eklenti **fiili iskontoyu** müşterinin fiyat
listesindeki fiyat ile satır fiyatı arasındaki fark olarak hesaplar (liste 100, fiyat 80 = iskonto %20), bunu
*Provv. sconto effettivo* (Komisyon fiili iskonto) sütununa yazar ve kurallar için kullanır.

Yüzdeler "yalnızca vergi" satırlarında da  
Normalde "yalnızca vergi" satırlarında komisyon yoktur (yüzdeler sıfır).

Peşinat faturalarında komisyon  
Seçenek etkinken peşinat faturaları hesaplanır ve komisyonları, onları kapatan kapanış faturasından **düşülür**;
böylece toplam komisyon tutarın tamamına ait komisyon olur.

Varsayılan ödeme tüm belgenin tahsilatında  
Ödemesi "Yapılandırmadan" olan satış çalışanları için geçerlidir: evet = belgenin tamamı tahsil edildiğinde tek bir
pay; hayır = taksit başına bir pay.

Alacak dekontları kayıtta değil vade tarihinde ödenir  
Normalde bir alacak dekontunun (negatif) komisyonu kayıt tarihinde ödenir. Seçenekle, dekontun ve ilgili olduğu
faturaların en uzak vade tarihinde ödenir.

Kuralların arama sırası  
Bir kural için olası 16 alan birleşimi, denendikleri sırayla. *Sıra* sütunundaki numara değiştirilir: 1
numaralı ilk denenir. Bkz. bölüm 7.

### Belgeler sekmesi

![Yapılandırma, Belgeler sekmesi](../../_img/commissionmanagement/cfg_documenti.png)

*Belgeler sekmesi: tahmin, elle satırlar, otomatik hesaplama*

Bir satış belgesi kaydedildiğinde tahmini komisyonu göster  
Bir sipariş, teklif, teslimat veya fatura eklendiğinde ya da güncellendiğinde durum çubuğu, satırların mevcut
yüzdeleriyle her hak sahibine ne kadar tahakkuk edeceğini gösterir. Örnek: *"Tahmini komisyonlar (Satış siparişi
1250): Rossi 63,00; Bianchi 9,00 - toplam 72,00"*. Yalnızca bilgi amaçlıdır: hiçbir şey kaydedilmez (bölüm 8).

Belge satırlarında elle değiştirilen yüzdeleri koru  
Satırdaki bir yüzdeyi düzelten kişi satırı "elle" yapar (*Provv. % manuali* (Komisyon elle %) sütunu): müşteri veya
temsilci değiştirildiğinde o satır yeniden atanmaz. Örnek: Rossi müşteriyle bir anlaşma için satırı %5'ten %4'e
indirir; sonra müşteriyi değiştirir: diğer satırlar yeniden atanır, bu satır %4'te kalır. Seçenek olmadan yeniden
atama tüm satırların üzerine yazar. "Elle" işareti kaldırılınca satır otomatiğe döner.

Fatura, peşinat faturası veya alacak dekontu kaydedilir kaydedilmez komisyonları hesapla  
Hesaplama SAP istemcisinden kaydetme sırasında yapılır (belge iskontosu için Hesaplama'da yapılan son seçimle):
böylece her ay Komisyon hesaplama'yı açmak gerekmez. Örnek: Rossi'nin 1001 numaralı faturası kaydedildiğinde durum
çubuğu *"Komisyonlar hesaplandı (Fatura 1001): Rossi 63,00; Bianchi 9,00"* der. İçe aktarmalarla veya başka
programlarla (DI API) oluşturulan belgeler istemciden geçmez: onlar için Komisyon hesaplama ve Kontroller kullanılır.

### Ödeme sekmesi

![Yapılandırma, Ödeme sekmesi](../../_img/commissionmanagement/cfg_liquidazione.png)

*Ödeme sekmesi: kısmi tahsilatlar ve kapalı dönem*

Kısmi tahsilatlar: komisyonun taksitte tahsil edilen tutarla orantılı kısmını öde  
Seçenek olmadan bir pay ancak taksit tamamen kapandığında ödenir: avans veya indirimlerde komisyon bekler. Örnek:
500'lük taksit, pay 22,05; müşteri 250 öder → 11,03 ödenir; kapanışta kalan 11,02. Bir tahsilat iptal edilirse
yalnızca fazlası ters kaydedilir (bölüm 12).

Kapalı dönem: komisyonları şu tarihe kadar kilitle (tarih)  
Bu tarihe kadar (dahil) komisyonlar yeniden hesaplanamaz veya silinemez, paylar değiştirilemez, ödeme yapılamaz ve
düzeltmeler kaydedilemez. Örnek: mart ekstreleri teslim edildikten sonra 31/03 girilir: mart faturaları yeniden
hesaplanmaz (hiç hesaplanmamış bir fatura yine de hesaplanabilir). Kapalı dönemde bir şeyi düzeltmek için: tarihi
geriye alın (veya işareti kaldırın), düzeltin, sonra geri koyun.

### Temsilciler sekmesi

Düzeltmelerden, bir satıcıya bağlı temsilcilerin satınalma faturası taslaklarını oluştur  
Düzeltmeler'de **Temsilci fatura taslakları** düğmesi her temsilci için bir hizmet satırlı bir satınalma faturası
taslağı (tutar negatifse alacak dekontu) oluşturur: tutar = ay içinde ödenen paylar + ayın düzeltmeleri ve
primleri. Örnek: Rossi (satıcı F0010), nisan: 22,05 + 50,00 - 20,00 = 52,05. **Satır hesabı** zorunludur
(komisyon gider hesabı, örn. 7xxxx Ödenen komisyonlar); **KDV kodu** temsilcinin faturalarındaki koddur (boş =
satıcının varsayılanı). Bölüm 13.

Primli yıllık satış kademeleri  
**Kademeler ve primler** menüsünü etkinleştirir: yıllık matrah eşiğine ulaşıldığında temsilci, düzeltme olarak
kaydedilen bir prim alır (yılın satışının %'si veya sabit tutar). Örnek: kademeler 100.000 → %0,5 ve 200.000 →
%1; Rossi 2026'da 150.000 faturalar: aralık düzeltmesinde 750,00 prim. Bölüm 15.

Ödenen ekstresinde gösterge niteliğinde stopaj: % ve açıklama  
Yalnızca bilgi amaçlıdır (alt ve üst sınır yok): "ödenen komisyonlar ve düzeltmeler" ekstresinin çıktısında ve
e-postasında bir "stopaj" satırı ve gösterge net tutar görünür. Örnek: 8,5 ve "Enasarco quota agente"
(Enasarco temsilci payı): ödenen 1.000,00 → gösterge stopaj -85,00, gösterge net 915,00. Boş veya 0 = satır yok.

![Yapılandırma, Temsilciler sekmesi](../../_img/commissionmanagement/cfg_agenti.png)

*Temsilciler sekmesi: fatura taslakları, kademeler ve gösterge stopaj (%8,5 Enasarco)*

### E-posta sekmesi

![Yapılandırma, E-posta sekmesi](../../_img/commissionmanagement/cfg_email.png)

*E-posta sekmesi: ekstrenin temsilcilere gönderimi*

Ekstrenin temsilcilere e-postayla gönderimi  
Komisyon ekstresindeki **Temsilcilere gönder** düğmesini etkinleştirir: her temsilci yalnızca kendi ekstresini
(HTML eki, her tarayıcıda açılıp yazdırılabilir) satış çalışanının (veya bağlı satıcının) e-posta adresine alır.
SMTP sunucusu, port, SSL/TLS, posta kutusunun kullanıcısı ve parolası ile gönderen girilmelidir; örnek:
`smtp.office365.com`, port 587, SSL evet, gönderen `provvigioni@azienda.it`. Parola şifrelenmiş olarak
kaydedilir.

Gönderimi dene  
Sekmede yazılan değerleri (kaydedilmemiş olsalar da) kullanarak belirtilen adrese bir deneme mesajı gönderir: bir
sorun varsa sunucunun hata mesajı hemen görünür.

### Uyarılar sekmesi

![Yapılandırma, Uyarılar sekmesi](../../_img/commissionmanagement/cfg_avvisi.png)

*Uyarılar sekmesi*

Tahsil edilmiş ve ödenmemiş pay şu kadar gün sonra sorun sayılır  
Kontroller'de "Ödenmemiş tahsilatlar" araması, taksiti bu kadar günden uzun süre önce tahsil edilmiş ve kimsenin
ödemediği payları bildirir. Örnek: 30; taksit 05/04'te tahsil edildi ve bugün 10/05: pay ödenene kadar sorunlar
arasında görünür.

Eklenti başlarken hızlı kontrollerin sorunlarını durum çubuğunda bildir  
Her açılışta hızlı kontroller: hesaplanacak son 90 günün belgeleri, komisyonlu iptal edilmiş belgeler, hesaplamadan
sonra değişen temsilci. Örnek: *"Komisyonlar: kontrol edilecek 3 sorun (Komisyonlar \> Kontroller)"*. Bölüm 16.

> Kaydederken Yapılandırma etkin seçeneklerin eksiksiz olduğunu kontrol eder: kapalı dönemin tarihi, taslaklar
> için mevcut ve kayıt yapılabilen bir hesap, 0 ile 99,99 arasında stopaj, e-posta için sunucu, port ve gönderen.

## 6. Temsilciler

![Temsilciler](../../_img/commissionmanagement/agenti.png)

*Temsilciler: SAP'nin tüm satış çalışanları, tabloda değiştirilebilir*

Tablo SAP'nin tüm satış çalışanlarını gösterir. Sütunlar doldurulur ve **Kaydet** düğmesine basılır: yalnızca
değiştirilen satış çalışanları kaydedilir (aynı alanlar satış çalışanlarının standart formunda, *User-Defined
Fields* (kullanıcı tanımlı alanlar) bölümünde de görünür).

| Sütun | Anlamı |
|---|---|
| Rol | Temsilci, Bölge sorumlusu, Alan sorumlusu, Müdür veya *(yönetilmiyor)*: komisyon yok. |
| Bölge sorumlusu, Alan sorumlusu, Müdür | Bu satış çalışanının üstleri: onun belgelerinden kendi yüzdelerini alırlar. Açılır listeler o role sahip satış çalışanlarını gösterir: önce rolleri atayıp kaydedin, sonra üstleri. Daha önce atanmış ve başka bir rolü olan ya da hiç rolü olmayan bir üst *«ad (farklı rol)»* olarak görünür: kendisine rol verilene kadar komisyon almaz (Kontroller de bunu bildirir). |
| Temsilci %, Bölge sorumlusu %, Alan sorumlusu %, Müdür % | Bu satış çalışanının belgelerinin **varsayılan** yüzdeleri; satıra hiçbir kural uygulanmadığında kullanılır. |
| Faturada % | Komisyonun **bu satış çalışanına** (hak sahibi olarak) ait olan ve belgenin kaydında tahakkuk eden kısmı; kalanı tahsilatta tahakkuk eder. 100 = tamamı faturada, 0 = tamamı tahsilatta. |
| Ödeme | Tahsilattaki kısım için: *Taksitle*, *Toplam üzerinden* veya *Yapılandırmadan* (Yapılandırma'daki seçeneği izler). |
| Satıcı | Temsilcinin komisyonları faturaladığı satıcı (iş ortağı): **fatura taslaklarının** muhatabı (bölüm 13); satış çalışanının e-postası yoksa ekstrenin gönderimi için onun e-postası kullanılır. |
| SAP kullanıcısı | Bu satış çalışanına karşılık gelen SAP kullanıcısı. «Estratto di tutti gli agenti» (Tüm temsilcilerin ekstresi) yetkisi olmayan bir kullanıcı Komisyon ekstresinde yalnızca kendisini ve bölge sorumlusu, alan sorumlusu veya müdürü olduğu satış çalışanlarını görür (bölüm 17). |
| E-posta (satış çalışanı kartı) | Satış çalışanının e-posta adresi (SAP kartı, salt okunur): e-postayla gönderilen ekstrenin alıcısı. |

Kaydederken yapılan kontroller: yüzdeler 0 ile 100 arasında, satıcı ve SAP kullanıcısı mevcut, bir satış çalışanı
kendisinin üstü olamaz. Bu kılavuzda kullanılan örnek:

| Satış çalışanı | Rol | Bölge sorumlusu | Alan sorumlusu | % tem. | % bölge s. | % alan s. | Faturada % | Ödeme |
|---------|---------------|-----------|-----------|-------|----------|----------|------------|-------------------|
| Rossi   | Temsilci        | Bianchi   | Neri      | 2     | 0,5      | 0,2      | 30         | Taksitle            |
| Bianchi | Bölge sorumlusu     |           |           | 3     |          |          | 0          | Yapılandırmadan |
| Neri    | (yönetilmiyor) |           |           |       |          |          |            |                   |
| Verdi   | Temsilci        |           |           | 1,5   |          |          | 100        | Yapılandırmadan |

Rossi'nin belgelerinde hak sahipleri Rossi (temsilci) ve Bianchi'dir (bölge sorumlusu); Neri, alan sorumlusu
olarak belirtilmiş olsa da bir rolü olana kadar hiçbir şey almaz.

## 7. Yüzde kuralları

![Yüzde kuralları](../../_img/commissionmanagement/regole.png)

*Örneğin yüzde kuralları*

Bir kural şunu söyler: "*bu özelliklere* sahip satırlar için yüzdeler şunlardır". Olası özellikler müşteri, müşteri
grubu, kalem, kalem grubu ve fiyat listesidir (müşterinin fiyat listesi); **yalnızca gereken alanlar** doldurulur ve
eklenti **birleşimi** kendiliğinden tanır (Birleşim sütunu). İzin verilen birleşimler 16 tanedir:

| Tür | Birleşim                        | Tür | Birleşim                               |
|------|-------------------------------------|------|--------------------------------------------|
| 1    | Müşteri / Kalem / Fiyat listesi        | 9    | Müşteri grubu / Kalem grubu / Fiyat listesi |
| 2    | Müşteri / Kalem                  | 10   | Müşteri grubu / Kalem grubu           |
| 3    | Müşteri / Kalem grubu / Fiyat listesi | 11   | Müşteri grubu / Fiyat listesi                   |
| 4    | Müşteri / Kalem grubu           | 12   | Müşteri grubu                             |
| 5    | Müşteri / Fiyat listesi                   | 13   | Kalem / Fiyat listesi                         |
| 6    | Müşteri                             | 14   | Kalem                                   |
| 7    | Müşteri grubu / Kalem / Fiyat listesi | 15   | Kalem grubu / Fiyat listesi                  |
| 8    | Müşteri grubu / Kalem           | 16   | Kalem grubu                            |

Müşteri ile müşteri grubu birlikte (veya kalem ile kalem grubu birlikte) kullanılamaz: kural kaydedilmez.

Kuralın diğer alanları:

- **Temsilci**: kural yalnızca o satış çalışanının belgeleri için geçerlidir; *(tümü)* = herkes için;
- **Başlangıç / Bitiş**: belgenin tarihiyle karşılaştırılan geçerlilik dönemi; iki tarihten yalnızca biri de olabilir;
- **Asgari iskonto**: satırın iskontosu en az bu değerdeyse kural geçerlidir (0 = her zaman). Daha çok iskontolu
  satışlara daha düşük yüzdeler vermeye yarar;
- **Etkin**: etkin olmayan bir kural arşivde kalır ama uygulanmaz.

### Bir satırın kuralı nasıl seçilir

1.  Birleşimler **Yapılandırma'daki sırayla** denenir (varsayılan 1 → 16, en özelden en genele).
2.  Her birleşim için önce **belgenin temsilcisinin** kuralları aranır (en az bir tane varsa), sonra herkes için
    olanlar. Geçerli bir kural bulan ilk birleşim kazanır: herkes için daha özel bir kural (örn. Müşteri / Kalem
    grubu), temsilcinin daha genel bir kuralına (örn. Kalem grubu) karşı kazanır.
3.  Aynı birleşimin birden fazla kuralı arasında başlangıç tarihi en yakın olan, sonra bitişi en yakın olan, sonra
    ulaşılan asgari iskontosu en yüksek olan kazanır.
4.  Hiçbir kural geçerli değilse temsilcinin varsayılan yüzdeleri kullanılır.

Şekildeki kurallarla örnek (R1 müşteri C001 + kalem grubu GA100 → 6/1; R2 yalnızca Rossi, grup GA100 → 7/1;
R3 kalem A1 → 4/0,5; R4 asgari iskonto 10 ile kalem A1 → 3/0,5; R5 müşteri grubu A, yıl 2026 → 5/1):

| Satır                                            | Temsilci / bölge sorumlusu yüzdeleri | Neden                                                          |
|-------------------------------------------------|--------------------------------|-----------------------------------------------------------------|
| Rossi, müşteri C001, kalem A9 (grup GA100) | 6 / 1                          | R1: Müşteri / Kalem grubu, Rossi'nin kuralından önce gelir |
| Rossi, müşteri C002, kalem A9                | 7 / 1                          | R2: temsilcinin kuralı                                          |
| Verdi, müşteri C002, kalem A9                | 1,5 / 0                        | kural yok: Verdi'nin varsayılan yüzdeleri                |
| Verdi, müşteri C002, kalem A1, iskonto 12     | 3 / 0,5                        | R4: asgari iskonto 10'a ulaşıldı (R3'e karşı kazanır)                    |
| Verdi, müşteri C002, kalem A1, iskonto 5      | 4 / 0,5                        | R3                                                              |
| Verdi, müşteri C003 (grup A), kalem A1     | 5 / 1                          | R5: Müşteri grubu, Kalem'den önce gelir                      |
| yukarıdaki gibi ama 2027'de                          | 4 / 0,5                        | R5'in süresi doldu, R3 kalır                                    |

### Form

- **Filtreler** (temsilci, müşteri, kalem, yalnızca etkin) ve **Ara**.
- Seçili satırlarda **Satır ekle**, **Satırları çoğalt** ve **Satırları sil** (soldaki satır başlığına tıklayarak);
  değişiklikler **Kaydet** ile kesinleşir. Tüm alanlar tabloda değiştirilir (oklar müşteriyi ve kalemi açar).
- **CSV olarak dışa aktar** gösterilen kuralları ";" ayırıcılı bir dosyaya kaydeder (Excel'de açılır); **CSV'den
  içe aktar** aynı sütunlara sahip bir dosyanın satırlarını ekler (Agente, Cliente, GruppoClienti, Articolo,
  GruppoArticoli, Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea, PercDirettore, Attiva):
  içe aktarılan satırlar kontrol edilip kaydedilmelidir.
- Kaydedilmemiş değişikliklerle kapatırken veya ararken eklenti onay ister.

## 8. Satış belgelerindeki yüzdeler

![Satış siparişi](../../_img/commissionmanagement/ordine.png)

*Satış siparişi: atanan yüzdelerle Provv. sütunları ve net fiyatlarda fiili iskonto*

Atama etkinken *Sales Quotation* (Satış teklifi), *Sales Order* (Satış siparişi), *Delivery* (Teslimat), *Return*
(İade), *A/R Invoice* (Satış faturası), *A/R Credit Memo* (Alacak dekontu) ve *A/R Down Payment Invoice* (Peşinat
faturası) belgelerinde:

- bir satırın **kalemi**, **iskontosu** veya **fiyatı** girildiğinde ya da değiştirildiğinde eklenti satırın dört
  yüzdesini (ve net fiyatlarda fiili iskontoyu) yazar;
- listeden birden fazla kalem seçildiğinde eklenen satırlar da tamamlanır;
- giriş aşamasındaki bir belgenin **müşterisi** veya **satış çalışanı** değiştirildiğinde tüm satırlar yeniden
  atanır. Dikkat: müşteri değiştirildiğinde SAP o müşterinin varsayılan satış çalışanını geri koyar; bu "hiçbiri"
  ise temsilci seçilene kadar satırlar olduğu gibi kalır.

Yüzdeler **elle değiştirilebilir** kalır ve belgeyle birlikte kaydedilir; yalnızca o satırın kalemi, fiyatı veya
iskontosu tekrar değiştirilirse yeniden yazılır. Kopyalanan belgeler (sipariş → teslimat → fatura) satırların
yüzdelerini de beraberinde getirir.

> *Provv. % agente*, *% capo zona*, *% capo area*, *% direttore* (Komisyon % temsilci, bölge sorumlusu, alan
> sorumlusu, müdür) ve *Provv. sconto effettivo* (Komisyon fiili iskonto) sütunları, belge açıldığında eklenti
> tarafından görünür ve değiştirilebilir yapılır; her zaman tercih edilen konumda olmaları için bir kez *Form
> Settings* (Form ayarları) içinde düzenlenebilirler (tablonun sağ üstündeki simge). Satış çalışanı olmayan ya da
> rolü olmayan bir satış çalışanına sahip belgelere hiçbir şey yazılmaz.

Bir satırın "yalnızca vergi" işareti istemcide bir olay oluşturmaz: yüzdeler satırın kalemi, fiyatı veya iskontosu
bir sonraki değişiminde (veya temsilci değiştirildiğinde) uyarlanır.

### Elle satırlar ("elle değiştirilen yüzdeleri koru" seçeneği)

![Elle satırlı sipariş](../../_img/commissionmanagement/ordine_manuale.png)

*Sipariş: yüzdesi elle düzeltilen satır "Provv. % manuali" alanında işaretlidir ve yeniden atanmaz*

Seçenek etkinken eklenti *Provv. % manuali* (Komisyon elle %) sütununu da gösterir. Bir satırın dört yüzdesinden
biri elle yazılır yazılmaz satır **elle olarak işaretlenir** ve o andan itibaren yeniden atanmaz: ne satırın kalemi,
fiyatı veya iskontosu değiştirildiğinde, ne belgenin müşterisi veya temsilcisi değiştirildiğinde, ne de listeden
başka kalemler seçildiğinde. Diğer satırlar kuralları izlemeye devam eder. Otomatiğe dönmek için işareti kaldırmak
yeterlidir: bir sonraki değişiklikte satır kuralların yüzdelerini tekrar alır. İşaret kopyalanan belgelere geçer ve
Kontrol'de (*Elle %* sütunu) görünür; orada elle satırlar düzeltme için önerilmez.

### Kayıtta tahmin ve otomatik hesaplama

![Durum çubuğunda tahmin](../../_img/commissionmanagement/stima.png)

*Sipariş eklendikten sonra durum çubuğu her hak sahibi için tahmini komisyonu gösterir*

Belgeler sekmesinin iki seçeneği, belge SAP istemcisinden **kaydedildiğinde** devreye girer:

- **Tahmin**: tekliflerde, siparişlerde, teslimatlarda, iadelerde, faturalarda, alacak dekontlarında ve peşinat
  faturalarında durum çubuğu, satırların mevcut yüzdeleriyle hak sahibi başına ne kadar tahakkuk edeceğini gösterir,
  örneğin *"Tahmini komisyonlar (Satış siparişi 1250): PRV Rossi 6,00; PRV Bianchi 1,00 - toplam 7,00"*. Belge
  iskontosu, Hesaplama'da yapılan son seçime göre dikkate alınır veya alınmaz. Hiçbir şey kaydedilmez.
- **Otomatik hesaplama**: istemciden **eklenen** faturalar, alacak dekontları ve (etkinse) peşinat faturaları,
  yalnızca o belge için Komisyon hesaplama çalıştırılmış gibi hemen hesaplanır; durum çubuğu *"Komisyonlar
  hesaplandı (Fatura 1001): ..."* der. Hesaplanan komisyonlar'da kaynak "Kayıtta otomatik"tir. Hesaplama mümkün
  değilse (peşinat zaten düşülmüş, kapalı dönem, yönetilmeyen temsilci) bir uyarı görünür ve belge normal şekilde
  kaydedilmiş olarak kalır: daha sonra Komisyon hesaplama'dan hesaplanır ve Kontroller onu "Hesaplanacak" arasında
  bildirir.

> İçe aktarmalarla, Service Layer ile veya DI API ile oluşturulan belgeler SAP istemcisinden geçmez: onlar için her
> zaman Komisyon hesaplama kullanılır (veya yalnızca hesaplanmamış belgeleri alan tüm dönemin hesaplaması).

## 9. % kontrolü ve ataması

![Yüzde kontrolü ve ataması](../../_img/commissionmanagement/controllo.png)

*Kontrol: belgenin yüzdeleri ("Belge") ve kuralların önerdikleri, farklı satırlar vurgulu*

Hesaplamadan önce dönemin belgelerindeki yüzdelerin kurallarla uyuştuğunu kontrol etmek yararlıdır (faturayı giren
kişi onları değiştirmiş olabilir ya da kurallar sonradan güncellenmiş olabilir).

1.  Temsilciyi (veya tümünü), dönemi ve belge türlerini seçin: **hesaplanmamış** faturalar, peşinat faturaları,
    alacak dekontları ve isteğe bağlı olarak açık satış siparişleri. **Kontrol et** düğmesine basın.
2.  Tablo her satır için mevcut yüzdeleri (*Belge*), kuralların bugün vereceği yüzdeleri (*Önerilen*) ve *Öneri
    kaynağı*nı (herkes için kural, temsilcinin kuralı, varsayılan yüzdeler) gösterir. Farklı satırlar vurgulanır ve
    zaten işaretlidir; "Yalnızca öneriden farklı satırlar" ile yalnızca bunlar görülür.
3.  Olduğu gibi bırakılacak satırların (istenen düzeltmeler) işaretini kaldırın ve **Önerilen %'leri uygula**
    düğmesine basın.

İşaretli satırlara ne olur:

- **açık satış siparişleri**: sipariş güncellenir; yüzdeler, ondan kopyalanacak belgelere geçer;
- **faturalar, peşinat faturaları ve alacak dekontları**: bunlar kaydedilmiş belgelerdir ve SAP bunların
  değiştirilmesine izin vermez (satırların kullanıcı alanları dahil). Düzeltilen yüzdeler eklenti tarafından kendi
  tablosuna kaydedilir ve hesaplamada belgedekilerin yerine kullanılır; SAP belgesi olduğu gibi kalır. *Zaten
  düzeltilmiş* sütunu bunu belirtir ve *Belge* sütunları o andan itibaren düzeltilmiş yüzdeleri gösterir.

![Elle satırlarla kontrol](../../_img/commissionmanagement/controllo_manuale.png)

*Açık siparişler üzerinde kontrol: öneriden farklı elle satırlar işaretlenmez ("elle %: 3")*

Bir satıra çift tıklamak belgeyi açar. Komisyonları hesaplanmış belgeler görünmez: bunları düzeltmek için
Hesaplanan komisyonlar kullanılır (bölüm 11). *Elle %* sütunu, yüzdeleri belge üzerinde elle düzeltilmiş satırları
gösterir: "elle değiştirilen yüzdeleri koru" seçeneğiyle bunlar işaretlenmez (bilerek işaretlenebilirler). Kapalı
dönem etkinken, tarihi dönem içinde olan kaydedilmiş belgeler düzeltilmez.

## 10. Komisyon hesaplama

![Komisyon hesaplama](../../_img/commissionmanagement/calcolo.png)

*Belge başına sonuçla komisyon hesaplama*

Dönemi (belge tarihi), türleri (faturalar, Yapılandırma'da etkinse peşinat faturaları, alacak dekontları) ve
**belge iskontosunun dikkate alınıp alınmayacağını** seçin (iskontolu belgenin tamamı her satırın matrahını düşürür).
**Hesapla**, dönemin **iptal edilmemiş**, yönetilen bir temsilciye sahip ve **hesaplanmamış** tüm belgelerini işler:
önce peşinat faturaları, sonra faturalar ve alacak dekontları. Tablo her belge için kaç hak sahibinin komisyonu
olduğunu, toplamı ve sonucu gösterir; çift tıklama belgeyi açar.

**Yalnızca belge** (tür ve numara) ile belirli bir belge hesaplanır veya **yeniden hesaplanır**, örneğin
yüzdelerin düzeltilmesinden sonra; yeniden hesaplama yalnızca hiçbir payı ödenmemiş veya kesinleşmemişse mümkündür.

### Hesaplama adım adım

Her hak sahibi için (temsilci ve rolü olan üstler):

1.  **Satır matrahı** = yerel para birimindeki satır toplamı, istenirse belge iskontosu kadar düşürülmüş; alacak
    dekontlarında negatif. Sıfır tutarlı satırlar (bedelsiz) sayılmaz.
2.  **Satır komisyonu** = matrah × satırın o rol için yüzdesi. Yüzdesi 0 olan satırlar sayılmaz.
3.  **Toplam** = satır komisyonlarının toplamı. Bir peşinatı kapatan faturalardan, peşinat üzerinde hesaplanmış
    komisyon düşülür (düşülen tutarla orantılı olarak).
4.  **Paylar**: faturadaki pay (taksit 0) kayıt tarihinde; kalanı taksitle (n. taksit n. taksitin vade tarihinde,
    yüzdesiyle orantılı, yuvarlamalar son taksite) veya toplam üzerinden (taksit -1, son taksitin vade tarihinde).
    Alacak dekontlarında tek bir negatif pay vardır (taksit 0, kayıtta veya seçenekle vade tarihinde).

Tutarlar 2 ondalığa yuvarlanır; komisyonun toplamı her zaman payların toplamıdır.

### Örnek: 1001 numaralı fatura

Rossi (%30 faturada, taksitle), müşteri C001, **%10 belge iskontosu**, %50'lik iki taksit (31/03 ve 30/04):

| Satır         | Satır toplamı | Matrah (−%10) | Temsilci % | Temsilci kom. | Bölge sorumlusu % | Bölge sorumlusu kom. |
|--------------|-------------|-------------------|----------|---------------|-------------|------------------|
| A1           | 1.000,00    | 900,00            | 5        | 45,00         | 1           | 9,00             |
| A2           | 500,00      | 450,00            | 4        | 18,00         | 0           | \-               |
| A3 (bedelsiz) | 0,00        | \-                | 5        | \-            |             |                  |
| Toplam       |             | 1.350,00          |          | 63,00         |             | 9,00             |

| Hak sahibi                         | Pay                 | Vade tarihi              | Tutar |
|--------------------------------------|-----------------------|-----------------------|---------|
| Rossi (temsilci, %30 faturada)     | taksit 0 – faturada | 10/03 (kayıt) | 18,90   |
|                                      | taksit 1 (%35)          | 31/03                 | 22,05   |
|                                      | taksit 2 (%35)          | 30/04                 | 22,05   |
| Bianchi (bölge sorumlusu, %0 faturada) | taksit 1 (%50)          | 31/03                 | 4,50    |
|                                      | taksit 2 (%50)          | 30/04                 | 4,50    |

Neri (alan sorumlusu), A1 satırında kendi sütununda %0,5 olsa da rolü olmadığı için hiçbir şey almaz.

### Peşinat faturaları

SAP bir peşinat faturasını siparişin tam satırlarıyla ve peşinatın tümleyenine eşit bir belge iskontosuyla kaydeder
(%30 peşinat = %70 iskonto): eklenti her zaman bu iskontoyu kullanır, dolayısıyla matrah peşinat payıdır (10.000 ×
%30 = 3.000 → %5 ile 150,00). Kapanış faturası peşinatı düştüğünde, onun komisyonundan (10.000 × %5 = 500,00)
hesaplanmış 150,00 çıkarılır: kalan 350,00 her zamanki gibi paylara bölünür. Kapanış faturasının hesaplanmış
komisyonları olduğu sürece peşinat yeniden hesaplanamaz ve silinemez (fatura düzeltilmelidir).

### Neler yeniden hesaplanmaz

- **ödenmiş veya kesinleşmiş** payları olan belgeler (önce ödeme kaldırılmalıdır, bölüm 11);
- hesaplanmış bir faturadan zaten düşülmüş peşinat faturaları;
- iptal edilmiş belgeler: hesaplanmazlar; iptalden önce hesaplanmışlarsa komisyonları Hesaplanan komisyonlar'dan
  elle silinmelidir (Ödeme bunları dikkate almaz).

## 11. Hesaplanan komisyonlar: görüntüleme ve düzeltme

![Hesaplanan komisyonlar](../../_img/commissionmanagement/provvigioni.png)

*Hesaplanan komisyonlar: liste, hak sahibinin %'si ile belge satırları ve paylar*

Üstteki liste belge ve hak sahibi başına bir satır gösterir (temsilci, tür, dönem, numara ve yalnızca ödenmemişler
filtreleri): matrah, komisyon, ödenen, ödenecek, hesaplama tarihi. Bir satıra tıklandığında altta, o hak sahibinin
yüzdesiyle **belge satırları** ve **paylar** görünür. Çift tıklama belgeyi SAP'de açar.

Değiştirilen %'lerle yeniden hesapla  
Alttaki satırlarda yüzde değiştirilir (*%* sütunu) ve yalnızca bu komisyon yeniden hesaplanır. SAP belgesine
dokunulmaz: kuralları değiştirmeden tek bir durumu düzeltmeye yarar. Örnek: A2 satırı %4'ten %6'ya → 63,00, 72,00
olur ve paylar 21,60 / 25,20 / 25,20.

Belgeden yeniden hesapla  
Belge satırlarının mevcut (veya Kontrol ile düzeltilmiş) yüzdeleriyle yeniden hesaplar: önceki düğmeyle yapılan
değişiklikleri geri alır ve belge üzerinde yapılan düzeltmeleri yansıtır.

Payları kaydet  
Payların ödeme tarihi, ödenen tutarı ve *Kesinleşmiş* işareti elle değiştirilebilir (prosedür dışındaki ödemeler,
düzenlemeler): Payları kaydet bunları kaydeder ve başlıktaki ödenen tutarı günceller.

Komisyonu sil  
Bu hak sahibinin belgedeki komisyonunu kaldırır; belge Hesaplama'dan tekrar hesaplanabilir hale gelir (yalnızca belge
veya dönem içinde).

Yeniden hesaplama ve silme şu durumlarda engellenir: bir pay zaten ödenmiş veya kesinleşmişse ("Komisyonlar zaten
ödenmiş veya kesinleşmiş: önce ödemeyi kaldırın": Payları kaydet'te ödenen tutarı sıfırlayın), belge **kapalı
dönemdeyse** (Yapılandırma'nın Ödeme sekmesi) ve, ihtiyaten, satış çalışanı belgenin temsilcisinin hiyerarşisinde
yer almıyorsa (yeniden hesaplama onu silerdi: istenen buysa Sil'i kullanın).

**İzlenebilirlik**: her başlık ve her pay *Kaynak*, *Kullanıcı* ve *Son değişiklik* gösterir: o veriyi en son kimin
ve nasıl yazdığı. Başlıkların kaynakları: *Hesaplama* (menüden), *Kayıtta otomatik* (faturanın kaydında), *Belgeden
yeniden hesaplama*, *Değiştirilen %'lerle yeniden hesaplama*; payların kaynakları: *Hesaplama*, *Ödeme*, *Ödenmemiş
ters kaydı*, *Elle* (Payları kaydet).

## 12. Ödeme

![Ödeme](../../_img/commissionmanagement/liquidazione.png)

*Ödeme: 31/03 itibarıyla ödenecek pay önerileri*

1.  **Son tarihi** (normalde ay sonu) belirtin, alacak dekontlarının dahil edilip edilmeyeceğini seçin ve isteğe
    bağlı olarak işlenecek temsilcileri işaretleyin (hiçbiri = tümü). **İşle**.
2.  Tablo şunları önerir:
    - **Öde** – vade tarihi son tarihe kadar olan, ödenmemiş ve kesinleşmemiş paylar:
      - faturadaki pay (taksit 0) her zaman, kendi vade tarihinde (belgenin kayıt tarihi);
      - bir taksitin payı, o taksit SAP'de **kapalı** göründüğünde; toplam üzerinden pay (taksit -1), tüm
        taksitler kapalı olduğunda;
      - önerilen **ödeme tarihi**, taksitin vade tarihi ile tahsilat tarihinden daha geç olanıdır.
        Tahsilat tarihi şunları dikkate alır: tahsilatlar (ödeme tarihi veya daha sonraysa vade tarihi), başarıyla
        tahsil edilen kambiyo senetleri, yevmiye kayıtları veya alacak dekontlarıyla mutabakatlar, fatura üzerine
        düzenlenen alacak dekontları; belirlenemezse vade tarihi geçerlidir.
    - **Ters kayıt** (kırmızı satırlar) – taksitleri kapalı görünmeyen (iptal edilen tahsilat, ödenmemiş), ödenmiş
      ve kesinleşmemiş paylar: ödeme kaldırılır ve tutar tekrar ödenecek duruma geçer.
3.  Kaydedilmeyecek satırların işaretini kaldırın, gerekirse ödeme tarihini düzeltin, kesinleştirilecek paylarda
    **Kesinleştir** işaretini koyun. Alttaki toplamlar işaretlere göre güncellenir.
4.  **Onayla** işaretli satırları kaydeder; belgelerin ödenen tutarı güncellenir ve sonraki bir işleme bunları
    tekrar önermez.

![Ters kayıt](../../_img/commissionmanagement/liquidazione_storno.png)

*Bir tahsilatın iptalinden sonra: ödenmiş payların ters kayıt önerisi*

Örnek: 1001 numaralı faturanın ilk taksiti (vade 31/03) 05/04'te tahsil edilmiştir. 30/04'e kadar işlendiğinde
Rossi'nin (22,05) ve Bianchi'nin (4,50) taksit 1 payları 05/04 ödeme tarihiyle önerilir. Tahsilat iptal edilirse
sonraki işleme iki payın ters kaydını önerir; Rossi'nin payı kesinleştirilmişse yalnızca Bianchi'nin ters kaydı
önerilir.

> **Kesinleşmiş** bir pay kesindir: ters kaydedilmez ve belgenin komisyonu yeniden hesaplanmaz. Komisyonlar
> temsilciye ödendiğinde kesinleştirin.

### Kısmi tahsilatlar (seçenek)

![Kısmi tahsilatlı ödeme](../../_img/commissionmanagement/liquidazione_parziale.png)

*Kısmi tahsilat: ödenebilir kısım, tam pay ve zaten ödenen tutarla sarı satırlar*

Normalde bir taksitin payı ancak taksit **kapalı** olduğunda ödenir: müşteri bir avans öderse komisyon bekler.
**Kısmi tahsilatlar** seçeneğiyle pay, tahsil edilen tutarla orantılı olarak ödenir: 816,75'lik taksit, pay 22,05,
müşteri 408,38 (yarısı) öder → **11,03** ödemesi önerilir (sarı satır, *Tam pay* 22,05 ve *Zaten ödendi* 0
sütunlarıyla), vade tarihinden sonraysa tahsilat tarihinde; kapanışta kalan **11,02** önerilir. Bir tahsilat iptal
edilirse ters kayıt ödenen tutarı hâlâ tahsil edilmiş kısma indirir (tahsil edilmiş bir şey kalmamışsa tamamını).
Faturadaki paylar (taksit 0) değişmez; "belge toplamı üzerinden" paylarda oran tüm taksitlerin tahsil edilen
tutarına göredir.

### Kapalı dönem (seçenek)

Bir ayın ekstreleri teslim edildiğinde dönem o tarihe kadar **kapatılabilir** (Yapılandırma'nın Ödeme sekmesi): o
andan itibaren tarihi dönem içinde olan belgeler için komisyonlar yeniden hesaplanmaz ve silinmez, paylar
değiştirilmez, dönem içinde bir tarihle ödeme veya ters kayıt yapılmaz, kapalı aylara düzeltme veya prim
kaydedilmez ve Kontrol kaydedilmiş belgeleri düzeltmez. Her durumda mesaj, herhangi bir onay sorusundan önce
*"Dönem gg/aa/yyyy tarihine kadar kapalı"* der (paylar zaten ödenmişse bunun yerine *"Komisyonlar zaten ödenmiş veya
kesinleşmiş"* der). Dönemin hiç hesaplanmamış bir faturası yine de hesaplanabilir. Bir şeyi düzeltmek için: tarihi
geriye alın (veya işareti kaldırın), düzeltin, sonra geri koyun.

## 13. Düzeltmeler

![Düzeltmeler](../../_img/commissionmanagement/conguagli.png)

*Bir ayın düzeltmeleri*

Temsilci ve ay başına, pozitif veya negatif elle girilen tutarlar (primler, geri ödemeler, geri alımlar,
düzeltmeler); bir sıra numarası ve bir açıklamayla. Yıl ve ay seçilir (ay değiştirmek için \< ve \> okları,
**Göster**), satır eklenir veya silinir ve **Kaydet** düğmesine basılır: ayın satırları tablodakilerle değiştirilir.
Düzeltmeler ayın "ödenen komisyonlar ve düzeltmeler" ekstresinde görünür. *Tür* sütunu *Elle* düzeltmeleri,
kademelerin kaydettiği *Kademe primi* satırlarından (bölüm 15) ayırır; bunlar burada görünür ama değiştirilemez.
Kapalı dönem etkinken kapalı aylar kaydedilmez.

### Temsilci fatura taslakları (seçenek)

![Temsilci fatura taslakları](../../_img/commissionmanagement/bozze.png)

*Düzeltmeler: altta ay için oluşturulan fatura taslakları, taslağa ve satıcıya bağlantıyla*

Temsilci komisyonları şirkete faturaladığında **Temsilci fatura taslakları** düğmesi belgeyi onun yerine hazırlar.
Seçilen ay için, bağlı bir **satıcısı** olan her yönetilen temsilci için (bölüm 6):

- tutar = **ay içinde ödenen** paylar (ödeme tarihine göre) + ayın **düzeltmeleri ve primleri**;
- pozitif tutar → *A/P Invoice* (**satınalma faturası**) taslağı; negatif → *A/P Credit Memo* (**satınalma
  alacak dekontu**) taslağı; sıfır → hiçbir şey;
- taslakta Yapılandırma'da belirtilen hesap üzerinde, seçilen KDV koduyla (veya satıcının varsayılanıyla) ve satır
  toplamı olarak tutarla bir hizmet satırı bulunur.

Örnek: Rossi (satıcı V20000), nisan: 05/04'te ödenen 22,05'lik taksit + +50,00 ve -20,00 düzeltmeler =
**52,05**'lik satınalma faturası taslağı. Sonunda bir mesaj temsilci temsilci özetler (taslak oluşturuldu, satıcı
yok, sıfır tutar, taslak zaten var). Ayın taslakları alttaki tabloda **durumla** (açık, kapalı yani faturaya
dönüştürülmüş, silinmiş), tarih ve kullanıcıyla yer alır; sarı ok taslağı veya satıcıyı açar. O ay için hâlâ
mevcut bir taslağı olan temsilci atlanır: yeniden oluşturmak için SAP'de taslağı silin. Taslak daha sonra SAP'den
diğer taslaklar gibi tamamlanır ve kaydedilir (temsilcinin faturasının numarası ve tarihi).

## 14. Komisyon ekstresi

![Komisyon ekstresi](../../_img/commissionmanagement/estratto.png)

*Nisan ayının "ödenen komisyonlar ve düzeltmeler" ekstresi, temsilciye göre gruplanmış*

Bir dönem ve bir temsilci veya tümü için, temsilciye göre gruplanmış (genişletmek ve daraltmak için oklar), altta
toplamı olan ve **CSV olarak dışa aktar** seçeneği bulunan (her temsilci için bir "Toplam" satırı, Excel'de
açılır) üç ekstre:

| Ekstre                          | Ne gösterir                                                                                  | Dönemin dayandığı tarih   |
|-----------------------------------|----------------------------------------------------------------------------------------------|----------------------|
| Hesaplanan komisyonlar             | belge ve hak sahibi başına bir satır: matrah, komisyon, ödenen                    | belge tarihi   |
| Ödenecek komisyonlar          | ödenmemiş (veya kısmen ödenmiş) ve kesinleşmemiş paylar                       | payın vade tarihi |
| Ödenen komisyonlar ve düzeltmeler | ödenen paylar artı dönemin aylarının düzeltmeleri: **temsilciye tanınacak tutardır** | ödeme tarihi |

### Yazdırma / PDF

![Yazdırılmış ekstre](../../_img/commissionmanagement/estratto_stampa.png)

*Tarayıcıda açılmış ekstre: temsilci başına bir blok, toplamlar ve gösterge stopaj*

**Yazdır / PDF** düğmesi gösterilen ekstreyi tarayıcıda sayfa düzeniyle açar: şirketi, ekstre türünü ve dönemi
gösteren başlık, her temsilci için satırları ve toplamıyla bir blok. Oradan yazdırılır veya PDF olarak kaydedilir
(Yazdır → "PDF olarak kaydet"). Yapılandırma'da **gösterge stopaj** belirtilmişse (örn. 8,5 "Enasarco quota
agente"), "ödenen komisyonlar ve düzeltmeler" ekstresi her temsilci için stopaj satırını ve **gösterge net** tutarı
da gösterir: bunlar temsilci için kolaylık sağlayan bilgilerdir, alt ve üst sınır yoktur.

### Temsilcilere gönder (seçenek)

E-postayla gönderim etkinken (Yapılandırma'nın E-posta sekmesi) **Temsilcilere gönder** düğmesi, gösterilen
ekstredeki her temsilciye ekinde HTML formatında **yalnızca kendi ekstresi** bulunan bir mesaj gönderir (her
tarayıcıda açılıp yazdırılabilir). Adres satış çalışanının adresidir veya bu yoksa bağlı satıcının adresidir. Sonunda
bir özet her temsilci için gönderimin başarılı olup olmadığını, adresin eksik olup olmadığını veya sunucunun hangi
hatayı verdiğini bildirir. Düğme yalnızca tüm temsilcilerin ekstresi üzerinde tam yetkisi olanlar için etkindir.

### Her sorumlu kendi temsilcilerini görür

Bir satış çalışanına bağlı olan (Temsilciler'deki *SAP kullanıcısı* sütunu) ve «Estratto di tutti gli agenti» (Tüm
temsilcilerin ekstresi) yetkisi olmayan bir SAP kullanıcısı açılır listede yalnızca *(temsilcilerim)* seçeneğini ve
kendisinin ve astlarının (bölge sorumlusu, alan sorumlusu veya müdürü olduğu satış çalışanları) adlarını bulur: bir
bölge sorumlusu diğerlerini görmeden kendi temsilcilerinin ekstresini görüntüleyebilir. Hiçbir satış çalışanına
bağlı olmayan biri, yetki olmadan hiçbir şey görmez.

## 15. Kademeler ve primler

![Kademeler ve primler](../../_img/commissionmanagement/scaglioni.png)

*Kademeler ve primler: üstte kademeler, altta yıl için hesaplanan primler*

"Primli yıllık satış kademeleri" seçeneğiyle (Yapılandırma'nın Temsilciler sekmesi) **Kademeler ve primler** menüsü
satışa bağlı yıl sonu primlerini yönetir. Bir **kademenin** şunları vardır: temsilci (veya *tümü*), yıl (veya *her
yıl*), yıllık matrah eşiği, prim türü (yılın *Yıllık satışın %'si* veya *Sabit tutar*), prim, açıklama, etkin.
Üstteki tabloda satır eklenir, değiştirilir ve silinir, sonra **Kademeleri kaydet** düğmesine basılır.

| Temsilci  | Yıl        | Eşik | Tür            | Prim | Açıklama       |
|---------|-------------|--------|-----------------|--------|-------------------|
| (tümü) | (her yıl) | 1.000  | Yıllık satışın %'si | 0,5    | Premio base       |
| (tümü) | (her yıl) | 10.000 | Yıllık satışın %'si | 1      | Premio 10.000     |
| Rossi   | 2026        | 12.000 | Sabit tutar   | 500,00 | Premio Rossi 2026 |

Bir yıl için **Primleri hesapla**: her temsilcinin satışı, hesaplanmış komisyonlarının matrahlarının toplamıdır
(tarihi yıl içinde olan faturalar ve alacak dekontları; kapanış faturalarına zaten dahil olan peşinat faturaları
hariç). Ulaşılan kademe, satışı aşmayan **en yüksek eşikli** kademedir; temsilcinin kademeleri herkes için olanlara,
belirli yıl da "her yıl"a göre önceliklidir. Prim = satış × % veya sabit tutar. Yukarıdaki kademelerle örnek: Rossi
13.150 → temsilcinin 12.000 kademesi → **500,00**; Bianchi 2.900 → 1.000 kademesi → %0,5 = **14,50**; Verdi 1.488 →
**7,44**. *Zaten kaydedildi* sütunu aynı yıl için zaten kaydedilmiş primi gösterir.

**İşaretli primleri kaydet**: işaretli satırlar seçilen ayda (normalde aralık) *Kademe primi* türünde düzeltmeler
olur: oradan diğer düzeltmeler gibi "ödenen komisyonlar ve düzeltmeler" ekstresine, fatura taslaklarına ve ayın
toplamlarına girer. Aynı yıl tekrar kaydedildiğinde mevcut prim değiştirilir (çoğaltılmaz); sıfır prim onu kaldırır.
Kapalı dönem etkinken kapalı aylara kayıt yapılmaz.

## 16. Kontroller ve başlangıç uyarıları

![Kontroller](../../_img/commissionmanagement/verifiche.png)

*Kontroller: dönemin sorunları, hatalar kırmızı*

**Kontroller** menüsü bir dönemde bir komisyonun eksik veya yanlış olmasına yol açabilecek her şeyi arar. Dönem
belirtilir, ödenmemiş tahsilatların da aranıp aranmayacağı seçilir (en yavaş aramadır) ve **Kontrol et** düğmesine
basılır: her sorunun bir önem derecesi (kırmızı **Hata**, **Uyarı**), onu bulan kontrol, temsilci, belge ve ne
yapılacağını içeren açıklama vardır. Çift tıklama belgeyi açar.

| Kontrol                | Ne bildirir                                                                                                                    | Ne yapılmalı                                       |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Hesaplanacak            | dönemin yönetilen temsilcili ve komisyonsuz faturaları, peşinatları ve alacak dekontları                                          | Komisyon hesaplama                             |
| Temsilci yok            | satış çalışanı olmayan veya rolü olmayan bir satış çalışanına sahip belgeler                                                               | istenip istenmediğini kontrol edin; Temsilciler'de rol verin |
| % olmayan satırlar | yönetilen temsilcili ve tüm satırlarının yüzdeleri sıfır olan belgeler                                                     | % kontrolü ve ataması veya eksik kurallar    |
| Temsilci değişti         | SAP'deki satış çalışanı komisyondaki kişiyle aynı olmayan hesaplanmış belgeler                                                    | Hesaplanan komisyonlar'da yeniden hesaplayın              |
| İptal edildi               | komisyonları hesaplanmış iptal edilmiş belgeler                                                                                   | Komisyonu sil                             |
| Temsilci hiyerarşisi        | rolü olmayan üst (onun kısmı tahakkuk etmez), üstü belirtilmemiş bir rolün varsayılan yüzdesi, mevcut olmayan SAP kullanıcısı | Temsilciler'de düzeltin                             |
| Çakışan kurallar      | dönemleri çakışan iki aynı etkin kural (aynı alanlar, iskonto ve satış çalışanı): yalnızca biri geçerlidir             | kuralları düzeltin                            |
| Ödenmemiş tahsilatlar   | taksiti Yapılandırma'da belirtilen günden daha uzun süre önce tahsil edilmiş ve ödenmemiş paylar                               | Ödeme                                    |

**Başlangıç uyarıları** seçeneğiyle, eklenti her başladığında hızlı kontrolleri çalıştırır (hesaplanacak son 90
günün belgeleri, son bir yıldaki değişen temsilci ve iptal edilmiş belgeler) ve bir şey bulursa bunu açılıştan
birkaç saniye sonra, yani olası lisans mesajlarından sonra durum çubuğunda bildirir: *"Komisyonlar: kontrol
edilecek 3 sorun (Komisyonlar \> Kontroller)"*. Sorun yoksa hiçbir şey yazmaz.

## 17. Yetkiler ve izlenebilirlik

Eklenti SAP'nin *General Authorizations* (Genel yetkiler) penceresinde (*Administration* › *System Initialization* ›
*Authorizations* (Yönetim › Sistem başlatma › Yetkiler)) *User Authorization* (Kullanıcı yetkisi) altında beş alt
öğeli **Provvigioni** (Komisyonlar) öğesini oluşturur. Süper kullanıcılar her zaman her şeye sahiptir; diğer
kullanıcılara her öğe için *No Authorization* (Yetki yok), *Read Only* (Yalnızca okuma) veya *Full Authorization*
(Tam yetki) atanır:

![Genel yetkiler](../../_img/commissionmanagement/autorizzazioni.png)

*Genel yetkiler: yetkisi olmayan bir kullanıcı için beş alt öğeli Provvigioni (Komisyonlar) öğesi*

| Yetki                          | Yalnızca okuma                                                              | Tam                                                                     |
|-----------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Configurazione (Yapılandırma)                          | –                                                                         | Yapılandırma'yı açmak ve kaydetmek                                           |
| Agenti, regole e scaglioni (Temsilciler, kurallar ve kademeler)              | görüntülemek                                                                | temsilcileri, kuralları ve kademeleri kaydetmek                                           |
| Controllo, calcolo e verifiche (Kontrol, hesaplama ve kontroller)          | Kontrol, Hesaplama, Hesaplanan komisyonlar, Kontroller'i görüntülemek           | %'leri uygulamak, hesaplamak, yeniden hesaplamak, payları kaydetmek, silmek             |
| Liquidazione, conguagli e bozze fatture (Ödeme, düzeltmeler ve fatura taslakları) | Ödeme ve Düzeltmeler'i görüntülemek                                       | ödemeleri onaylamak, düzeltmeleri kaydetmek, primleri kaydetmek, taslak oluşturmak |
| Estratto di tutti gli agenti (Tüm temsilcilerin ekstresi)            | tüm temsilcilerin ekstresini görmek (olmadan: yalnızca kendininkiler, bölüm 14) | e-postayla gönderim de                                                          |

Yetki olmadan menü öğesi durum çubuğunda *"İşleve izin verilmiyor: «…» yetkisi gerekir (Genel yetkiler \>
Provvigioni)"* yanıtını verir; yalnızca okuma yetkisiyle pencere açılır ama değişiklik yapan düğmeler *"İşleme izin
verilmiyor: «…» üzerinde tam yetki gerekir (Genel yetkiler \> Provvigioni)"* yanıtını verir.

**İzlenebilirlik**: komisyonların başlıkları ve payları son yazmanın kaynağını, kullanıcısını ve tarihini kaydeder
(bölüm 11); düzeltmeler değişikliğin kullanıcısını ve tarihini; fatura taslakları onları kimin ve ne zaman
oluşturduğunu. Eklentinin günlüğü (bölüm 19) hataları ve yapı güncellemelerini kaydeder.

## 18. Sık sorulan sorular ve sorunlar

Yüzdeler belgeye yazılmıyor  
Kontrol edin: Yapılandırma'daki seçeneği; belgenin rolü olan bir satış çalışanına sahip olduğunu; müşterinin dolu
olduğunu. Müşteri değiştirildikten sonra temsilciyi tekrar seçin.

Faturada bir yüzdeyi düzelttim ama SAP kaydetmeme izin vermiyor  
Kaydedilmiş faturalar değiştirilemez. % kontrolü ve ataması (hesaplamadan önce) veya Hesaplanan komisyonlar →
Değiştirilen %'lerle yeniden hesapla (sonra) kullanın.

"Komisyonlar zaten ödenmiş veya kesinleşmiş"  
Yeniden hesaplamak veya silmek için Hesaplanan komisyonlar'da payların ödenen tutarını sıfırlayın (Payları kaydet) ve
kesinleştirmeyi kaldırın. Paylar gerçekten temsilciye ödendiyse dokunmamak daha iyidir: farkı düzeltme olarak
kaydedin.

"Peşinat, komisyonları hesaplanmış bir faturadan zaten düşülmüş"  
Önce kapanış faturasının komisyonunu düzeltin veya silin, sonra peşinatı, sonra faturayı yeniden hesaplayın.

Bir pay ödemede önerilmiyor  
Taksit SAP'de kapalı değil (kısmi veya kaydedilmemiş ödeme), vade tarihi son tarihten sonra ya da pay zaten
ödenmiş/kesinleşmiş. İptal edilmiş belgelerin payları önerilmez: komisyonu silin.

İlk açılışta SAP tüm pencereleri kapatmak istiyor  
Kullanıcı alanları oluşturulurken bu normaldir: oluşturma bitene kadar (birkaç dakika) Yes (Evet) yanıtını verin.
Eklentinin bir güncellemesi alan eklediğinde de geçerlidir; istemci yarıda kapatılırsa oluşturma eklenti yeniden
başladığında devam eder.

"Dönem ... tarihine kadar kapalı"  
İşlem kapalı dönem içindeki bir tarihle ilgilidir (Yapılandırma, Ödeme sekmesi). Düzeltme gerçekten gerekliyse:
kilidin tarihini geriye alın, düzeltin, sonra geri koyun.

"İşleve izin verilmiyor"  
SAP kullanıcısının yetkisi yok (bölüm 17): Genel yetkiler'de, Provvigioni (Komisyonlar) öğesinde atayın.

Fatura kaydedildi ama durum çubuğu "Komisyonlar hesaplanmadı" diyor  
Otomatik hesaplama mümkün değildi (peşinat zaten düşülmüş, kapalı dönem, yönetilmeyen temsilci): belge normal
şekilde kaydedilmiştir; onu Komisyon hesaplama'dan hesaplayın (Kontroller onu "Hesaplanacak" arasında listeler).

E-posta gönderimi hata veriyor  
Yapılandırma'nın E-posta sekmesinde "Gönderimi dene" düğmesini kullanın: sunucunun mesajı sunucunun, portun, SSL'nin
veya kimlik bilgilerinin yanlış olup olmadığını söyler. "E-posta adresi olmayan" temsilciler satış çalışanının veya
bağlı satıcının kartında tamamlanmalıdır.

Belgenin bir satırı kuralların yüzdelerini almıyor  
"Elle değiştirilen yüzdeleri koru" seçeneğiyle satır elle olarak işaretlenmiştir (Provv. % manuali (Komisyon elle %)
sütunu): işareti kaldırıp kalemi, fiyatı veya iskontoyu değiştirin ya da elle düzeltin.

Eklenti işlem yaparken SAP yanıt vermiyor  
Kontrol et, Hesapla, İşle ve Uygula sırasında SAP eklentiyi bekler (durum çubuğu *"Please wait..."* (Lütfen
bekleyin...)): pencereyi kapatmayın ve eklentiyi sonlandırmayın, aksi halde istemci beklemede kalır ve yeniden
başlatılması gerekir.

## 19. Veriler ve teknik notlar

| Nerede                                                         | Ne                                                                                                                                                                                                |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (satış çalışanları)                                  | `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (SAP kullanıcısı) alanları                         |
| Pazarlama belgelerinin satırları (RDR1, INV1, RIN1, DPI1...) | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (yüzdeler), `_ScEff` (fiili iskonto), `_Man` (elle satır)                                                                                               |
| `@XEI_PRV_REGOLE`                                            | yüzde kuralları                                                                                                                                                                            |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`            | hesaplanan komisyonlar: belge ve hak sahibi başına başlık, satırlar, paylar (kod = tür-DocEntry-satış çalışanı\[-satır/taksit\], örn. `13-386-61-2`); kaynak, kullanıcı ve değişiklik tarihiyle başlıklar ve paylar |
| `@XEI_PRV_PERC`                                              | kaydedilmiş belgelerin satırları için Kontrol ile düzeltilen yüzdeler                                                                                                                             |
| `@XEI_PRV_CONG`                                              | düzeltmeler (tür M elle / P prim, primin referans yılı)                                                                                                                               |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                            | kademeler; oluşturulan fatura taslakları (temsilci, ay, taslak, satıcı, tutar)                                                                                                                         |
| `@XEI_SETTINGS` (XEI.CommissionManagement kapsamı)            | Yapılandırma seçenekleri (şifrelenmiş SMTP parolası) ve veri yapısının sürümü                                                                                                            |
| Yetkiler (OUPT)                                        | `XEI_PRV` ve alt öğeleri `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                             |

- Belge türleri: 13 fatura, 203 peşinat faturası, 14 alacak dekontu, 17 sipariş (yalnızca kontrolde).
- Her şey SAP'nin DI API'sinden geçer (veritabanına doğrudan bağlantı yok).
- Performans: belgelerde satırlar toplu olarak okunur (tek bir çağrı) ve yalnızca değişen hücreler yazılır;
  müşteriler, kalemler ve fiyat listeleri pencere başına bir kez okunur. Ödemede tahsilat tarihleri (en ağır arama)
  yalnızca gerçekten ödenebilir paylar için hesaplanır.
- Günlük: `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
