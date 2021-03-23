from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

def get_search_url():
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    request_url  = "https://stocks.finance.yahoo.co.jp/"
     
    session = HTMLSession()
    print(request_url)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup

def parse(url):

    stock_ranking_text = url.find("div",attrs={"class":"ymuiHeaderBGDark2 ymui3DHeaderDark"}).find('div').find('h2')
    if stock_ranking_text is not None: stock_ranking_text = stock_ranking_text.getText()
    else: stock_ranking_text = ""



    price_increased = url.find("div",attrs={"class":"boardFinDark"}).find('table').find('tr').find('td', attrs={"class":"tableColLine"}).find('dl', attrs = {"class":"yjSt"})  #.find('table').find('tbody').find('tr').find('td')[0]
    price_dropped = url.find("div",attrs={"class":"boardFinDark"}).find('table').find('tr').find('td').find('dl', attrs = {"class":"yjSt"})     #.find('table').find('tbody').find('tr').find('td')[1]

    # print(price_increased)
    # print(price_increased)



    price_increased_text = price_increased.find('dt').find("span",attrs={"class":"floatL"})
    if price_increased_text is not None: price_increased_text = price_increased_text.getText()
    else: price_increased_text = ""

    price_increased_companies= price_increased.find('dt').find("span",attrs={"class":"floatR"}).find("strong",attrs={"class":"greenFin"})
    if price_increased_companies is not None: price_increased_companies= price_increased_companies.getText()
    else: price_increased_text = ""

    price_increased_comp_1_name = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_1_name is not None: price_increased_comp_1_name = price_increased_comp_1_name.getText()
    else: price_increased_comp_1_name = ""

    price_increased_comp_1_url = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_1_url is not None: price_increased_comp_1_url = price_increased_comp_1_url.get('href')
    else: price_increased_comp_1_url = ""

    price_increased_comp_1_price_L = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_increased_comp_1_price_L is not None: price_increased_comp_1_price_L = price_increased_comp_1_price_L.getText()
    else: price_increased_comp_1_price_L = ""

    price_increased_comp_1_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_increased_comp_1_price_R is not None: price_increased_comp_1_price_R = price_increased_comp_1_price_R.getText()
    else: price_increased_comp_1_price_R = ""

    price_increased_comp_2_name = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_2_name is not None: price_increased_comp_2_name = price_increased_comp_2_name.getText()
    else: price_increased_comp_2_name = ""

    price_increased_comp_2_url = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_2_url is not None: price_increased_comp_2_url = price_increased_comp_2_url.get('href')
    else: price_increased_comp_2_url = ""

    price_increased_comp_2_price_L = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_increased_comp_2_price_L is not None: price_increased_comp_2_price_L = price_increased_comp_2_price_L.getText()
    else: price_increased_comp_2_price_L = ""

    price_increased_comp_2_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_increased_comp_2_price_R is not None: price_increased_comp_2_price_R = price_increased_comp_2_price_R.getText()
    else: price_increased_comp_2_price_R = ""

    price_increased_comp_3_name = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_3_name is not None: price_increased_comp_3_name = price_increased_comp_3_name.getText()
    else: price_increased_comp_3_name = ""

    price_increased_comp_3_url = price_increased.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_increased_comp_3_url is not None: price_increased_comp_3_url = price_increased_comp_3_url.get('href')
    else: price_increased_comp_3_url = ""

    price_increased_comp_3_price_L = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_increased_comp_3_price_L is not None: price_increased_comp_3_price_L = price_increased_comp_3_price_L.getText()
    else: price_increased_comp_3_price_L = ""

    price_increased_comp_3_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_increased_comp_3_price_R is not None: price_increased_comp_3_price_R = price_increased_comp_3_price_R.getText()
    else: price_increased_comp_3_price_R = ""



    price_dropped_text = price_dropped.find('dt').find("span",attrs={"class":"floatL"})
    if price_dropped_text is not None: price_dropped_text = price_dropped_text.getText()
    else: price_dropped_text = ""

    price_dropped_companies = price_dropped.find('dt').find("span",attrs={"class":"floatR"}).find("strong",attrs={"class":"greenFin"})
    if price_dropped_companies is not None: price_dropped_companies = price_dropped_companies.getText()
    else: price_dropped_companies = ""

    price_dropped_comp_1_name = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_1_name is not None: price_dropped_comp_1_name = price_dropped_comp_1_name.getText()
    else: price_dropped_comp_1_name = ""

    price_dropped_comp_1_url = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_1_url is not None: price_dropped_comp_1_url = price_dropped_comp_1_url.get('href')
    else: price_dropped_comp_1_url = ""

    price_dropped_comp_1_price_L = price_dropped.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_dropped_comp_1_price_L is not None: price_dropped_comp_1_price_L = price_dropped_comp_1_price_L.getText()
    else: price_dropped_comp_1_price_L = ""

    price_dropped_comp_1_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_dropped_comp_1_price_R is not None: price_dropped_comp_1_price_R = price_dropped_comp_1_price_R.getText()
    else: price_dropped_comp_1_price_R = ""

    price_dropped_comp_2_name = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_2_name is not None: price_dropped_comp_2_name = price_dropped_comp_2_name.getText()
    else: price_dropped_comp_2_name = ""

    price_dropped_comp_2_url = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_2_url is not None: price_dropped_comp_2_url = price_dropped_comp_2_url.get('href')
    else: price_dropped_comp_2_url = ""

    price_dropped_comp_2_price_L = price_dropped.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_dropped_comp_2_price_L is not None: price_dropped_comp_2_price_L = price_dropped_comp_2_price_L.getText()
    else: price_dropped_comp_2_price_L = ""

    price_dropped_comp_2_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_dropped_comp_2_price_R is not None: price_dropped_comp_2_price_R = price_dropped_comp_2_price_R.getText()
    else: price_dropped_comp_2_price_R = ""

    price_dropped_comp_3_name = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_3_name is not None: price_dropped_comp_3_name = price_dropped_comp_3_name.getText()
    else: price_dropped_comp_3_name = ""

    price_dropped_comp_3_url = price_dropped.find('dd').find("span",attrs={"class":"floatL"}).find('a')
    if price_dropped_comp_3_url is not None: price_dropped_comp_3_url = price_dropped_comp_3_url.get('href')
    else: price_dropped_comp_3_url = ""

    price_dropped_comp_3_price_L = price_dropped.find('dd').find("span",attrs={"class":"ymuiEditLink mar0"})
    if price_dropped_comp_3_price_L is not None: price_dropped_comp_3_price_L = price_dropped_comp_3_price_L.getText()
    else: price_dropped_comp_3_price_L = ""

    price_dropped_comp_3_price_R = price_increased.find('dd').find("span",attrs={"class":"ymuiEditLink mar0 fixWidth"})
    if price_dropped_comp_3_price_R is not None: price_dropped_comp_3_price_R = price_dropped_comp_3_price_R.getText()
    else: price_dropped_comp_3_price_R = ""

    
    
    columns = url.find("div",attrs={"class":"boardFinDark marB10"}).find('table').find('tr').find_all('td')
    
    
    volume = columns[0].find('dl', attrs={"class":"yjSt"})

    volume_text = volume.find("dt")
    if volume_text is not None: volume_text = volume_text.getText()
    else: volume_text = ""

    volume_companies = volume.find_all("dd")

    volume_company_1_name = volume_companies[0].find("a")
    if volume_company_1_name is not None: volume_company_1_name = volume_company_1_name.getText()
    else: volume_company_1_name = ""

    volume_company_1_url = volume_companies[0].find("a")
    if volume_company_1_url is not None: volume_company_1_url = volume_company_1_url.get('href')
    else: volume_company_1_url = ""

    volume_company_2_name = volume_companies[1].find("a")
    if volume_company_2_name is not None: volume_company_2_name = volume_company_2_name.getText()
    else: volume_company_2_name = ""

    volume_company_2_url = volume_companies[1].find("a")
    if volume_company_2_url is not None: volume_company_2_url = volume_company_2_url.get('href')
    else: volume_company_2_url = ""

    volume_company_3_name = volume_companies[2].find("a")
    if volume_company_3_name is not None: volume_company_3_name = volume_company_3_name.getText()
    else: volume_company_3_name = ""

    volume_company_3_url = volume_companies[2].find("a")
    if volume_company_3_url is not None: volume_company_3_url = volume_company_3_url.get('href')
    else: volume_company_3_url = ""


    volume_increase_rate = columns[1].find('dl', attrs={"class":"yjSt"})
    
    volume_increase_rate_text = volume_increase_rate.find("dt")
    if volume_increase_rate_text is not None: volume_increase_rate_text = volume_increase_rate_text.getText()
    else: volume_increase_rate_text = ""

    volume_increase_rate_companies = volume_increase_rate.find_all("dd")

    volume_increase_rate_company_1_name = volume_increase_rate_companies[0].find("a")
    if volume_increase_rate_company_1_name is not None: volume_increase_rate_company_1_name = volume_increase_rate_company_1_name.getText()
    else: volume_increase_rate_company_1_name = ""

    volume_increase_rate_company_1_url = volume_increase_rate_companies[0].find("a")
    if volume_increase_rate_company_1_url is not None: volume_increase_rate_company_1_url = volume_increase_rate_company_1_url.get('href')
    else: volume_increase_rate_company_1_url = ""

    volume_increase_rate_company_2_name = volume_increase_rate_companies[1].find("a")
    if volume_increase_rate_company_2_name is not None: volume_increase_rate_company_2_name = volume_increase_rate_company_2_name.getText()
    else: volume_increase_rate_company_2_name = ""

    volume_increase_rate_company_2_url = volume_increase_rate_companies[1].find("a")
    if volume_increase_rate_company_2_url is not None: volume_increase_rate_company_2_url = volume_increase_rate_company_2_url.get('href')
    else: volume_increase_rate_company_2_url = ""

    volume_increase_rate_company_3_name = volume_increase_rate_companies[2].find("a")
    if volume_increase_rate_company_3_name is not None: volume_increase_rate_company_3_name = volume_increase_rate_company_3_name.getText()
    else: volume_increase_rate_company_3_name = ""

    volume_increase_rate_company_3_url = volume_increase_rate_companies[2].find("a")
    if volume_increase_rate_company_3_url is not None: volume_increase_rate_company_3_url = volume_increase_rate_company_3_url.get('href')
    else: volume_increase_rate_company_3_url = ""


    search_rate_increase = columns[2].find('dl', attrs={"class":"yjSt"})
    
    search_rate_increase_text = search_rate_increase.find("dt")
    if search_rate_increase_text is not None: search_rate_increase_text = search_rate_increase_text.getText()
    else: search_rate_increase_text = ""

    search_rate_increase_companies = search_rate_increase.find_all("dd")

    search_rate_increase_company_1_name = search_rate_increase_companies[0].find("a")
    if search_rate_increase_company_1_name is not None: search_rate_increase_company_1_name = search_rate_increase_company_1_name.getText()
    else: search_rate_increase_company_1_name = ""

    search_rate_increase_company_1_url = search_rate_increase_companies[0].find("a")
    if search_rate_increase_company_1_url is not None: search_rate_increase_company_1_url = search_rate_increase_company_1_url.get('href')
    else: search_rate_increase_company_1_url = ""

    search_rate_increase_company_2_name = search_rate_increase_companies[1].find("a")
    if search_rate_increase_company_2_name is not None: search_rate_increase_company_2_name = search_rate_increase_company_2_name.getText()
    else: search_rate_increase_company_2_name = ""

    search_rate_increase_company_2_url = search_rate_increase_companies[1].find("a")
    if search_rate_increase_company_2_url is not None: search_rate_increase_company_2_url = search_rate_increase_company_2_url.get('href')
    else: search_rate_increase_company_2_url = ""

    search_rate_increase_company_3_name = search_rate_increase_companies[2].find("a")
    if search_rate_increase_company_3_name is not None: search_rate_increase_company_3_name = search_rate_increase_company_3_name.getText()
    else: search_rate_increase_company_3_name = ""

    search_rate_increase_company_3_url = search_rate_increase_companies[2].find("a")
    if search_rate_increase_company_3_url is not None: search_rate_increase_company_3_url = search_rate_increase_company_3_url.get('href')
    else: search_rate_increase_company_3_url = ""

    
    number_of_posts_by_brand = columns[3].find('dl', attrs={"class":"yjSt"})
    
    number_of_posts_by_brand_text = number_of_posts_by_brand.find("dt")
    if number_of_posts_by_brand_text is not None: number_of_posts_by_brand_text = number_of_posts_by_brand_text.getText()
    else: number_of_posts_by_brand_text = ""

    number_of_posts_by_brand_companies = number_of_posts_by_brand.find_all('dd')

    number_of_posts_by_brand_company_1_name = number_of_posts_by_brand_companies[0].find("a")
    if number_of_posts_by_brand_company_1_name is not None: number_of_posts_by_brand_company_1_name = number_of_posts_by_brand_company_1_name.getText()
    else: number_of_posts_by_brand_company_1_name = ""

    number_of_posts_by_brand_company_1_url = number_of_posts_by_brand_companies[0].find("a")
    if number_of_posts_by_brand_company_1_url is not None: number_of_posts_by_brand_company_1_url = number_of_posts_by_brand_company_1_url.get('href')
    else: number_of_posts_by_brand_company_1_url = ""

    number_of_posts_by_brand_company_2_name = number_of_posts_by_brand_companies[1].find("a")
    if number_of_posts_by_brand_company_2_name is not None: number_of_posts_by_brand_company_2_name = number_of_posts_by_brand_company_2_name.getText()
    else: number_of_posts_by_brand_company_2_name = ""

    number_of_posts_by_brand_company_2_url = number_of_posts_by_brand_companies[1].find("a")
    if number_of_posts_by_brand_company_2_url is not None: number_of_posts_by_brand_company_2_url = number_of_posts_by_brand_company_2_url.get('href')
    else: number_of_posts_by_brand_company_2_url = ""

    number_of_posts_by_brand_company_3_name = number_of_posts_by_brand_companies[2].find("a")
    if number_of_posts_by_brand_company_3_name is not None: number_of_posts_by_brand_company_3_name = number_of_posts_by_brand_company_3_name.getText()
    else: number_of_posts_by_brand_company_3_name = ""

    number_of_posts_by_brand_company_3_url = number_of_posts_by_brand_companies[2].find("a")
    if number_of_posts_by_brand_company_3_url is not None: number_of_posts_by_brand_company_3_url = number_of_posts_by_brand_company_3_url.get('href')
    else: number_of_posts_by_brand_company_3_url = ""

    price_increase_rate = {
        'price_increased_text': price_increased_text,
        'price_increased_companies': price_increased_companies,

        'price_increased_comp_1_name': price_increased_comp_1_name,
        'price_increased_comp_1_url': price_increased_comp_1_url,
        'price_increased_comp_1_price_L': price_increased_comp_1_price_L,
        'price_increased_comp_1_price_R': price_increased_comp_1_price_R,

        'price_increased_comp_2_name': price_increased_comp_2_name,
        'price_increased_comp_2_url': price_increased_comp_2_url,
        'price_increased_comp_2_price_L': price_increased_comp_2_price_L,
        'price_increased_comp_2_price_R': price_increased_comp_2_price_R,

        'price_increased_comp_3_name': price_increased_comp_3_name,
        'price_increased_comp_3_url': price_increased_comp_3_url,
        'price_increased_comp_3_price_L': price_increased_comp_3_price_L,
        'price_increased_comp_3_price_R': price_increased_comp_3_price_R,

    }

    price_drop_rate = {
        'price_dropped_text': price_dropped_text,
        'price_dropped_companies': price_dropped_companies,

        'price_dropped_comp_1_name': price_dropped_comp_1_name,
        'price_dropped_comp_1_url': price_dropped_comp_1_url,
        'price_dropped_comp_1_price_L': price_dropped_comp_1_price_L,
        'price_dropped_comp_1_price_R': price_dropped_comp_1_price_R,

        'price_dropped_comp_2_name': price_dropped_comp_2_name,
        'price_dropped_comp_2_url': price_dropped_comp_2_url,
        'price_dropped_comp_2_price_L': price_dropped_comp_2_price_L,
        'price_dropped_comp_2_price_R': price_dropped_comp_2_price_R,

        'price_dropped_comp_3_name': price_dropped_comp_3_name,
        'price_dropped_comp_3_url': price_dropped_comp_3_url,
        'price_dropped_comp_3_price_L': price_dropped_comp_3_price_L,
        'price_dropped_comp_3_price_R': price_dropped_comp_3_price_R,

    }

    volume = {
        'volume_text': volume_text,

        'volume_company_1_name': volume_company_1_name,
        'volume_company_1_url': volume_company_1_url,

        'volume_company_2_name': volume_company_2_name,
        'volume_company_2_url': volume_company_2_url,

        'volume_company_3_name': volume_company_3_name,
        'volume_company_3_url': volume_company_3_url,

    }

    volume_increase_rate = {
        'volume_increase_rate_text': volume_increase_rate_text,

        'volume_increase_rate_company_1_name': volume_increase_rate_company_1_name,
        'volume_increase_rate_company_1_url': volume_increase_rate_company_1_url,

        'volume_increase_rate_company_2_name': volume_increase_rate_company_2_name,
        'volume_increase_rate_company_2_url': volume_increase_rate_company_2_url,

        'volume_increase_rate_company_3_name': volume_increase_rate_company_3_name,
        'volume_increase_rate_company_3_url': volume_increase_rate_company_3_url,

    }

    search_rate_increase = {
        'search_rate_increase_text': search_rate_increase_text,

        'search_rate_increase_company_1_name': search_rate_increase_company_1_name,
        'search_rate_increase_company_1_url': search_rate_increase_company_1_url,

        'search_rate_increase_company_2_name': search_rate_increase_company_2_name,
        'search_rate_increase_company_2_url': search_rate_increase_company_2_url,

        'search_rate_increase_company_3_name': search_rate_increase_company_3_name,
        'search_rate_increase_company_3_url': search_rate_increase_company_3_url,

    }

    number_of_posts_by_brand = {
        'number_of_posts_by_brand_text': number_of_posts_by_brand_text,

        'number_of_posts_by_brand_company_1_name': number_of_posts_by_brand_company_1_name,
        'number_of_posts_by_brand_company_1_url': number_of_posts_by_brand_company_1_url,

        'number_of_posts_by_brand_company_2_name': number_of_posts_by_brand_company_2_name,
        'number_of_posts_by_brand_company_2_url': number_of_posts_by_brand_company_2_url,

        'number_of_posts_by_brand_company_3_name': number_of_posts_by_brand_company_3_name,
        'number_of_posts_by_brand_company_3_url': number_of_posts_by_brand_company_3_url,

    }

    stock_ranking = {
        'stock_ranking_text': stock_ranking_text,

        'price_increase_rate': price_increase_rate,
        'price_drop_rate': price_drop_rate,
        'Volume': volume,
        'volume_increase_rate': volume_increase_rate,
        'search_rate_increase': search_rate_increase,
        'number_of_posts_by_brand': number_of_posts_by_brand
    }
    
    output = {
        'stock_ranking' : stock_ranking
    }

    return output
    
    
def main_fun_2():
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    page = get_search_url()
    scraped_data = parse(page)

    file = open('yahoo-finance-jp-summary.json', 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data

if __name__ == '__main__':
    main_fun_2()