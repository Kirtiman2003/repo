
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
class WebCrawler:
    def __init__(self):
        self.visited_url = set()
    def crawl(self, url, depth = 3, delay = 1):
        if(depth == 0 or url in self.visited_url):
            return
        try:
            if(not self.is_allowed_by_robots(url)):
                print(f"Skipping {url} due to robots.txt rules.")
                return
            res = requests.get(url)
            if(res.status_code == 200):
                soup = BeautifulSoup(res.text, "html.parser")
                self.index_page(url, soup)
                self.visited_url.add(url)
                for link in soup.find_all("a"):
                    new_url = link.get("href")
                    if(new_url and new_url.startswith("http")):
                        time.sleep(delay)
                        self.crawl(new_url, depth - 1, delay)
        except Exception as e:
            print(f"Error crawling {url} : {e}")
    def is_allowed_by_robots(self, url):
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
        res = requests.get(robots_url)
        if(res.status_code == 200):
            robots_txt = res.text
            if("User-agent: *" in robots_txt):
                start_index = robots_txt.find("User-agent: *")
                end_index = robots_txt.find("User-agent:", start_index + 1)
                if(end_index == -1):
                    end_index = len(robots_txt)
                relevant_section = robots_txt[start_index: end_index]
                if("Disallow:/" in relevant_section):
                    return False
        return True
    def index_page(self, url, soup):
        title = soup.title.string if soup.title else "No title!"
        para = soup.find("p").get_text() if soup.find("p") else "No paragraph found!"
        print(f"Indexing: {url}")
        print(f"Title: {title}")
        print(f"First Paragraph: {para}")
        print("-"*60)
crawler = WebCrawler()
crawler.crawl("https://10fastfingers.com/typing-test/english")
