# brainfuck程式轉換器
能夠將輸入的文本轉換成brainfuck程式

## [English](readme.en_EN.md) | 繁體中文 

# 使用方法
## 方法1
使用vs code的[brainfuckHelper](https://marketplace.visualstudio.com/items?itemName=ComputerElite.brainfuckhelper)擴充套件

在main.bf按F1之後選Execute brainfuck就能執行了

## 方法二 
使用brainfuck線上編譯器

到[線上編譯器](https://ashupk.github.io/Brainfuck/brainfuck-visualizer-master/index.html#)

把main.bf的內容輸入進去然後按Run即可

# 注意事項
這個程式只是進行簡單的文本轉換成ascii再轉換成brainfuck程式，沒有input功能

線上編譯器的記憶體單元數上限是27，此專案是將文本輸出後就會將該單元清空，所以從頭到尾只會占用一個單元，不過未來想改造專案要注意