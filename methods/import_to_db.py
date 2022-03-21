import pwinput
import pymysql
from sqlalchemy import create_engine

def df_to_db(df):
    print("\n")
    # user = input("Please enter name of the user: ")
    # pw = pwinput.pwinput(f"Enter password for mysql {user}: ")
    # engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
    #                         .format(user=user,
    #                                 pw=pw,
    #                                 db="lol idk"))
    # df.to_sql("from_mozilla", con = engine, if_exists = 'append', chunksize = 1000)