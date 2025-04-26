# Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).
import random

height, soccer, basketball = [], [], []
for i in range(20):
    height.append(random.randint(150, 200))
    if height[i] < 190:
        soccer.append(height[i])
    else:
        basketball.append(height[i])
print(len(soccer), 'юнош направлены в футбольную команду и', len(basketball), 'в баскетбольную')
print(soccer)
print(basketball)

