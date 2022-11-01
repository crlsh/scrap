from bs4 import BeautifulSoup
import requests
 
url = 'http://publicpay.ca.gov/Reports/RawExport.aspx'
url_get = requests.get(url)
soup = BeautifulSoup(url_get.content, 'lxml')
col = soup.find('div', class_="column_main")
col_all = col.find_all('a')
for link in col_all:
   print(link.get('href'))