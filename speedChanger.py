import glob
import os
import subprocess
import sys


def atempo_validator(speed):
    # 引数で指定された倍率が0.1~9.9 の範囲に入っているかチェック
    if speed >= 0.1 or speed <= 9.9:
        return True
    else:
        return False

def atempo_option_generator(speed):
    atempo_option = ""
    # ffmpegに与える引数が1つの場合
    if speed >= 0.5 and speed <= 2:
        atempo_option =  "atempo="+ str(speed)
    # ffmpegに与える引数が2つ以上の場合
    else:
        atempo_option_temp_list = []
        # 引数が0.5未満の場合
        if speed < 0.5:
            while speed < 0.5:
                atempo_option_temp_list.append("atempo=0.5")
                speed /= 0.5
        # 引数が2よりも大きい場合
        else:
            while speed > 2:
                atempo_option_temp_list.append("atempo=2")
                speed /= 2
        # 引数となる文字列の生成
        atempo_option_temp_list.append("atempo=" + str(speed))
        atempo_option = ','.join(atempo_option_temp_list)
    return atempo_option


def change_audio_speed(input_file, output_file, speed):
    attempo_option = atempo_option_generator(speed)
    # subprocessでターミナル上に入力するコマンドを実行
    command = ['ffmpeg', '-i', input_file, '-filter:a', attempo_option, output_file]
    subprocess.run(command)

def process_all_mp3_files(speed):
    # 現在のディレクトリ内のすべてのMP3ファイルを取得
    mp3_files = glob.glob("*.mp3")
    for mp3_file in mp3_files:
        # 出力ファイル名を作成
        output_file = f"{speed}_{mp3_file}"
        # 速度を変更して保存
        change_audio_speed(mp3_file, output_file, speed)

if __name__ == "__main__":
    # 引数の数チェック
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <speed[ 0.1 <= speed <= 9.9 ]>")
        sys.exit(1)
    # 引数のチェック
    try:
        speed = float(sys.argv[1])
    except ValueError:
        print("Error: Speed must be a numeric value.")
        sys.exit(1)
    # 引数の倍率範囲チェック
    if not atempo_validator(speed):
        print("Error: Speed is out of range.")
        sys.exit(1)
    # メイン処理の実行
    process_all_mp3_files(speed)
