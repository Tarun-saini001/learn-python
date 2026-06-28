import math
import random
from datetime import datetime

print(math.sqrt(25))
print(random.randint(1,10))
print(datetime.now())

now=datetime.now()
print(now.strftime("%Y-%m-%d"))          # 2026-06-28
print(now.strftime("%d/%m/%Y"))          # 28/06/2026
print(now.strftime("%B %d, %Y"))         # June 28, 2026
print(now.strftime("%a, %d %b %Y"))      # Sun, 28 Jun 2026
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 2026-06-28 15:45:12
print(now.strftime("%I:%M:%S %p"))       # 03:45:12 PM