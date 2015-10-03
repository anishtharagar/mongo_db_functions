from scipy import stats
import statistics
import pymongo
import mongo_connect
import stats_data_parser
import stats_plot


def stat_functions_usage(mongo_host,mongo_db_name,x_field_name = [], y_field_name = [],mongo_collection_name = [], functions = [],query = []):


        #return_data = mongo_connect.mongo_collect_data(mongo_host,mongo_db_name,mongo_collection_name)
        #x_axis_data_points, y_axis_data_points = stats_data_parser.stats_parser("2d_graph", return_data)

        keys_x = []
        keys_y = []
        return_data = mongo_connect.mongo_custom_collect_2d_graph_data(mongo_host,mongo_db_name,mongo_collection_name,x_field_name,y_field_name)
        #x_axis_data_points, y_axis_data_points = stats_data_parser.stats_data_parser_series_data("2d_graph",return_data,x_field_name,y_field_name)
        xaxis_data_points, y_axis_data_points = stats_data_parser.stats_data_parser_series_data("2d_graph",return_data,x_field_name,y_field_name)

#        for i in range(len(x_field_name)):
#            print len(xaxis_data_points.__getitem__(x_field_name.__getitem__(i)))
#            print len(y_axis_data_points.__getitem__(y_field_name.__getitem__(i)))

        stats_plot.stats_plot_2d_graph_series_plot(x_field_name,y_field_name,xaxis_data_points,y_axis_data_points)
        #for i in range(0,1):
        #    print return_data[i]
        #print return_data[140000]

        #stats_plot.stats_plot_2d_graph("x_label_test","y_label_test",x_axis_data_points,y_axis_data_points)


stat_functions_usage('127.0.0.1','raw_data',["rain","meandewpti"],["maxpressurei","mintempi"],["nyc_subset"])

