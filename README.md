# Crypto_Report
   Generate Initial reports on Cryptocurrencies that may look promising

   1. Install pycoingecko
       https://pypi.org/project/pycoingecko/
       pip install pycoingecko --user

   2. Install pycoingecko
       https://pypi.org/project/pycoingecko/
       pip3 install pycoingecko --user

   3. Install Google News API
       pip3 install GoogleNews --user

   4. Run with Python 3
       python3 generate_report.py

   5. Run collecting the news for a given keywords/coins:
       python3 collect-google-news.py --coin AMPL --keyword Decentralized --duration 7d

       ** It seems to be picking up too much noise.
        * Generic query would be: 
             Decentralized Finance news when:1d
       ** Stores to file, but also prints it out in a easy to read way using pprint (Pretty Print).
          python3 collect-google-news.py --duration 24h
          # Also for now I disabled the usage below of the keyword and coin as it was
            not helping, and lots of false positive news.
        

   Example:
   Collecting Google news:
    For 7 days '7d':
      python3 collect-google-news.py --coin AMPL --keyword Decentralized --duration 7d
      python3 collect-google-news.py --coin SNX --keyword Decentralized --duration 7d

    For 24 hours '24h':
      python3 collect-google-news.py --coin SNX --keyword Decentralized --duration 24h
      python3 collect-google-news.py --coin AMPL --keyword Decentralized --duration 24h

    $ ls -alrt reports/goog*
    -rw-r--r--  1 USER 185  26958 Jul 27 23:24 reports/google_news-Decentralized-AMPL-072720-232436.csv
    -rw-r--r--  1 USER 185  26958 Jul 27 23:24 reports/google_news-Decentralized-SNX-072720-232451.csv
    -rw-r--r--  1 USER 185   8285 Jul 27 23:25 reports/google_news-Decentralized-SNX-072720-232523.csv
    -rw-r--r--  1 USER 185   8285 Jul 27 23:25 reports/google_news-Decentralized-AMPL-072720-232536.csv
   
