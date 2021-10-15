import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7]
days = ['','Not Friday', 'Not Friday', 'Not Friday',
        'Not Friday', 'Friday', 'Not Friday', 'Not Friday', '']
meter = [0, 0, 0, 0, 1000, 0, 0, 0]

fig, ax = plt.subplots(figsize=(5, 5))

ax.bar(x, meter)
ax.set_xticklabels(days)
ax.set_title('Fridayness meter')
ax.set_xlabel('Weekday')
ax.set_ylabel('Fridayness score')

plt.show()
