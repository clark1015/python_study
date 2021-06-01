import pip._vendor.requests
from bs4 import BeautifulSoup

indeed_result= pip._vendor.requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result.text)

indeed_soup=BeautifulSoup(indeed_result.text,"html.parser")

print(indeed_soup)