import logging
from pycoingecko import CoinGeckoAPI
import time

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

cg = CoinGeckoAPI()


class GeckoReport:

    def __init__(self):
        pass

    def get_coins_markets(self, page_limit=0):
        cm_list = []
        page = 1
        while True:
            logger.debug(f'page: {page}')
            cm_page = cg.get_coins_markets(
                vs_currency='usd',
                per_page='250',
                page=str(page),
                price_change_percentage='24h,7d,30d'
            )

            [cm_list.append(cm) for cm in cm_page]

            if page == page_limit or len(cm_page) == 0:
                break

            page += 1

            # Remain below API rate limit
            #time.sleep(0.5)
        
        return cm_list


if __name__ == '__main__':
    from pprint import pprint

    gecko_report = GeckoReport()
    coins_markets = gecko_report.get_coins_markets()

    pprint(coins_markets)
    logger.debug(f'len(coins_markets): {len(coins_markets)}')