# -*- encoding: utf8-*-
import re

class ParseAddress(object):
    
    @classmethod
    def parse(cls, address):

        if address is None:
            return {}
        pattern = u"(?P<zipcode>(^\d{5}|^\d{3})?)(?P<city>\D+[縣市])(?P<district>\D+?(市區|鎮區|鎮市|[鄉鎮市區]))(?P<others>.+)"

        matchs = re.search(pattern, address)
        result = {}
        if matchs is not None:
            result['zipcode'] = matchs.group('zipcode')
            result['city'] = matchs.group('city')
            result['district'] = matchs.group('district')
            result['others'] = matchs.group('others')

        return result

if __name__ == '__main__':
    ParseAddress.parse("臺北市中正區金門街1~30號")