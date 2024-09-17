

Bonjour,

Il existe de nombreux logiciels et scripts pour télécharger des vidéos à partir d'un lien. Voici un exemple de script Python utilisant la bibliothèque `pytube` :

1. Installez la bibliothèque `pytube` en utilisant pip :

```bash
pip install pytube
```

2. Créez un fichier Python (par exemple, `download_video.py`) et collez le code suivant :

```python
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()

if __name__ == "__main__":
    video_url = input("Entrez l'URL