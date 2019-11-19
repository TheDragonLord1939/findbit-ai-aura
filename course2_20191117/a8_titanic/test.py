# coding:utf8

# Microsoft YaHei

from matplotlib.font_manager import _rebuild

_rebuild()

import matplotlib.font_manager

a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)

# Microsoft Sans Serif

from matplotlib import pyplot as plt

data_dict = {
    "name_data": ["延边", "杭州", "深圳", "上海", "未知"], "val_data": [54, 54, 90, 279, 594]}

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 8), dpi=100)
plt.plot(data_dict["name_data"], data_dict["val_data"])

plt.show()
