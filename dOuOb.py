from bs4 import BeautifulSoup as bs
import requests as req
import re
import random
keyword_Tsai = "蔡"
keyword_Han = "韓"
keyword_Ko = "柯"
keyword_Gou = "郭"
percent = "%"

url = 'https://udn.com/news/story/6656/3992412'


    
r = req.get(url)
sp = bs(r.text,'html.parser')
main_content = str(sp.find("div",id = "story_body_content").find_all("p"))


 
keyword_Tsai_in_where = [ i for i,v in enumerate(main_content) if v==keyword_Tsai ] 
keyword_Han_in_where = [ a for a,b in enumerate(main_content) if b==keyword_Han ]
keyword_Ko_in_where = [ c for c,d in enumerate(main_content) if d==keyword_Ko ]
keyword_Gou_in_where = [ e for e,f in enumerate(main_content) if f==keyword_Gou ]
percent_in_where = [s for s,k in enumerate(main_content) if k==percent]
    
Tsai_ = []
Han_ = []
Ko_ = []
Gou_ = []
num = 0
T_position =[]
H_position = []
K_position = []
G_position = []

for i in percent_in_where :
    
    for j in keyword_Tsai_in_where :
        if ((i-j) <= 15) and ((i-j)>0) :
            
            print(main_content[j:i])
            T_position.append(j)
            t = float(re.findall("(\d+\.+\d)",main_content[j:i])[0])
            if type(t) == float :
                Tsai_.append(t)
                
            
            
    for k in keyword_Han_in_where :
        if ((i-k) <= 15) and ((i-k)>0) :
            
            print(main_content[k:i])
            H_position.append(k)
            h = float(re.findall("(\d+\.+\d)",main_content[k:i])[0])
            if type(h) == float :
                Han_.append(h)
                
            
    for l in keyword_Ko_in_where :
        if ((i-l) <= 15) and ((i-l)>0) :
            
            print(main_content[l:i])
            K_position.append(l)
            ko = re.findall("(\d+\.+\d)",main_content[l:i])[0]
            k = float(ko)

            if type(k) == float :
                Ko_.append(k)
                
            
    for m in keyword_Gou_in_where :
        if ((i-m) <= 15) and ((i-m)>0) :
            
            print(main_content[m:i])
            G_position.append(m)
            g = float(re.findall("(\d+\.+\d)",main_content[m:i])[0])
            if type(g) == float :
                Gou_.append(g)

print('-----------------')                
print(T_position)
print(H_position)  
print(K_position)  
print(G_position)  
print('-----------------')
print(Tsai_)
print(Han_)
print(Ko_)
print(Gou_)


