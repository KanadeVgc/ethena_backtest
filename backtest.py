import pandas as pd
import matplotlib.pyplot as plt
from utils import load_from_csv, calculate_returns

def run_backtest():
    """
    執行回測並繪製報酬曲線
    """
    # 讀取 Funding Rate 資料
    print("讀取 Funding Rate 資料...")
    df = load_from_csv('eth_funding_rates.csv')
    
    # 計算報酬
    print("計算報酬...")
    df = calculate_returns(df)
    
    # 計算基本統計數據
    total_return = df['cumulative_returns'].iloc[-1]
    avg_return = df['returns'].mean()
    max_drawdown = (df['cumulative_returns'] - df['cumulative_returns'].cummax()).min()
    
    print("\n回測結果統計：")
    print(f"總報酬率: {total_return:.2%}")
    print(f"平均每期報酬率: {avg_return:.4%}")
    print(f"最大回撤: {max_drawdown:.2%}")
    
    # 繪製報酬曲線
    plt.figure(figsize=(12, 6))
    plt.plot(df['datetime'], df['cumulative_returns'] * 100)
    plt.title('Ethena Delta-Neutral 策略累積報酬曲線')
    plt.xlabel('日期')
    plt.ylabel('累積報酬率 (%)')
    plt.grid(True)
    
    # 儲存圖表
    plt.savefig('backtest_results.png')
    print("\n回測結果圖表已儲存至 backtest_results.png")

if __name__ == "__main__":
    run_backtest() 