from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

#ticker = 'JPXN'

def get_search_ticker(ticker_search_keyword):

    ticker_search_url = "https://finance.yahoo.com/lookup?s=%s" % ticker_search_keyword
     
    session = HTMLSession()

    ticker_resp = session.get(ticker_search_url)
    ticker_soup = BeautifulSoup(ticker_resp.text, "lxml")

    ticker = ticker_soup.find("td", attrs={"class": "data-col0 Ta(start) Pstart(6px) Pend(15px)"}).find("a").getText()

    return ticker


def get_search_url(ticker_search_keyword):

    ticker_search_url = "https://finance.yahoo.com/lookup?s=%s" % ticker_search_keyword
     
    session = HTMLSession()

    ticker_resp = session.get(ticker_search_url)
    ticker_soup = BeautifulSoup(ticker_resp.text, "lxml")

    ticker_url = ticker_soup.find("td", attrs={"class": "data-col0 Ta(start) Pstart(6px) Pend(15px)"}).find("a").get('href')

    base_url = "https://finance.yahoo.com/"

    request_url = urljoin(base_url, ticker_url)
     
    session = HTMLSession()

    #request_url = base_url + query_keyword
    print(request_url)
    resp = session.get(request_url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup

def parse(page, ticker):

    previous_close = page.find("td",attrs={"data-test":"PREV_CLOSE-value"})
    if previous_close is not None: previous_close = previous_close.getText() #.replace('\n', '')
    else: previous_close = ""

    o_open = page.find("td",attrs={"data-test":"OPEN-value"})
    if o_open is not None: o_open = o_open.getText()
    else: o_open = ""

    bid = page.find("td",attrs={"data-test":"BID-value"})
    if bid is not None: bid = bid.getText()
    else: bid = ""

    ask = page.find("td",attrs={"data-test":"ASK-value"})
    if ask is not None: ask = ask.getText()
    else: ask = ""

    days_range = page.find("td",attrs={"data-test":"DAYS_RANGE-value"})
    if days_range is not None: days_range = days_range.getText()
    else: days_range = ""

    week_range_52 = page.find("td",attrs={"data-test":"FIFTY_TWO_WK_RANGE-value"})
    if week_range_52 is not None: week_range_52 = week_range_52.getText()
    else: week_range_52 = ""

    volume = page.find("td",attrs={"data-test":"TD_VOLUME-value"})
    if volume is not None: volume = volume.getText()
    else: volume = ""

    avg_volume = page.find("td",attrs={"data-test":"AVERAGE_VOLUME_3MONTH-value"})
    if avg_volume is not None: avg_volume = avg_volume.getText()
    else: avg_volume = ""

    market_cap = page.find("td",attrs={"data-test":"MARKET_CAP-value"})
    if market_cap is not None: market_cap = market_cap.getText()
    else: market_cap = ""

    net_asset = page.find("td",attrs={"data-test":"NET_ASSETS-value"})
    if net_asset is not None: net_asset = net_asset.getText()
    else: net_asset = ""

    nav = page.find("td",attrs={"data-test":"NAV-value"})
    if nav is not None: nav = nav.getText()
    else: nav = ""
    
    pe_ratio_ttm = page.find("td",attrs={"data-test":"PE_RATIO-value"})
    if pe_ratio_ttm is not None: pe_ratio_ttm = pe_ratio_ttm.getText()
    else: pe_ratio_ttm = ""

    eps_ratio = page.find("td",attrs={"data-test":"EPS_RATIO-value"})
    if eps_ratio is not None: eps_ratio = eps_ratio.getText()
    else: eps_ratio = ""

    earnings_date = page.find("td",attrs={"data-test":"EARNINGS_DATE-value"})
    if earnings_date is not None: earnings_date = earnings_date.getText()
    else: earnings_date = ""

    dividend_and_yield = page.find("td",attrs={"data-test":"DIVIDEND_AND_YIELD-value"})
    if dividend_and_yield is not None: dividend_and_yield = dividend_and_yield.getText()
    else: dividend_and_yield = ""
    
    ex_dividend_date = page.find("td",attrs={"data-test":"EX_DIVIDEND_DATE-value"})
    if ex_dividend_date is not None: ex_dividend_date = ex_dividend_date.getText()
    else: ex_dividend_date = ""
    
    one_year_target_price = page.find("td",attrs={"data-test":"ONE_YEAR_TARGET_PRICE-value"})
    if one_year_target_price is not None: one_year_target_price = one_year_target_price.getText()
    else: one_year_target_price = ""

    yyield = page.find("td",attrs={"data-test":"TD_YIELD-value"})
    if yyield is not None: yyield = yyield.getText()
    else: yyield = ""

    ytd_daily_total_return = page.find("td",attrs={"data-test":"ASK-value"})
    if ytd_daily_total_return is not None: ytd_daily_total_return = ytd_daily_total_return.getText()
    else: ytd_daily_total_return = ""

    beta_5Y_monthly = page.find("td",attrs={"data-test":"BETA_5Y-value"})
    if beta_5Y_monthly is not None: beta_5Y_monthly = beta_5Y_monthly.getText()
    else: beta_5Y_monthly = ""

    expense_ratio_net = page.find("td",attrs={"data-test":"ASK-value"})
    if expense_ratio_net is not None: expense_ratio_net = expense_ratio_net.getText()
    else: expense_ratio_net = ""

    inception_date = page.find("td",attrs={"data-test":"ASK-value"})
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

    return output

def main_fun_2(keyword):
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    page = get_search_url(keyword)
    ticker = get_search_ticker(keyword)
    scraped_data = parse(page, ticker)


    file = open('%s-summary.json' % (ticker), 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':

    ticker_search_keyword = 'tesla'

    main_fun_2(ticker_search_keyword)