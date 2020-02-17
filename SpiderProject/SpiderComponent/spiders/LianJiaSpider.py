import sys 
import os
sys.path.append("D:\Repo\EstateDataAnalysis\SpiderProject\SpiderComponent\Items")
import LianJiaItem
from scrapy.spiders import Spider

class LianJiaSpider(Spider):
    name = 'LianJia'
    start_urls = ['https://nj.ke.com/ershoufang/']

    def parse(self, response):
        titles = response.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/')
        for title in titles:
            print(title)
