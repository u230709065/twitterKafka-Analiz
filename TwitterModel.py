from dataclasses import dataclass
import pandas as pd


@dataclass
class VeriSatiri: #dataclasses modülünden gelen bir dekoratördür (süsleyicidir). Normal bir sınıfta tek tek yazman gereken standart metotları (__init__, __repr__, __eq__ vb.) sınıfın değişkenlerine bakarak otomatik olarak üretir.
    user_name : str
    user_location : str
    user_description : str
    user_followers : int
    user_friends : int
    date : str
    text:str


    def __str__(self):
        return (f"UserName : {self.user_name} | UserLoc : {self.user_location} | UserDesc : {self.user_description} | UserFollowers : {self.user_followers}" 
        f" | UserFriends : {self.user_friends} | Date : {self.date} | Text : {self.text}")


    

