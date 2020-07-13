import null as null
from bs4 import BeautifulSoup
import requests

i = 0
html = ''
url = 'http://www.laohuangli.net/'
res = ''  # 改成星乃res
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
Data = []
tempdata = []
length = 0
bs = null


def connect():
    global bs
    try:
        resp = requests.get(headers=headers, url=url)
    except requests.exceptions.ConnectionError:
        print('连不上了铁汁')  # 星乃报错
        return False
    if resp.status_code == requests.codes.ok:
        html = resp.text
    else:
        print(str(resp.status_code) + "了铁汁")
        return False

    bs = BeautifulSoup(html, "html.parser")
    return True


# 处理数据
def get_data(bs):
    trlist = bs.find_all('tr', attrs={'bgcolor': '#FFFFFF'})

    # 前几个

    for tr in trlist[0:7]:
        if len(Data) == 0:
            Data.append('分析')  # 单独处理
        tdlist1 = tr.find_all('td', attrs={'class': 't_11'})  # 行名
        tdlist2 = tr.find_all('td', attrs={'class': 't_12'})  # 内容
        data_format_com(tdlist1, tdlist2)

    # 中间几个

    for tr in trlist[7:11]:
        tdlist1 = tr.find_all('td', attrs={'class': 't_11'})
        tdlist2 = tr.find_all('td', attrs={'style': 'font-size:12px;'})
        data_format_com(tdlist1, tdlist2)

    # 最后几个

    for tr in trlist[11:14]:
        tdlist1 = tr.find_all('td', attrs={'class': 't_11'})
        tdlist2 = tr.find_all('td', attrs={'class': 't_12'})
        data_format_com(tdlist1, tdlist2)


# 公共处理部分

def data_format_com(tdlist1, tdlist2):
    for td in tdlist1:
        Data.append(td.get_text().strip())
    for td in tdlist2:
        tempdata = td.get_text().replace('\r\r', '').replace('\n\n', '').replace('\t\t', '').replace('  ', '').strip()
        # length = len(tempdata)
        Data.append(tempdata)


# 过长单独处理分行

def data_format_sp(str):
    if len(str) < 8:
        return str
    for i in range(6, len(str), 6):
        if str[i] == ' ':
            str = str[0:i] + '\n' + str[i + 1:]
        elif str[i - 1] == ' ':
            str = str[0: i - 1] + '\n' + str[i:]
        elif str[i + 1] == ' ':
            str = str[0: i + 1] + '\n' + str[i + 2:]
        print(str)
    return str


# 图片生成模块

def new_graph(data):
    from prettytable import PrettyTable
    from PIL import Image, ImageDraw, ImageFont

    tab = PrettyTable()
    # 表格内容插入

    for data in Data[9 * 13:(9 * 13) + 13]:
        Data[Data.index(data)] = data_format_sp(data)
    for data in Data[10 * 13:(10 * 13) + 13]:
        Data[Data.index(data)] = data_format_sp(data)
    for data in Data[13 * 13:(13 * 13) + 13]:
        Data[Data.index(data)] = data[0:4] + '\n ' + data[4:]

    # for i in range(0,14):
    #     tab.add_row(Data[i*13:(i*13)+13])

    # 时刻
    tab.add_row(Data[1 * 13:(1 * 13) + 13])
    # 吉凶
    tab.add_row(Data[5 * 13:(5 * 13) + 13])
    # 时宜
    tab.add_row(Data[9 * 13:(9 * 13) + 13])
    # 时忌
    tab.add_row(Data[10 * 13:(10 * 13) + 13])
    # 财喜
    tab.add_row(Data[13 * 13:(13 * 13) + 13])

    tab_info = str(tab)
    space = 5

    # PIL模块中，确定写入到图片中的文本字体
    font = ImageFont.truetype('C:\\Windows\\Fonts\\SimSun.ttc', 20, encoding='utf-8')
    # Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), (255, 255, 255, 0))
    # ImageDraw向图片中进行操作，写入文字或者插入线条都可以
    draw = ImageDraw.Draw(im, "RGB")
    # 根据插入图片中的文字内容和字体信息，来确定图片的最终大小
    img_size = draw.multiline_textsize(tab_info, font=font)
    # 图片初始化的大小为10-10，现在根据图片内容要重新设置图片的大小
    im_new = im.resize((img_size[0] + space * 2, img_size[1] + space * 2))
    del draw
    del im
    draw = ImageDraw.Draw(im_new, 'RGB')
    # 批量写入到图片中，这里的multiline_text会自动识别换行符

    draw.multiline_text((space, space), tab_info, fill=(0, 0, 0), font=font)

    im_new.save(res + 'huangli.png', "png")
    del draw
    # print(tab)


def main():
    if connect():
        get_data(bs)
        new_graph(Data)


if __name__ == '__main__':
    main()
