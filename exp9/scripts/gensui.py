import numpy as np
import pandas as pd

# 定数
mu_0 = 4 * np.pi * 1e-7  # 真空透磁率 [H/m]
epsilon_0 = 8.854187817e-12  # 真空誘電率 [F/m]
f = 1e9  # 周波数 [Hz]
omega = 2 * np.pi * f  # 角周波数 [rad/s]
sigma_dielec = 0.02  # FR4の損失正接 (tan δ)
sigma_cond = 5.8e7  # 銅の導電率 [S/m]
h = 1e-3  # 基板厚 [m]
epsilon_r = 4.7  # FR4の比誘電率

# 実効誘電率を計算する関数
def calc_epsilon_eff(W):
    return (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 + 12 * h / W)**-0.5

# 位相定数を計算する関数
def calc_beta(sqrt_epsilon_eff):
    epsilon_eff = sqrt_epsilon_eff**2
    return omega * np.sqrt(epsilon_eff * mu_0)

# 減衰定数を計算する関数
def calc_alpha(sqrt_epsilon_eff, beta):
    epsilon_eff = sqrt_epsilon_eff**2
    tan_delta = sigma_dielec
    Rs = np.sqrt(omega * mu_0 / (2 * sigma_cond))
    zeta = np.sqrt(mu_0 / (epsilon_0 * epsilon_eff))
    return 0.5 * np.sqrt(epsilon_eff) * beta * tan_delta + (epsilon_eff * Rs) / (zeta * h)

# 各特性インピーダンスのWを設定
W_values = [7.632451e-3, 3.871652e-3, 2.150932e-3, 1.418567e-3, 1.028369e-3]  # W [m]
Z0_values = [30, 40, 50, 60, 70]  # Z0 [Ω]

# 計算結果を保存
results = []
for W, Z0 in zip(W_values, Z0_values):
    sqrt_epsilon_eff = np.sqrt(calc_epsilon_eff(W))
    beta = calc_beta(sqrt_epsilon_eff)
    alpha = calc_alpha(sqrt_epsilon_eff, beta)
    results.append({"Z0 (Ω)": Z0, "W (mm)": W * 1e3, "alpha (Np/m)": alpha, "beta (rad/m)": beta})

# データフレームに変換
df_results = pd.DataFrame(results)

# 結果を表示
print("\n計算結果:")
print(df_results.to_string(index=False))
