# Coded by Sezer Yavuzer Bozkır <admin@sezerbozkir.com>
# Date: 18.06.2017

from peewee import *
from playhouse.pool import PooledMySQLDatabase
from config import Config

db = PooledMySQLDatabase(**Config.mysql)


class BaseModel(Model):
    class Meta:
        database = db


class Articles_Dev(BaseModel):
    id = PrimaryKeyField(db_column="id")
    url = TextField(db_column="url")
    publish_date = TextField(db_column="publish_date")
    category = TextField(db_column="category")
    question = TextField(db_column="question")
    answer = TextField(db_column="answer")

    class Meta:
        db_table = "articles"


if __name__ == '__main__':
    # db.create_table(Articles, safe=True)
    for icerik in Articles_Dev.select().limit(10):
        print(icerik.category)