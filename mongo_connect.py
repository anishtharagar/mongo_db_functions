import pymongo


def mongo_load(mongo_db_host,mongo_db_name,mongo_collection_name,keys = [],data_payload = []):
    mongo_db_conn = pymongo.Connection (mongo_db_host)
    mongo_db_conn_cursor = mongo_db_conn [mongo_db_name]
    mongo_collections_cursor = mongo_db_conn_cursor [mongo_collection_name]

    data_load={}

    for i in range(len(data_payload)):
        data_load.__setitem__(keys.__getitem__(i),data_payload.__getitem__(i))



    mongo_collections_cursor.insert(data_load)
    mongo_db_conn.close()


