import pymysql

def read_file(file_path):
    '''(str) -> list
    
    Return parsed data from file as a list of trimerred strings. One element
    of the list is one line from the file without \n char.
    '''
    input_list = []

    # open file for reading
    file = open(file_path, 'r')

    # loop for deleting \n from the end of each line and adding the line to list
    for line in file:
        input_list.append(line.rstrip())
    
    
    file.close()

    return input_list

def get_day_total(in_list):
    '''(list) -> float

    Return the sum of costs spent on particular day. Take string from IN_LIST,
    parse it, get cost of one product and summarize it.
    '''
    day_total = 0
    i = 0

    for s in in_list:
        prod_cost = get_param(in_list[i], 'cost')
        day_total += prod_cost
        i += 1

    return round(day_total, 2)

def get_param(params_str, param_type):
    '''(str, str) -> object

    Return value of PARAM_TYPE from PARAMS_STR. The value can be any of Python's
    types. Function gets PARAMS_STR as list of params separated by commas and
    returns certain param chosen by PARAM_TYPE. Format of PARAM_STR can be found
    in Spec.txt > File format.
    '''
    split_list = []
    
    split_list = params_str.split(',')

    if param_type.lower() == 'cat':
        value = split_list[0]
    elif param_type.lower() == 'nme':
        value = split_list[1]
    elif param_type.lower() == 'cost':
        value = float(split_list[2])

    return value

def log_to_file(file_path, value):
    '''
    (str, value) -> no return

    Writes '---...--- + new_line' and VALUE to the end of FILE_PATH

    '''

    file = open(file_path, 'a')

    file.write('-' * 50 + '\n')

    s = 'Total: ' + str(value)
    file.write(s)

def get_db_connection(db_name, db_user, db_pwd):
    '''
    (str, str, str) -> connection
    
    Function retrives DB_NAME, DB_USER, DB_PWD, opens db connection using PYMYSQL lib and returns the connection.
    
    '''
    
    connection = pymysql.connect(host="localhost", port=3306, user=db_user, passwd=db_pwd, db=db_name)
    
    return connection

