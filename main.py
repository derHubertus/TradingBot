import alpaca_trade_api as alpaca

endpoint_url = "https://api.alpaca.markets"

api = alpaca.REST("AKIZMY06T8MIP4ADKKOJ", "EHwINcWqlhZmEEnf0gRugRzqe8wUSsaDhHcPOkn7", endpoint_url)

account = api.get_account()
print(account.status)

