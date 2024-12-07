import numpy as np
import pandas as pd

# 計算関数
def calc_Z(W_h):
    A = 377  # 真空の特性インピーダンス [Ω]
    return A * (W_h + (2 / (np.pi)) * (1 + np.log(1 + (np.pi / 2) * W_h))) ** (-1)

# データリスト
data = [
    {"sqrt_epsilon_eff": 1.85, "W_h": 4.34},
    {"sqrt_epsilon_eff": 1.85, "W_h": 3.19},
    {"sqrt_epsilon_eff": 1.9, "W_h": 2.35},
    {"sqrt_epsilon_eff": 1.9, "W_h": 1.89},
    {"sqrt_epsilon_eff": 2, "W_h": 1.51},
]

# 計算結果を保存
results = []
for entry in data:
    Zo = calc_Z(entry["W_h"])  # Z0 を計算
    Z = Zo / entry["sqrt_epsilon_eff"]  # Z を計算
    results.append({"sqrt_epsilon_eff": entry["sqrt_epsilon_eff"], "W_h": entry["W_h"], "Zo (Ω)": Zo, "Z (Ω)": Z})

# データフレーム化
df_results = pd.DataFrame(results)

# 結果を表示
print(df_results)
