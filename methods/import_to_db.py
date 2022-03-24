import pwinput
import pymysql
from sqlalchemy import create_engine

def df_to_db(param):
    print("\n")
    df = param.df
    uname = input("Please enter name of the user: ")
    pwd = pwinput.pwinput(f"Enter password for mysql {uname}: ")
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host="localhost:3306", db="getting_started", user=uname, pw=pwd))
    df.to_sql("from_mozilla", con = engine, if_exists = 'append', chunksize = 1000)