import json
import os

DATA_FILE = 'articles.json'

def load_articles():
    """Loads articles from the JSON data file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_articles(articles):
    """Saves articles to the JSON data file."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)

def add_article(articles):
    """Adds a new article to the collection."""
    print("\nYeni Makale Ekle:")
    title = input("Başlık: ").strip()
    url = input("URL: ").strip()
    tags_input = input("Etiketler (virgülle ayırın, örn: python, web, veri): ").strip()
    tags = [tag.strip().lower() for tag in tags_input.split(',') if tag.strip()]
    notes = input("Notlar (isteğe bağlı): ").strip()

    if not title or not url:
        print("Başlık ve URL boş bırakılamaz.")
        return

    new_article = {
        "title": title,
        "url": url,
        "tags": tags,
        "notes": notes
    }
    articles.append(new_article) # This illustrates "kişisel listelerimizi nasıl oluşturacağımızı" (how to create our personal lists)
    save_articles(articles)
    print("Makale başarıyla eklendi.")

def list_articles(articles):
    """Lists all articles in the collection."""
    if not articles:
        print("\nHenüz hiç makale eklenmemiş.")
        return

    print("\n--- Kayıtlı Makaleler ---")
    for i, article in enumerate(articles):
        print(f"\n{i+1}. Başlık: {article['title']}")
        print(f"   URL: {article['url']}")
        print(f"   Etiketler: {', '.join(article['tags']) if article['tags'] else 'Yok'}")
        if article['notes']:
            print(f"   Notlar: {article['notes']}")
    print("------------------------")

def search_articles(articles):
    """Searches articles by keyword in title, URL, or tags."""
    if not articles:
        print("\nHenüz hiç makale eklenmemiş.")
        return

    keyword = input("\nArama anahtar kelimesi (başlık, URL veya etiketlerde ara): ").strip().lower()
    if not keyword:
        print("Arama anahtar kelimesi boş olamaz.")
        return

    found_articles = []
    for article in articles:
        if keyword in article['title'].lower() or \
           keyword in article['url'].lower() or \
           any(keyword in tag for tag in article['tags']):
            found_articles.append(article)

    if not found_articles:
        print(f"'{keyword}' anahtar kelimesiyle eşleşen makale bulunamadı.")
        return

    print(f"\n--- '{keyword}' için Arama Sonuçları ---")
    for i, article in enumerate(found_articles):
        print(f"\n{i+1}. Başlık: {article['title']}")
        print(f"   URL: {article['url']}")
        print(f"   Etiketler: {', '.join(article['tags']) if article['tags'] else 'Yok'}")
        if article['notes']:
            print(f"   Notlar: {article['notes']}")
    print("------------------------------------")
    # This search/filter functionality helps with "bilgiyi eleştirel bir gözle değerlendirme, organize etme" (critically evaluating and organizing information)

def main():
    articles = load_articles()

    while True:
        print("\n--- Bilgi Küratörü ---")
        print("1. Makale Ekle")
        print("2. Tüm Makaleleri Listele")
        print("3. Makale Ara")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın: ").strip()

        if choice == '1':
            add_article(articles)
        elif choice == '2':
            list_articles(articles) # This demonstrates "ortak bir dijital kütüphane oluşturalım" (let's create a common digital library) conceptually, by listing the curated items.
        elif choice == '3':
            search_articles(articles)
        elif choice == '4':
            print("Çıkılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
