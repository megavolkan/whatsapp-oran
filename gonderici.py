import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ayarlar
JSON_DOSYASI = "liste.json"
GORSEL_KLASORU = "gorseller"

def mesajlari_gonder():
    chrome_options = Options()
    user_data_dir = os.path.expanduser("~") + "/Library/Application Support/Google/Chrome/Default"
    if os.path.exists(user_data_dir):
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 40)

    try:
        with open(JSON_DOSYASI, "r", encoding="utf-8") as f:
            kullanicilar = json.load(f)
    except Exception as e:
        print(f"Hata: JSON dosyası okunamadı: {e}")
        driver.quit()
        return

    print(f"Toplam {len(kullanicilar)} kişi işlenecek.")

    for kisi in kullanicilar:
        isim = kisi.get("name", "Bilinmeyen Kişi")
        telefon = kisi.get("tel", "").replace(" ", "").replace("-", "").replace("+", "")
        gorsel_id = kisi.get("id", "")

        if not telefon:
            continue

        gorsel_dosya = gorsel_id if gorsel_id.endswith(".jpg") else f"{gorsel_id}.jpg"
        gorsel_yolu = os.path.abspath(os.path.join(GORSEL_KLASORU, gorsel_dosya))
        mesaj_metni = f"Merhaba {isim}, size özel oran görseliniz ekte yer almaktadır."

        if os.path.exists(gorsel_yolu):
            try:
                print(f"Gönderiliyor: {isim} ({telefon})")
                
                # Sadece sohbeti aç (metni URL'den göndermiyoruz, resimle birlikte ekleyeceğiz)
                url = f"https://web.whatsapp.com/send?phone={telefon}"
                driver.get(url)
                
                # Sayfanın yüklenmesi için bekle
                time.sleep(10)
                
                # Dosya ekleme inputunu bul
                attach_xpath = '//input[@type="file"]'
                attach_input = wait.until(EC.presence_of_element_located((By.XPATH, attach_xpath)))
                attach_input.send_keys(gorsel_yolu)
                
                # Resim önizleme ekranının gelmesini bekle
                time.sleep(3)
                
                # Mesaj metnini (caption) yaz
                # Önizleme ekranındaki yazı kutusunu bul (role='textbox')
                try:
                    caption_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]')))
                    caption_box.send_keys(mesaj_metni)
                    time.sleep(1)
                except:
                    print("Caption kutusu bulunamadı, metinsiz devam ediliyor.")

                # Gönder butonuna tıkla
                # Fotoğraf önizleme ekranındaki gönder butonu
                send_xpath = '//span[@data-icon="send"]'
                send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, send_xpath)))
                send_btn.click()

                print(f"Başarılı: {isim}")
                time.sleep(7) # Mesajın gerçekten gitmesi ve sayfanın boşalması için süre

            except Exception as e:
                print(f"Hata: {isim} kişisine gönderilemedi. Hata: {e}")
        else:
            print(f"Hata: {gorsel_yolu} bulunamadı.")

    print("Tüm işlemler tamamlandı.")
    driver.quit()

if __name__ == "__main__":
    mesajlari_gonder()
