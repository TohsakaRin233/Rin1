# coding=utf-8
import null
from bs4 import BeautifulSoup
import requests
import random
import json

ID = input("请输入商品ID:")
# ID = '616282010499'
URL = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.17.77f72140AUTpt0&id=' + ID + '&ns=1&abbucket=8'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.3',
    'Referer': 'https://item.taobao.com/item.htm',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

item_detail_URL = 'http://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=' + ID + '&modules=price,xmpPromotion,couponActivity'

item_detail_header = {'accept': '*/*',
                      'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
                      'cookie': '_uab_collina=157536891332404269866249; _umdata=GAA24D554CF618E62C27D1EF6E9E8D1B6D81AE6',  # 已登录cookie
                      'referer': 'https://item.taobao.com/item.htm',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                    'Chrome/83.0.4103.116 Safari/537.36'}

html = ''
bs = null
json_data = null


def get_proxies():
    proxies_pool = [
    ]
    return random.choices(proxies_pool)[0]


def connect():
    global bs, json_data
    # proxies = get_proxies()
    try:
        resp = requests.get(headers=headers, url=URL, )
        resp2 = requests.get(headers=item_detail_header, url=item_detail_URL, )
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        return False
    if resp.status_code == requests.codes.ok:
        html = resp.text
    if resp2.status_code == requests.codes.ok:
        bs2 = BeautifulSoup(resp2.text, "html.parser")
        json_data = json.loads(bs2.get_text())
    else:
        print(resp.status_code)
        return False

    bs = BeautifulSoup(html, "html.parser")
    return True


def get_data():
    global bs
    title = bs.find('title').get_text()
    img = bs.find('img', attrs={'id': "J_ImgBooth"}).get('src')
    sell_counter = bs.find('strong', attrs={'id': "J_SellCounter"})

    if json_data['code']['message'] == 'SUCCESS':
        prime_price = json_data['data']['price']
        discount_price = json_data['data']['promotion']['promoData']['def'][0]['price']
        print(title)
        print('图片链接：'+'https://' + img)
        print(sell_counter)
        print('原价：'+prime_price)
        print('优惠价：'+discount_price)
        if len(json_data['data']['couponActivity']['coupon']) != 0:
            coupon_list = json_data['data']['couponActivity']['coupon']['couponList']
            for coupon in coupon_list:
                print(coupon['title'])
        else:
            print("暂无优惠券")




def main():
    if connect():
        get_data()


if __name__ == '__main__':
    main()
