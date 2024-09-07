# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:51:44 2024

@author: akif
"""
from ultralytics import YOLO


model = YOLO("weight.pt")  # Model dosyasının yolunu doğru şekilde belirtin

# Tahmin yapılacak resmi yükleyin
image_path = "tumor.jpg"


results = model.predict(image_path, save=True)


for result in results:
    
    print(result.boxes.xyxy)  
    print(result.boxes.conf)  
    print(result.boxes.cls)   


print(f"Sonuçlar kaydedildi: {results[0].save_dir}")
