import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, \
                        ForeignKey, Numeric, CheckConstraint
from datetime import datetime
from config import database, user, password
from sqlalchemy import select

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5433/{database}", pool_pre_ping=True)
conn = engine.connect()

metadata = MetaData()

user_tg_table = Table("user_table", metadata,
    Column("id", String(50), primary_key=True)
)

# ins = user_tg_table.insert().values(
#     id = "30"
# )

# conn = engine.connect()
# r = conn.execute(ins)


metadata.create_all(engine)