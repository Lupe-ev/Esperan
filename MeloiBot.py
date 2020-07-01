import discord
import random

def get_rand_range(dict_table, value):
    for key in dict_table:
        if key[0] <= value <= key[1]:
            return dict_table[key]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$destroy'):
        vals = message.content.split(" ")
        if len(vals)!=3:
            await message.channel.send('Please use the format:\n$destroy itemName itemValue')
        else:
            item_name = vals[1]
            item_value = int(vals[2])
            rand = random.randint(1,100)
            value_dict = {(0,75): 0.5,
                          (76,80): 0.55,
                          (81,85): 0.6,
                          (86,90): 0.7,
                          (91,95): 0.8,
                          (96,99): 0.9,
                          (100,100): 1}
            return_perc = get_rand_range(value_dict, rand)
            return_value = item_value * return_perc
            await message.channel.send("Value returned from %s is %d gold with a roll of %d (return %.2f %%)" % (item_name, return_value, rand, return_perc))
            return print("Value returned from %s is %d gold with a roll of %d (return %.2f %%)" % (item_name, return_value, rand, return_perc))

client.run('NzIzMjA5NzMwMDk2MzY1NjEw.XuuTyw.LtHiwGzXu21lCzo44clrCuqva7Y')
