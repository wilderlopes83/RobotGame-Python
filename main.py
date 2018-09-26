import robot
import reward
import random

robot1 = robot.Robot(5, 5)
r1 = reward.Reward(random.randrange(1, 11, 1), random.randrange(1, 11, 1), "money")
r2 = reward.Reward(random.randrange(1, 11, 1), random.randrange(1, 11, 1), "fuel")
r3 = reward.Reward(random.randrange(1, 11, 1), random.randrange(1, 11, 1), "cake")
r4 = reward.Reward(random.randrange(1, 11, 1), random.randrange(1, 11, 1), "sweet")
r5 = reward.Reward(random.randrange(1, 11, 1), random.randrange(1, 11, 1), "coin")

rewards = [r1, r2, r3, r4, r5]

#print( rewards)

for i in range(10):
    mov = input("Informe o movimento desejado:")
    if mov == "l":
        robot1.move_left()
    elif mov == "r":
        robot1.move_right()
    elif mov == "u":
        robot1.move_up()
    elif mov == "d":
        robot1.move_down()
    else:
        print('Movimento não reconhecido')        
        continue
    
    print("Posição atual: x={}, y={}".format(robot1.x, robot1.y))
    for item in rewards:
        if (item.x == robot1.x and item.y == robot1.y):
            print("Recompensa encontrada {}".format(item.name))

