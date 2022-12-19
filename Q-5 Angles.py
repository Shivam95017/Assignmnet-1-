import math
for angle in range(0,346,15):
    print(angle,".....",round(math.sin((angle*math.pi)/180),4),round(math.cos((angle*math.pi)/180),4))
