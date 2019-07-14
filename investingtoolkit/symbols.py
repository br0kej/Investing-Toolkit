import requests


class Symbols:
    # Class for Stocks & Share Symbols.

    def __init__(self, symbol, apiKey=''):
        self.symbol = symbol
        self.baseUrl = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='
        self.url: str = None
        self.response = None
        self.apiKey = apiKey

    def set_url(self):
        """
        Takes a Symbol and builds lookup Alpha Vantage URL.
        """
        self.url = self.baseUrl + self.symbol + '&apikey=' + self.apiKey

    def get_response(self):
        """
        Retrieves the information from Alpha Vantage API & convert to JSON.
        """
        self.response = requests.get(self.url).json()

        if '01. symbol' not in self.response['Global Quote']:
            raise ValueError('No Price Information Found')

    def get_current_price(self):
        """
        Uses the Alpha Vantage Response to return the stock/share current price.
        """
        self.current_price = float(self.response['Global Quote']['05. price'])

    def get_high(self):
        """
        Uses the Alpha Vantage Response to return the stock/share daily high.
        """
        self.high = self.response['Global Quote']['03. high']

    def get_low(self):
        """
        Uses the Alpha Vantage Response to return the stock/share daily low.
        """
        self.low = self.response['Global Quote']['04. low']

    def summary(self):
        """
        Uses the Alpha Vantage Response to print a data summary.
        """
        print('\nName: {}\nPercentage Change: {}\nPoint Change: {}\nPrice: {}\nHigh: {}\nLow: {}\n'.format(
            self.response['Global Quote']['01. symbol'],
            self.response['Global Quote']['10. change percent'],
            self.response['Global Quote']['09. change'],
            self.response['Global Quote']['05. price'],
            self.response['Global Quote']['03. high'],
            self.response['Global Quote']['04. low']
        ))

    def work_out_profit_loss(self, gain=20, loss=10):
        """
        Uses the Alpha Vantage API to look up a stock symbols
        current value and then uses user inputted gain and loss percentages
        to calculate cash out and stop loss thresholds
        """
        multiplier = 1 + (gain / 100)
        gain_price = round(self.current_price * float(multiplier), 3)

        divider = 1 + (loss / 100)
        loss_price = round(self.current_price / float(divider), 3)

        print('Current Price: {}\nGain Price: {} ({}% Gain)\nStop Loss Price: {} ({}% Loss)\n'.format(
            self.current_price,
            gain_price,
            gain,
            loss_price,
            loss
        ))

    def how_many_shares(self, value=''):
        """
        Use the stocks current price to determine how many shares can be bought with
        a user inputted monetary amount.
        """
        pence_value = int(value) * 100
        number_of_shares = float(pence_value) / float(self.current_price)
        print("The number of " + self.symbol + " shares which can be bought with £" + str(value) + " is " + str(
            round(number_of_shares, 5)))