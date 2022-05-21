from discordbot.discord_automessage import sendMessage, channelInfo
import time
import random


messages_list = [
    "Hello Everyone",
    "Hey",
    "Let's Do this",
    "To the Moon",
    "I'm tired ooo",
    "We have to keep trying hard",
    "Where y'all at",
    "Lolmaooo",
    "Money must be made",
    "One Last One",
    "Stay Active",
    "Let's Goooooo",
    "Stay Positive",
    "We Keep Going",
    "-message",
    "let's go geeks 💫"
]

for i in range(90):
    try:
        print(f"Number 1----> {i}")
        index = random.randrange(0, len(messages_list))
        sendMessage(916009605476278322, messages_list[index])
        time.sleep(10)
        """index = random.randrange(0, len(messages_list))
        sendMessage(892467700599754762, messages_list[index])
        time.sleep(10)
        index = random.randrange(0, len(messages_list))
        sendMessage(892467271681843240, messages_list[index])
        time.sleep(10)
        index = random.randrange(0, len(messages_list))
        sendMessage(892468097066348654, messages_list[index])
        print("\n\n")
        time.sleep(280)"""
    except:
        pass