
# Serenity Bug Bounty Otomatize Aracı

**Serenity (Go, Python, ve Bash Aracı)**, web güvenlik testlerini hızlı ve otomatik bir şekilde gerçekleştirmek için tasarlanmış bir araçtır. Bu araç, subdomain tarama, HTTP durumu kontrolü, ve güvenlik açığı taraması gibi işlemleri otomatize etmenize yardımcı olur. Bug Bounty programlarına katılmadan önce ve web uygulamalarını güvenceye almadan önce bu aracı kullanarak hedeflerinizi test edebilirsiniz.

## Gereksinimler

Serenity'ı kullanmadan önce aşağıdaki gereksinimlere sahip olmalısınız:

- Python
- Go
- Colorama (Python paketi)
- Gerekli Go araçları: subfinder, httpx, nuclei

## Kurulum

Serenity'ı kullanmadan önce aşağıdaki adımları takip ederek kurulumu yapmalısınız:

1. Python bağımlılıklarını yüklemek için aşağıdaki komutları çalıştırın:

   ```bash
   python -m pip install colorama
Bash betiğini yüklemek için bash.sh dosyasını çalıştırabilirsiniz. Bu betik, Serenity için gerekli Go araçlarını yükler. Eğer bu araçlar zaten yüklü ise bu adımı atlayabilirsiniz.
    ./bash.sh

Kullanım
Serenity'ı kullanmak için aşağıdaki adımları takip edin:

Subdomain listesi oluşturun veya kullanmak istediğiniz subdomain listesinin yolunu belirtin. Program sizi bu bilgiyi girmeniz için yönlendirecektir.

Subdomain taraması başlatmak için belirtilen subdomain listesi üzerinde tarama işlemini başlatın.

HTTP durumu kontrolü yapmak için otomatik olarak httpx aracını kullanın.

Güvenlik açıkları taraması yapmak için nuclei aracını kullanın.

Tarama sonuçları, CVE listesi, düşük, orta, yüksek, kritik ve bilinmeyen riskli sonuçlar ayrı ayrı listelenecektir.

#Örnek Kullanım


Örnek bir subdomain listesi olarak sub.txt dosyasını kullanabilirsiniz. Bu dosyanın içeriği örnek.com gibi hedef domainleri içermelidir.


   example.com

Ardından Serenity'ı çalıştırmak için Python betiği olan python.py dosyasını kullanabilirsiniz:

    python python.py

Serenity, subdomain taramasından sonra HTTP durumu kontrolü ve güvenlik açığı taraması yapacak ve sonuçları ayrı ayrı listeler halinde sunacaktır.

Serenity (Go, Python, ve Bash Aracı) ile web güvenlik testlerini otomatize edebilir ve potansiyel güvenlik açıklarını belirlemek için kullanabilirsiniz. Bug Bounty programlarına katkıda bulunurken, bu aracı kullanarak hedeflerinizi güvenceye alabilirsiniz.

