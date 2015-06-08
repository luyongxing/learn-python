#-*- coding:utf-8 -*-
import urllib 
from bs4 import BeautifulSoup
import json
help_info = u'利用python爬虫抓取网页获得源代码'
print '%s'%help_info

url = raw_input(' website address:')

a = urllib.urlopen(url).read()

soup=BeautifulSoup(a)
all_script = soup.find_all("script")

script_date = []
for tag in all_script:
if len(tag.attrs) == 0:
    date_write = tag.get_text()
    script_date.append(date_write)
   
    json_date=[]
    ret = True
    for s in script_date:
begin = s.find('g_page_config')
if begin == -1:
    continue
end = s.find('g_srp_loadCss')
if end == -1:
    continue
begin = begin+len('g_page_config')+2
ss = s[begin:end].strip()
json_date.append(ss[:-1])
#print type(tag)   #结果为<class 'bs4.element.Tag'>

params = json.loads(json_date[0])
#print type(params)       #结果为<type 'dict'>
#print params.keys()      #结果为[u'pageName', u'map', u'mods', u'feature', u'mainInfo']
a_params = params[u'mods']
#print a_params.keys()    #结果为[u'feedback', u'spuseries', u'personalbar', u'shopcombotip', u'related', u'header', u'shopstar', u'tab', u'noresult', u'apasstips', u'navtabtags', u'spucombo', u'nav', u'tips', u'phonenav', u'supertab', u'vbaby', u'navtablink', u'itemlist', u'choosecar', u'pager', u'p4p', u'debugbar', u'shopcombo', u'sortbar', u'bottomsearch', u'sc', u'tbcode']
b_params = a_params[u'itemlist']
#print b_params.keys()    #结果为[u'status', u'export', u'data']
c_params = b_params[u'data']   
#print c_params.keys()    #结果为[u'spmModId', u'trace', u'sellers', u'isSameStyleView', u'auctions', u'postFeeText', u'query', u'recommendAuctions']
d_params = c_params[ u'auctions']
#type(d_params)      
#print d_params

file = open ( 'search_info.txt', 'w')
hml='\t\t\t\t商品名称\t\t\t\t\t商品详情\t\t\t\t店铺名称\t\t\t\t店铺网址\t\t\t\t\t店铺所在地\t\t\t\t'
ddd=hml.decode('utf-8')
file.write(ddd.encode('gbk')+'\n')
for key in d_params:
#print type(key)

print u"商品名称:",key[u'raw_title'],u"商品详情：",key["detail_url"],u"店铺名称：",key["nick"],u"店铺网址:",key["shopLink"],u"店铺所在地:",key["item_loc"]

file.write(key[u'raw_title'].encode('gbk')+'\t')
file.write(key["detail_url"].encode('gbk')+'\t')
file.write(key["nick"].encode('gbk')+'\t')
file.write(key["shopLink"].encode('gbk')+'\t')
file.write(key["item_loc"].encode('gbk')+'\n')
file.close()