import json
import os
import time

import pywhatkit as kit

# Ayarlar
JSON_DOSYASI = "liste.json"
GORSEL_KLASORU = "gorseller"  # Görsellerin olduğu klasör yolu


def mesajlari_gonder():
    # JSON dosyasını oku
    try:
        with open(JSON_DOSYASI, "r", encoding="utf-8") as f:
            kullanicilar = json.load(f)
    except Exception as e:
        print(f"Hata: JSON dosyası okunamadı: {e}")
        return

    print(
        f"Toplam {len(kullanicilar)} kişi işlenecek. Lütfen WhatsApp Web'in tarayıcıda açık olduğundan emin olun."
    )
    time.sleep(5)  # Başlamadan önce 5 saniye bekle

    for kisi in kullanicilar:
        isim = kisi.get("name", "Bilinmeyen Kişi")
        telefon = kisi.get("tel", "")
        gorsel_id = kisi.get("id", "")

        # Telefon numarası boşsa atla
        if not telefon:
            print(f"Uyarı: {isim} için telefon numarası boş, atlanıyor.")
            continue

        # Telefon numarasının başında + olduğundan emin ol
        if not telefon.startswith("+"):
            telefon = f"+{telefon}"

        # gorsel_id zaten .jpg içeriyorsa direkt kullan, içermiyorsa ekle
        if not gorsel_id.endswith(".jpg"):
            gorsel_dosya = f"{gorsel_id}.jpg"
        else:
            gorsel_dosya = gorsel_id

        gorsel_yolu = os.path.join(GORSEL_KLASORU, gorsel_dosya)
        mesaj_metni = f"Merhaba {isim}, size özel oran görseliniz ekte yer almaktadır."

        # Görselin varlığını kontrol et
        if os.path.exists(gorsel_yolu):
            try:
                print(f"Gönderiliyor: {isim} ({telefon}) - Görsel: {gorsel_id}.jpg")

                # Görsel ve mesajı gönderir
                # wait_time: Tarayıcıyı açtıktan sonra bekleme süresi
                # close_tab: Gönderim sonrası sekmeyi kapatır
                kit.send_whats_image(
                    telefon, gorsel_yolu, mesaj_metni, wait_time=20, tab_close=True
                )

                print(f"Başarılı: {isim}")

                # Spam filtresine takılmamak için her gönderimden sonra bekleme süresi
                print("Bir sonraki mesaj için 30 saniye bekleniyor...")
                time.sleep(30)

            except Exception as e:
                print(f"Hata: {isim} kişisine gönderilemedi. Hata: {e}")
        else:
            print(f"Hata: {gorsel_yolu} dosyası bulunamadı, bu kişi atlanıyor.")


if __name__ == "__main__":
    mesajlari_gonder()
