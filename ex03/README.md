# 第3回
## 迷路ゲーム：迷えるこうかとん（ex03/maze.py）
### ゲーム概要
- ex03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に沿ってこうかと
んを移動させるゲーム
- 実行するたびに迷路の構造が変化する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- 練習ではこうかとんの画像だったのをネットからフリー画像を拾って使用した。
### ToDo（実装しようと思ったけど時間がなかった）
- ランダムに設置する敵キャラを追加しようとした。
- スタート地点とゴール地点を設置し、その場所にスタートとゴールという文字を置きたかった。
- ゴール地点に到着した際に演出を出したかった。
- ゴールをした後にまた別の構造の迷路が出るようにしたかった。
- 迷路の色を変更したかった。
### メモ
- Canvasクラス（図形描画）
- width:キャンパスの幅
- heightキャンパスの高さ
- bg:背景色