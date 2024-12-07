import numpy as np
import pandas as pd

# ファイルのパスと伝送線路の長さ（例: 0.1m）
file_path = "your_file_path.s2p"  # 実際のファイル名に置き換えてください
line_length = 0.1  # 伝送線路の長さ [m]

# データを読み込む
data = pd.read_csv(file_path, comment='!', delim_whitespace=True, header=None)

# 必要な列を抽出
freq = data[0]  # 周波数 [GHz]
S11_re = data[1]  # S11の実部
S11_im = data[2]  # S11の虚部

# S11の絶対値を計算
S11_mag = np.sqrt(S11_re**2 + S11_im**2)

# 減衰定数を計算
attenuation_constant = -np.log(S11_mag) / line_length  # 単位: [Np/m]

# 結果をDataFrameにまとめる
result = pd.DataFrame({
    "Frequency (GHz)": freq,
    "S11 Magnitude": S11_mag,
    "Attenuation Constant (Np/m)": attenuation_constant
})

# 結果を表示
print(result)

# 必要に応じてCSVに出力
result.to_csv("attenuation_constant.csv", index=False)
