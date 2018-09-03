from selenium.webdriver.common.keys import Keys
from umihico_commons.chrome_wrapper import ALL_ELEMENTS, RETERN_TEXT


def nomura_apply_ipo(chrome, deal_password):
    applied_codes = []
    get_code_action = ("//span[@class='txt-code']", RETERN_TEXT)
    ipo_list_xpath = "//a[@class='btn-secondary ico-r']"
    for i in range(100):
        actions = [
            "https://hometrade.nomura.co.jp/web/rmfTrdStkIpoLstAction.do",
            (ipo_list_xpath, i),
            ("//div[@class='layout-panel']/label", ALL_ELEMENTS),
            "//button[@class='btn-proceed apl-js-btn-agreem']",
            get_code_action,
            ("//p[contains(@class, 'ico-doc-text')]/a", ALL_ELEMENTS),
            "//button[@class='btn-proceed apl-js-btn-agreem']",
            "//button[@class='btn-proceed']",
            ("//input[@id='passwd']", deal_password),
            "//button[@class='btn-proceed']",

        ]
        try:
            elements = chrome.do_actions(actions)
        except (Exception, ) as e:
            if ipo_list_xpath in str(e):
                break
            else:
                raise
        applied_code = elements[actions.index(get_code_action)]
        applied_codes.append(applied_code)
    return applied_codes


def daiwa_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def mizuho_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def nikko_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def mufj_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def sbi_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def monex_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def matsui_apply_ipo(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


if __name__ == '__main__':

    from umihico_commons.chrome_wrapper import Chrome
    try:
        from login import *
    except (Exception, ) as e:
        from .login import *
    from passwords import load_passwords
    password_dict = load_passwords()
    chrome = Chrome()
    test_funcs = [
        (nomura_login, nomura_apply_ipo, "nomura"),
        # (daiwa_login,daiwa_apply_ipo "daiwa"),
        # (mizuho_login,mizuho_apply_ipo "mizuho"),
        # (nikko_login,nikko_apply_ipo "nikko"),
        # (mufj_login,mufj_apply_ipo "mufj"),
        # (sbi_login,sbi_apply_ipo "sbi"),
        # (monex_login,monex_apply_ipo "monex"),
        # (matsui_login,matsui_apply_ipo "matsui"),
    ]
    for test_login_func, test_apply_func, password_key in test_funcs:
        login_args = password_dict[password_key]["login_args"]
        test_login_func(chrome, *login_args)
        apply_args = password_dict[password_key]["apply_args"]
        applied_codes = test_apply_func(chrome, *apply_args)
        print(applied_codes)
