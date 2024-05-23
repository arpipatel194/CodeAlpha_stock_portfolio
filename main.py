import requests 

class StockPortfolio:
    def _init_(self):
        self.portfolio = {}

    def add_stock(self, symbol):
        if symbol in self.portfolio:
            print("Stock already exists in the portfolio.")
            return
        self.portfolio[symbol] = {}

    def remove_stock(self, symbol):
        if symbol not in self.portfolio:
            print("Stock not found in the portfolio.")
            return
        del self.portfolio[symbol]

    def track_performance(self):
        for symbol in self.portfolio:
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=0ID2TDSM3HFMVENY"
            response = requests.get(url)
            data = response.json()
            latest_close = float(data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['4. close'])
            self.portfolio[symbol]['latest_close'] = latest_close
            print(f"{symbol}: Latest Close Price - {latest_close}")

if __name__ == "requests":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL")
    portfolio.add_stock("GOOGL")
    portfolio.track_performance()