from investingtoolkit.symbols import Symbols
from investingtoolkit.apikeys import ApiKeys
from investingtoolkit import db_setup, stock_search
import os

checks = ApiKeys()
checks.check_keys_directory()
if checks.directory_exists is False:
    checks.make_keys_directory()

av = ApiKeys(api='AlphaVantage')

if os.path.exists("keys/" + av.api_name + ".p") is False:
    av.input_api_key()
else:
    av.get_api_key_path()
    av.load_api_key()

if db_setup.db_presence_check() is False:
    db_setup.db_creation()

if __name__ == "__main__":
    print("\nStocks & Shares Toolkit")
    try:
        while True:
            print("""\nOptions:\n[1] Search for an Equity\n[2] Lookup Equity\n""")
            option = input("Please Select An Options: ")
            if option is '1':
                stock_search.search_equity(av.loaded_api_key)

            elif option is '2':
                symbol = input("Please Enter A Stock/Share Symbol: ")
                x = Symbols(symbol, av.loaded_api_key)
                x.set_url()
                x.get_response()
                x.get_current_price()
                x.get_high()
                x.get_low()

                print("""Options: 1) Print Summary 2) Profit & Stop Loss Calculator 3) No. Shares for Value""")
                option = input("\nOption: ")

                if option is '1':
                    x.summary()
                elif option is '2':
                    x.work_out_profit_loss()
                elif option is '3':
                    value = input("\nHow much money are you aiming to spend? (£) ")
                    x.how_many_shares(value)
                else:
                    print('Invalid Entry')
            else:
                print('Broken')
    except KeyboardInterrupt:
        print("\nProgram Exited")