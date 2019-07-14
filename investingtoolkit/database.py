from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


SQLITE = 'sqlite'

# Table Names
SYMBOLS = 'symbols'
HOLDINGS = 'holdings'
WATCHLIST = 'watchlist'


class Database:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):

        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print('[+] ' + str(self.db_engine))

        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):

        metadata = MetaData()

        symbols = Table(SYMBOLS, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('symbol', String, nullable=False),
                        Column('symbol_name', String),
                        Column('symbol_type', String),
                        Column('region', String),
                        Column('currency', String)
                        )

        holdings = Table(HOLDINGS, metadata,
                         Column('id', Integer, primary_key=True),
                         Column('symbol', None, ForeignKey('symbols.id')),
                         Column('value', Integer),
                         Column('buy_price', Integer),
                         Column('date_added', Integer),
                         )

        try:
            metadata.create_all(self.db_engine)
            print("[+] Tables created")

        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    def execute_query(self, query=''):

        if query == '': return
        print(query)

        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)

            except Exception as e:
                print(e)

    def print_all_data(self, table ='', query=''):

        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)
                result.close()
                print("\n")

# SYMBOL DB TABLE QUERYS/INSERTS
    def save_symbol(self, selected_stock):

        selected_symbol = str(selected_stock['1. symbol'])
        selected_symbol_name = selected_stock['2. name']
        selected_symbol_type = selected_stock['3. type']
        selected_symbol_region = selected_stock['4. region']
        selected_symbol_currency = selected_stock['8. currency']

        print(type(selected_symbol))

        query = "INSERT INTO {}(symbol, symbol_name, symbol_type, region, currency) " \
                "VALUES ('{}' , '{}', '{}', '{}', '{}')".format(SYMBOLS, selected_symbol, selected_symbol_name, str(selected_symbol_type), selected_symbol_region, selected_symbol_currency)
        self.execute_query(query)

    def save_to_symbols(self, selected_stock):
        dbms = Database(SQLITE, dbname='db.sqlite')
        dbms.save_stock(selected_stock)

# Holdings DB TABLE QUERYS/INSERTS
    def save_holding(self, selected_stock):
        pass

    def sample_query(self):
        query = "SELECT id, symbol, symbol_name, symbol_type, region, currency FROM {TBL_SYM}".format(TBL_SYM=SYMBOLS)
        self.print_all_data(query=query)

    def sample_insert(self) -> object:
        query = "INSERT INTO {}(symbol, symbol_name, symbol_type, region, currency) " \
                "VALUES('AMD','Advanced Micro Devices Inc', 'Equity', 'United States', 'USD')".format(SYMBOLS)
        self.execute_query(query)

    def check_if_in_db(self, symbol):
        # TODO
        symbol = symbol

        query = "SELECT * FROM symbol WHERE symbol = {}".format(symbol)
        self.print_all_data(query=query)