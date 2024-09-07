# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:51:44 2024

@author: akif
"""
from ultralytics import YOLO

# Eğitilmiş modelinizi yükleyin
model = YOLO("weight.pt")  # Model dosyasının yolunu doğru şekilde belirtin

# Tahmin yapılacak resmi yükleyin
image_path = "tumor.jpg"

# Nesne tespiti yap
results = model.predict(image_path, save=True)

# Her bir sonucu liste içinde döndürdüğü için döngü ile tespitleri gezelim
for result in results:
    # Her bir tespit edilen nesnenin detaylarını yazdıralım
    print(result.boxes.xyxy)  # Bounding box koordinatları
    print(result.boxes.conf)  # Konfidans skorları
    print(result.boxes.cls)   # Sınıf etiketleri (örneğin tümör)

# Sonuçlar kaydedildiği için yolunu da gösterebiliriz
print(f"Sonuçlar kaydedildi: {results[0].save_dir}")
