from discord_automessage import sendMessage, channelInfo
import time
import random


messages_list = [
    "This project looks very interesting.",
    "I am interested, and I will support this project until it is successful according to the plan"
    "Don't be lazy for something good is awaiting you",
    "Keep typing for guys we can do it and keep healthy too",
    "This is a very Nice Project.",
    "We should keep trying hard",
    "The Pain is worth it Guys. Let's Keep Moving.",
    "This is going to be a massive one Guys. Let's Keep Working",
    "to the world",
    "Hello Everyone, Try This out.",
    "I love swalana.",
    "A Great Country",
    "Keep Moving Guys",
    "We Go Hard or We Go Home Guys."
]

for i in range(10000):
    print(f"Number 1----> {i}")
    index = random.randrange(0, len(messages_list))
    sendMessage(872911192820162650, messages_list[index])
    sendMessage(888118378571640885, messages_list[index])
    sendMessage(888118690099392522, messages_list[index])
    sendMessage(888119773152550942, messages_list[index])
    sendMessage(888190363683131412, messages_list[index])
    sendMessage(888119111299772496, messages_list[index])
    sendMessage(888472298905018368, messages_list[index])
    sendMessage(888119532940582934, messages_list[index])
    sendMessage(888119618269503579, messages_list[index])
    sendMessage(888119349653692426, messages_list[index])
    print("\n\n")
    time.sleep(120)