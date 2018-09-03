from selenium.webdriver.common.keys import Keys


def nomura_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def daiwa_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def mizuho_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def nikko_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def mufj_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def sbi_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def monex_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def matsui_login(chrome, branch_no, account_no, login_password):
    actions = [
        "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiInitAction.do",
        ("//input[@id='branchNo']", branch_no),
        ("//input[@id='accountNo']", account_no),
        ("//input[@id='passwd1']", login_password),
        ("//input[@id='passwd1']", Keys.RETURN),
    ]
    chrome.do_actions(actions)


def login_test():
    from umihico_commons.chrome_wrapper import Chrome
    from passwords import load_passwords
    password_dict = load_passwords()
    chrome = Chrome()
    test_login_funcs = [
        (nomura_login, "nomura"),
        # (daiwa_login, "daiwa"),
        # (mizuho_login, "mizuho"),
        # (nikko_login, "nikko"),
        # (mufj_login, "mufj"),
        # (sbi_login, "sbi"),
        # (monex_login, "monex"),
        # (matsui_login, "matsui"),
    ]
    for test_login_func, password_key in test_login_funcs:
        login_args = password_dict[password_key]["login_args"]
        test_login_func(chrome, *login_args)


if __name__ == '__main__':
    login_test()
