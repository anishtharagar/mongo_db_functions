#mongo connect to load data into mongodb, default port for mongodb is asssumed.


import pymongo


def mongo_load(mongo_db_host,mongo_db_name,mongo_collection_name,keys = [],data_payload = []):

    try:
            mongo_db_conn = pymongo.Connection (mongo_db_host)
            mongo_db_conn_cursor = mongo_db_conn [mongo_db_name]
            mongo_collections_cursor = mongo_db_conn_cursor [mongo_collection_name]
            data_load={}

            for i in range(len(data_payload)):
                data_load.__setitem__(keys.__getitem__(i),data_payload.__getitem__(i))

            mongo_collections_cursor.insert(data_load)
            mongo_db_conn.close()
    except OSError as e:
        print "OS Error({0}): {1}", format(e.errno, e.strerror)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except  ValueError:
        print "Could not convert data to an integer."
    except  SystemError as e:
        print "System Error({0})", format(e.message)
    except:
        print "Unexpected error:", sys.exc_info()[0]

def mongo_get(mongo_db_host,mongo_db_name,mongo_collection_name,mongo_query):

    try:
        print mongo_db_host
    except OSError as e:
        print "OS Error({0}): {1}", format(e.errno, e.strerror)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except  SystemError as e:
        print "System Error({0})", format(e.message)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error:", sys.exc_info()[0]


