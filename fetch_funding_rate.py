import ccxt
import pandas as pd
from datetime import datetime, timedelta
from utils import timestamp_to_datetime, save_to_csv

def fetch_funding_rates():
    """
    從 Binance 抓取 ETH 永續合約的歷史 Funding Rate 資料
    """
    # 初始化 Binance 交易所物件
    exchange = ccxt.binance({
        'enableRateLimit': True,  # 啟用請求頻率限制
    })
    
    # 設定要抓取的交易對
    symbol = 'ETH/USDT:USDT'
    
    # 設定時間範圍（從 2023 年開始）
    start_date = datetime(2023, 1, 1)
    end_date = datetime.now()
    
    # 儲存所有 Funding Rate 資料
    all_funding_rates = []
    
    # 每次抓取 1000 筆資料
    limit = 1000
    
    # 從開始日期開始抓取
    current_date = start_date
    
    print("開始抓取 Funding Rate 資料...")
    
    while current_date < end_date:
        try:
            # 抓取 Funding Rate 歷史資料
            funding_rates = exchange.fetch_funding_rate_history(
                symbol,
                since=int(current_date.timestamp() * 1000),
                limit=limit
            )
            
            if not funding_rates:
                break
                
            # 將資料加入列表
            all_funding_rates.extend(funding_rates)
            
            # 更新時間
            current_date = timestamp_to_datetime(funding_rates[-1]['timestamp']) + timedelta(hours=8)
            
            print(f"已抓取至 {current_date}")
            
        except Exception as e:
            print(f"抓取資料時發生錯誤: {e}")
            break
    
    # 將資料轉換為 DataFrame
    df = pd.DataFrame(all_funding_rates)
    
    # 轉換時間戳為可讀格式
    df['datetime'] = df['timestamp'].apply(timestamp_to_datetime)
    
    # 選擇需要的欄位
    df = df[['datetime', 'fundingRate']]
    
    # 儲存資料
    save_to_csv(df, 'eth_funding_rates.csv')
    
    print(f"共抓取 {len(df)} 筆資料")

if __name__ == "__main__":
    fetch_funding_rates() 