# -*- coding: utf-8 -*-
import numpy as np

liste=[1,3,777,88,787,8786,656,565,44]

a=np.arange(15).reshape(3,5)
print(a)
print(type(a))
print(a.ndim+"")

b=np.arange(10)
print(b)
print(b.shape)
print(b.ndim)

#%%
import numpy as np
a=np.array([1,3,5,7,9])

print(a.dtype)

b=np.array([[1,1,2],[16,7,67],[2,23,45]])

b2=np.array([1,1,2,16,7,67,2,23,45]).reshape(3,3)# np.array tek tek girmekle aynı
print(b2)
print(b)
print(b.ndim)
print()
#%%linspace ile çalışmak

import numpy as np


a=np.linspace(1,10,10) #1 den 10 a kadar eşit aralıklarla 10 sayı yazdır
b=np.linspace(31,90,11)
print(b)
print(a)
#%%SINUS HESAPLAMA
from numpy import pi

d=np.linspace(0,2*pi,100)
#print(d)
print(np.sin(d))
#%%

a=np.array([1,234,34,23])
b=np.arange(4)

c=a-b
d=b**3

e=10*np.sin(a)

print(e>7)
print(a*b)#elementwise product
print(a@b)#matris çarpımı
print(a.dot(b))

f=np.ones((2,4))
g=np.zeros((2,4))
rand=np.random.random((2,4))
i=np.sum(b)
j=np.min(b)
l=np.sqrt(b)
#%%indexing and slicing

sayilar1=np.linspace(0,30,6)

#print(sayilar1[0:3])

sayilar2=sayilar1.reshape(2,3)

print(sayilar2[:,0])#ilk kısım satır ikinci sütun
print(sayilar2[:,0:2])
print(sayilar2[-1,:])#-1 son satırdaki bütün sütundaki verileri  ver diyor
print(sayilar2[:,-1])#son sütundaki bütün satırdaki verileri ver diyor

#%%shape manipulation

a=np.floor(10*np.random.random((3,4)))

#print(a)
#print(a.shape)
#print(a.ravel()) #3,4 lük arrayi düze çevirir

#print(a.reshape(4,3))
a=a.reshape(2,6)

print(a.T)
print(a.reshape(2,-1))
#%%stacking

a=np.floor(10*np.random.random((2,3)))
b=np.floor(10*np.random.random((2,3)))

print(a)
print(b)

print(" ")
c=np.vstack((a,b)) #dikey olarak birleştiir
print(c)

d=np.hstack((a,b))#yatay olarak birleştirir
print(d)

#%%COPY AND View


a=np.arange(10)
print(a)

b=a

print(a[2])
print(b[2])
b[0]=100

print(a)
print(b)#bu kısım cok öneml bnin değiştirdiğimiz zaman a da değişiyor çünkü bellekte aynı yeri kullanıyorlar.O yüzden böyle kopya alınmaz.

c=a.copy()

c[0]=1000

print(c)
print(a)#değişmediğini gördük

d=a.view()#bu işlem shape değiştirdiğimizde copy alırken shapelerin değişmesini datanın aynı kalmasını sağlar.
print("****")

d[0]=25

d.shape=2,5
print(a)
print(d)

#%%PANDAS

import pandas as pd
import numpy as np

data=np.array(["Engin","Derin","Salih"])

s=pd.Series(data)

data2={"matematik" :10, "fizik" :100,"coğrafya":20}
s2=pd.Series(data2)
print(s2)

s3=pd.Series(5,index=[1,2])

print(s3)

#%%Dataframele çalışmak


import pandas as pd
import numpy as np


data=[10,20,30,40,50]
df=pd.DataFrame(data)
print(df)

data2=[["Engin",33,"Ankara"],["Derin",4,"Ankara"],["Sami",78,"istanbul"]]
df2=pd.DataFrame(data2,columns=["isim","yaş","şehir"],index=[1,2,3])
print(df2)

data3={"isim":["Engin","Derin","Salih"],
       "yaş":[33,4,78],
       "şehir":["ankara","istanbul","izmir"]}
df3=pd.DataFrame(data3,columns=["isim","yaş","şehir"],index=[1,2,3])
print(df3)

#del df3["şehir"] df3 şehir kolonunu siler
#df3.pop("şehir")
#print(df3)
#%%
#print(df3.loc[2]) #2.data
#print(df3.iloc[1])#2.datayı 

df4=df3.append(df2)

print(df4)
print(df4.head())#ilk 5 sıradaki datayı gösterir
print(df4.tail())#son 5 sıradaki datayı gösterir
#%%pandas datasetle uğraşma örneği

import pandas as pd

notlar=pd.read_csv("grades.csv")
notlar.columns=["isim","soyisim","SSN","Test1","Test2","Test3","Test4","Final","grade"]
print(type(notlar))
print(notlar.head())
print(notlar["isim"])
print(notlar.iloc[2])
print(notlar[1:5])
#%%indexing and slicing

import pandas as pd

notlar=pd.read_csv("grades.csv")
notlar.columns=["isim","soyisim","SSN","Test1","Test2","Test3","Test4","Final","grade"]

print(notlar.loc[:5,"isim"]) #0 dahile 5 e kadar kaydın ismini gösterdi.
print(notlar.loc[:5,["isim","Final"]])
print(notlar.loc[:5,:"Final"])#Finale kadar ki kolonları gösterir.
#%%filtreleme
import pandas as pd

films=pd.read_csv("imdb_1000.csv")

print(films)
print(films.columns)
print(films.tail())
print(films.title.head())
print(films[:9][['title','star_rating']].head())
print(films[films['star_rating']>8.5][films['star_rating']<9.0][["title","star_rating"]]) #8.5ve 9 arası puandan fgilmleri gördük
print(films[films['star_rating']>7.5][["title","star_rating"]])#7.5 dan büyük veri kümeleri için gördük

#%%query ile filtreleme

print(films.query("star_rating>9.0 & star_rating>9.2")[["title","star_rating"]])
#%%groupby çalışma

import pandas as pd

data=pd.read_csv("imdb_1000.csv")

print(data.columns)
print(films.star_rating.mean()) #ortalamayı buldu
print(films.groupby("genre").star_rating.mean()) #genreye göre puan ortalamaya baktık

#%%drop ve axis 

films=pd.read_csv("imdb_1000.csv")
print(films.columns)

print(films.drop('content_rating',axis=1).head())

#films=films.drop('content_rating',axis=1) #kalıcı olmasını istiyorsak kaldırdığımız kolonun
#films=films.drop(2,axis=0)#satırdan siler 2.satır silinir


rowsTodrop=[1,23,7,87,22,898]
films=films.drop(rowsTodrop,axis=0) #arraydeki numaralı saatırları siler
#%%Kayıp veriler Missing Data ile Çalışma


import pandas as pd

url="http://bit.ly/uforeports"

data=pd.read_csv(url)
print(data[["City",
            "Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())

print(data.isnull().head(100))

#print(data.notnull().head(100)) bu da kulanılabilir tam tersi gösterimi

print(data.isnull().sum())#KAÇ TANE HER KOLONDA  BOŞ OLAN DATA SAYILARINI VERİR.

print(data[data.City.isnull()])#city kolonundaki bütün boş olanları gösterir

#%%dropna ile çalışmak#
print(data.shape)
print(data.dropna()) #eğer herhangi satırda bir boşluk varsa onu datasetinden çıkarır
print(data.dropna(how="all"))#tüm satırları boş olanları kaldırır. default durumda "any" olur

data=data.dropna(subset=["City","Colors Reported"],how="all")#eğer bulunan iki kolonda boşsa veriyi sil demek
#%%fillna ile çalışmak
import pandas as pd

url="http://bit.ly/uforeports"

data=pd.read_csv(url)

data['Shape Reported'].fillna(value='Belirsiz',inplace=True)#Shape Reported kolonundaki boş verilerin yerine belirsiz yazdık.
print(data['Shape Reported'].value_counts(dropna=False))
print(data.shape)

#%%String fonksiyonlarıyla çalışmak (Veriyi Değiştirmek!!!!!)
print("engin demirog".upper())

import pandas as pd

orders=pd.read_table("orders.tsv")

#print(orders.head())
#print(orders.columns)
#print(orders.item_name.str.upper())
#print(orders.item_name.str.contains("Chicken"))#item_name kolonunda chicken kelimesi geçen dataları gösterir

print(type(orders.choice_description))
orders.choice_description=orders.choice_description.str.replace('[','').str.replace(']','') #istediğim veriyi burda parantezleri değiştirir değiştirmede yardımcı olur ilk kısım değiştirilen

#print(orders.choice_description)

#%%Join ve merge yapmadım tekrar aç izle istersen iki tabloyu birleştirir aynı kayıtlardan duplicate olmaz. Concat ile 2 datasetini birleştirir