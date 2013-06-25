import MySQLdb
import os
import lib

home_dir = os.getenv("HOME")
file_path = home_dir + '/Stat/Costs/'
#file_path = '/home/tonyr/Work/Costs/Data/costs_20121207.csv'
DB_QUERY_GET_LIST_OF_UNPROCESSED_FILES = "select file_name from costs.files_arrivals_control where processed_flag = 'N';"
db_name = "costs"
db_user = "root"
db_pwd = "root"
rows_affected = 0

files_to_process = []

db_conn = lib.get_db_connection(db_name, db_user, db_pwd)
cur = db_conn.cursor()

# Get list of unprocessed file names from DB
rows_affected = cur.execute(DB_QUERY_GET_LIST_OF_UNPROCESSED_FILES)
print "Number of unprocessed FILE_NAMEs in DB:", rows_affected
if rows_affected == 0:
    print 'There is no files in DB.'
else:
    db_result = cur.fetchall() # returns 2-dim array
    for nme in db_result:
        files_to_process.append(list(nme)[0])
print "FILE_NAMEs from DB are:", files_to_process


# Read data from file and put it in list
for file_name in files_to_process:
    raw_list = lib.read_file(file_path + file_name)

    print "raw_list:", raw_list

    lib.load_file_data_to_db(cur, raw_list, file_name)

# Calculate total costs for certain day
#day_total = lib.get_day_total(raw_list)

#print(day_total)
