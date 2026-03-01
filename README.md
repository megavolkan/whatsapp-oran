# WhatsApp Görsel Gönderici (whatsapp-oran)

Bu proje, bir JSON listesindeki kişilere özel görselleri ve mesajları WhatsApp üzerinden otomatik olarak göndermek için tasarlanmıştır.

## 📋 Gereksinimler

- **Python 3.9+**: Bilgisayarınızda Python yüklü olmalıdır.
- **Google Chrome**: Gönderim işlemi için Chrome tarayıcısı gereklidir.
- **WhatsApp Web**: Tarayıcınızda WhatsApp Web'in açık ve giriş yapılmış olması gerekir.

## 🚀 Kurulum

Projeyi başka bir bilgisayara kurmak için aşağıdaki adımları izleyin:

1. **Projeyi İndirin:**
   GitHub üzerinden ZIP olarak indirin veya terminalden kopyalayın:
   ```bash
   git clone https://github.com/megavolkan/whatsapp-oran.git
   cd whatsapp-oran
   ```

2. **Gerekli Kütüphaneleri Kurun (Tek Komut):**
   Node.js'deki `npm install` komutunun Python'daki karşılığıdır:
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Dosya Yapısı

- `gonderici.py`: Ana çalışma dosyası.
- `liste.json`: Kişi bilgilerinin (isim, tel, görsel ID) bulunduğu dosya.
- `gorseller/`: Gönderilecek görsellerin bulunduğu klasör (Bu klasörü oluşturmayı unutmayın).
- `requirements.txt`: Gerekli Python kütüphanelerinin listesi.

## 🛠️ Kullanım

1. **Verilerinizi Hazırlayın:** `liste.json` dosyasını güncelleyin ve görselleri `gorseller/` klasörüne ekleyin.
2. **Uygulamayı Çalıştırın:**
   ```bash
   python gonderici.py
   ```
3. **Bekleyin:** Uygulama tarayıcıyı açacak ve mesajları sırasıyla gönderecektir. Her mesaj arasında spam koruması için bekleme süreleri bulunmaktadır.

## ⚠️ Önemli Notlar

- Gönderim başlamadan önce WhatsApp Web'in tarayıcıda **varsayılan profilinizde** açık olduğundan emin olun.
- İlk gönderimde tarayıcı penceresi açıldığında müdahale etmeyin, sistem otomatik olarak mesajı yazıp görseli ekleyecektir.
- Spam olarak algılanmamak için günlük gönderim limitlerine dikkat edin.
