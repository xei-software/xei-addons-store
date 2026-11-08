---
title: XEI.ContoLavoro – Fason üretim
description: Fasonculara verilen işleri SAP Business One'da, siparişten ve bileşenlerin gönderilmesinden mamulün geri gelmesine kadar yönetir.
lang: tr
prodotto: XEI.ContoLavoro
versione: 1.2.1
stato: approvato
---

# XEI.ContoLavoro

**SAP Business One'da fason üretim.** Her iş için bir fason iş emri; fasoncuya verilen siparişi, gönderilen
bileşenleri, geri dönüşleri ve mamulün girişini bir arada tutar, durum her zaman günceldir.

## Tanım

Fason üretimi elle takip etmek, satınalma siparişlerini, nakilleri ve girişleri uyumlu tutmak ve her an hangi
fasoncuda ne bulunduğunu bilmek demektir. XEI.ContoLavoro ile bunu SAP Business One yapar:

- her iş için, elde edilecek ürünler ve bunların ürün ağacıyla bir **fason iş emri** açılır: gönderilecek bileşenler
  ve ödenecek işçilikler;
- **fasoncuya verilen satınalma siparişi** fason iş emrinden oluşur ve her değişiklikte uyumlu kalır;
- **bileşenler** fire ve geri dönüşlerle birlikte fasoncunun deposuna gönderilir;
- **üretim girişi**, ürünün ve işçiliklerin girişini ve tüketilen bileşenlerin çıkışını tek bir işlemde kaydeder;
- fason iş emri her an neyin gönderildiğini, neyin kullanıldığını, fasoncuda neyin kaldığını ve neyin eksik olduğunu
  gösterir ve tamamlandığında kendiliğinden kapanır.

## Başlıca işlevler

- Ürünler, Ürün ağacı, Bileşenler ve Belgeler sekmeli **fason iş emri**: bağlı tüm SAP belgeleri gruplanmış ve
  açılmaya hazır.
- **Üretim siparişlerinden fason üretim**: bir üretim siparişinin dış aşamaları fason iş emri olur, bileşenler her
  geri dönüşte çekilir ve tüm işçilikler geri geldiğinde mamul depoya girer.
- Fasoncudaki fason iş emri partilerinden ve son kullanma tarihine göre önerilen, elle değiştirilebilen **partiler ve
  seri numaraları**; giren ürünün partisi yapılandırılabilir bir betikle hesaplanır.
- Fasoncu ve ürün bazında **işçilik fiyatlarıyla**, her kayıtta yeniden hesaplanan ürün **maliyetleri**.
- Bileşenlerin **toplu nakli**, aynı fasoncudaki **iş emirleri arasında nakil** ve mal girişlerinin **toplu
  kapatılması**.

## Gereksinimler

| | |
|---|---|
| SAP Business One | 10.0 veya üzeri |
| Veritabanı | Microsoft SQL Server veya SAP HANA (SAP HANA'da kurulum sırasında bir test yapılması önerilir) |
| Programın dilleri | İtalyanca, İngilizce, Almanca, Fransızca, İspanyolca, Türkçe |
| Sistem | SAP istemcisinin bulunduğu bilgisayarda Microsoft .NET Framework 4.8 |
| Kurulum | SAP Business One Extension Manager |
| Lisans | **Licenza** (Lisans) menüsüne girilen XEI lisans kodu (30 gün ücretsiz deneme) |

## Güncel sürüm

**1.2.1** – [sürüm notlarına](../../manuali/tr/contolavoro/note-rilascio-1.2.1.md) ve kullanım kılavuzuna bakın.
