# by poseidon, inspired by kill.py

import asyncio


from userge import userge


@userge.on_cmd("gali$", about={'header': "slang to a bitch with power of bot"})

async def gali_func(message):   
    animation_chars =[
    "teri maa ki chut randwe......",
    "lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge------>^<",
    " maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye ......",
    "bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale ........^.|.^>><<",
    "tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo......._____>",
    "jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod ------->^<",
    "kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod.....",
    "tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche^.^___",
    "I'm sorry I hurt your feelings when I called you madarchod. I thought you already knew that ------______>",
    "<b>You are proof that evolution CAN go in reverse</b>"
    ]
    for i in range(10):
        await asyncio.sleep(5)
        await message.edit(animation_chars[i])