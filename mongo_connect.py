#mongo connect to load data into mongodb, default port for mongodb is asssumed.


import pymongo
import sys


def mongo_load(mongo_db_host,mongo_db_name,mongo_collection_name,align_type,data_payload = {}):

    try:
            mongo_db_conn = pymongo.Connection (mongo_db_host)
            mongo_db_conn_cursor = mongo_db_conn [mongo_db_name]
            mongo_collections_cursor = mongo_db_conn_cursor [mongo_collection_name]
            if align_type == 'split':
                for key,values in data_payload.items():
                    loader_data = {key: values}
                    mongo_collections_cursor.insert(loader_data)
            elif align_type == 'join':
                mongo_collections_cursor.insert(data_payload)
            else:
                raise ValueError ('kindly specify value for align type')
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


#### Function to delete the collection and load new data into the collection which was deleted.

def mongo_delete_load(mongo_db_host_del,mongo_db_name_del,mongo_collection_name_del,align_type_del,data_payload_del = []):

    try:
        mongo_db_conn_del = pymongo.Connection (mongo_db_host_del)
        mongo_db_conn_cursor_del = mongo_db_conn_del [mongo_db_name_del]
        mongo_collections_cursor_del = mongo_db_conn_cursor_del [mongo_collection_name_del]
        mongo_collections_cursor_del.remove()
        mongo_db_conn_del.close()

        mongo_load(mongo_db_host_del,mongo_db_name_del,mongo_collection_name_del,align_type_del,data_payload_del)

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


def mongo_collect_data(mongo_host,mongo_db_name,mongo_collection_name = []):
    try:
        mongo_db_conn = pymongo.Connection(mongo_host)
        mongo_db_conn_cursor = mongo_db_conn[mongo_db_name]
        doc_list = {}
        return_data = {}
        for i in range(len(mongo_collection_name)):
            print len(mongo_collection_name)
            collection_name = mongo_collection_name.__getitem__(i)
            print mongo_collection_name.__getitem__(i)
            mongo_collection_cursor = mongo_db_conn_cursor[collection_name]
            doc_list[i] = mongo_collection_cursor.find()
        k=0
        for j in range(len(doc_list)):
             for document in doc_list[j]:
                return_data[k] = document
                k=k+1

        return return_data
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
