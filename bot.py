from discord import Client, Embed
import random
from datetime import datetime, timedelta
import asyncio
from dotenv import load_dotenv
import os


client = Client()
load_dotenv()


TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
@client.event
async def on_ready():
    cnl = client.get_channel(CHANNEL_ID)
    await cnl.send("`Motivational Quotes Channel has been activated`")
    print(f'We have logged in as {client.user}')
    await schedule_daily_message()


@client.event
async def on_message(msg):
    usr_nm = str(msg.author).split("#")[0]
    usr_msg = str(msg.content)
    cnl = str(msg.channel.name)
    print(f"{usr_nm}\n{usr_msg}\nFrom:\n{cnl}")

    commands_lst = ["!!random", "!!quote", "!!lets chat"]
    if msg.author == client.user:
        return

    if msg.channel.name == "bot_test":
        if usr_msg.lower() == "hello":
            await msg.channel.send(f"Hello {usr_nm}")
            return
        elif usr_msg.lower() == "bye":
            await msg.channel.send(f"Bye, Have a nice day {usr_nm}!")
            return
        elif usr_msg.lower() == "!!list":
            await msg.channel.send(f"Here are the commands\n")
            for i in commands_lst:
                await msg.channel.send(i)
            return
        elif usr_msg.lower() == "!!random":
            await msg.channel.send(f"Here is your random number {random.randrange(10000)}")
            return
        elif usr_msg.lower() == "!!quote":

            embed = Embed(title = "Quote of the day", color = 0x00A300)
            embed.add_field(name = "If you feel like you have substitutes then, Remember", value = "DO or DIE", inline = False)
            embed.set_footer(text = "Because Life is Binary")
            await msg.channel.send(embed = embed)
            return

async def schedule_daily_message():
    now = datetime.now()
    then = now + timedelta(days = 1)
    new_then = then.replace(hour = 6, minute = 0)
    wait_time = (new_then - now).total_seconds()
    await asyncio.sleep(wait_time)
    channel = client.get_channel(CHANNEL_ID)
    embed = Embed(title = "Quote of the day", color = 0x00A300)
    embed.add_field(name = "@everyone If you feel like you have substitutes then, Remember", value = "DO or DIE", inline = False)
    embed.set_footer(text = "Because Life is Binary")
    await channel.send(embed = embed)


client.run(TOKEN)

