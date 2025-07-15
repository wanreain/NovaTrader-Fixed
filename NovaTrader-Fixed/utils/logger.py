import csv
from datetime import datetime

def log_trade(signal, price, quantity, file_path="trade_log.csv"):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), signal, price, quantity])