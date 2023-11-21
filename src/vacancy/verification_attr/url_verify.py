
class UrlVerify:
    """Verification the url attribute of the Vacancy class"""

    def __init__(self, url):
        self.url = url

    @classmethod
    def verify_url(cls, url):
        url_list = url.split('//')
        if url_list[0] == 'https:':
            return url
        else:
            return ' - '


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        url = self.verify_url(url)
        self.__url = url
