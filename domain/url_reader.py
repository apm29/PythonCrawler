import urllib2


def down_url(url):

    pass


class UrlReader(object):
    def __init__(self):
        self.set_result = set()
        pass
    def add(self, data):
        print data
        self.set_result.add(data)
        pass

    def output(self):
        #print self.set_result
        print 'craw result:'
        print '----------------------------------'
        for data in self.set_result:
            print data
        pass