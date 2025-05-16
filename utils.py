import pandas as pd
from datetime import datetime, timedelta

def timestamp_to_datetime(timestamp):
    """
    將時間戳轉換為 datetime 格式
    
    Args:
        timestamp (int): Unix 時間戳（毫秒）
    
    Returns:
        datetime: 轉換後的日期時間
    """
    return datetime.fromtimestamp(timestamp / 1000)

def datetime_to_str(dt):
    """
    將 datetime 轉換為字串格式
    
    Args:
        dt (datetime): 日期時間物件
    
    Returns:
        str: 格式化的日期時間字串
    """
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def save_to_csv(df, filename):
    """
    將 DataFrame 儲存為 CSV 檔案
    
    Args:
        df (pandas.DataFrame): 要儲存的資料
        filename (str): 檔案名稱
    """
    df.to_csv(filename, index=False)
    print(f"資料已儲存至 {filename}")

def load_from_csv(filename):
    """
    從 CSV 檔案讀取資料
    
    Args:
        filename (str): 檔案名稱
    
    Returns:
        pandas.DataFrame: 讀取的資料
    """
    return pd.read_csv(filename)

def calculate_returns(funding_rates):
    """
    計算累積報酬
    
    Args:
        funding_rates (pandas.DataFrame): Funding Rate 資料
    
    Returns:
        pandas.DataFrame: 包含累積報酬的資料
    """
    # 計算每期的報酬率
    funding_rates['returns'] = funding_rates['fundingRate'].astype(float)
    
    # 計算累積報酬
    funding_rates['cumulative_returns'] = (1 + funding_rates['returns']).cumprod() - 1
    
    return funding_rates 