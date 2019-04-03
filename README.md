# OR-Final-Project
### Requirement
```
pip install pulp
```
## Background and Motivation
### Why/How
#### "The New Era On Ice"
這個賽季花式滑冰改動了原有的規則，先前紀錄也隨之封存重新開始。許多新秀接連竄起，經驗豐富的選手更積極調整自己的競技狀態。
那麼要如何計算出選手在自我所能達到的範圍內，在新賽制中取得高分呢？

### Problem definition
#### 目標：最大化跳躍技術分（GOE+0之TES）
我們想針對「跳躍」這個技術動作的安排，透過製作新制度的計算模型，尋找在能力範圍內選手能達到的最理想跳躍技術分計畫。
*（旋轉及步法與節目藝術性編排較相關，非此次計算目標）*
## Data collection
### 男單長曲技術動作
- **7組跳躍**（T、S、Lo、F、Lz、A六種形式）
    - 所有++三週或以上跳躍只能重複兩種++，其中++至多允許一種四周跳++，並且++重複跳躍至少一次是在連跳++或連續跳中完成，且++整套節目只能重複兩種跳躍++
    - 所有++兩週以上的跳躍不得重複超過一次++
    - 必須包含++一個以上的Axel(A)跳躍++
    - ++組合跳最多三組++，其中最多允許一組三連跳
    - 後半段的++最後三組跳躍會有10%的分數加成++
- 3個旋轉、2組步法（以四個定級計分，不在此次考慮範圍）
### data form
以[SkatingScores.com](http://skatingscores.com/)的數據為基準。
以跳躍被標記<（圈數不足）及<<（降組）者為失敗，
標記!（用刃不清）與GOE負分者為半成功
來計算跳躍成功率。
### 跳躍
#### 單跳
![](https://media1.tenor.com/images/a02090a0eb09ba8fb14581f4ce7df067/tenor.gif?itemid=4764290)
單跳（含組合跳中之基礎跳躍）成功率
![](https://i.imgur.com/vIxtRlG.jpg)
#### 組合跳
![](https://media1.tenor.com/images/b428756cd2004c32fbb72ac1d5f6ee21/tenor.gif?itemid=4764283)
組合跳中接續跳之成功率
![](https://i.imgur.com/QPLLq1x.jpg)
## Methodology
Max Profit問題
## Model Formulation 
### (Objective Function and Constraints)
#### 參數設定
* 基礎跳成功率
* $br1,br2,...,br12$ 
* 組合跳成功率 
* $cr1,cr2,...,cr8$
* 每種跳躍基本分
* $bp1,bp2,bp3,...,bp12,cp1,cp2,...,cp8$
#### 決策變數（Binary）
* 十二種基礎跳中，每種跳躍都可能重複一次，可以選或不選
* $b1_1,b1_2,b2_1,b2_2,...,b12_1,b12_2$ 
* 
* 八種組合跳中，每種跳躍都可能重複一次，可以選或不選
* $c1_1,c1_2,c2_1,c2_2,...,c8_1,c8_2$ 
#### 限制式
* 選擇七個基礎跳躍:
* $b1_1+b1_2+b2_1+b2_2+...+b12_1+b12_2=7$
* 組合跳至少一個、最多三個：
* $c1_1+c1_2+c2_1+c2_2+...+c8_1+c8_2>=1$
* $c1_1+c1_2+c2_1+c2_2+...+c8_1+c8_2<=3$
* 四周跳跟三周跳只能有兩個重複：
* b1_2+b2_2+b3_2+...+b12_2+c1_2+...+c8_2<=2
* 三周跳中只能有兩個重複
* （基礎跟組合皆為3T加上其他三周跳的重複次數小於三）：
* $b1_1+c1_1+b2_2+b3_2+b4_2+c2_2+c3_2...<=3$
*  ...
* 基礎跳跟組合跳重複的跳躍只能有兩個：
* b6_1+b6_2+c6_1+c6_2<=2
* b8_1+b8_2+c8_1+c8_2<=2
* ...
* 至少要有一次Axel跳躍
* b11_1+b11_2+b12_1+b12_2>=1 
##### 目標式
$Max$ $Z =\sum_{k=1}^{N}b_k\cdot br_k\cdot bp_k+\sum_{k=1}^{N}c_k\cdot cr_k\cdot cp_k$
### Analysis results
![](https://i.imgur.com/yoKvsm3.png)
- 羽生結弦 4Lz 4s+3s 4s+3s 4lo 3a+3t 4t 3lo 79.36
- Nathan Chen 4lz 4lz+(1)+3s 4s+3s 4f  4t+3t 3a 3lz 82.81
- 宇野昌磨 4f 4s+3f 4s+3f 4lo 4t+3t 3a 3lo 80.86
- Mikhail Kolyada 4lz 4t+3s 4t+3t 4s  3a+3t 3lz 3lo 74.17
- 車俊煥 4s 4t+3lo 4t+(1)+3s 3a 3a+3t 3lz 3lo 71.37
- Jason Brown 3a 3a+3s 3lz+3t 3f 3lo+3t 2a 2a 53.44
- 金博洋 4lz 4lz+3s 4s+3s 4t 3a+3t 3lz 3f 76.71
- 曹志禕 4t 4t+3t 3lz+3t 3a 3f+(1)+2lo 3lo 3s 59.39
### Conclusion
- 僅供參考（？）
- 選手的體力消耗無法量化，這是理想狀態的結果。
- 有些跳躍在連接上會需要微調（加入Euler、1lo）等才是人體工學上可行的，最終依然需要人工調整，因此choreographer很重要！
- 可以當作是選手為進步所設定的目標，但真的要全數完成老實說有點太血汗了XD
- 祝福選手們未來都能夠健康無傷突破自己的紀錄！
