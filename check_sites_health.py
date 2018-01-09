import requests
from whois import whois
from datetime import datetime, timedelta
import sys


def load_urls4check(path):
    with open(path, 'r') as urls:
        return urls.read().split()


def is_server_respond_with_200(url):
    try:
            return requests.get(url).ok
    except ValueError:
            return 'url don\'t respond'


def get_domain_expiration_date(url, days):
    try:
            return whois(url).expiration_date + timedelta(days=days) > datetime.now()
    except ValueError:
            return 'url doesn\'t respond'


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        days = int(sys.argv[2])
        urls_list = load_urls4check(path)
        for url in urls_list:
            if is_server_respond_with_200(url) and get_domain_expiration_date(url, days):
                print('{} is OK!'.format(url))
            else:
                print('{} is not OK!'.format({url}))
    except (FileNotFoundError, ValueError, IndexError):
        print('Cannot read file or missing one of the arguments')
