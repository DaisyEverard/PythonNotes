import matplotlib.pyplot as plt
import numpy as np

def getXPfromLevel(level):
    if 1 <= level <= 16:
        return int(level ** 2 + 6 * level)
    elif 17 <= level <= 31:
        return int(2.5 * level ** 2 - 40.5 * level + 360)
    elif level >= 32:
        return int(4.5 * level ** 2 - 162.5 * level + 2220)
    else:
        return 0

levels = list(range(1, 101))
xp_values = [getXPfromLevel(level) for level in levels]

plt.figure(figsize=(12, 6))
plt.plot(levels, xp_values, marker='o', linestyle='-', color='blue')
plt.title('Experience Required per Level (1 to 100)')
plt.xlabel('Level')
plt.ylabel('XP Required for Level')
plt.grid(True)
plt.xticks(np.arange(0, 101, 5))
plt.tight_layout()
plt.show()
