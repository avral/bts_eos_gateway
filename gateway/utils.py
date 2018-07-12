from eosiopy.nodenetwork import NodeNetwork


def account_exists(account_name):
    return 'account_name' in NodeNetwork.get_account({
        'account_name': account_name
    })
