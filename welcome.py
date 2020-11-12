from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)

how_many_snakes = 2
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


# print(snake_string * how_many_snakes)