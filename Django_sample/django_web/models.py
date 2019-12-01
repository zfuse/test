from django.db import models
from mongoengine import *
from mongoengine import connect
connect('house',host='127.0.0.1',port=27017)
# Create your models here.
class ArtiInfo(Document):
    diqu=StringField()#des严格和数据库中的key对应
    house_title=StringField()
    sumprice=StringField()
    #tags=ListField(StringField())
    size1=StringField()
    roomnum=StringField()
    singleprice=StringField()
    building=StringField()
    sub=StringField()
    xiaoqu=StringField()
    city=StringField()
    floow=StringField()
    orient=StringField()
    address=StringField()

    meta={'collection':'hbhouse'}



