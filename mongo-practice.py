from sqlite3 import connect
import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://root:zxc50053@mycluster.7tjho.mongodb.net/?retryWrites=true&w=majority")
db = client.test  # 選擇操作 test 資料庫

collection = db.users  # 選擇操作 users 集合
# 把資料新增到集合中

collection.insert_one({
    "name": "123",
    "gender": "男"
})

print("資料新增成功")
