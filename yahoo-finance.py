from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

ticker = 'JPXN'


def get_search_url(query_keyword):
    """
    parse html page form url
    :param text:
    :return:
    keyword': elements from the queries
    """

    request_url = "http://finance.yahoo.com/quote/%s?p=%s" % (ticker, ticker)
     
    session = HTMLSession()

    #request_url = base_url + query_keyword
    print(request_url)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup

def parse(url, query_keyword):

    previous_close = url.find("td",attrs={"data-test":"PREV_CLOSE-value"})
    if previous_close is not None: previous_close = previous_close.getText() #.replace('\n', '')
    else: previous_close = ""

    o_open = url.find("td",attrs={"data-test":"OPEN-value"})
    if o_open is not None: o_open = o_open.getText()
    else: o_open = ""

    bid = url.find("td",attrs={"data-test":"BID-value"})
    if bid is not None: bid = bid.getText()
    else: bid = ""

    ask = url.find("td",attrs={"data-test":"ASK-value"})
    if ask is not None: ask = ask.getText()
    else: ask = ""

    days_range = url.find("td",attrs={"data-test":"DAYS_RANGE-value"})
    if days_range is not None: days_range = days_range.getText()
    else: days_range = ""

    week_range_52 = url.find("td",attrs={"data-test":"FIFTY_TWO_WK_RANGE-value"})
    if week_range_52 is not None: week_range_52 = week_range_52.getText()
    else: week_range_52 = ""

    volume = url.find("td",attrs={"data-test":"TD_VOLUME-value"})
    if volume is not None: volume = volume.getText()
    else: volume = ""

    avg_volume = url.find("td",attrs={"data-test":"AVERAGE_VOLUME_3MONTH-value"})
    if avg_volume is not None: avg_volume = avg_volume.getText()
    else: avg_volume = ""

    market_cap = url.find("td",attrs={"data-test":"MARKET_CAP-value"})
    if market_cap is not None: market_cap = market_cap.getText()
    else: market_cap = ""

    net_asset = url.find("td",attrs={"data-test":"NET_ASSETS-value"})
    if net_asset is not None: net_asset = net_asset.getText()
    else: net_asset = ""

    nav = url.find("td",attrs={"data-test":"NAV-value"})
    if nav is not None: nav = nav.getText()
    else: nav = ""
    
    pe_ratio_ttm = url.find("td",attrs={"data-test":"PE_RATIO-value"})
    if pe_ratio_ttm is not None: pe_ratio_ttm = pe_ratio_ttm.getText()
    else: pe_ratio_ttm = ""

    eps_ratio = url.find("td",attrs={"data-test":"EPS_RATIO-value"})
    if eps_ratio is not None: eps_ratio = eps_ratio.getText()
    else: eps_ratio = ""

    earnings_date = url.find("td",attrs={"data-test":"EARNINGS_DATE-value"})
    if earnings_date is not None: earnings_date = earnings_date.getText()
    else: earnings_date = ""

    dividend_and_yield = url.find("td",attrs={"data-test":"DIVIDEND_AND_YIELD-value"})
    if dividend_and_yield is not None: dividend_and_yield = dividend_and_yield.getText()
    else: dividend_and_yield = ""
    
    ex_dividend_date = url.find("td",attrs={"data-test":"EX_DIVIDEND_DATE-value"})
    if ex_dividend_date is not None: ex_dividend_date = ex_dividend_date.getText()
    else: ex_dividend_date = ""
    
    one_year_target_price = url.find("td",attrs={"data-test":"ONE_YEAR_TARGET_PRICE-value"})
    if one_year_target_price is not None: one_year_target_price = one_year_target_price.getText()
    else: one_year_target_price = ""

    yyield = url.find("td",attrs={"data-test":"TD_YIELD-value"})
    if yyield is not None: yyield = yyield.getText()
    else: yyield = ""

    ytd_daily_total_return = url.find("td",attrs={"data-test":"ASK-value"})
    if ytd_daily_total_return is not None: ytd_daily_total_return = ytd_daily_total_return.getText()
    else: ytd_daily_total_return = ""

    beta_5Y_monthly = url.find("td",attrs={"data-test":"BETA_5Y-value"})
    if beta_5Y_monthly is not None: beta_5Y_monthly = beta_5Y_monthly.getText()
    else: beta_5Y_monthly = ""

    expense_ratio_net = url.find("td",attrs={"data-test":"ASK-value"})
    if expense_ratio_net is not None: expense_ratio_net = expense_ratio_net.getText()
    else: expense_ratio_net = ""

    inception_date = url.find("td",attrs={"data-test":"ASK-value"})
    if inception_date is not None: inception_date = inception_date.getText()
    else: inception_date = ""

    output = {
        "Previous Close": previous_close, 
        "Open": o_open, 
        "Bid":  bid, 
        "Ask":  ask, 
        "Day's Range": days_range, 
        "52 Week Range": week_range_52, 
        "Volume": volume, 
        "Avg. Volume": avg_volume,
        "Market Cap": market_cap, 
        "Net Asset": net_asset,
        "NAV": nav,
        "PE Ratio (TTM)": pe_ratio_ttm,
        "EPS Ratio(TTM)": eps_ratio,
        "Earnings Date": earnings_date,
        "Dividend and Yield": dividend_and_yield,
        "Ex Dividend Date": ex_dividend_date,
        "One Year Target Price": one_year_target_price,
        "Yield": yyield,
        "YTD Daily Total Return": ytd_daily_total_return, 
        "Beta (5Y Monthly)": beta_5Y_monthly, 
        "Expense Ratio (net)": expense_ratio_net,
        "Inception Date": inception_date, 
        "ticker": ticker
    }
    
    file = open('%s-summary.json' % (ticker), 'w', encoding='utf-8')
    json.dump(output, file, ensure_ascii=False)

    return output

    # "Previous Close": "16.94", 
    # "Open": "19.39", 
    # "Bid": "0.00 x 40700", 
    # "Ask": "0.00 x 21500", 
    # "Day's Range": "19.11 - 19.44", 
    # "52 Week Range": "5.35 - 19.44", 
    # "Volume": "42,258,862", 
    # "Avg. Volume": "1,027,481", 
    # "Net Asset": "3.411B", 
    # "Beta (5Y Monthly)": "1.90", 
    # "PE Ratio (TTM)": "35.57", 
    # "EPS (TTM)": 0.54, 
    # "Earnings Date": "2021-05-04 to 2021-05-10", 
    # "Forward Dividend & Yield": "0.12 (0.71%)", 
    # "Ex-Dividend Date": "Mar 11, 2021", 
    # "1y Target Est": 18.11, 
    # "url": "http://finance.yahoo.com/quote/STAY?p=STAY", 
    # "ticker": "STAY"
    

def main_fun_2(query):
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    query_keyword = query
    page = get_search_url(query_keyword)
    scraped_data = parse(page, query_keyword)


    with open('%s-summary.json' % (ticker), 'w') as fp:
        json.dump(scraped_data, fp, indent=4)

    return scraped_data


if __name__ == '__main__':
    
    main_fun_2(ticker)