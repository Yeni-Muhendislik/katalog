import os
from git import Repo
import shutil

# GitHub repo URL (kendi kullanıcı adınla değiştir)
GITHUB_REPO = "https://github.com/yeni-muhendislik/katalog.git"
LOCAL_PATH = "temp_repo"
PDF_PATH = "yeni-muhendislik-katalog.pdf"   # güncel PDF dosyan
TARGET_FILE = "katalog.pdf"

def update_catalog():
    # Repo daha önce klonlandıysa sil
    if os.path.exists(LOCAL_PATH):
        shutil.rmtree(LOCAL_PATH)

    # Repo'yu klonla
    print("📥 Repo klonlanıyor...")
    repo = Repo.clone_from(GITHUB_REPO, LOCAL_PATH)

    # Yeni PDF'yi repo içine kopyala
    shutil.copy(PDF_PATH, os.path.join(LOCAL_PATH, TARGET_FILE))

    # Git işlemleri
    repo.index.add([TARGET_FILE])
    repo.index.commit("📦 Katalog güncellendi")
    origin = repo.remote(name="origin")
    origin.push()

    print("✅ Yeni katalog başarıyla güncellendi!")

if __name__ == "__main__":
    update_catalog()
