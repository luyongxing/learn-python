#-*- coding:utf-8 -*-
import urllib 
from bs4 import BeautifulSoup
import json
help_info = u'����python����ץȡ��ҳ���Դ����'
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
#print type(tag)   #���Ϊ<class 'bs4.element.Tag'>

params = json.loads(json_date[0])
#print type(params)       #���Ϊ<type 'dict'>
#print params.keys()      #���Ϊ[u'pageName', u'map', u'mods', u'feature', u'mainInfo']
a_params = params[u'mods']
#print a_params.keys()    #���Ϊ[u'feedback', u'spuseries', u'personalbar', u'shopcombotip', u'related', u'header', u'shopstar', u'tab', u'noresult', u'apasstips', u'navtabtags', u'spucombo', u'nav', u'tips', u'phonenav', u'supertab', u'vbaby', u'navtablink', u'itemlist', u'choosecar', u'pager', u'p4p', u'debugbar', u'shopcombo', u'sortbar', u'bottomsearch', u'sc', u'tbcode']
b_params = a_params[u'itemlist']
#print b_params.keys()    #���Ϊ[u'status', u'export', u'data']
c_params = b_params[u'data']   
#print c_params.keys()    #���Ϊ[u'spmModId', u'trace', u'sellers', u'isSameStyleView', u'auctions', u'postFeeText', u'query', u'recommendAuctions']
d_params = c_params[ u'auctions']
#type(d_params)      
#print d_params

file = open ( 'search_info.txt', 'w')
hml='\t\t\t\t��Ʒ����\t\t\t\t\t��Ʒ����\t\t\t\t��������\t\t\t\t������ַ\t\t\t\t\t�������ڵ�\t\t\t\t'
ddd=hml.decode('utf-8')
file.write(ddd.encode('gbk')+'\n')
for key in d_params:
#print type(key)

print u"��Ʒ����:",key[u'raw_title'],u"��Ʒ���飺",key["detail_url"],u"�������ƣ�",key["nick"],u"������ַ:",key["shopLink"],u"�������ڵ�:",key["item_loc"]

file.write(key[u'raw_title'].encode('gbk')+'\t')
file.write(key["detail_url"].encode('gbk')+'\t')
file.write(key["nick"].encode('gbk')+'\t')
file.write(key["shopLink"].encode('gbk')+'\t')
file.write(key["item_loc"].encode('gbk')+'\n')
file.close()