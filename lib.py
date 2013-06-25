import MySQLdb

DB_QUERY_INSERT_NEW_FILE = "insert into costs.files_arrivals_control (purchase_date, file_name, actual_arrival_time, processed_time, processed_flag)"

def read_file(file_path):
    '''(str) -> list of list
    
    Return parsed data from file as a list of list of trimerred strings. One element
    of the list is one line from the file without \n char and splitted by ','.
    '''
    input_list = []
    files_list = []
    category = []
    product_name = []
    cost = []

    # open file for reading
    file = open(file_path, 'r')

    # loop for deleting \n from the end of each line and adding the line to list
    for line in file:
        input_list.append(unicode(line.strip(), 'utf-8').split(','))
    
    file.close()
    
#    for line in input_list:
        

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
    
    connection = MySQLdb.connect(host="localhost", port=3306, user=db_user, passwd=db_pwd, db=db_name, charset='utf8')
    
    return connection

def load_file_data_to_db(cursor, file_data, file_name):
    '''
    (db_connection, str, str) -> None
    
    Function retrievs data from file as list of list and insert record to db with this data. Also it updates FILES_ARRIVALS_CONTROL table with PROCESSED_FLAG = 'Y' for this file.
    
    '''
    #cursor = db_conn.cursor()
    rows_affected = cursor.execute("SELECT PURCHASE_DATE FROM costs.files_arrivals_control WHERE FILE_NAME = '" + file_name + "';")
    if rows_affected == 0:
        print 'There is no such FILE_NAME [', file_name, '] in FILES_ARRIVALS_CONTROL.'
    else:
        db_result = cursor.fetchall() # returns 2-dim array
        purchase_date = str(db_result[0][0]).strip()
    
    for data_row in file_data:
        DB_INSERT_QUERY = u"insert into costs.purchase_details (purchase_date, file_name, prod_type, prod_name, cost, processed_time) values(" + purchase_date + ", '" + file_name + "', '" + data_row[0].strip() + "', '" + data_row[1].strip() + "', " + data_row[2].strip() + ", sysdate());"
        
        print "Insert query is:", DB_INSERT_QUERY
        
        rows_affected = cursor.execute(DB_INSERT_QUERY)
        
        if rows_affected == 0:
            print "Row from file [", file_name, "] was not inserted to DB"
        
        cursor.execute("commit;")

def get_purchase_date(file_name):
    '''
    (str) -> str
    
    Cut PURCHASE_DATE from given FILE_NAME (file name format: costs_<PURCHASE_DATE>.csv)
    
    '''
    
    return file_name[6:-4]














