---
title: XEI.ItemGenerator 1.4.0 – Sürüm notları
lang: tr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Sürüm notları

Programın arayüzü henüz Türkçe değildir: menü ve alan adları, ekranda göründükleri
şekliyle İngilizce verilmiş, yanlarına Türkçe karşılıkları eklenmiştir.

## Bu sürümün işlevleri

- **Öneri olarak varyant devralma.** *Inherit variants* (Varyantları devral) ile önceki bir düzeyde seçilen seçenekler
  önerilir ve bunları devralan düzeyde değiştirilebilir. Sağ tık menüsü **Back to the proposed options** (Önerilen
  seçeneklere dön) komutunu sunar.
- **Devralmayı zorlama.** Taban değerlerinde *Force inheritance* (Devralmayı zorla) seçeneği: önceki düzeyin seçimini
  zorunlu kılar; bu seçim değer üzerinde değiştirilemez.
- **Varyantlarda kullanıcı tablosu ve kullanıcı alanı.** *Variants and Options* (Varyantlar ve Seçenekler) içinde bir
  kullanıcı tablosu ve bir kalem kullanıcı alanı belirtilir: kalemler oluşturulurken seçilen seçenekler tabloya eklenir
  ve alana yazılır.
- **Generate Items (Kalemleri Oluştur).** Varyant bölmesi ağaçta seçili değerin varyantlarını gösterir; bir onay kutusu
  düzeye göre tam görünümü açar.
- **Oluşturulacak kalemler listesi.** *Add to list clears the list of items to generate first* (Listeye ekle, önce
  listeyi temizler; varsayılan olarak açık) ayarıyla liste yalnızca son seçimi içerir; ayar kapalıyken kalemler birikir.
- **Numaralı menüler.** Code Configurator (Kod Yapılandırıcı) menü öğeleri çalışma sırasına göre 0'dan 7'ye
  numaralandırılmıştır: Settings (Ayarlar), Base Definition (Taban Tanımı), Variants and Options (Varyantlar ve
  Seçenekler), Variant Structures (Varyant Yapıları), Generate Items (Kalemleri Oluştur), Consistency Check (Tutarlılık
  Kontrolü), Check Configuration (Yapılandırmayı Kontrol Et), Excel Import / Export (Excel İçe / Dışa Aktarma).
- **Seçim listeli alt düzey.** *Base Definition* (Taban Tanımı) içinde Sub-level (Alt düzey) sütunu tabanların seçim
  listesinden doldurulur ve ok bağlı tabanı açar. Elle yazılan ve taban olmayan bir kod reddedilir.
- **Yapılandırma kontrolü ve Excel**, devralmayı ve varyantların kullanıcı tablolarını ve alanlarını kapsar.
- SAP Business One stiline uygun, derli toplu başlıklara sahip **pencereler**.
- **Programın dilleri**: İtalyanca, İngilizce, Almanca, Fransızca ve İspanyolca.

## Kurulum

- Pakete dahil olan XEICore 1.1.1 gerektirir.
- İlk açılışta eklenti veri yapısını kendiliğinden hazırlar.
