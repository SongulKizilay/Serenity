import subprocess
import os
import colorama
from colorama import Fore, Style

# Renk tanımlamaları
success_color = Fore.GREEN
error_color = Fore.RED
info_color = Fore.YELLOW
reset_color = Style.RESET_ALL

def dosyalari_sil(klasor, dosyalar):
    for dosya_adı in dosyalar:
        dosya_yolu = os.path.join(klasor, dosya_adı)
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

def run_command(command):
    exit_code = os.system(command)
    if exit_code == 0:
        print(success_color + f"'{command}' komutu başarıyla çalıştırıldı." + reset_color)
    else:
        print(error_color + f"'{command}' komutu çalıştırılırken bir hata oluştu. Çıkış kodu: {exit_code}" + reset_color)

def install_and_run_bash_script(script_path):
    if not os.path.exists(script_path):
        try:
            install_command = f"chmod +x {script_path} && ./{script_path}"
            result = subprocess.run(install_command, shell=True, check=True, text=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            print("Çıkış kodu:", result.returncode)
            print("Çıkış:")
            print(result.stdout)
            print("Hata:")
            print(result.stderr)
        except subprocess.CalledProcessError as e:
            print("Hata oluştu:", e)
    else:
        print("bash.sh dosyası zaten mevcut. İşlem devam ediyor.")

# Renk tanımlamaları
success_color = Fore.GREEN
error_color = Fore.RED
info_color = Fore.YELLOW
reset_color = Style.RESET_ALL

klasor2 = "/root/Desktop/bug/"
silinecek_dosyalar = ["httpx.txt", "nuclei.txt", "subdomain.txt"]

# Dosyaları kontrol et ve sil
dosyalari_sil(klasor2, silinecek_dosyalar)

bash_script = "./bash.sh"  # Bash betiğinin dosya yolu

# Bash betiği yüklü mü kontrol et
install_and_run_bash_script(bash_script)

# Taranacak adreslerin listesini giriniz
print(info_color + "Taranacak adreslerin listesini giriniz" + reset_color)
dosya_yolu = input("Dosya yolunu girin: ")

# Subdomain listesi taranıyor
print(info_color + "Subdomain listesi taranıyor" + reset_color)
print("****************************************************************")

komut = f"cd /root/go/bin && ./subfinder -dL {dosya_yolu} >> /root/Desktop/bug/subdomain.txt"
run_command(komut)

# httpx
print("################################################################")
komut2 = f"cd /root/go/bin/ && cat '/root/Desktop/bug/subdomain.txt' | ./httpx >> /root/Desktop/bug/httpx.txt"
run_command(komut2)

# nuclei
print("################################################################")
komut3 = f"cd /root/go/bin/ && ./nuclei -l '/root/Desktop/bug/httpx.txt'  -o '/root/Desktop/bug/nuclei.txt'"
run_command(komut3)

# Tarama sonucu çıkan CVE listesi
print("******************************************\n")
print(info_color + "Tarama sonucu çıkan CVE listesi" + reset_color)
komut4 = "grep CVE* /root/Desktop/bug/nuclei.txt "
run_command(komut4)

# Tarama sonucu çıkan low sonuçların listesi
print("******************************************\n")
print(info_color + "Tarama sonucu çıkan low sonuçların listesi" + reset_color)
komut5 = "grep '\[low\]' /root/Desktop/bug/nuclei.txt "
run_command(komut5)

# Tarama sonucu çıkan medium listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan medium listesi" + reset_color)
komut6 = "grep '\[medium\]' /root/Desktop/bug/nuclei.txt "
run_command(komut6)

# Tarama sonucu çıkan high listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan high listesi" + reset_color)
komut7 = "grep '\[high\]' /root/Desktop/bug/nuclei.txt "
run_command(komut7)

# Tarama sonucu çıkan critical listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan critical listesi" + reset_color)
komut8 = "grep '\[critical\]' /root/Desktop/bug/nuclei.txt "
run_command(komut8)

# Tarama sonucu çıkan unknown listesi
print("################################################################")
print(info_color + "Tarama sonucu çıkan unknown listesi" + reset_color)
komut9 = "grep '\[unknown\]' /root/Desktop/bug/nuclei.txt "
run_command(komut9)

# Ses dosyasını çalmak için kullanılacak fonksiyon
def play_audio():
    subprocess.run(["mpv", "fbı.mp3"])

try:
    while True:
        subprocess.run(["mpv", "--loop", "fbı.mp3"])
except KeyboardInterrupt:
    print("Ctrl+C tuş kombinasyonu algılandı. Çıkılıyor...")
