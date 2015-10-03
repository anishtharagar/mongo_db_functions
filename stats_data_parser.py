import sys
from fnmatch import  *


##########stats_parser function takes 2 arguments
########### arguments listed below
#--> 1 . data_parser_type --> type of data to be parsed at this moment only value supported is 2d_graph
#--> 2.  python list  passed as an argument, this is the data which needs to be parsed.

def stats_parser (*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '2':
        print "List of arguments passed does not match the data type %.3d" % count_arg_length
        sys.exit()

    data_parser_type = args.__getitem__(0).__str__()
    data_list = args.__getitem__(1)

    if data_parser_type == '2d_graph':
        data_sample = {}
        key = []

        x_axis_data_points = []
        y_axis_data_points = []

        for i in range(len(data_list)):
            data_sample = (dict(data_list[i]))
            key = data_sample.keys()
            if key[0] == 'x':
                x_axis_data_points.append(data_sample.values())
            elif key[0] == 'y':
                y_axis_data_points.append(data_sample.values())

        x_list_collection = str(x_axis_data_points.__getitem__(0)).split(",")
        y_list_collection = str(y_axis_data_points.__getitem__(0)).split(",")
        x_temp = []
        y_temp = []

        for i in range(len(x_list_collection)):
            if '[' in x_list_collection[i]:
                print "gameon for ["
                x_temp = str(x_list_collection.__getitem__(i)).split("[")
                y_temp = str(y_list_collection.__getitem__(i)).split("[")
        for i in range(len(x_list_collection)):
            if '[' in x_list_collection[i]:
                print "skipping for data alignment"
            else:
                x_temp.append(str(x_list_collection.__getitem__(i)))
                y_temp.append(str(y_list_collection.__getitem__(i)))
        x_list_collection = []
        y_list_collection = []
        for i in range(len(x_temp)):
            if ']' in x_temp[i]:
                print "gameon for ]"
                x_list_collection = str(x_temp.__getitem__(i)).split("]")
                y_list_collection = str(y_temp.__getitem__(i)).split("]")
        x2_temp = []
        y2_temp = []
        for i in range (len(x_temp)):
            if ']' in x_temp[i]:
                print "skipping for data alignment"
            elif 'u' in x_temp[i]:
                print "skipping for data alignment"
            else:
                x2_temp.append(str(x_temp.__getitem__(i)))
                y2_temp.append(str(y_temp.__getitem__(i)))
        x2_temp.append(str(x_list_collection.__getitem__(0)))
        y2_temp.append(str(y_list_collection.__getitem__(0)))

        x_axis_data_points = []
        y_axis_data_points = []
        x_axis_data_points = x2_temp
        y_axis_data_points = y2_temp
        print x_axis_data_points
        print y_axis_data_points
        return x_axis_data_points, y_axis_data_points
    else:
        print "Data parser type not supported"
        sys.exit()


def stats_data_parser_series_data(*args):
    count_arg_length = len(args)
    if count_arg_length.__str__() != '4':
        print "List of arguments passed does not match the data type %.3d" % count_arg_length
        sys.exit()
    data_parser_type = args.__getitem__(0).__str__()
    data_list = []
    data_list = args.__getitem__(1)
    x_field_names = args.__getitem__(2)
    y_field_names = args.__getitem__(3)
    dict_of_values = {}
    sort_string = []
    string_value_x = []
    string_value_y = []
    remove_brace_x = []
    remove_brace_y = []
    x_array = []
    y_array = []
    x_list = {}
    y_list = {}

    if data_parser_type == '2d_graph':


        for j in range(len(x_field_names)):
            for i in range(len(data_list)):
                   if (str(x_field_names[j]) in data_list[i]) and (str(y_field_names[j]) in data_list[i]):
                        sort_string = (str(data_list[i]).split(","))
                        if (x_field_names[j] in sort_string[0]) and (y_field_names[j] in sort_string[1]):
                            string_value_x = str(sort_string[0]).split(":")
                            remove_brace_x = str(string_value_x[1]).split("}")
                            x_array.append(remove_brace_x[0])
                            #x_list.__setitem__(x_field_names[j],string_value_x[1])
                            string_value_y = str(sort_string[1]).split(":")
                            remove_brace_y = str(string_value_y[1]).split("}")
                            y_array.append(remove_brace_y[0])
                            #y_list.__setitem__(y_field_names[j],string_value_y[1])
                        elif (x_field_names[j] in sort_string[1]) and (y_field_names[j] in sort_string[0]):
                            string_value_x = str(sort_string[1]).split(":")
                            remove_brace_x = str(string_value_x[1]).split("}")
                            x_array.append(remove_brace_x[0])
                            #x_list.__setitem__(x_field_names[j],string_value_x[1])
                            string_value_y = str(sort_string[0]).split(":")
                            remove_brace_y = str(string_value_y[1]).split("}")
                            y_array.append(remove_brace_y[0])
                           #y_list.__setitem__(y_field_names[j],string_value_y[1])
                        else:
                            print "something messed up check data alignment"
                            sys.exit

            x_list.__setitem__(x_field_names[j],x_array)
            y_list.__setitem__(y_field_names[j],y_array)
            x_array = []
            y_array = []





        return x_list,y_list
