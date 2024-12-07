import matplotlib.pyplot as plt
import numpy as np
import skrf as rf  # scikit-rfライブラリを使用

# Touchstoneファイルのパス
file_path = "../data/day4/60_stab.s2p"

# Touchstoneファイルの読み込み
try:
    network = rf.Network(file_path)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit()

# 周波数（Hz）をGHzに変換
frequencies = network.f / 1e9  # 周波数 [GHz]

# Sパラメータの絶対値 (dB)
s11_db = 20 * np.log10(np.abs(network.s[:, 0, 0]))  # S11
s21_db = 20 * np.log10(np.abs(network.s[:, 1, 0]))  # S21
s12_db = 20 * np.log10(np.abs(network.s[:, 0, 1]))  # S12
s22_db = 20 * np.log10(np.abs(network.s[:, 1, 1]))  # S22

# プロット
plt.figure(figsize=(10, 6))
plt.plot(frequencies, s11_db, label="|S11| (dB)")
plt.plot(frequencies, s21_db, label="|S21| (dB)")


# グラフの設定
# plt.title("S-parameters vs Frequency", fontsize=16)
plt.xlabel("Frequency (GHz)", fontsize=14)
plt.ylabel("Magnitude (dB)", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# 結果を保存
output_path = "../data/day4/60_stab_plot.png"
plt.savefig(output_path)
print(f"Plot saved to '{output_path}'.")

# プロットを表示
plt.show()
