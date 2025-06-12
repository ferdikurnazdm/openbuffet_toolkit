# OpenBuffet Toolkit

![GitHub Tag](https://img.shields.io/github/v/tag/ferdikurnazdm/openbuffet_toolkit)
![PyPI - Version](https://img.shields.io/pypi/v/openbuffet-toolkit)
![GitHub License](https://img.shields.io/github/license/ferdikurnazdm/openbuffet_toolkit)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ferdikurnazdm/openbuffet_toolkit)



OpenBuffet ekosistemi için geliştirilmiş modüler bir Python araç kütüphanesidir. Bu toolkit; konfigürasyon yönetimi, loglama, zaman profilleme ve Hugging Face entegrasyonu gibi çok yönlü yardımcı bileşenler içerir. 

Modern uygulamalarda yeniden kullanılabilirliği artırmak, entegrasyonları sadeleştirmek ve yazılım kalitesini yükseltmek amacıyla tasarlanmıştır.

## Uyumluluk

- **Python Versiyonu**: 3.8+
- **Platform Desteği**: Tüm platformlar
- **Kullanım Alanları**: FastAPI servisleri, veri işleme pipeline'ları, model tabanlı uygulamalar

## Özellikler

-  Ortam değişkenlerini `.env` dosyasından yükleyebilme (`ConfiguratorEnvironment`)
-  Dosyaya ve konsola loglama yapan, thread-safe `LoggerManager`
-  Fonksiyonları çalışma süresine göre profilleyen `Profiler`
-  Hugging Face üzerinde model ve veri yükleme/indirme işlemleri yapan `HuggingFaceHelper`
-  Açık kaynak, genişletilebilir yapı.

## Kurulum

### Pip ile Kurulum

```bash
pip install openbuffet-toolkit
```

### Geliştirme Modunda Kurulum

```bash
git clone https://github.com/ferdikurnazdm/openbuffet_toolkit.git
cd openbuffet_toolkit
pip install -e .
```

## Kullanım Örnekleri

### LoggerManager Kullanımı

```python
from openbuffet_toolkit.logger import LoggerManager

logger = LoggerManager().get_logger()
logger.info("Sistem başlatıldı.")
```

### Ortam Değişkenlerini Yükleme

```python
from openbuffet_toolkit.configurator import ConfiguratorEnvironment

config = ConfiguratorEnvironment()
api_key = config.get("API_KEY")
```

### Profiler Dekoratörü

```python
from openbuffet_toolkit.profiler import Profiler

@Profiler.time_taken(label="DEBUG: ")
def iş_yap():
    # İşlem kodları
    pass
```

### HuggingFaceHelper ile Model Yönetimi

```python
from openbuffet_toolkit.hfhelper import HuggingFaceHelper

hf = HuggingFaceHelper(
    hf_username="kullaniciadi",
    hf_token="hf_abc123",
    hf_reponame="proje-adi",
    local_dir="./model"
)

# Repository oluştur
hf.create_repo_if_not_exist()

# Dosya yükle
hf.upload_file("model_bundle.joblib")

# Dosya indir
hf.download_file("model_bundle.joblib", local_dir="./indirilenler")
```
### TextOps ile Metin İşleme
```python
from openbuffet_toolkit.textops import TextOps
```
#### Türkçe karakterleri ASCII'ye çevirme
```python
text = "Çok güzel bir gün! Şöyle böyle..."
clean_text = TextOps.transliterate_turkish(text)
print(clean_text)  # "Cok guzel bir gun! Soyle boyle..."
```
#### Unicode normalizasyon
```python
normalized = TextOps.normalize_unicode("Café naïve résumé")
```
#### Noktalama işaretlerini kaldırma
```python
no_punct = TextOps.remove_punctuation("Merhaba, dünya!")
print(no_punct)  # "Merhaba dünya"
```
#### Boşlukları düzenleme
```python
clean_spaces = TextOps.simplify_spaces("Çok    fazla\n\nboşluk\t\tvar")
print(clean_spaces)  # "Çok fazla boşluk var"
```
#### Tümünü bir arada temizleme
```python
messy_text = "  Çağdaş    Türkiye'de...  teknoloji!!!  \n\n"
clean_result = TextOps.clean(
    messy_text,
    use_transliterate=True,    # Türkçe karakterleri çevir
    use_unicode=True,          # Unicode normalize et
    use_punctuation=True,      # Noktalama kaldır
    use_spaces=True,           # Boşlukları düzenle
    strip_result=True          # Baş/son boşlukları temizle
)
print(clean_result)  # "Cagdas Turkiyede teknoloji"
```

### MSSQLHelper ile Veritabanı İşlemleri
```python
from openbuffet_toolkit.tool_database import MSSQLHelper

db = MSSQLHelper(
    server="localhost",
    database="TestDB",
    user="sa",
    password="Password123",
    trusted_connection=False
)

# Veri çekme
rows = db.execute_query("SELECT * FROM Users WHERE IsActive = ?", [1])

# Veri ekleme
db.execute_non_query("INSERT INTO Users (Name, IsActive) VALUES (?, ?)", ["Ali", 1])

# Procedure çalıştırma
result = db.execute_stored_procedure("sp_GetActiveUsers")

db.close()
```



## Testler

Projeyi test etmek için:

```bash
pytest tests/
```

## Katkı ve İletişim

Bu proje açık kaynaklıdır ve katkılara açıktır. Geri bildirim veya katkı için lütfen GitHub üzerinden issue oluşturun veya pull request gönderin.

- **E-posta**: ferdikurnazdm@gamil.com
- **GitHub**: https://github.com/ferdikurnazdm/openbuffet_toolkit

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.