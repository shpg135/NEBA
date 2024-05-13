import pandas as pd
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read('/ssd/NEBA_new/input/config.ini')

# CSV文件路径
csv_file_path = '20240403_boxscore.csv'

# MySQL数据库连接信息
mysql_host = config.get('database', 'host')
mysql_user = config.get('database', 'user')
mysql_password = config.get('database', 'password')
mysql_db = config.get('database', 'database')
mysql_table = 'pf_player_gamelog_full_copy1'

# 读取CSV文件到DataFrame
df = pd.read_csv(csv_file_path)

# 建立MySQL数据库连接
engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}')

# 将DataFrame写入MySQL数据库
df.to_sql(mysql_table, con=engine, if_exists='append', index=False)

# 关闭数据库连接
engine.dispose()
