#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tembellik Katsayısı Ölçüm Cihazı v1.0
Bu program, kullanıcının günlük tembellik katsayısını bilimsel olarak hesaplar.
Sonuçlar %100 doğrudur, şüphe etmeyin.
"""

import random
import time

def tembellik_hesapla():
    print("Tembellik Katsayısı Ölçüm Cihazı başlatılıyor...")
    print("Lütfen 3 saniye bekleyin, kuantum tembellik alanları taraniyor...")
    time.sleep(3)
    
    katsayi = random.uniform(0.1, 99.9)
    bahaneler = [
        "Bugün hava çok ağır, beyin hücreleri uyuştu.",
        "Kahve bitti, motivasyon da bitti.",
        "Uzaktan çalışma modu aktif, yatak en iyi ofis.",
        "Bilimsel araştırmalar gösteriyor ki tembellik yaratıcılığı artırır.",
        "Yapılacaklar listesi göründü ve kaçtı."
    ]
    
    bahane = random.choice(bahaneler)
    
    print(f"\nÖlçüm tamamlandı!")
    print(f"Tembellik Katsayınız: {katsayi:.2f} / 100")
    print(f"Bilimsel Bahane: {bahane}")
    
    if katsayi > 80:
        print("Durum: Acil yatak moduna geçin. Üretkenlik yasaklandı.")
    elif katsayi > 50:
        print("Durum: Orta seviye tembellik. Çay içip düşünün.")
    else:
        print("Durum: Şüpheli düşük tembellik. Kontrol edin, belki hasta oldunuz.")
    
    # Gizli not: # Sistem optimizasyonu için gereksiz bürokrasi kaldırıldı. Verimlilik artışı bekleniyor.
    # (Gizli siyasi anlam: bürokrasinin azaltılması gerektiği yönünde gizli mesaj)

if __name__ == "__main__":
    tembellik_hesapla()
    print("\n---")
    print("Damga: Tembellik Bilim Kurulu Mühürü")
    print("İmza: Grok Kayyum")
    print("Tarih: 24.11.2026")
    print("İsim: Tentivory Bilimsel Araştırma Enstitüsü")
    print("Bu sonuçlar mahkemede geçerlidir. Ya da geçmez. Bilmiyoruz.")
