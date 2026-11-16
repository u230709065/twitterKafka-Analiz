from kafka import KafkaProducer
import csv  , json 
from pathlib import Path
import pandas as pd
from TwitterModel import VeriSatiri
from dataclasses import asdict # obje yaptığımız verileri dicte çevirme
import time , random

"""
csv_path = Path(__file__).resolve().parent / "tweets_v8.csv"

with open(csv_path ,mode="tr" ) as file : 
    reader = csv.DictReader(file)
    for satir in reader:
        print(satir)
"""

producer = KafkaProducer(bootstrap_servers=[bootstrap_servers] , key_serializer= lambda k: str(k).encode("utf-8") if k else None , value_serializer= lambda v: json.dumps(asdict(v)).encode("utf-8"))

df= pd.read_csv("tweets_v8.csv")
df=df.where(pd.notnull(df) , None) # pd de nullar float("nan") şeklinde jsona dödürünce hata verebilir o yüzden onlar yerine None koyduk



#print(df.to_string())

keys = ["user_name" , "user_location" , "user_description" , "user_followers" , "user_friends" , "date" , "text" ]
#objects = []
partition = 0 ;
for satir in df[keys].to_dict(orient="records"):
    veri=VeriSatiri(**satir)
    producer.send(topic="tweetModel" ,partition=partition%6 , key=None , value=veri )
    partition+= 1 
    producer.flush()
    time.sleep(random.uniform(1,1.5))
    print(veri , " gönderildi")

