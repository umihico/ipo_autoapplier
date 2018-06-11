from umihico_commons.chrome_wrapper import Chrome
from passwords import passwords
from selenium.webdriver.common.keys import Keys


def test():
    url = "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do"
    c = Chrome(cookie_key=None, headless=False)
    c.get(url)
    c.xpath(
        "//input[@id='branchNo']")[0].send_keys(passwords['nomura_ht']['branch_no'])
    c.xpath(
        "//input[@id='accountNo']")[0].send_keys(passwords['nomura_ht']['account_no'])
    c.xpath(
        "//input[@id='passwd1']")[0].send_keys(passwords['nomura_ht']['password'])
    c.xpath(
        "//input[@id='passwd1']")[0].send_keys(Keys.RETURN)
    c.get("https://hometrade.nomura.co.jp/web/rmfTrdStkIpoLstAction.do")


if __name__ == '__main__':
    test()
    "github test"
