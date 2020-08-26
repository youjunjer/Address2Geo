'''
1.Apply a Google Map Geo API Key
2.Create a csv file and put all addresses in one column with name 'address'
3.csv file must utf8 encoding
4.Install Win64OpenSSL for https protocal. (https://slproweb.com/products/Win32OpenSSL.html)
'''
import requests
import json
import numpy
import pandas as pd
StoreData = pd.read_csv('address.csv') 
geo=[]
storeaddress = StoreData['address'] #address data in the 'address' column
for i in range(storeaddress.size-1):  
  print(i)
  try:
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + storeaddress[i] + '&key=AIzaSyDSDe5BXTPUec8dAfa44MkqsqslA4Sp484',verify=False)  
    if r.status_code ==200:
      data=json.loads(r.text) 
      geo.append(str(data['results'][0]['geometry']['location']['lat']) + ';' + str(data['results'][0]['geometry']['location']['lng']))
  except:
    #give 0;0 if address can't be parsed
    geo.append('0;0')    
df = pd.DataFrame(geo, columns= ['geo']) #export geodata to geo.csv
df.to_csv(r'geo.csv', index = False, header=True)
