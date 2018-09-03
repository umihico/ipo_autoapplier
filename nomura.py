from umihico_commons.chrome_wrapper import Chrome
from selenium.webdriver.common.keys import Keys
try:
    from passwords import passwords
except (Exception, ) as e:
    from .passwords import passwords


def login(c):
    url = "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do"
    c.get(url)
    c.xpath(
        "//input[@id='branchNo']")[0].send_keys(passwords['nomura']['branch_no'])
    c.xpath(
        "//input[@id='accountNo']")[0].send_keys(passwords['nomura']['account_no'])
    c.xpath(
        "//input[@id='passwd1']")[0].send_keys(passwords['nomura']['password'])
    c.xpath(
        "//input[@id='passwd1']")[0].send_keys(Keys.RETURN)


def apply_ipo(c):
    risk_agreement_checkboxes = c.xpath("//div[@class='layout-panel']/label")
    for checkbox in risk_agreement_checkboxes:
        checkbox.click()
    c.xpath(
        "//button[@class='btn-proceed apl-js-btn-agreem']")[0].click()
    documents = c.xpath("//p[contains(@class, 'ico-doc-text')]/a")
    for document in documents:
        document.click()
    c.xpath(
        "//button[@class='btn-proceed apl-js-btn-agreem']")[0].click()
    c.xpath("//button[@class='btn-proceed']")[0].click()
    c.xpath(
        "//input[@id='passwd']")[0].send_keys(passwords['nomura']['deal_password'])
    c.xpath("//button[@class='btn-proceed']")[0].click()


def test():
    c = Chrome(cookie_key=None, headless=False)
    login(c)
    ipo_list_url = "https://hometrade.nomura.co.jp/web/rmfTrdStkIpoLstAction.do"
    c.get(ipo_list_url)
    ipo_index = 0
    while True:
        ipo_buttons_xpath = "//a[@class='btn-secondary ico-r']"
        ipo_buttons = c.xpath(ipo_buttons_xpath)
        if ipo_index < len(ipo_buttons):
            ipo_buttons[ipo_index].click()
            apply_ipo(c)
            ipo_index += 1
            c.get(ipo_list_url)
        else:
            break


if __name__ == '__main__':
    test()
