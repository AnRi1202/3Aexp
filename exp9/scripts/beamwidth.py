import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# CSV ファイルのパス
csv_file = "../data/day5/20241125_patch1_4GHz_amp.csv"
csv_file = "../data/day5/20241125_patch8Ghz_true_amp.csv"



# データの読み込み
data = pd.read_csv(csv_file, header=0)

# 出力フォルダを作成
output_folder = "./output"
os.makedirs(output_folder, exist_ok=True)

# 一行目（周波数）をタイトルに取得
frequencies = data.columns[0:]  # 最初の列を除外 (周波数列)

# 一列目（位相）を角度に変換
phases = data.iloc[:, 0].values  # 最初の列 (位相)

# 特定の周波数（4GHz）の列を取得
target_frequency = "4000000000.0"  # 周波数の文字列
if target_frequency in frequencies:
    values = data[target_frequency].values  # 指定列のデータ
    angles = np.deg2rad(phases)  # 度をラジアンに変換

    # 最大振幅と-3dBのラインを計算
    max_amplitude = np.max(values)
    threshold = max_amplitude - 3

    # 円上にプロット
    plt.figure(figsize=(6, 6))
    plt.polar(angles, values, label=f"{target_frequency} Hz")
    plt.polar(angles, [threshold] * len(angles), 'r--', label="-3 dB Threshold")  # -3dBラインを追加

    # グラフ設定
    plt.legend(loc="upper right")
    plt.tight_layout()

    # グラフを保存
    polar_plot_path = os.path.join(output_folder, "polar_plot_8GHz.png")
    plt.savefig(polar_plot_path)
    plt.close()  # プロットを閉じる

    print(f"Polar plot saved to {polar_plot_path}")
else:
    print(f"Frequency {target_frequency} not found in the data.")

# 周波数 (列ヘッダから2列目以降を取得)
frequencies = data.columns[1:].astype(float) / 1e9  # GHz に変換

# 特定の行を選択 (例: 0行目, 位相=0° の場合)
row_index = 0  # 対象とする行のインデックス
phase = data.iloc[row_index, 0]  # 最初の列 (位相, 度)
magnitude = data.iloc[row_index, 1:].values  # 残りの列 (振幅データ, dB)

# 線形プロット
plt.figure(figsize=(10, 6))
plt.plot(frequencies, magnitude, marker="o", linestyle="-", color="b", label=f"Phase: {phase}°")

# -3dBのラインを追加
plt.axhline(y=threshold, color='r', linestyle='--', label="-3 dB Threshold")

# プロットの設定
plt.xlabel("Frequency (GHz)", fontsize=12)
plt.ylabel("Magnitude (dB)", fontsize=12)
plt.grid(True)
plt.legend(fontsize=10)

# グラフを保存
line_plot_path = os.path.join(output_folder, "line_plot_phase_0deg_8GHz.png")
plt.savefig(line_plot_path)
plt.close()  # プロットを閉じる

print(f"Line plot saved to {line_plot_path}")
