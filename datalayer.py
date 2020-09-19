# dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table

from config import connect_string

class dataLayer():
    def __init__(self):
        self.engine = create_engine(connect_string)
        # self.conn = self.engine.connect()
        self.connect_string = connect_string
        self.inspector = inspect(self.engine)
        self.tables = self.inspector.get_table_names()
        self.Base = automap_base()
        self.Base.prepare(self.engine, reflect=True)
        self.Subjects = self.Base.classes['subjects']
        self.meta = MetaData()

    def get_BabyNames():
        session = Session(self.engine)

        results = session.query(self.babynames.names)

        df = pd.read_sql(results.statement, session.connection())

        session.close()
        return list(df.names)
