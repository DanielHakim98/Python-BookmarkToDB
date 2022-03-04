from bs4 import BeautifulSoup
import re
import codecs
from datetime import datetime
import pandas as pd
from IPython.display import display
import numpy as np
from urllib.request import Request,urlopen
from urllib.error import URLError, HTTPError
import os


class bookmark_saver(BeautifulSoup):
    def __init__(self, fname):
        if not os.path.isfile(fname):
            raise FileNotFoundError("File path is not valid")
        self.file = codecs.open(fname,'r','utf-8').read()
        self.soup = BeautifulSoup(self.file,'lxml')
        self.bookmarks_raw=self.soup.findAll("a")
        self.bookmarks = list(self.bookmarks_raw)
        self.delect_icon_att()
        self.df = self.create_df()

    def delect_icon_att(self):
        for item in self.bookmarks:
            del item['icon']

    def create_df(self):
        book_list = []
        for item in self.bookmarks:
            book_dict = self.dict_to_record(item)
            book_list.append(book_dict)
        starlist_df = pd.DataFrame(data=book_list)
        if 'last_charset' in starlist_df.columns.tolist():
            starlist_df=starlist_df.drop(columns='last_charset')
        return starlist_df
    
    def dict_to_record(self,item):
        record={}
        record['Title']=str(item.contents[0])
        record.update(item.attrs)
        for key in record:
            if key == 'add_date' or key=='last_modified':
                ts=int(record[key])
                record[key]=datetime.utcfromtimestamp(ts).\
                            strftime('%Y-%m-%d %H:%M:%S')
        return record    
    
    def export_to_csv(self,path):
        if not path.endswith('.csv'):
            raise ValueError("File path doesn't end with .csv")
        self.df.to_csv(path)

#Source filepath (in .html) ---> "C:\\DiskC_Data Stars\\mozilla_bookmarks\\latestBookmark.html"
#Save filepath (in .csv)    ---> "C:\\DiskC_Data Stars\\mozilla_bookmarks\\bookmark_table.csv"


source_path = input("Please enter filepath for targeted html file: ")
bkmk_1 = bookmark_saver(source_path)
save_path = input("Please enter filename or filepath to save extracted data into csv file: ")
bkmk_1.export_to_csv(save_path)