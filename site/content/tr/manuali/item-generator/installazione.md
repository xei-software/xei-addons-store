---
title: XEI.ItemGenerator – Kurulum, lisans, menüler ve yetkiler
description: XEI.ItemGenerator'ın nasıl kurulacağı, lisansın nasıl etkinleştirileceği, menülerin nerede bulunacağı ve yetkilerin nasıl atanacağı.
lang: tr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Kurulum, lisans, menüler ve yetkiler

Programın arayüzü henüz Türkçe değildir: menü, pencere ve alan adları ekranda göründükleri şekliyle İngilizce verilmiş, yanlarına Türkçe karşılıkları eklenmiştir.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server (SAP HANA henüz desteklenmemektedir) |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Program dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca |

## Kurulum

1. `XEI.ItemGenerator.zip` paketini indirin.
2. SAP Business One'da **Extension Manager**'ı açın, paketi içe aktarın ve şirkete atayın.
3. İlk başlatmada eklenti tabloları, alanları, nesneleri ve yetki girişlerini kendisi oluşturur.
4. İşlem tamamlandığında **SAP istemcisini bir kez yeniden başlatın**: taban ve varyant pencereleri
   eklentinin alanlarını SAP başlatılırken okur.

Eklentinin her güncellemesi aynı şekilde ve aynı yeniden başlatmayla kurulur.

## Lisans

Eklenti, XEI tarafından verilen bir **lisans kodu** ile çalışır. Kayıt olduktan sonra e-posta ile
30 gün geçerli bir deneme kodu alırsınız.

- Geçerli bir kod olmadan eklenti **kilitlidir**: menüsünde yalnızca *Information* (Bilgi) ve
  *License* (Lisans) kalır ve başlangıçta durumu ve nedeni gösteren **License** (Lisans) penceresi
  kendiliğinden açılır.
- Pencere **şirket kodunu** ve **sunucu kodunu** gösterir: lisans kodunu almak için bunları *Copy*
  (Kopyala) ile [license@xeisrl.com](mailto:license@xeisrl.com) adresine gönderin.
- Bir SAP **süper kullanıcısı**, alınan kodu *Enter a license code* (Lisans kodu girin) alanına
  yapıştırır ve *Save code* (Kodu kaydet) düğmesine basar: eklentinin kilidi, SAP yeniden
  başlatılmadan hemen açılır.
- Kod, yapıştırıldığı şirket (veritabanı) için geçerlidir: her şirket için ayrı bir kod gerekir.
- Aynı pencere istenildiği zaman *License* (Lisans) menüsünden açılır: lisansın durumu, bitiş
  tarihi, numarası ve kapsamı.

![Eklenti kilitliyken License penceresi](../../_img/itemgenerator/27_licenza.png)

*Eklenti kilitliyken License (Lisans) penceresi: neden, şirket ve sunucu kodları, kod alanı.*

## Menüler

Girişler **Modules › Administration › Add-Ons › XEI-Addon › Code Configurator** (Modüller › Yönetim ›
Eklentiler › XEI-Addon › Kod Yapılandırıcı) altında ve aynı şekilde **Inventory › Item Management ›
Code Configurator** (Stok › Kalem yönetimi › Kod Yapılandırıcı) altında bulunur.

| Giriş | İşlev |
|---|---|
| 0. Settings (Ayarlar) | eklentinin seçenekleri (kullanım kılavuzu, bölüm 3) |
| 1. Base Definition (Taban Tanımı) | tabanlar ve değerler: kod ağacı (bölüm 5) |
| 2. Variants and Options (Varyantlar ve Seçenekler) | varyantlar ve seçenekleri (bölüm 4) |
| 3. Variant Structures (Varyant Yapıları) | bir değer için sorulacak varyant grupları (bölüm 4) |
| 4. Generate Items (Kalemleri Oluştur) | kalemlerin bileşimi ve oluşturulması (bölüm 9) |
| 5. Consistency Check (Tutarlılık Kontrolü) | oluşturulan kalemlerin bileşimlerinin yeniden hesaplanması (bölüm 14) |
| 6. Check Configuration (Yapılandırmayı Kontrol Et) | tüm yapılandırmanın kontrolü (bölüm 12) |
| 7. Excel Import / Export (Excel İçe / Dışa Aktarma) | yapılandırmanın bir Excel dosyasına aktarılması (bölüm 13) |
| Information, Translations, License (Bilgi, Çeviriler, Lisans) | XEI eklentilerinde ortak girişler (yalnızca XEI-Addon altında); License: lisansın durumu ve kodu |

Sağ tıklama ile ayrıca satış teklifi ve satış siparişi satırlarında **Configure Item...** (Kalemi
Yapılandır...) (bölüm 10) ve oluşturulmuş bir kalemin kalem ana verilerinde **Generate Similar
Items...** (Benzer Kalemler Oluştur...) (bölüm 11) bulunur.

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
| Definizione basi (Taban tanımı) | tabanları değiştirme | görüntüleme |
| Definizione varianti (Varyant tanımı) | varyantları değiştirme | görüntüleme |
| Strutture varianti (Varyant yapıları) | yapıları değiştirme | görüntüleme |
| Generazione articoli (Kalem oluşturma) | kalem oluşturma (teklif ve siparişlerden de) | listeyi oluşturmadan derleme |
| Configurazione, verifica, import/export (Ayarlar, kontrol, içe/dışa aktarma) | yapılandırmayı kaydetme, Excel'den içe aktarma, tutarlılık kontrolü | yapılandırmayı görüntüleme, kontrol etme, dışa aktarma |

Yetki yoksa menü girişi durum çubuğunda "Function not authorized" (İşlev yetkili değil) mesajını
gösterir.

## Destek

Lisanslar için: [license@xeisrl.com](mailto:license@xeisrl.com). Destek için:
[info@xeisrl.com](mailto:info@xeisrl.com). Talebinizde eklentinin sürümünü (*Information* (Bilgi)
menüsü) ve sorunun bir açıklamasını belirtin.
