---
title: XEI.ItemGenerator – Kalem kodu yapılandırıcı
description: SAP Business One'da kod, tanımlar, veriler, fiyat ve ürün ağacı sizin belirlediğiniz kurallarla oluşturulan kalemler yaratın.
lang: tr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator

**SAP Business One için kalem kodu yapılandırıcı.** Ürünün özelliklerini seçin;
eklenti kalemi kalem ana verilerinde kodu, tanımları, verileri, fiyatı ve ürün ağacı
hazır olarak oluşturur.

## Tanım

Ürünlerini çok sayıda kombinasyonda (ölçü, yüzey, renk, aksesuar) satan firmalar her
kombinasyon için elle bir kalem açarak zaman kaybeder ve aynı ürün için farklı kodlar ve
tanımlar oluşması riskiyle karşılaşır.

XEI.ItemGenerator ile kuralları bir kez tanımlarsınız, eklenti kalemleri oluşturur:

- **kod**, düzey düzey seçilen değerlerden oluşur (örneğin `PE` üst dolap → `MU` duvara
  monte → `070` yükseklik 70 cm = `PEMU070`); buna varyantları ayıran bir sıra numarası
  eklenir;
- **varyantların** (örneğin renk veya yüzey) kendi seçenekleri vardır ve bunlar önceki
  düzeylerden devralınabilir;
- kalemin **tanımları, grupları, ölçü birimleri, özellikleri, ölçüleri, ağırlığı ve
  fiyatı** seçilen değerlerden ve seçeneklerden elde edilir;
- **ürün ağacı**, her değerin ve seçeneğin bileşenleriyle oluşturulur.

Bir kombinasyon zaten varsa eklenti yeni bir kopya açmak yerine mevcut kalemi bulur.

## Başlıca işlevler

- Eklentinin SAP'deki ana verileriyle **taban, varyant ve yapı tanımı**.
- Kod ağacı ve varyant ağacı bulunan, boyutu değiştirilebilir bir pencerede **kalem
  oluşturma**; pencere açıkken SAP kullanılmaya devam eder.
- **Satış tekliflerinden ve satış siparişlerinden kalem yapılandırma**: belge satırında
  sağ tıklayın, kalemi oluşturun ve satıra ekleyin.
- Daha önce oluşturulmuş bir kalemin ana verilerinden **benzer kalemler oluşturma**: bir
  seçeneği değiştirmek yeterlidir.
- Tanım, genişletilmiş tanım ve yabancı dildeki adı oluşturmak için **tanım formülü**.
- Hata listesi ve düzeltilecek veriyi doğrudan açma olanağıyla **yapılandırma kontrolü**.
- Yapılandırmanın **Excel ile içe ve dışa aktarılması**; başka bir şirkete kopyalamak
  için de kullanılabilir.
- SAP Genel yetkiler içinde özel **yetkiler**.
- Kalem ana verilerinde kalemin **resim küçük görüntüsü**.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Kurulum | SAP Business One Extension Manager |
| Lisans | eklentinin **License** (Lisans) menüsüne girilen XEI lisans kodu (30 gün ücretsiz deneme) |

## Güncel sürüm

**1.4.0** – [sürüm notlarına](../../manuali/tr/itemgenerator/note-rilascio-1.4.0.md) bakın.
