---
title: XEI.ContoLavoro 1.2.0 – Sürüm notları
description: SAP Business One için XEI.ContoLavoro 1.2.0'ın işlevleri ve düzeltmeleri.
lang: tr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Sürüm notları

## Bu sürümün işlevleri

- «Üretim siparişlerinden iş emri oluştur» listesinde, «Hazır olmayan satırları da göster» onay kutusuyla, fason iş emrine dönüşemeyen işçilikler de, nedeni ve yapılması gerekenle birlikte «Neden / uyarılar» sütununda görünür.
- Bir ürün ağacını kaydettiğinizde, bir uyarı «Lavorazione terzista» (Fasoncu işçiliği) alanında düzeltilmesi gereken
  kodları bildirir: kaynaklar, kalem olmayan kodlar, «Conto lavoro» (Fason üretim) işareti olmayan kalemler, ürün
  ağacının satırı olmayan işçilikler, geriye dönük çekilen bileşenler.
- Eklentinin menüsünde **Licenza** (Lisans) penceresiyle XEI lisansı: durum, şirket ve sunucu kodları, kodun
  girilmesi; 30 gün ücretsiz deneme.

## Bu sürümün düzeltmeleri

- Kesintiye uğrayan bir fason iş emri, üretim siparişinin aynı satırından başka bir fason iş emri oluşturulmasını
  engellemez.
- Bir dış işçiliğe bağlı geriye dönük çekilen bileşenler fasoncuya gönderilmez ve üretim siparişi bunları yalnızca bir
  kez çeker.
- Fason iş emrinin numaralandırma serisi yoksa, *Fason iş emri* açılırken eklenti serinin nerede tanımlanacağını bildirir.
- Bileşenlerin toplu nakli varsayılan yapılandırmada etkindir; seçenek kapalıyken menü girişi işlevin devre dışı olduğunu bildirir.
- Üretim siparişlerinden oluşturulan fason iş emirleri, iş emirlerinin varsayılan fiyat listesini kullanır (Yapılandırma › Genel): liste yoksa «İş emri oluştur» listenin girilmesini ister.
- «Üretim siparişlerinden iş emri oluştur» listesinde satırlar seçilir ve tedarikçi değiştirilir.
