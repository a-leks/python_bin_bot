import logging
import requests

logger = logging.getLogger()


# "https://tetnet.binancefuture.com"
# "wss://fstream.binance.com"

def get_contracts():

    requests.get("https://fapi.binance.com")