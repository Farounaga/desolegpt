import discord
import os
import random
from discord.ext import commands

print(f"Available environment variables: {os.environ}")

TOKEN = os.getenv("DISCORD_TOKEN")  # Получаем токен из переменной окружения

print("DISCORD_TOKEN (exists):", 'DISCORD_TOKEN' in os.environ)
print("DISCORD_TOKEN (value):", os.getenv("DISCORD_TOKEN"))
print(f"DISCORD_TOKEN from env: {TOKEN}")  # Добавь это в начало кода

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Путь к папке с видео
VIDEO_FOLDER = "./files/"

номерочек = 863100432914317393
видосики = ["karla.mp4", "karla2.mp4", "karla3.mp4"]

KEYWORDS = {
    "amogus": ["amogus.mp4"],
    "anglais": ["anglais.mp4"],
    "bad": ["bad.mp4"],
    "bierre": ["bierre.mp4"],
    "cactus": ["cactus.mp4"],
    "ceinture": ["ceinture.mp4"],
    "chat": ["chat.mp4", "chat2.mp4", "chat3.mp4", "chat4.mp4", "chat5.mp4", "chat6.mp4"],
    "chien": ["chien.mp4"],
    "coeur": ["coeur.mp4"],
    "coq": ["coq.mp4", "coq2.mp4"],
    "cours": ["cours.mp4"],
    "dance": ["dance.mp4", "dance2.mp4", "dance3.mp4", "dance4.mp4", "dance5.mp4", "dance6.mp4", "dance7.mp4", "dance8.mp4"],
    "denitste": ["denitste.mp4"],
    "docteur": ["docteur.mp4"],
    "envoyer": ["envoyer.mp4"],
    "erika": ["erika.mp4"],
    "fumer": ["fumer.mp4", "fumer2.mp4"],
    "guitare": ["guitare.mp4"],
    "gym": ["gym.mp4", "gym2.mp4", "gym3.mp4"],
    "hardcore": ["hardcore.mp4"],
    "jar": ["jar.mp4"],
    "lapin": ["lapin.mp4", "lapin2.mp4"],
    "manger": ["manger.mp4"],
    "naruto": ["naruto.mp4"],
    "nuit": ["nuit.mp4", "nuit2.mp4", "nuit3.mp4", "nuit4.mp4"],
    "pigeon": ["pigeon.mp4"],
    "potter": ["potter.mp4"],
    "python": ["python.mp4"],
    "rouler": ["rouler.mp4"],
    "salade": ["salade.mp4"],
    "shrek": ["shrek.mp4"],
    "smack": ["smack.mp4"],
    "smile": ["smile.mp4"],
    "spin": ["spin.mp4"],
    "stop": ["stop.mp4"],
    "thé": ["the.mp4"],
    "tomber": ["tomber.mp4"],
    "triste": ["triste.mp4"],
    "turk": ["turk.mp4"],
    "vache": ["vache.mp4"],
    "voter": ["voter.mp4"],
    "woman": ["woman.mp4", "woman2.mp4"],

}

@bot.event
async def on_ready():
    print(f"🔥 Halo {bot.user} !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Если пишет Карла → отправить случайное видео, не важно что она пишет
    if message.author.id == номерочек:
        video_file = random.choice(видосики)
        video_path = os.path.join(VIDEO_FOLDER, video_file)

        if os.path.exists(video_path):
            await message.channel.send(file=discord.File(video_path))
        else:
             print(f"❌ AYO: file {video_file} not found!")

    else:
        # Если пишет кто-то другой → проверяем ключевые слова
        for keyword, video_files in KEYWORDS.items():
            if keyword in message.content.lower():
                video_file = random.choice(video_files)
                video_path = os.path.join(VIDEO_FOLDER, video_file)

                if os.path.exists(video_path):
                    await message.channel.send(file=discord.File(video_path))
                else:
                    print(f"❌ AYO: file {video_file} not found!")

    await bot.process_commands(message)


bot.run(TOKEN)