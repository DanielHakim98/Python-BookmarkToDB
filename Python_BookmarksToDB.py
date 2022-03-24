from classes.bookmarks_class import *
from methods.import_to_db import df_to_db

# Source filepath (in .html)
# ---> "C:\\DiskC_Data Stars\\mozilla_bookmarks\\latestBookmark.html"

# Save filepath (in .csv)
# --->"C:\\DiskC_Data Stars\\mozilla_bookmarks\\bookmark_table.csv"

# To check available names in global space from bookmarks_class
# ---> print(globals())

source_path = "C:\\DiskC_Data Stars\\mozilla_bookmarks\\latestBookmark.html"
save_path = "C:\\DiskC_Data Stars\\mozilla_bookmarks\\bookmark_table.csv"

# To insert user defined path:
# source_path = input("Please enter filepath for targeted html file: ")
bkmk_1 = bookmark_saver(source_path)

#To insert user defined path for .csv:
# save_path = input("Please enter filename or filepath to save extracted data into csv file: ")
bkmk_1.export_to_csv(save_path)


#df_to_db(bkmk_1.df)