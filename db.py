import pymongo
from typing import List, Dict, Any

## Import rule variabel dari model.py
from model import SensorModel

## Koneksi database
client = pymongo.MongoClient("mongodb+srv://Wafirotul:wafielif@cluster0.zvlxeza.mongodb.net/?retryWrites=true&w=majority")

## Test DB Connection
# db = client.test
# print(db)

## Create DB
TDb = client["Data-kecepatan"]

## Create Table
TSensor = TDb['Wafirotul']

# Method CREATE
def db_create_sensor(sensor: SensorModel) -> bool:
    #insert_one -> masukkan data ke db
    TSensor.insert_one(sensor.__dict__)

# Methon READ
def db_list_sensors() -> List[SensorModel]:
    #find() -> menemukan/read semua data di tabel
    return [SensorModel.from_dict(r) for r in TSensor.find()]
