import argparse
import csv
import datetime
from geckoreport import GeckoReport
import logging
import os

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument(
    '--pages', '-p', type=int, default=7,
    help='Number of pages of coins to retrieve from Coingecko.'
    )
args = parser.parse_args()

# Number of 250 coin pages to include in report (0 for all available)
page_limit = args.pages

# Directory for report output
report_directory = 'reports'

if not os.path.exists(report_directory):
    logger.info('Creating report directory.')
    os.makedirs(report_directory)


if __name__ == '__main__':
    gecko_report = GeckoReport()

    logger.info('Gathering report data.')
    report_data = gecko_report.get_coins_markets(page_limit=page_limit)

    #csv_header = 'Rank, Symbol, Name, ID, Price, MarketCap, Volume, 24h_high, 24h_low, Price_change_24h, Price_change_30d, MarketCap_change_24hr, Circulated_supply, Total_supply, All-time_high_percentage, All-time_low_percentage'

    dt_current = datetime.datetime.now().strftime('%m%d%y-%H%M%S')

    report_file = f'{report_directory}/gecko_report-{dt_current}.csv'

    report_fields = [
        'name',
        'symbol',
        'id',
        'market_cap_rank',
        'market_cap',
        'market_cap_change_24h',
        'market_cap_change_percentage_24h',
        'current_price',
        'high_24h',
        'low_24h',
        'price_change_24h',
        'price_change_percentage_24h',
        'price_change_percentage_24h_in_currency',
        'price_change_percentage_7d_in_currency',
        'price_change_percentage_30d_in_currency',
        'ath',
        'ath_change_percentage',
        'ath_date',
        'atl',
        'atl_change_percentage',
        'atl_date',
        'roi',
        'circulating_supply',
        'total_supply',
        'total_volume',
        'image',
        'last_updated'
    ]

    logger.info('Writing data to csv file.')
    with open(report_file, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=report_fields)
        
        csv_writer.writeheader()

        for coin in report_data:
            csv_writer.writerow(coin)
    
    logger.info('Done.')