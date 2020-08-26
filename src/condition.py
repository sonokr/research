import numpy as np

# 条件値（いずれ設定ファイルにまとめる）
dt = 0.002
Tend = 3.0

TE = 0.8  # 駆動時間
SE = np.pi / 2  # 目標角

Nrk = round(Tend / dt)
Nte = round(TE / dt)

# リンク1のパラメータ
ome1 = 12.68
z1 = 15.49 * 10 ** (-3)
a1 = 2.266 * 10 ** (-1)
b1 = 2.004 * 10 ** (-3)

# リンク2のパラメータ
ome2 = 10.71
z2 = 14.27 * 10 ** (-3)
a2 = 2.570 * 10 ** (-1)
b2 = 5.822 * 10 ** (-3)

# トルク関数のパラメータ
g1 = 2.996 * 10 ** (-2)
g2 = 6.652 * 10 ** (-2)
g3 = 5.237 * 10 ** (-2)
cs = 4.202 * 10 ** (-2)
