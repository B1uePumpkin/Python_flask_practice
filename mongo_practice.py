# 載入pymongo套件
import pymongo
from bson.objectid import ObjectId
# 連線到MongoDB

client = pymongo.MongoClient("mongodb+srv://root:Password@mycluster.b0llbe5.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster")

# 把資料放進資料庫
db = client.test # 選擇使用test資料庫
collection = db.users # 選擇操作users集合
# 新增一筆資料
# result = collection.insert_one({'name': 'Kevin',
#                         'age': 20})
# print("新增成功"+str(result.inserted_id))

# 新增多筆資料
# result = collection.insert_many([{'name': 'David',
#                         'level': 1},
#                         {'name': 'Tom',
#                         'level': 1},
#                         {'name': 'Mary',
#                          'level': 1
#                          }])

# print("新增成功"+str(result.inserted_ids))

# 查詢資料
# result = collection.find_one(ObjectId("65ffbe51e10ff6aa7dcab083"))
# print(result)
# print(result["name"])
# print(result["age"])

# 一次取得多筆資料
# results = collection.find()
# for result in results:
#     print(result["name"])


# 更新資料
# result = collection.update_one(
#     {
#         'name': 'Kevin' 
#     },{
#         '$set': {
#             'age': 25        
#             }
#         }
#     )


# 更新多筆資料
# result = collection.update_many(
#     {
#         'level': 3
#     },{
#         '$set': {
#             'level': 3
#             }
#         }
#     )

# print("符合查詢"+str(result.matched_count))
# print("更新成功"+str(result.modified_count))


# 刪除資料
# result = collection.delete_one({
#     'level': 3
# })
# print("刪除成功"+str(result.deleted_count))

# 刪除多筆資料
# result = collection.delete_many({
#     'level': 3
# })
# print("刪除成功"+str(result.deleted_count))