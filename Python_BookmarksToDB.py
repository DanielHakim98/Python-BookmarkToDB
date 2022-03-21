from bookmarks_class import *

#Source filepath (in .html) ---> "C:\\DiskC_Data Stars\\mozilla_bookmarks\\latestBookmark.html"
#Save filepath (in .csv)    ---> "C:\\DiskC_Data Stars\\mozilla_bookmarks\\bookmark_table.csv"
# To check available names in global space from bookmarks_class ---> print(globals())

source_path = input("Please enter filepath for targeted html file: ")
bkmk_1 = bookmark_saver(source_path)
save_path = input("Please enter filename or filepath to save extracted data into csv file: ")
bkmk_1.export_to_csv(save_path)

# conn = sqlite3.connect('Bookmarks_list_db')
# c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS Bookmarks(
#             Title TEXT,
#             href TEXT,
#             add_date TEXT,
#             last_modified TEXT,
#             icon_uri TEXT,
#             tags TEXT)''')

# conn.commit()


# bkmk_1.df.to_sql('Bookmarks',conn, if_exists = 'replace', index = False)
