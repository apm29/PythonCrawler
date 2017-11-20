import urllib2
import cookielib

from domain import url_manager, url_parser, url_downloader, url_reader


class UrlCrawler:
    def __init__(self):
        self.manager = url_manager.UrlManager()
        self.parser = url_parser.UrlParser()
        self.downloader = url_downloader.UrlDownloader()
        self.reader = url_reader.UrlReader()
        pass

    def craw(self, source):
        """
        :param source: str
        :return: Any
        """
        self.manager.add_new_url(source)
        count = 1
        while self.manager.has_url() :
            url=self.manager.get_available_url()
            #print url
            html_content=url_downloader.download(url)
            new_urls,data=self.parser.parse_content(html_content,url)
            self.reader.add(data)
            self.manager.add_new_urls(new_urls)
            count=count+1
            if count>80:
                break
            #self.manager.remove_crawled_url(url)
            pass
        self.reader.output()
        return None


print __name__
if __name__ == "__main__":
    source_url = "http://www.imooc.com/video/10689"
    url_crawler = UrlCrawler()
    url_crawler.craw(source=source_url)
