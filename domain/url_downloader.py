import re
import urllib2


class UrlDownloader(object):
    pass


def download(url):
    try:

        content = urllib2.urlopen(url=url)
    except:
        print "request fail ",url
        return ""
    return content
