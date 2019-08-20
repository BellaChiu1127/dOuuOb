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
percent_in_where = [s for s,w in enumerate(main_content) if w==percent]
    
Tsai_ = []
Han_ = []
Ko_ = []
Gou_ = []
num = 0
T_position =[]
H_position = []
K_position = []
G_position = []

t = h = k = g =  0
t0 = h0 = k0 = g0 =  0
for i in percent_in_where :
    t=t0
    h=h0
    k=k0
    g=g0
    
    for j in keyword_Tsai_in_where :

        if ((i-j) <= 15) and ((i-j)>0) :
            
            print(main_content[j:i])
            T_position.append(j)

            t = float(re.findall("(\d+\.+\d)",main_content[j:i])[0])
            
            if type(t) == float :
                Tsai_.append(t)
            
              
    if t == t0 :
        Tsai_.append('Nan')        
    for n in keyword_Han_in_where :
        if ((i-n) <= 15) and ((i-n)>0) :
            
            print(main_content[n:i])
            H_position.append(n)
            h = float(re.findall("(\d+\.+\d)",main_content[n:i])[0])
            if type(h) == float :
                Han_.append(h)
            
    if h == h0 :
        Han_.append('Nan')        
    for l in keyword_Ko_in_where :
        if ((i-l) <= 15) and ((i-l)>0) :
            
            print(main_content[l:i])
            K_position.append(l) 
            k = float(re.findall("(\d+\.+\d)",main_content[l:i])[0])
            if type(k) == float :
                Ko_.append(k)
            
    if k == k0 :
        Ko_.append('Nan')
    for m in keyword_Gou_in_where :
        if ((i-m) <= 15) and ((i-m)>0) :
            
            print(main_content[m:i])
            G_position.append(m)
            g = float(re.findall("(\d+\.+\d)",main_content[m:i])[0])
            if type(g) == float :
                Gou_.append(g)
            
    if g == g0 :
        Gou_.append('Nan')

if len(Tsai_) == len(Han_) == len(Ko_) == len(Gou_):
    print('%----------------%')
    print('數據有效，開始分析')
    print('%----------------%')
else :
    print('%----------------%')
    print('無效的數據，程式已停止')
    print('%----------------%')
    

print(Tsai_)
print(Han_)
print(Ko_)
print(Gou_)
print('-----------')
data0 = 0

for data0 in range(len(Tsai_)): 


    if type(Tsai_[data0]) == float  and type(Tsai_[(data0)+2]) == float:
        print ("藍綠比較：")
        print("蔡英文：",Tsai_[(data0)+0],"％")
        print("韓國瑜：",Han_[(data0)+1],"％")
        print("\n")
        
    elif type(Tsai_[data0]) == float and type(Tsai_[(data0)+3]) == float:
        if type(Ko_[(data0)+2]) == float :
            print("蔡韓柯比較：")
            print("蔡英文：",Tsai_[(data0+0)],"％")
            print("韓國瑜：",Han_[(data0+1)],"％")
            print("柯文哲：",Ko_[(data0+2)],"％")
            print("\n")
        if type(Gou_[(data0)+2]) == float :
            print("蔡韓郭比較：")
            print("蔡英文：",Tsai_[(data0+0)],"％")
            print("韓國瑜：",Han_[(data0+1)],"％")
            print("郭台銘：",Gou_[(data0+2)],"％")
            print("\n")
            
    elif type(Tsai_[data0]) == float and type(Tsai_[(data0)+4]) != float:
        print ("蔡韓柯郭比較：")
        if type(Ko_[(data0)+2]) == float :
            print("蔡英文：",Tsai_[(data0+0)],"％")
            print("韓國瑜：",Han_[(data0+1)],"％")
            print("柯文哲：",Ko_[(data0+2)],"％")
            print("郭台銘：",Ko_[(data0+3)],"％")
            print("\n")
        if type(Gou_[(data0)+2]) == float :
            print("蔡英文：",Tsai_[(data0+0)],"％")
            print("韓國瑜：",Han_[(data0+1)],"％")
            print("柯文哲：",Ko_[(data0+3)],"％")
            print("郭台銘：",Gou_[(data0+2)],"％")
            print("\n")
            
    
        

