# Ethena Funding Rate 回測工具

這個專案用於回測 Ethena 的 Delta-Neutral 策略是否能透過 Funding Rate 獲利。專案會從 Binance 抓取 ETH 永續合約的歷史 Funding Rate 資料，並進行簡單的回測分析。

## 功能特點

- 從 Binance 抓取 ETH 永續合約的歷史 Funding Rate 資料
- 計算策略的累積報酬
- 繪製報酬曲線圖表
- 提供基本的回測統計數據

## 系統需求

- Python 3.8+
- pip（Python 套件管理器）

## 安裝步驟

1. 克隆此專案：
```bash
git clone https://github.com/yourusername/ethena_backtest.git
cd ethena_backtest
```

2. 安裝必要套件：
```bash
pip install -r requirements.txt
```

## 使用說明

1. 抓取歷史資料：
```bash
python fetch_funding_rate.py
```

2. 執行回測：
```bash
python backtest.py
```

## 專案結構

- `fetch_funding_rate.py`: 抓取歷史 Funding Rate 資料
- `backtest.py`: 執行回測並產生報酬曲線
- `utils.py`: 共用工具函式
- `eth_funding_rates.csv`: 儲存的歷史資料
- `requirements.txt`: 專案依賴套件列表

## 注意事項

- 回測結果僅供參考，不構成投資建議
- 實際交易時需考慮手續費、滑價等因素
- 建議在執行回測前先了解 Delta-Neutral 策略的風險 