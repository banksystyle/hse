import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import re

df_out = pd.read_excel('table.xlsx')
for area in df_out.area.unique():
    ms = df_out[df_out.area == area]
    plt.figure(figsize=(18, 18))
    plt.scatter(x = ms['x'],
                y = ms['y'],
                alpha=1, s=100,
                c = ms['color'],
                marker='o',
                linewidths=1,
                edgecolors='#000000')
    plt.grid(alpha=0.1)

    for x, y, c, k in ms[['x', 'y', 'color', 'keyword']].values:
        if len(k) > 15:
            k = k[:len(k) // 2] + '\n' + k[len(k) // 2:]
        plt.text(x, y+0.2, k, color=c, fontsize=10, horizontalalignment='center')

    patch = [mpatches.Patch(color=c, label=l) for c, l in zip(ms.color.unique(), ms.cluster_name.unique())]
    plt.legend(handles=patch)
    
    plt.savefig('area_{}.svg'.format(re.sub('\W','_',area)), dpi=150)
