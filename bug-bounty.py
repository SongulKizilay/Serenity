import os
import colorama
from colorama import Fore, Style
import subprocess

# Renk tanımlamaları
success_color = Fore.GREEN
error_color = Fore.RED
info_color = Fore.YELLOW
reset_color = Style.RESET_ALL

klasor2 = "/root/Desktop/Serenity/"
silinecek_dosyalar = ["httpx.txt", "nuclei.txt", "subdomain.txt"]

# Dosyaları kontrol et ve sil
for dosya_adı in silinecek_dosyalar:
    dosya_yolu = os.path.join(klasor2, dosya_adı)
    if os.path.exists(dosya_yolu):
        try:
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)
                print(f"{dosya_adı} dosyası silindi.")
            else:
                os.rmdir(dosya_yolu)
                print(f"{dosya_yolu} dizini silindi.")

        except Exception as e:
            print(f"{dosya_adı} dosyası/dizini silinirken bir hata oluştu: {str(e)}")

bash_script = "./bash.sh"  # Bash betiğinin dosya yolu

# Bash betiği yüklü mü kontrol et
if not os.path.exists(bash_script):
    try:
        # Bash betiği yüklü değilse, yükleyip sonra çalıştır
        install_command = f"chmod +x {bash_script} && ./{bash_script}"
        result = subprocess.run(install_command, shell=True, check=True, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        # Çıktıyı yazdırın
        print("Çıkış kodu:", result.returncode)
        print("Çıkış:")
        print(result.stdout)
        print("Hata:")
        print(result.stderr)

    except subprocess.CalledProcessError as e:
        print("Hata oluştu:", e)
else:
    print("bash.sh dosyası zaten mevcut. İşlem devam ediyor.")

# Taranacak adreslerin listesini giriniz
print(info_color + "Taranacak adreslerin listesini giriniz" + reset_color)
dosya_yolu = input("Dosya yolunu girin: ")

# Subdomain listesi taranıyor
print(info_color + "Subdomain listesi taranıyor" + reset_color)
print("****************************************************************")

komut = f"cd /root/go/bin && ./subfinder -dL {dosya_yolu} >> /root/Desktop/Serenity/subdomain.txt"
exit_code = os.system(komut)

if exit_code == 0:
    print(success_color + f"'{komut}' komutu başarıyla çalıştırıldı. subdomain.txt dosyası oluşturuldu" + reset_color)
else:
    print(error_color + f"'{komut}' komutu çalıştırılırken bir hata oluştu. Çıkış kodu: {exit_code}" + reset_color)

# httpx
print("################################################################")
komut2 = f"cd /root/go/bin/ && cat '/root/Desktop/Serenity/subdomain.txt' | ./httpx >> /root/Desktop/Serenity/httpx.txt"
exit_code = os.system(komut2)

if exit_code == 0:
    print(success_color + f"'{komut2}' komutu başarıyla çalıştırıldı. httpx.txt dosyası oluşturuldu" + reset_color)
else:
    print(error_color + f"'{komut2}' komutu çalıştırılırken bir hata oluştu. Çıkış kodu: {exit_code}" + reset_color)

# nuclei
print("################################################################")
komut3 = f"cd /root/go/bin/ && ./nuclei -l '/root/Desktop/Serenity/httpx.txt'  -o '/root/Desktop/Serenity/nuclei.txt'"
exit_code = os.system(komut3)

if exit_code == 0:
    print(success_color + f"'{komut3}' komutu başarıyla çalıştırıldı. nuclei.txt dosyası oluşturuldu" + reset_color)
else:
    print(error_color + f"'{komut3}' komutu çalıştırılırken bir hata oluştu. Çıkış kodu: {exit_code}" + reset_color)

# Tarama sonucu çıkan CVE listesi
print("******************************************\n")
print(info_color + "Tarama sonucu çıkan CVE listesi" + reset_color)
komut4 = "awk '/CVE-[0-9]{4}-[0-9]{4,8}/ {print}' /root/Desktop/Serenity/nuclei.txt "
sonuc4 = os.system(komut4)
if sonuc4 == 0:
    print(success_color + f"'{komut4}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut4}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc4}" + reset_color)

# Tarama sonucu çıkan low sonuçların listesi
print("******************************************\n")
print(info_color + "Tarama sonucu çıkan low sonuçların listesi" + reset_color)
komut5 = "awk '/\[low\]/' /root/Desktop/Serenity/nuclei.txt "
sonuc5 = os.system(komut5)
if sonuc5 == 0:
    print(success_color + f"'{komut5}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut5}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc5}" + reset_color)

# Tarama sonucu çıkan medium listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan medium listesi" + reset_color)
komut6 = "awk '/\[medium\]/'  /root/Desktop/Serenity/nuclei.txt"
sonuc6 = os.system(komut6)
if sonuc6 == 0:
    print(success_color + f"'{komut6}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut6}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc6}" + reset_color)

# Tarama sonucu çıkan high listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan high listesi" + reset_color)
komut7 = "awk '/\[high\]/' /root/Desktop/Serenity/nuclei.txt"
sonuc7 = os.system(komut7)
if sonuc7 == 0:
    print(success_color + f"'{komut7}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut7}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc7}" + reset_color)

# Tarama sonucu çıkan critical listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan critical listesi" + reset_color)
komut8 = "awk '/\[critical\]/' /root/Desktop/Serenity/nuclei.txt "
sonuc8 = os.system(komut8)
if sonuc8 == 0:
    print(success_color + f"'{komut8}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut8}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc8}" + reset_color)

# Tarama sonucu çıkan unknown listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan unknown listesi" + reset_color)
komut9 = "awk '/\[unknown\]/'  /root/Desktop/Serenity/nuclei.txt "
sonuc9 = os.system(komut9)
if sonuc9 == 0:
    print(success_color + f"'{komut9}' başarıyla çalıştırıldı." + reset_color)
else:
    print(error_color + f"'{komut9}' çalıştırılırken bir hata oluştu. Çıkış kodu: {sonuc9}" + reset_color)

# Ses dosyasını çalmak için kullanılacak fonksiyon
def play_audio():
    subprocess.run(["mpv", "fbı.mp3"])

try:
    while True:
        subprocess.run(["mpv", "--loop", "fbı.mp3"])
except KeyboardInterrupt:
    print("Ctrl+C tuş kombinasyonu algılandı. Çıkılıyor...")
