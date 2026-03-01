# WhatsApp Görsel Gönderici (whatsapp-oran)

Bu proje, bir JSON listesindeki kişilere özel görselleri ve mesajları WhatsApp üzerinden otomatik olarak göndermek için tasarlanmıştır.

## 📋 Gereksinimler

- **Python 3.9+**: Bilgisayarınızda Python yüklü olmalıdır.
- **Google Chrome**: Gönderim işlemi için Chrome tarayıcısı gereklidir.
- **WhatsApp Web**: Tarayıcınızda WhatsApp Web'in açık ve giriş yapılmış olması gerekir.

## 🚀 Kurulum ve Hazırlık

### 1. Python Yükleme
- **Windows:** [python.org](https://www.python.org/downloads/) adresinden indirin. Yüklerken **"Add Python to PATH"** kutucuğunu mutlaka işaretleyin.
- **Mac/Linux:** Genellikle yüklü gelir. Kontrol için terminale `python3 --version` yazın.

### 2. Projeyi İndirme
Projeyi GitHub'dan ZIP olarak indirin ve klasöre çıkarın veya terminalden çekin:
```bash
git clone https://github.com/megavolkan/whatsapp-oran.git
cd whatsapp-oran
```

### 3. Bağımlılıkları Kurma (npm install gibi)
Terminali (veya CMD) proje klasöründe açın ve şu komutu çalıştırın:
- **Windows:** `pip install -r requirements.txt`
- **Mac/Linux:** `pip3 install -r requirements.txt`

## 🛠️ Kullanım

1. **Verileri Hazırlayın:** `liste.json` dosyasını güncelleyin ve gönderilecek görselleri `gorseller/` klasörüne ekleyin.
2. **Uygulamayı Çalıştırın:**
   - **Windows:** `python gonderici.py`
   - **Mac/Linux:** `python3 gonderici.py`
3. **Süreci İzleyin:** Uygulama tarayıcıyı açacak ve mesajları sırasıyla gönderecektir.

## ⚠️ Önemli Notlar ve İpuçları

- **WhatsApp Web:** Tarayıcınızda (Chrome) WhatsApp Web'in **varsayılan profilinizde** açık ve giriş yapılmış olduğundan emin olun.
- **Müdahale Etmeyin:** İlk gönderimde tarayıcı penceresi açıldığında fareye veya klavyeye dokunmayın; sistem otomatik olarak mesajı yazıp görseli ekleyecektir.
- **Bekleme Süreleri:** Spam filtresine takılmamak için her mesaj arasında 30 saniyelik bir bekleme süresi ayarlanmıştır (`gonderici.py` içinden değiştirilebilir).
- **Hata Alırsanız:** Windows'ta `python` komutu çalışmazsa `py gonderici.py` komutunu deneyebilirsiniz.
