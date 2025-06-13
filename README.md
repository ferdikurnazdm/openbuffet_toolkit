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

## Katkı ve İletişim

Bu proje açık kaynaklıdır ve katkılara açıktır. Geri bildirim veya katkı için lütfen GitHub üzerinden issue oluşturun veya pull request gönderin.

- **E-posta**: ferdikurnazdm@gamil.com
- **GitHub**: https://github.com/ferdikurnazdm/openbuffet_toolkit

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.