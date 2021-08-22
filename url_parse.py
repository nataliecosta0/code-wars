"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet
"""
import unittest
import re

def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

class TestStringMethods(unittest.TestCase):
    def test_domain_name_google(self):
        self.assertEqual(domain_name("http://google.com"), "google")
    
    def test_domain_name_co_jpe(self):
        self.assertEqual(domain_name("http://google.co.jp"), "google")
    
    def test_domain_name_xakep(self):
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
    
    def test_domain_name_youtube(self):
        self.assertEqual(domain_name("https://youtube.com"), "youtube")

if __name__ == '__main__':
    unittest.main()