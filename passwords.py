

try:
    import plain_passwords as p_pwds
except (Exception, ) as e:
    from . import plain_passwords as p_pwds


def load_passwords():
    nomura = {
        'branch_no': p_pwds.nomura_branch_no,
        'account_no': p_pwds.nomura_account_no,
        'login_password': p_pwds.nomura_login_password,
        'deal_password': p_pwds.nomura_deal_password,
        'login_args': (p_pwds.nomura_branch_no, p_pwds.nomura_account_no, p_pwds.nomura_login_password),
        'apply_args': (p_pwds.nomura_deal_password,), }
    # daiwa = {
    #     'branch_no': p_pwds.daiwa_branch_no,
    #     'account_no': p_pwds.daiwa_account_no,
    #     'user_name': p_pwds.daiwa_user_name,
    #     'login_id': p_pwds.daiwa_login_id,
    #     'login_password': p_pwds.daiwa_login_password,
    #     'deal_password': p_pwds.daiwa_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # mizuho = {
    #     'branch_no': p_pwds.mizuho_branch_no,
    #     'account_no': p_pwds.mizuho_account_no,
    #     'user_name': p_pwds.mizuho_user_name,
    #     'login_id': p_pwds.mizuho_login_id,
    #     'login_password': p_pwds.mizuho_login_password,
    #     'deal_password': p_pwds.mizuho_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # nikko = {
    #     'branch_no': p_pwds.nikko_branch_no,
    #     'account_no': p_pwds.nikko_account_no,
    #     'user_name': p_pwds.nikko_user_name,
    #     'login_id': p_pwds.nikko_login_id,
    #     'login_password': p_pwds.nikko_login_password,
    #     'deal_password': p_pwds.nikko_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # mufj = {
    #     'branch_no': p_pwds.mufj_branch_no,
    #     'account_no': p_pwds.mufj_account_no,
    #     'user_name': p_pwds.mufj_user_name,
    #     'login_id': p_pwds.mufj_login_id,
    #     'login_password': p_pwds.mufj_login_password,
    #     'deal_password': p_pwds.mufj_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # sbi = {
    #     'branch_no': p_pwds.sbi_branch_no,
    #     'account_no': p_pwds.sbi_account_no,
    #     'user_name': p_pwds.sbi_user_name,
    #     'login_id': p_pwds.sbi_login_id,
    #     'login_password': p_pwds.sbi_login_password,
    #     'deal_password': p_pwds.sbi_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # monex = {
    #     'branch_no': p_pwds.monex_branch_no,
    #     'account_no': p_pwds.monex_account_no,
    #     'user_name': p_pwds.monex_user_name,
    #     'login_id': p_pwds.monex_login_id,
    #     'login_password': p_pwds.monex_login_password,
    #     'deal_password': p_pwds.monex_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    # matsui = {
    #     'branch_no': p_pwds.matsui_branch_no,
    #     'account_no': p_pwds.matsui_account_no,
    #     'user_name': p_pwds.matsui_user_name,
    #     'login_id': p_pwds.matsui_login_id,
    #     'login_password': p_pwds.matsui_login_password,
    #     'deal_password': p_pwds.matsui_deal_password,
    #     'login_args': (),
    #     'apply_args': ()}
    passwords = {
        "nomura": nomura,
        # 'daiwa': daiwa,
        # 'mizuho': mizuho,
        # 'nikko': nikko,
        # 'mufj': mufj,
        # 'sbi': sbi,
        # 'monex': monex,
        # 'matsui': matsui,
    }
    return passwords
