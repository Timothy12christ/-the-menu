# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:23:31 2019

@author: ASUS
"""
products=[]#建立products 這個空清單
while True:#無限迴圈
    box1=input('請輸入東西')
    if box1 =='q':
        break
    box2=input('請輸入價格')
    z=[]
    z.append(box1)    
    z.append(box2)    
    products.append(z)
#    products.append(z)#
#print(products[0])
with open('products.csv','w')as f:#用f開啟products 這個檔案
    for n in products :#把products 分別用for n 一個一個開啟
         f.write(z[0]+','+z[1]+'\n')
        
        
        
        
        