from pymongo import MongoClient
from pprint import pprint
import datetime
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://heroku_24353wrj:tq5ltjpkpib8p3nbm17jcu6084@ds155278.mlab.com:55278/heroku_24353wrj")
db = client.heroku_24353wrj
journals = db.journals

journal = {
"year":"2005",
"month":"october",
"date":"30",
"date_added":datetime.datetime.utcnow()
}

journals.insert(journal)
#print (journal_id)

