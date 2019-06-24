import time
from datetime import datetime
count = 0
while count < 10:
    print("Count: "+str(count) )
    if count < 5:
        print("Menor que: ")
        time.sleep(3)
        print("Time: ")
        print(datetime.now())
        print("")
        count += 1
    else:
        print("Maior que: ")
        time.sleep(3)
        print("Time: ")
        print(datetime.now())
        print("")
        count += 1
