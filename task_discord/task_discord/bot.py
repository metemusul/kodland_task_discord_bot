
import discord
from discord.ext import commands
import sqlite3
from database import get_db_connection

# BOT TOKENİNİ BURAYA YAPIŞTIR (GÜVENLİĞE DİKKAT ET!)
TOKEN = "MTM1MDE4NjA0ODE2NDA2OTM4Ng.GTDs6A.QF9upnFCEH6cmp-FFgfCbnZWKzLtHy4Jy3USaA"

# Tüm izinleri aç
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} olarak giriş yaptı.')

@bot.command()
async def add_task(ctx, *, description: str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, 0))
    conn.commit()
    conn.close()
    await ctx.send(f'✅ Görev eklendi: {description}')

@bot.command()
async def delete_task(ctx, task_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'🗑 Görev silindi: {task_id}')

@bot.command()
async def show_tasks(ctx):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()

    if tasks:
        task_list = "\n".join([f"{task[0]}: {task[1]} {'(✅ Tamamlandı)' if task[2] else '(⏳ Bekliyor)'}" for task in tasks])
        await ctx.send(f"📋 **Görevler:**\n{task_list}")
    else:
        await ctx.send("📭 Hiç görev bulunmamaktadır.")

@bot.command()
async def complete_task(ctx, task_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'✅ Görev tamamlandı olarak işaretlendi: {task_id}')

bot.run(TOKEN)
