class UrlManager(object):
    def __init__(self):
        self.url_list = set()
        self.used_list = set()
        pass

    def add_new_url(self, source):
        print "start craw! " + source
        self.url_list.add(source)
        # print self.url_list.__len__()
        pass

    def has_url(self):
        return self.url_list.__len__() > 0

    def get_available_url(self):
        if self.url_list.__len__() > 0:
            pop = self.url_list.pop()
            self.used_list.add(pop)
            return pop
        else:
            return ""

    def add_new_urls(self, new_urls):
        # print new_urls
        #
        for url in new_urls:
            if url not in self.used_list and url not in self.url_list:
                self.url_list.add(url)

        pass

    def remove_crawled_url(self, url):
        self.url_list.remove(url)
        pass
