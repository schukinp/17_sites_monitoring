import requests
from whois import whois
from datetime import datetime, timedelta
import sys


def load_urls4check(path):
    with open(path, 'r') as file:
        return file.read().split()


def is_server_respond_with_200(file):
    response = []
    for url in file:
        try:
            response.append(requests.get(url).status_code == 200)
        except ValueError:
            response.append('url don\'t respond')
    return response


def get_domain_expiration_date(file, days):
    response = []
    for url in file:
        try:
            domain = whois(url)
            response.append((domain.expiration_date + timedelta(days=days)) > datetime.now())
        except ValueError:
            response.append('url doesn\'t respond')
    return response


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        days = int(sys.argv[2])
        urls_list = load_urls4check(path)
        for key, value in dict(
           zip(urls_list,
               zip(is_server_respond_with_200(urls_list),
                   get_domain_expiration_date(urls_list, days)))).items():
            if value == (True, True):
                print('{} is OK!'.format(key))
            else:
                print('{} is not OK!'.format(key))
    except (FileNotFoundError, ValueError, IndexError):
        print('Cannot read file or missing one of the arguments')
