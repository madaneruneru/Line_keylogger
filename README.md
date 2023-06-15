# LineKeylogger

## 介紹
側錄 Line 聊天內容的小工具

## 注意
請將此工具用於正向學習和有益的目的，並避免不適當的使用。

## 開發環境
- 作業系統 :  Window 10
- 程式語言 : Python 2.7.16
- 套件 : pyHook, win32api, Numpy, OpenCV

## 程式功能
- 針對 Line視窗 進行鍵盤的側錄
- 當使用者開啟Line並輸入文字以後，才會開始對特定的聊天室窗進行螢幕上的截圖以及動態顯示。

## Todo
- 側錄後能將動態顯示存為錄影檔案
- 側錄後的截圖及錄製檔案傳至遠端

## Demo
### 聊天視窗進行截圖
左邊視窗為 Line 聊天室窗，右邊 scn2.bmp 為聊天對話截圖

![](/demo/%E8%81%8A%E5%A4%A9%E8%A6%96%E7%AA%97%E9%80%B2%E8%A1%8C%E6%88%AA%E5%9C%96.JPG)

### 聊天視窗動態顯示
左邊視窗為 Line 聊天室窗，右邊 screenbox 為聊天即時動態顯示

![](/demo/%E8%81%8A%E5%A4%A9%E8%A6%96%E7%AA%97%E5%8B%95%E6%85%8B%E9%A1%AF%E7%A4%BA.jpg)