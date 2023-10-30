import pandas as pd
import matplotlib.pyplot as plt 

cities = '5'
code = 'ar' + cities
df = pd.read_csv('../saidas/SA/' + code + '_solution.csv', sep=';')



y = df['Solution']
x = list(range(1, len(y)+1))

fig,ax = plt.subplots()

fig.set_size_inches(6, 4)
ax.plot(x, y, "-", label="Complete model", linewidth=2.0, markersize=12, color='#006bb3')

ax.set_xlabel("Iteração", fontsize=24, labelpad=8)
ax.set_ylabel("Distância total",fontsize=24)

ax.set_xticks([0, 50, 100, 150, 200, 250, 300])
ax.set_xticklabels([0, 50, 100, 150, 200, 250, 300], fontsize=22)

#ax.set_yticks([3000, 7000, 12000, 16000, 22000])
#ax.set_yticklabels([3000, 7000, 12000, 16000, 22000], fontsize=22)

ax.set_yticks([3000, 5000, 7000, 9000, 11000])
ax.set_yticklabels([3000, 5000, 7000, 9000, 11000], fontsize=22)

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', **tkw, labelsize=22)

ax.set_title('TSP '+ cities + ' nós', fontsize=22)
#ax.tick_params(axis='x', **tkw, labelsize=16)

ax.grid(b=True, which='major', linestyle='--')

plt.savefig(code + ".pdf", bbox_inches='tight')

#plt.show()