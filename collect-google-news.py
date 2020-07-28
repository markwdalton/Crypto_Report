import argparse
import csv
import datetime
import logging
import os

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('--keyword', '-k', type=str, default='crypto', help='A additional keyword default is crypto could use DeFi or similar.')
parser.add_argument('--coin', '-c', type=str, default='BTC', help='The project keyword name you wish to search for from Google News.')
parser.add_argument('--duration', '-d', type=str, default='24h', help='The amount of time to search for 24 hours: 24h, for 7 days:  7d, for 2 months:  2m, note it only returns 100 results.')

args = parser.parse_args()

# Additional keyword to narrow down: DeFi, crypto or alternate name.
keyword = args.keyword
# Coin name or symbol or project name
coin = args.coin
# Duration: For hours: #h, Days: #d, Months: #m
duration = args.duration

from pygooglenews import GoogleNews
gn = GoogleNews(lang = 'en', country = 'US')

report_directory = 'reports'

if not os.path.exists(report_directory):
    logger.info('Creating report directory.')
    os.makedirs(report_directory)

# search for the best matching articles that mention crypto
# and Decenteralized or DeFi, and over the past 24 hours 
#
search = gn.search('{keyword} {coin}', when=duration) 
#  search = gn.search('Decenteralized finance AMPL', when = '24h')

#  +Decentralized OR +DeFi', when = '6m')

print(search['feed'].title)

# Each entry contains the fields:
#   title; title_detail[type, language, base, value]; links[rel, type, href] ; link ; id ; guidislink, published ; published_parsed ; summary ; summary_detail ; source ; title ; sub_articles
# 
# [{'title': 'This Week in DeFi - June 26th: Latest DeFi News, Trends & Lending Rates - DeFi Rate', 'title_detail': {'type': 'text/plain', 'language': None, 'base': '', 'value': 'This Week in DeFi - June 26th: Latest DeFi News, Trends & Lending Rates - DeFi Rate'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://defirate.com/this-week-in-defi-june-26th/'}], 'link': 'https://defirate.com/this-week-in-defi-june-26th/', 'id': 'CBMiMWh0dHBzOi8vZGVmaXJhdGUuY29tL3RoaXMtd2Vlay1pbi1kZWZpLWp1bmUtMjZ0aC_SAQA', 'guidislink': False, 'published': 'Fri, 26 Jun 2020 07:00:00 GMT', 'published_parsed': time.struct_time(tm_year=2020, tm_mon=6, tm_mday=26, tm_hour=7, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=178, tm_isdst=0), 'summary': '<a href="https://defirate.com/this-week-in-defi-june-26th/" target="_blank">This Week in DeFi - June 26th: Latest DeFi News, Trends & Lending Rates</a>&nbsp;&nbsp;<font color="#6f6f6f">DeFi Rate</font>', 'summary_detail': {'type': 'text/html', 'language': None, 'base': '', 'value': '<a href="https://defirate.com/this-week-in-defi-june-26th/" target="_blank">This Week in DeFi - June 26th: Latest DeFi News, Trends & Lending Rates</a>&nbsp;&nbsp;<font color="#6f6f6f">DeFi Rate</font>'}, 'source': {'href': 'https://defirate.com', 'title': 'DeFi Rate'}, 'sub_articles': []},

## print(search['entries'].title)

dt_current = datetime.datetime.now().strftime('%m%d%y-%H%M%S')
 
report_file = f'{report_directory}/google_news-{keyword}-{coin}-{dt_current}.csv'

# published_parsed', 'source', 'summary_detail', 'title_detail', 'links'
google_news_fields = [
   'title',
   'title_detail',
   'links',
   'link',
   'id',
   'guidislink',
   'published',
   'published_parsed',
   'summary',
   'summary_detail',
   'source',
   'sub_articles'
]

with open(report_file, 'w', newline='') as csv_file:
   csv_writer = csv.DictWriter(csv_file, fieldnames=google_news_fields)

   logger.info('Writing data to csv file.')
   for coin in search['entries']:
      csv_writer.writerow(coin)
      # print(coin)
