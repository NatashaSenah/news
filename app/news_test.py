import unittest
from .models import news

News = news.News

class NewsTest(unittest.TestCase):
   
    def setUp(self):
        
        self.new_news = News(1234,'ABCNews','A government officer being imprissoned','general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()