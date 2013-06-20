#################################################################
# Script gets list of filenames that present in folder,         #
#  but do not present in DB. Then it loads that filenames to DB.#
#-------------------------------                                #
# Author: Anton Rovba                                           #
# Created: 23/01/2013                                           #
# Updated: 20/06/2013 -- fixed converting query result from     #
#                        tuple to list of strings               #
#################################################################

import MySQLdb
import os
from time import gmtime, strftime, localtime

file_path = '/home/nurton/Stat/Costs/'
#file_path = '/home/tonyr/Work/Costs/Data/costs_20121207.csv'
DB_QUERY_GET_LIST_OF_FILES = "select file_name from costs.files_arrivals_control;"
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
print "Number of FILE_NAMEs in DB:", rows_affected
if rows_affected == 0:
    print 'There is no files in DB.'
else:
    db_result = cur.fetchall() # returns 2-dim array
    for nme in db_result:
        db_list_of_files.append(list(nme)[0])
print "FILE_NAMEs from DB are:", db_list_of_files

# Get list of file names from filesystem
for file_name in os.listdir(file_path):
    folder_list_of_files.append(file_name)
print "Files from OS:", folder_list_of_files

# Get file names that present in filesystem, but do not present in DB
files_to_process = [x for x in folder_list_of_files if x not in db_list_of_files]
print "Files to process are:", files_to_process

# Get local system time
local_sysdate = strftime("%Y-%m-%d %H:%M:%S", localtime())

for nme in files_to_process:
    rows_affected = cur.execute("insert into costs.files_arrivals_control (purchase_date, file_name, actual_arrival_time,  processed_time, processed_flag) values (20121207, '%s', SYSDATE(), null, 'N');" % (nme))
    if rows_affected == 0:
        print "Record for file", nme, "was not inserted to FILES_ARRIVALS_CONTROL."
rows_affected = cur.execute("commit;")


db_conn.close()
