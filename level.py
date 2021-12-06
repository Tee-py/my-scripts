from discord_automessage import sendMessage, channelInfo
import time
import random


messages_list = [
    "Keep typing for guys we can do it and keep healthy too",
    "We should keep trying hard",
    "Omo To make money no easy ooo😂😂",
    "Hand don dey pain me self😂😂",
    "We go hard or we go home",
    "The strong shall make mouth",
    "Make i go price Lambo👍"
]

for i in range(10000):
    try:
        print(f"Number 1----> {i}")
        index = random.randrange(0, len(messages_list))
        sendMessage(892466763130863616, messages_list[index])
        time.sleep(10)
        index = random.randrange(0, len(messages_list))
        sendMessage(892467700599754762, messages_list[index])
        time.sleep(10)
        index = random.randrange(0, len(messages_list))
        sendMessage(892467271681843240, messages_list[index])
        time.sleep(10)
        index = random.randrange(0, len(messages_list))
        sendMessage(892468097066348654, messages_list[index])
        print("\n\n")
        time.sleep(280)
    except:
        pass