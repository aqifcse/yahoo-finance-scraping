from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import codecs
import json

ticker = 'KOSDAQ'


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    request_url = "https://finance.naver.com/sise/sise_index.nhn?code=%s" % (ticker)
     
    session = HTMLSession()

    #request_url = base_url + query_keyword
    print(request_url)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup

def parse(url, query_keyword):

    now_value = url.find("em",attrs={"id":"now_value"})
    if now_value is not None: now_value = now_value.getText() #.replace('\n', '')
    else: now_value = ""

    change_value_and_rate = url.find("span",attrs={"id":"change_value_and_rate"})
    if change_value_and_rate is not None: change_value_and_rate = change_value_and_rate.getText()
    else: change_value_and_rate = ""

    table = url.find('table', attrs={"class":"table_kos_index"}) # Fetching Table
    rows = table.find_all('tr') # Feching table rows

    dl = url.find('dl', attrs={"class":"lst_kos_info"}) # Feching all data from description list
    dd = dl.find_all('dd')
    dt = dl.find_all('dt')

    # Fetching Table Data
    tab_r1c1_text  = rows[0].find('th', attrs={"class":"th"})
    if tab_r1c1_text is not None: tab_r1c1_text = tab_r1c1_text.getText() #.replace('\n', '')
    else: tab_r1c1_text = ""
    
    tab_r1c1_value = rows[0].find('td', attrs={"id":"quant"})
    if tab_r1c1_value is not None: tab_r1c1_value = tab_r1c1_value.getText() #.replace('\n', '')
    else: tab_r1c1_value = ""

    
    tab_r2c1_text  = rows[1].find('th')
    if tab_r2c1_text is not None: tab_r2c1_text = tab_r2c1_text.getText() #.replace('\n', '')
    else: tab_r2c1_text = ""

    tab_r2c1_value = rows[1].find('td', attrs={"id":"high_value"})
    if tab_r2c1_value is not None: tab_r2c1_value = tab_r2c1_value.getText() #.replace('\n', '')
    else: tab_r2c1_value = ""


    tab_r3c1_text  = rows[2].find('th')
    if tab_r3c1_text is not None: tab_r3c1_text = tab_r3c1_text.getText() #.replace('\n', '')
    else: tab_r3c1_text = ""

    tab_r3c1_value = rows[2].find('td', attrs={"class":"td"})
    if tab_r3c1_value is not None: tab_r3c1_value = tab_r3c1_value.getText() #.replace('\n', '')
    else: tab_r3c1_value = ""


    tab_r1c2_text  = rows[0].find('th', attrs={"class":"th2"})
    if tab_r1c2_text is not None: tab_r1c2_text = tab_r1c2_text.getText() #.replace('\n', '')
    else: tab_r1c2_text = ""

    tab_r1c2_value = rows[0].find('td', attrs={"id":"amount"})
    if tab_r1c2_value is not None: tab_r1c2_value = tab_r1c2_value.getText() #.replace('\n', '')
    else: tab_r1c2_value = ""

    
    tab_r2c2_text  = rows[1].find('th')
    if tab_r2c2_text is not None: tab_r2c2_text = tab_r2c2_text.getText() #.replace('\n', '')
    else: tab_r2c2_text = ""

    tab_r2c2_value = rows[1].find('td', attrs={"id":"low_value"})
    if tab_r2c2_value is not None: tab_r2c2_value = tab_r2c2_value.getText() #.replace('\n', '')
    else: tab_r2c2_value = ""

    tab_r3c2_text  = rows[2].find('th')
    if tab_r3c2_text is not None: tab_r3c2_text = tab_r3c2_text.getText() #.replace('\n', '')
    else: tab_r3c2_text = ""

    tab_r3c2_value = rows[2].find('td', attrs={"class":"td2"})
    if tab_r3c2_value is not None: tab_r3c2_value = tab_r3c2_value.getText() #.replace('\n', '')
    else: tab_r3c2_value = ""


    tab_r4c1_text  = rows[3].find('td').find('ul').find('li', attrs={"class":"lst"}).find('span')
    if tab_r4c1_text is not None: tab_r4c1_text = tab_r4c1_text.getText() #.replace('\n', '')
    else: tab_r4c1_text = ""

    tab_r4c1_value = rows[3].find('td').find('ul').find('li', attrs={"class":"lst"}).find('a')
    if tab_r4c1_value is not None: tab_r4c1_value = tab_r4c1_value.getText() #.replace('\n', '')
    else: tab_r4c1_value = ""

    
    tab_r4c2_text  = rows[3].find('td').find('ul').find('li', attrs={"class":"lst2"}).find('span')
    if tab_r4c2_text is not None: tab_r4c2_text = tab_r4c2_text.getText() #.replace('\n', '')
    else: tab_r4c2_text = ""

    tab_r4c2_value = rows[3].find('td').find('ul').find('li', attrs={"class":"lst2"}).find('a')
    if tab_r4c2_value is not None: tab_r4c2_value = tab_r4c2_value.getText() #.replace('\n', '')
    else: tab_r4c2_value = ""


    tab_r4c3_text  = rows[3].find('td').find('ul').find('li', attrs={"class":"lst3"}).find('span')
    if tab_r4c3_text is not None: tab_r4c3_text = tab_r4c3_text.getText() #.replace('\n', '')
    else: tab_r4c3_text = ""

    tab_r4c3_value = rows[3].find('td').find('ul').find('li', attrs={"class":"lst3"}).find('a')
    if tab_r4c3_value is not None: tab_r4c3_value = tab_r4c3_value.getText() #.replace('\n', '')
    else: tab_r4c3_value = ""


    tab_r4c4_text  = rows[3].find('td').find('ul').find('li', attrs={"class":"lst4"}).find('span')
    if tab_r4c4_text is not None: tab_r4c4_text = tab_r4c4_text.getText() #.replace('\n', '')
    else: tab_r4c4_text = ""

    tab_r4c4_value = rows[3].find('td').find('ul').find('li', attrs={"class":"lst4"}).find('a')
    if tab_r4c4_value is not None: tab_r4c4_value = tab_r4c4_value.getText() #.replace('\n', '')
    else: tab_r4c4_value = ""

    tab_r4c5_text  = rows[3].find('td').find('ul').find('li', attrs={"class":"lst5"}).find('span')
    if tab_r4c5_text is not None: tab_r4c5_text = tab_r4c5_text.getText() #.replace('\n', '')
    else: tab_r4c5_text = ""

    tab_r4c5_value = rows[3].find('td').find('ul').find('li', attrs={"class":"lst5"}).find('a')
    if tab_r4c5_value is not None: tab_r4c5_value = tab_r4c5_value.getText() #.replace('\n', '')
    else: tab_r4c5_value = ""

    # Fetching Description List Data

    des_c1c1_value = dd[0].find('span')
    if des_c1c1_value is not None: des_c1c1_value = des_c1c1_value.getText() #.replace('\n', '')
    else: des_c1c1_value = ""

    des_c1c1_text  = dd[0]
    if des_c1c1_text is not None: des_c1c1_text = des_c1c1_text.getText().replace(des_c1c1_value, '')
    else: des_c1c1_text = ""


    des_c1c2_value = dd[1].find('span')
    if des_c1c2_value is not None: des_c1c2_value = des_c1c2_value.getText() #.replace('\n', '')
    else: des_c1c2_value = ""

    des_c1c2_text  = dd[1]
    if des_c1c2_text is not None: des_c1c2_text = des_c1c2_text.getText().replace(des_c1c2_value, '')
    else: des_c1c2_text = ""

  
    des_c1c3_value = dd[2].find('span')
    if des_c1c3_value is not None: des_c1c3_value = des_c1c3_value.getText() #.replace('\n', '')
    else: des_c1c3_value = ""

    des_c1c3_text  = dd[2]
    if des_c1c3_text is not None: des_c1c3_text = des_c1c3_text.getText().replace(des_c1c3_value, '')
    else: des_c1c3_text = ""


    des_c2c1_value = dd[3].find('span')
    if des_c2c1_value is not None: des_c2c1_value = des_c2c1_value.getText() #.replace('\n', '')
    else: des_c2c1_value = ""

    des_c2c1_text  = dd[3]
    if des_c2c1_text is not None: des_c2c1_text = des_c2c1_text.getText().replace(des_c2c1_value, '')
    else: des_c2c1_text = ""


    des_c2c2_value = dd[4].find('span')
    if des_c2c2_value is not None: des_c2c2_value = des_c2c2_value.getText() #.replace('\n', '')
    else: des_c2c2_value = ""

    des_c2c2_text  = dd[4]
    if des_c2c2_text is not None: des_c2c2_text = des_c2c2_text.getText().replace(des_c2c2_value, '')
    else: des_c2c2_text = ""


    des_c2c3_value = dd[5].find('span')
    if des_c2c3_value is not None: des_c2c3_value = des_c2c3_value.getText() #.replace('\n', '')
    else: des_c2c3_value = ""

    des_c2c3_text  = dd[5]
    if des_c2c3_text is not None: des_c2c3_text = des_c2c3_text.getText().replace(des_c2c3_value, '')
    else: des_c2c3_text = ""


    tab_r4_text  = rows[3].find('th').find('span')
    if tab_r4_text is not None: tab_r4_text = tab_r4_text.getText() #.replace('\n', '')
    else: tab_r4_text = ""

    tab_r4_value = {
        'tab_r4c1_text': tab_r4c1_text,
        'tab_r4c1_value' : tab_r4c1_value,

        'tab_r4c2_text': tab_r4c2_text,
        'tab_r4c2_value' : tab_r4c2_value,

        'tab_r4c3_text': tab_r4c3_text,
        'tab_r4c3_value' : tab_r4c3_value,
         
        'tab_r4c4_text': tab_r4c4_text,
        'tab_r4c4_value' : tab_r4c4_value,

        'tab_r4c5_text': tab_r4c5_text,
        'tab_r4c5_value' : tab_r4c5_value
    }

    table_data = {
        'tab_r1c1_text': tab_r1c1_text,
        'tab_r1c1_value'  : tab_r1c1_value,
        
        'tab_r2c1_text': tab_r2c1_text,
        'tab_r2c1_value'      : tab_r2c1_value,

        'tab_r3c1_text': tab_r3c1_text,
        'tab_r3c1_value'      : tab_r3c1_value,

        'tab_r1c2_text':tab_r1c2_text,
        'tab_r1c2_value' : tab_r1c2_value,

        'tab_r2c2_text':tab_r2c2_text,
        'tab_r2c2_value'      : tab_r2c2_value,

        'tab_r3c2_text': tab_r3c2_text,
        'tab_r3c2_value'      : tab_r3c2_value, 
        
        'tab_r4_text': tab_r4_text,
        'tab_r4_value'     : tab_r4_value
    }

    des_c1_text  = dt[0].getText()
    des_c1_value = {
        'des_c1c1_text'     : des_c1c1_text,
        'des_c1c1_value'    : des_c1c1_value,

        'des_c1c2_text'     : des_c1c2_text,
        'des_c1c2_value'    : des_c1c2_value,

        'des_c1c3_text'    : des_c1c3_text,
        'des_c1c3_value'   : des_c1c3_value
    }

    des_c2_text  = dt[1].getText()
    des_c2_value = {
        'des_c2c1_text'  : des_c2c1_text,
        'des_c2c1_value' : des_c2c1_value,

        'des_c2c2_text'  : des_c2c2_text,
        'des_c2c2_value' : des_c2c2_value,

        'des_c2c3_text'  : des_c2c3_text,
        'des_c2c3_value' : des_c2c3_value
    }

    description_list_data = {
        'des_c1_text'  : des_c1_text,
        'des_c1_value' : des_c1_value,
         
        'des_c2_text'  : des_c2_text,
        'des_c2_value' : des_c2_value,
    }

    output = {
        "ticker": ticker,
        "Now Value": now_value, 
        "Change Value and Rate": change_value_and_rate, 
        "Table Data": table_data,
        "Description List": description_list_data    
    }

    # table = url.find('table', attrs={"class":"table_kos_index"})
    # rows = table.find_all('tr')
    # for row in rows:
    #     cols = row.find_all(['th', 'td'])
    #     cols = [ele.text.strip() for ele in cols]
    #     table_data.append(cols)
    
    # dl = url.find('dl', attrs={"class":"lst_kos_info"})
    # descriptions = dl.find_all(['dt', 'dd'])

    # for description in descriptions:
    #     description_list.append(description.getText())

    return output

def main_fun_2(query):
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    query_keyword = query
    page = get_search_url(query_keyword)
    scraped_data = parse(page, query_keyword)


    with open('%s-summary.json' % (ticker), 'w', encoding='utf-8') as file:
        json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':
    
    main_fun_2(ticker)






# from lxml import html
# from requests_html import HTMLSession
# from collections import OrderedDict
# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
# from urllib.parse import urljoin
# import codecs
# import json

# ticker = 'KOSDAQ'


# def get_search_url(query_keyword):
#     """
#     parse html page form url
#     :param text:
#     :return:
#     keyword': elements from the queries
#     """

#     request_url = "https://finance.naver.com/sise/sise_index.nhn?code=%s" % (ticker)
     
#     session = HTMLSession()

#     #request_url = base_url + query_keyword
#     print(request_url)
#     resp = session.get(request_url)
#     soup = BeautifulSoup(resp.text, "lxml")
#     return soup

# def parse(url, query_keyword):

#     now_value = url.find("em",attrs={"id":"now_value"})
#     if now_value is not None: now_value = now_value.getText() #.replace('\n', '')
#     else: now_value = ""

#     change_value_and_rate = url.find("span",attrs={"id":"change_value_and_rate"})
#     if change_value_and_rate is not None: change_value_and_rate = change_value_and_rate.getText()
#     else: change_value_and_rate = ""

#     table_data = []
#     description_list = []

#     output = {
#         "ticker": ticker,
#         "Now Value": now_value, 
#         "Change Value and Rate": change_value_and_rate, 
#         "Table Data": table_data,
#         "Description List": description_list    
#     }

#     table = url.find('table', attrs={"class":"table_kos_index"})
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all(['th', 'td'])
#         cols = [ele.text.strip() for ele in cols]
#         table_data.append(cols)
    
#     dl = url.find('dl', attrs={"class":"lst_kos_info"})
#     descriptions = dl.find_all(['dt', 'dd'])

#     for description in descriptions:
#         description_list.append(description.getText())

#     return output

# def main_fun_2(query):
#     """
#     main function for interact with this module
#     :param text: user input
#     :return: product_title, product_price
#     """
#     query_keyword = query
#     page = get_search_url(query_keyword)
#     scraped_data = parse(page, query_keyword)


#     with open('%s-summary.json' % (ticker), 'w', encoding='utf-8') as file:
#         json.dump(scraped_data, file, ensure_ascii=False)

#     return scraped_data


# if __name__ == '__main__':
    
#     main_fun_2(ticker)