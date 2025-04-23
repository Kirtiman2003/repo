
import requests
from bs4 import BeautifulSoup
class WebCrawler:
    def __init__(self):
        self.visited_url = set()
    def crawl(self, url, depth = 3):
        if(depth == 0 or url in self.visited_url):
            return
        try:
            res = requests.get(url)
            if(res.status_code == 200):
                soup = BeautifulSoup(res.text, "html.parser")
                self.index_page(url, soup)
                self.visited_url.add(url)
                for link in soup.find_all("a"):
                    new_url = link.get("href")
                    print(f"Crawling : {new_url}")
                    if(new_url and new_url.startswith("http")):
                        self.crawl(new_url, depth - 1)
        except Exception as e:
            print(f"Error crawling {url} : {e}")
    def index_page(self, url, soup):
        title = soup.title.string if soup.title else "No title!"
        para = soup.find("p").get_text() if soup.find("p") else "No para found!"
        print(f"Indexing: {url}")
        print(f"Title: {title}")
        print(f"First Paragraph: {para}")
        print("-"*60)
crawler = WebCrawler()
crawler.crawl("https://www.example.com")
