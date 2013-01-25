import MySQLdb
import os

file_path = '/home/nurka/Stat/Costs/'
#file_path = '/home/tonyr/Work/Costs/Data/costs_20121207.csv'
DB_QUERY_GET_LIST_OF_FILES = "select file_name from costs.files_arrivals_control"
db_name = "costs"
db_user = "root"
db_pwd = "root"
rows_affected = 0

folder_list_of_files = []
db_list_of_files = []
files_to_process = []

db_conn = MySQLdb.connect(host="localhost", port=3306, user=db_user, passwd=db_pwd, db=db_name)
cur = db_conn.cursor()

# Get list of file names from DB
rows_affected = cur.execute(DB_QUERY_GET_LIST_OF_FILES)
print(rows_affected)
if rows_affected == 0:
    print('There is no files in DB.')
else:
    db_result = cur.fetchall() # returns 2-dim array
    for nme in db_result[0]:
        db_list_of_files.append(nme)
print(db_list_of_files)

# Get list of file names from filesystem
for file_name in os.listdir(file_path):
    folder_list_of_files.append(file_name)
print(folder_list_of_files)

# Get file names that present in filesystem, but do not present in DB
files_to_process = [x for x in folder_list_of_files if x not in db_list_of_files]
print(files_to_process)



db_conn.close()