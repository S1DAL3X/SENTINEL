#python 3.7.7
#by S1DAL3X
import os
import discord
import json
import requests
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])
client = commands.Bot(command_prefix = settings['prefix'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx):# Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Фыр Фыр, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

#команда для рандомной фотки лисы
@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомная фотка лисы =)') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

#команда для вывода информации о боте
@bot.command()
async def info(ctx):
    embed=discord.Embed(title="by S1DAL3X", url="https://data.whicdn.com/images/289164972/original.png", description="Foxy - это Discord-бот, написанный на Python и discord.py", color=0xc48227)
    embed.set_author(name="Foxy", url="https://github.com/S1DAL3X", icon_url="https://lisaland.ru/wp-content/uploads/2020/04/lisa10044-1144x1258.jpg")
    embed.set_thumbnail(url="https://data.whicdn.com/images/289164972/original.png")
    embed.add_field(name="Команды", value="$hello | $fox | $info | $join | $leave | $send_hello | $clear", inline=False)
    embed.add_field(name="Воспроизведение музыки", value="Скоро этот бот научится делать Циркус прямо в канале", inline=False)
    embed.set_footer(text="**даже лиса знает, что дед - 3.14дор**")
    await ctx.send(embed=embed)

#команда для подключения к войс чату(каналу)
@bot.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        vocie = await channel.connect()
        await ctx.send(f'Foxy присоединился к {channel}!')

#команда для выхода из войс чата(канала)
@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        vocie = await connect.channel()
        await ctx.send(f'Foxy отсоединился от канала {channel}!')

#команда для отправки сообщения автору сообщения
@bot.command()
async def send_author(ctx):
    await ctx.author.send('Hello World!')

#отправка сообщения от другого пользователя
@bot.command()
async def send_hello( ctx, member: discord.Member):
    await member.send( f'{member.name}, привет от {ctx.author.name}')
    await ctx.send(f'{ ctx.author.name } отправил Привет пользователю {ctx.author.name}')

#команда для удаления сообщений (по умолчанию 100)
@bot.command(pass_context = True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)

#команда для вывода сообщений канала в консоль
@bot.command()
async def on_spy(ctx):
    channel = ctx.message.author.voice.channel
    await ctx.send(f'Прослушка на канале {channel} вкл!')
    @bot.event
    async def on_message(message):
        console_log = 'Message from {0.author}: {0.content}'.format(message)
        print(console_log)
        f = open("discord_chat_log.txt", "a", encoding='utf-8')
        f.write(console_log + "\n")

        
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена
