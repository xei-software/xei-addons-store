---
title: XEI.CommissionManagement – Temsilci komisyonları
description: SAP Business One'da temsilcilerin, bölge sorumlularının, alan sorumlularının ve direktörlerin komisyonlarını kurallardan her temsilcinin dökümüne kadar hesaplar ve öder.
lang: tr
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement

**SAP Business One'da satış temsilcisi komisyonları.** Yüzdeler belge satırlarına kendiliğinden gelir; eklenti
komisyonları hesaplar, müşteriler ödedikçe öder ve her temsilcinin dökümünü hazırlar.

## Tanım

Komisyonları elle veya hesap tablolarında hesaplamak, her ay faturaları, tahsilatları ve temsilcilerle yapılan
anlaşmaları yeniden gözden geçirmek demektir; hata riski vardır ve dökümler ERP'deki verilerle uyuşmayabilir.

XEI.CommissionManagement ile her şey SAP Business One'da kalır:

- her fatura satırı en fazla **dört yüzde** taşır: temsilci, bölge sorumlusu, alan sorumlusu ve direktör;
- yüzdeler müşteri, müşteri grubu, kalem, kalem grubu, fiyat listesi, dönem ve iskontoya göre **kurallardan** ya da
  temsilcinin varsayılan yüzdelerinden gelir ve elle düzeltilebilir;
- komisyon **faturada** hak edilen bir paya ve **tahsilatta** hak edilen paylara bölünür; taksit taksit ya da belge
  toplamı üzerinden;
- **ödeme**, tahsil edilen payları önerir ve yeniden ödenmemiş duruma düşen taksitlerin paylarını ters kaydeder;
- her temsilcinin **dökümü** CSV olarak dışa aktarılır, PDF olarak yazdırılır veya e-posta ile gönderilir.

## Başlıca işlevler

- **Temsilciler ve hiyerarşi**: her satış çalışanı için rol, bölge sorumlusu, alan sorumlusu, direktör, varsayılan
  yüzdeler, faturadaki pay ve ödeme türü.
- Ayarlanabilir arama sırası, asgari iskonto ve geçerlilik dönemi olan, CSV olarak dışa ve içe aktarılabilen
  **yüzde kuralları**.
- Belge doldurulurken **satış belgelerinde yüzdeler**; kaydederken tahmini komisyon ve elle düzeltilen satırların
  korunması.
- **% kontrolü ve atanması**: belgelerin yüzdelerini kurallarla karşılaştırır ve toplu olarak düzeltir.
- Satış faturaları, peşinat faturaları ve alacak dekontları üzerinde **hesaplama**; fatura kaydedilirken otomatik
  olarak da.
- Tahsil edilen payların **ödenmesi**; kısmi tahsilatlarla orantılı olarak da, kapalı dönemle.
- **Düzeltmeler**, yıllık ciro üzerinden **kademeler ve primler** ve temsilcilerin **taslak faturaları**.
- Anormallik **kontrolleri** ve SAP Genel yetkilerinde eklentiye özel **yetkiler**.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| E-posta | erişilebilir bir SMTP posta sunucusu; yalnızca dökümleri temsilcilere e-posta ile göndermek için (Yapılandırma › E-posta) |
| Kurulum | SAP Business One Extension Manager |
| Lisans | eklentinin **Licenza** (Lisans) menüsüne girilen XEI lisans kodu (30 gün ücretsiz deneme) |

## Güncel sürüm

**1.1.1** – [sürüm notlarına](../../manuali/tr/commissionmanagement/note-rilascio-1.1.1.md) ve
[kullanım kılavuzuna](../../manuali/tr/commissionmanagement/manuale-utente.md) bakın.
