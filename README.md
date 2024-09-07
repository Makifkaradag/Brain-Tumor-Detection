# Brain-tumor-detection

# Beyin Tümörü Tespiti Projesi

Bu proje, YOLOv8 kullanarak MRI görüntülerinde beyin tümörlerini tespit etmektedir. YOLOv8 modeli ile eğitilmiş bir ağırlık dosyası kullanarak, model beyin tümörlerini tespit etmek için tahminler yapacaktır.

```markdown

Projeyi çalıştırmak içn aşağıdaki adımlar izlemelidir:

1. Gerekli Yazılımlar
Projeyi çalıştırmadan önce, aşağıdaki yazılımların kurulu olduğundan emin olun:

- **Python 3.7 veya üstü**: [Python.org](https://www.python.org/downloads/)
- **Git** (Opsiyonel, projeyi klonlamak için): [Git](https://git-scm.com/downloads)

2. Projeyi Klonlama
Projeyi GitHub'dan klonlayabilirsiniz. Terminal veya komut satırında aşağıdaki komutu kullanarak projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/kullaniciadi/brain_tumor_detection.git
```

Eğer Git kullanmak istemiyorsanız, projeyi GitHub sayfasından zip olarak indirip çıkartabilirsiniz.



### 3. Gerekli Python Kütüphanelerini Yükleme
Projede kullanılan kütüphaneleri yüklemek için, proje dizininde aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

Bu komut, projede kullanılan `ultralytics`, `torch`, `opencv-python` ve diğer gerekli kütüphaneleri kuracaktır.



### 4. Modeli İndirme
Eğitilmiş YOLOv8 modelini aşağıdaki bağlantıdan indirin:

[Modeli İndir](https://drive.google.com/file/d/1oTTmtZhmyZ57elhTb_8t5K_qIj-vKSbi/view?usp=sharing)

İndirdiğiniz **weight.pt** dosyasını proje dizinine kopyalayın. Dosya yapısı şu şekilde olmalıdır:

```
brain_tumor_detection/
│
├── main.py
├── plate.pt  # Model dosyasını buraya yerleştirin
├── requirements.txt
├── README.md
└── diğer dosyalar...
```


### 5. Projeyi Çalıştırma
Projeyi çalıştırmak için terminal veya komut satırında proje dizinine gidin ve aşağıdaki komutu çalıştırın:

```bash
python main.py
```





### 6. Sonuçları Görüntüleme
Model tarafından işlenen görüntüler ve tahmin sonuçları, `runs/detect/predict` klasörüne kaydedilecektir.

---

