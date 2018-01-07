# Sites Monitoring Utility

The script tracks the status of url by following criteria:
* url response is 200
* domain expiration date is more than [number of days] from now

# Status logic

URL is OK! if:
* the response is 200
* the domain expiration date is more than [number of days] from now

URL is not OK! if either:
* response iы not 200
OR URL doesn't respond
* the domain expiration date is not more than [number of days] from now
OR impossible to get expiration date
OR URL doesn't respond

# To run the code

* Put your file into root script folder
* Run check_sites_health.py [file name.extension] [number of days]

Example of script launch on Linux, Python 3.5:
```
$ python check_sites_health.py urls.txt 30
http://www.yandex.ru is OK!
http://www.vk.ru is OK!
http://www.rbc.ru is OK!
http://www.xyz123.com.ua is not OK!
```
Windows launches the same

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
