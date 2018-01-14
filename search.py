# -*- encoding:utf-8 -*-
from urllib import urlopen
import urllib
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#urllib.quote("中国".decode('utf-8').encode('gbk'))  格式
def search(question):
    result_list = []
    result_list.extend(search_zhidao(question))
    return result_list


def search_zhidao(question):
    result_list = []
    url = 'https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word={}'.\
        format(urllib.quote(question.decode('utf-8').encode('gbk')))
    print(url)
    result = requests.get(url)
    # 解析页面
    body = BeautifulSoup(result.content, 'html5lib')
    # print body
    good_result_div = body.find(class_='list-header').find('dd')
    second_result_div = body.find(class_='list-inner').find(class_='list')
    if good_result_div is not None:
        good_result = good_result_div.get_text()
        result_list.append(good_result)
        print(good_result.strip())

    if second_result_div is not None:
        second_result_10 = second_result_div.findAll('dl')  # .find(class_='answer').get_text()
        if second_result_10 is not None and len(second_result_10) > 0:
            for index, each_result in enumerate(second_result_10):
                result_dd = each_result.dd.get_text()
                result_list.append(result_dd)
                if index < 3:
                    print(result_dd)
    return result_list
if __name__ == '__main__':
    search_zhidao('股票一手是多少股')