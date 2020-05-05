import requests
from bs4 import BeautifulSoup
from webbrowser import open

class main:
    def __init__(self):
        self.user_id = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        self.base_urls = {'Türkiye':'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuUnlHZ0pVVWlnQVAB?hl=tr&gl=TR&ceid=TR%3Atr',
                          'İngiltire':'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pIUWlnQVAB?hl=en-GB&gl=GB&ceid=GB%3Aen',
                          'Amerika':'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'}
        self.NewsTitle = []
        self.NewsContent = []
        self.NewsUrl = []


    def Scrap(self):
        print("[LOG]\tVar olan ülkeler: ", self.base_urls.keys())
        try:
            country = input('Lütfen bir ülke giriniz: ').title()
            page = requests.get(self.base_urls.get(country), headers= self.user_id)
            source = page.text
            soup = BeautifulSoup(source, 'html.parser')
        except:
            print("[LOG]\tYanlış / Var olmayan bir ülke adı girdiniz!")
            country = input('Lütfen bir ülke giriniz: ').title()
            page = requests.get(self.base_urls.get(country), headers=self.user_id)
            source = page.text
            soup = BeautifulSoup(source, 'html.parser')

        data2 = soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')
        for item in data2:
            items = item.find('a')
            self.NewsTitle.append(items.text)

        a = len(self.NewsTitle)

        data = soup.find_all('a', class_='VDXfz')
        for item in data:
            self.NewsUrl.append("https://news.google.com/" + item['href'])
        del self.NewsUrl[a:]

        data3 = soup.find_all('h4', class_='ipQwMb ekueJc gEATFF RD0gLb')
        for item in data3:
            items= item.find('a')
            self.NewsContent.append(items.text)
        del self.NewsContent[a:]

        self.Open()

    def Open(self):
        print(f"toplam {len(self.NewsTitle)} güncel haber bulundu.")
        rasgele = int(input('Kaçıncı haberi görmek istersin?'))
        print("[LOG]\tSeçtiğin haberin başlığı: {}".format(self.NewsTitle[rasgele]))
        open(self.NewsUrl[rasgele])


if __name__ == '__main__':
    main().Scrap()
