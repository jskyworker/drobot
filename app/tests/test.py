import unittest
from urllib2 import HTTPError, urlopen


def analyze_drobot_404(url):
    try:
        urlopen(url, timeout=4)
    except HTTPError as e:
        print(str(e))


def analyze_drobot_args(urllist):
    for i in urllist:
        r = urlopen(i, timeout=4)
        print(r.read())

class DrobotTests(unittest.TestCase):
    """ Tests for simple flask application
    """

    def setUp(self):
        self.url404 = 'http://localhost:8080/get'
        self.url2 = ['http://localhost:8080/get?uid=1', 'http://localhost:8080/get?date=2015-05-10']

    def test_args(self):
        analyze_drobot_404(self.url404)
        #analyze_drobot_args(self.url2)
        #self.assertEqual(analyze_drobot_args(self.url2), )

if __name__ == '__main__':
    unittest.main()