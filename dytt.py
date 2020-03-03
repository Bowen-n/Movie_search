import lxml
import requests
from lxml import etree


class Dytt:
    
    def __init__(self):
        self.url = 'https://www.ygdy8.com'
        self.search_url = 'http://s.dydytt.net/plus/s0.php'
        self.params = {'typeid': 1}
        self.xpath = {
            'item_url': './/a[contains(@href, "/html") and not(contains(@href, "http"))]//@href',
            'item_name': './/a[contains(@href, "/html") and not(contains(@href, "http"))]//text()',
            'download_link': './/td[contains(@style, "WORD")]/a/text()'
        }
    

    def search(self, movie):
        ''' Search movie
        Args:
            movie - `str`
        Return:
            Download links
        '''
        self.params['keyword'] = movie.encode('gb2312')
        urls, names = self._search_item()

        if len(urls) == 0:
            return None

        for index in range(len(urls)):
            urls[index] = self.url + urls[index]
        
        movie_list = []

        for url in urls:
            response = requests.get(url)
            response.encoding = 'gb2312'
            source = etree.HTML(response.text)

            download_link = source.xpath(self.xpath['download_link'])[0]

            if 'BD' in download_link:
                definition = 'BD'
            elif 'HD' in download_link:
                definition = 'HD'
            else:
                definition = None
            
            movie = {
                'name': names[urls.index(url)],
                'link': download_link,
                'definition': definition
            }
            movie_list.append(movie)
        
        return movie_list


    def _search_item(self):
        response = requests.get(self.search_url, self.params)
        response.encoding = 'gb2312'
        source = etree.HTML(response.text)
        
        item_urls = source.xpath(self.xpath['item_url'])
        item_names = source.xpath(self.xpath['item_name'])
        item_names = self._tidy_item_names(item_names)

        return item_urls, item_names
    

    def _tidy_item_names(self, item_names):
        new_item_names = []

        while len(item_names):
            movie_name = ''
            for i in range(3):
                movie_name += item_names.pop(0)
            new_item_names.append(movie_name)

        return new_item_names



