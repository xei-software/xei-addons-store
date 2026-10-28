---
title: XEI.ItemGenerator – Kurulum, lisans, menüler ve yetkiler
description: XEI.ItemGenerator'ın nasıl kurulacağı, lisansın nasıl etkinleştirileceği, menülerin nerede bulunacağı ve yetkilerin nasıl atanacağı.
lang: tr
prodotto: XEI.ItemGenerator
versione: 1.5.0
stato: approvato
---

# XEI.ItemGenerator – Kurulum, lisans, menüler ve yetkiler

Eklentinin menü, pencere ve alan adları, Türkçe SAP Business One'da göründükleri şekliyle verilmiştir.
SAP Business One'ın kendi menü ve alanlarının adları İngilizce olarak, yanlarında Türkçe karşılıklarıyla
verilmiştir.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Program dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |

## Kurulum

1. `XEI.ItemGenerator.zip` paketini indirin.
2. SAP Business One'da **Extension Manager**'ı açın, paketi içe aktarın ve şirkete atayın.
3. İlk başlatmada eklenti tabloları, alanları, nesneleri ve yetki girişlerini kendisi oluşturur.
4. İşlem tamamlandığında **SAP istemcisini bir kez yeniden başlatın**: baz ve varyant pencereleri
   eklentinin alanlarını SAP başlatılırken okur.

Eklentinin her güncellemesi aynı şekilde ve aynı yeniden başlatmayla kurulur.

## Lisans

Eklenti, XEI tarafından verilen bir **lisans kodu** ile çalışır.

- **Deneme**: denemeyi talep ettikten sonra e-posta ile, gönderimden itibaren 30 gün boyunca her
  şirkette geçerli bir **deneme kodu** alırsınız.
- **Satın alma**: **Licenza** (Lisans) penceresindeki iki kodu XEI'ye gönderir ve lisans kodunu
  alırsınız.

**Licenza** (Lisans) penceresi:

- Geçerli bir kod olmadan eklenti **kilitlidir**: menüsünde yalnızca *Informazioni* (Bilgi) ve
  *Licenza* (Lisans) kalır ve başlangıçta durumu ve nedeni gösteren **Licenza** penceresi
  kendiliğinden açılır.
- Pencere **şirket kodunu** ve **sunucu kodunu** gösterir: lisansı satın almak için bunları *Copia*
  (Kopyala) ile [license@xeisrl.com](mailto:license@xeisrl.com) adresine gönderin.
- Bir SAP **süper kullanıcısı**, alınan kodu *Inserisci un codice di licenza* (Lisans kodu girin) alanına
  yapıştırır ve *Salva codice* (Kodu kaydet) düğmesine basar: eklentinin kilidi, SAP yeniden
  başlatılmadan hemen açılır.
- Deneme kodu her şirkette geçerlidir. Lisans kodu, gönderilen kodların şirketi (veritabanı) veya
  sunucusu için geçerlidir.
- Aynı pencere istenildiği zaman *Licenza* (Lisans) menüsünden açılır: lisansın durumu, bitiş
  tarihi, numarası ve kapsamı.

![Eklenti kilitliyken Licenza penceresi](../../_img/itemgenerator/27_licenza.png)

*Eklenti kilitliyken Licenza (Lisans) penceresi: neden, şirket ve sunucu kodları, kod alanı.*

## Menüler

Girişler **Modules › Administration › Add-Ons › XEI-Addon › Code Configurator** (Modüller › Yönetim ›
Eklentiler › XEI-Addon › Kod Yapılandırıcı) altında ve aynı şekilde **Inventory › Item Management ›
Code Configurator** (Stok › Kalem yönetimi › Kod Yapılandırıcı) altında bulunur.

| Giriş | İşlev |
|---|---|
| 0. Ayarlar | eklentinin seçenekleri (kullanım kılavuzu, bölüm 3) |
| 1. Baz Tanımı | bazlar ve değerler: kod ağacı (bölüm 5) |
| 2. Varyantlar ve Seçenekler | varyantlar ve seçenekleri (bölüm 4) |
| 3. Varyant Yapıları | bir değer için sorulacak varyant grupları (bölüm 4) |
| 4. Kalemleri Oluştur | kalemlerin bileşimi ve oluşturulması (bölüm 9) |
| 5. Tutarlılık Kontrolü | oluşturulan kalemlerin bileşimlerinin yeniden hesaplanması (bölüm 14) |
| 6. Yapılandırmayı Kontrol Et | tüm yapılandırmanın kontrolü (bölüm 12) |
| 7. Excel İçe / Dışa Aktarma | yapılandırmanın bir Excel dosyasına aktarılması (bölüm 13) |
| Informazioni, Traduzioni, Licenza (Bilgi, Çeviriler, Lisans) | XEI eklentilerinde ortak girişler, İtalyanca görünür (yalnızca XEI-Addon altında); Licenza: lisansın durumu ve kodu |

Sağ tıklama ile ayrıca satış teklifi ve satış siparişi satırlarında **Kalemi yapılandır...** (bölüm 10) ve oluşturulmuş bir kalemin kalem ana verilerinde **Benzer kalemler oluştur...** (bölüm 11) bulunur.

## Yetkiler

**Administration › System Initialization › Authorizations › General Authorizations** (Yönetim › Sistem
başlatma › Yetkiler › Genel yetkiler) içinde eklenti **Configuratore codici XEI** (XEI Kod
Yapılandırıcı) dalını ekler. Her giriş için *Full Authorization* (Tam yetki), *Read-Only* (Salt
okunur) veya *No Authorization* (Yetki yok) atanabilir. Süper kullanıcıların her zaman tam erişimi
vardır.

![Genel yetkilerde yapılandırıcı dalı](../../_img/itemgenerator/23_autorizzazioni.png)

*Yetkisi olmayan bir kullanıcı için genel yetkilerde yapılandırıcı dalı.*

| Giriş | Tam | Salt okunur |
|---|---|---|
| Definizione basi (Baz tanımı) | bazları değiştirme | görüntüleme |
| Definizione varianti (Varyant tanımı) | varyantları değiştirme | görüntüleme |
| Strutture varianti (Varyant yapıları) | yapıları değiştirme | görüntüleme |
| Generazione articoli (Kalem oluşturma) | kalem oluşturma (teklif ve siparişlerden de) | listeyi oluşturmadan derleme |
| Configurazione, verifica, import/export (Ayarlar, kontrol, içe/dışa aktarma) | yapılandırmayı kaydetme, Excel'den içe aktarma, tutarlılık kontrolü | yapılandırmayı görüntüleme, kontrol etme, dışa aktarma |

Yetki yoksa menü girişi durum çubuğunda "Function not authorized" (İşlev yetkili değil) mesajını
gösterir.

## Destek

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com). Destek için:
[info@xeisrl.com](mailto:info@xeisrl.com). Talebinizde eklentinin sürümünü (*Informazioni* (Bilgi)
menüsü) ve sorunun bir açıklamasını belirtin.
