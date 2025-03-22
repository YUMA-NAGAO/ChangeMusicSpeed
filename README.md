
# Change Music Speed

## 概要
このスクリプトは、指定した倍率で MP3 ファイルの再生速度を変更するツールです。  
複数の MP3 ファイルを一括処理でき、出力ファイルは元のファイル名に指定倍率をプレフィックスとして付与して保存されます。

---

## 動作環境
- **Python 3.x**  
  Python 3.x がインストールされ、コマンドラインから実行可能であること

- **FFmpeg**  
  FFmpeg がインストールされ、システムの PATH に追加されていること

### FFmpeg インストール例
```bash
# macOS (Homebrew)
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
https://ffmpeg.org/download.html からインストーラをダウンロード
```

---

## 使用方法

### 1. スクリプトの配置
音声ファイルがあるディレクトリに `speedChanger.py` を配置します。  
例:
```bash
# 音声ファイルがあるディレクトリに移動
cd /path/to/audio/files

# スクリプトをダウンロードまたはコピー
curl -O https://example.com/speedChanger.py  # 例: リモートから取得
```

### 2. 実行コマンド
ターミナルで以下のように実行します。
```bash
python3 speedChanger.py <倍率>
```
#### 例: 1.5 倍速に変換する場合
```bash
python3 speedChanger.py 1.5
```

---

## 処理の詳細

### 入力
- 現在のディレクトリにある **.mp3 ファイル【全て】** を対象に処理を行います。

### 出力
- 出力ファイル名は `[倍率]_[元のファイル名].mp3` となります。  
  例: `music.mp3` を 1.5 倍速に変更 → `1.5_music.mp3`

### 対応倍率
- **0.1 倍 ～ 9.9 倍** まで指定可能  
  ※ FFmpeg の atempo フィルタは直接 0.5〜2 の倍率しか対応していないため、指定倍率がこの範囲外の場合は内部で複数のフィルタを組み合わせて処理します。

---

## 注意事項
⚠️ **重要**  
- **元のファイルは変更されず、別ファイルとして出力されます。**  
- 異常な倍率（数値でない、または範囲外）を指定すると、エラーメッセージが表示され処理は中断されます。  
- 処理時間は、ファイルのサイズや指定倍率に依存します。

---

## エラーメッセージ例
```bash
# 引数が不足している場合
Usage: python3 script.py <speed[ 0.1 <= speed <= 9.9 ]>

# 数値以外の入力の場合
Error: Speed must be a numeric value.

# 指定した倍率が有効範囲外の場合
Error: Speed is out of range.
```

---

## ライセンス
MIT License  
Copyright (c) 2023 YourName

---

---

この README.md を利用することで、利用者がスクリプトの環境設定から実行方法、エラーメッセージの内容までを一目で把握できるようになります。
