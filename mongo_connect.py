#mongo connect to load data into mongodb, default port for mongodb is asssumed.


import pymongo
import sys
#### Function to load new data into an existing or new collection.
#argument list for the mongo_load is given below
#mongo_db_host --> hostname or ip on which the mongodb is hosted.
#mongo_db_name --> database name on which the collection exists
#mongo_collection_name --> collection which needs to be edited.
#data_type --> currently only 2d_graph is supported.
    # The rest of the parameters are data_type specific in case of 2d_graph, we need 2 extra arguments.
         #x_cordinates_list --> list of x axis values
         #y_cordinates_list --> list of y axis values

def mongo_load(*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '6':
        print "List of arguments passed does not match the data type %.3d" % args.count()
        sys.exit()


    data_type_del = args.__getitem__(3).__str__()

    if data_type_del == '2d_graph':
        print "game on!!!!"
    else:
        raise ValueError ('kindly specify the right data_type')
        sys.exit()

    try:
            mongo_db_host = args.__getitem__(0).__str__()
            mongo_db_name = args.__getitem__(1).__str__()
            mongo_collection_name = args.__getitem__(2).__str__()
            x_cordinates = args.__getitem__(4)
            y_cordinates = args.__getitem__(5)

            mongo_db_conn = pymongo.Connection (mongo_db_host)
            mongo_db_conn_cursor = mongo_db_conn [mongo_db_name]
            mongo_collections_cursor = mongo_db_conn_cursor [mongo_collection_name]
            """
           if align_type == 'split':
                for key,values in data_payload.items():
                    loader_data = {key: values}
                    mongo_collections_cursor.insert(loader_data)
            elif align_type == 'join':
                mongo_collections_cursor.insert(data_payload)
            else:
                raise ValueError ('kindly specify value for align type')
            mongo_db_conn.close()
            """

            if data_type_del == '2d_graph':
                  mongo_collections_cursor.insert({'x': x_cordinates.__str__()})
                  mongo_collections_cursor.insert({'y': y_cordinates.__str__()})
            else:
                 raise ValueError ('Wrong data type kindly pass the right data_type')
                 sys.exit()


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


#### Function to delete the collection and load new data into the collection which was deleted.
#argument list for the mongo_delete_load is given below
#mongo_db_host_del --> hostname or ip on which the mongodb is hosted.
#mongo_db_name_del --> database name on which the collection exists
#mongo_collection_name_del --> collection which needs to be edited.
#data_type_del --> currently only 2d_graph is supported.
    # The rest of the parameters are data_type specific in case of 2d_graph, we need 2 extra arguments.
         #x_cordinates_list --> list of x axis values
         #y_cordinates_list --> list of y axis values
def mongo_delete_load(*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '6':
        print "List of arguments passed does not match the data type %.3d" % args.count()
        sys.exit()

    data_type_del = args.__getitem__(3).__str__()

    if data_type_del == '2d_graph':
        print "game on!!!!"
    else:
        raise ValueError ('kindly specify the right data_type')
        sys.exit()

    try:
        mongo_db_host_del = args.__getitem__(0).__str__()
        mongo_db_name_del = args.__getitem__(1).__str__()
        mongo_collection_name_del = args.__getitem__(2).__str__()
        x_cordinates = args.__getitem__(4)
        y_cordinates = args.__getitem__(5)
        mongo_db_conn_del = pymongo.Connection (mongo_db_host_del)
        mongo_db_conn_cursor_del = mongo_db_conn_del [mongo_db_name_del]
        mongo_collections_cursor_del = mongo_db_conn_cursor_del [mongo_collection_name_del]
        mongo_collections_cursor_del.remove()
        mongo_db_conn_del.close()

        mongo_load(mongo_db_host_del,mongo_db_name_del,mongo_collection_name_del,data_type_del,x_cordinates,y_cordinates)

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

#### Function to delete the collection and load new data into the collection which was deleted.
#argument list for the mongo_collect_data is given below
#mongo_db_host --> hostname or ip on which the mongodb is hosted.
#mongo_db_name --> database name on which the collection exists
#mongo_collection_name --> collection which needs to be edited.

#def mongo_collect_data(mongo_host,mongo_db_name,mongo_collection_name = []):

def mongo_collect_data(*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '3':
        print "number of arguments passed to the function does not meet the criteria."
        sys.exit()


    mongo_host = args.__getitem__(0).__str__()
    mongo_db_name = args.__getitem__(1).__str__()
    mongo_collection_name = args.__getitem__(2)
    try:
        mongo_db_conn = pymongo.Connection(mongo_host)
        mongo_db_conn_cursor = mongo_db_conn[mongo_db_name]
        doc_list = {}
        return_data = {}
        for i in range(len(mongo_collection_name)):
            collection_name = mongo_collection_name.__getitem__(i)
            mongo_collection_cursor = mongo_db_conn_cursor[collection_name]
            doc_list.__setitem__(i, mongo_collection_cursor.find({}, {'_id': 0}))


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


def mongo_query_data(mongo_host,mongo_db_name,mongo_collection_name = [],query = []):
     try:
        mongo_db_conn = pymongo.Connection(mongo_host)
        mongo_db_conn_cursor = mongo_db_conn[mongo_db_name]
        doc_list = {}
        return_data = {}
        query_format = {}
        query_format = query
        print query_format.__dict__.keys()

        count_records = 0
        for i in range(len(mongo_collection_name)):
            collection_name = mongo_collection_name.__getitem__(i)
            mongo_collection_cursor = mongo_db_conn_cursor[collection_name]
            for z in range (len (query_format.__dict__.__getitem__(collection_name))):
                print len(query_format.__dict__.__getitem__(collection_name))
                query_array = query_format.__dict__.__getitem__(collection_name)
                for y in range(len(query_array)):
                    doc_list[count_records] = mongo_collection_cursor.find(query_format.__getitem__(y))
                    count_records = count_records.__int__() + 1

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

