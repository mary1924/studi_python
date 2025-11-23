import threading, random, time

warehouses = [random.randint(100, 300) for _ in range(3)]
earnings = [0, 0, 0, 0, 0]
attempts = 10


def runner(i):
    global warehouses, earnings
    for _ in range(attempts):
        w = random.randint(0, 2)       
        amt = random.randint(10, 30)  
        chance = random.random()       

        if chance < 0.2:              
            stolen = 0
        elif chance < 0.4:            
            stolen = min(warehouses[w], amt//2)
        else:                          
            stolen = min(warehouses[w], amt)

        warehouses[w] -= stolen
        earnings[i] += stolen * 5
        time.sleep(random.uniform(0.1, 0.4))  


threads = []
for i in range(5):
    t = threading.Thread(target=runner, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print("Склади:", warehouses)
print("Заробіток по бігунах:", earnings)
print("Загальний дохід:", sum(earnings))