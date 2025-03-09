import discord
from discord import app_commands, Embed
from discord.ext import commands
import responses
import random
import asyncio
import os
from elevenlabs.client import ElevenLabs
from elevenLabsFunctions import text_to_speech_file
from restrictedwords import prohibited_words 
from config import *
from constants import *
from utilities import *

# Function to send messages
async def send_message(message, user_message, is_private):
    try: 
        response = responses.get_response(user_message) 
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Regular Command Handling
async def handle_regular_commands(message):
    # Extracting user info and message content
    username = str(message.author)
    user_message = str(message.content).lower()
    
    # user_data[username] = user_data.get(username, 0) + 1
    # save_user_data(user_data)
    
    # Roll a D10
    if user_message == "!d10":
        num = random.randint(1, 10)
        if (num < 5): 
            await message.channel.send(f"You rolled a {num}! Sadly, you failed the stat check... :(")
        else: 
            await message.channel.send(f"Yay, you rolled a {num}! You passed the stat check! :D")

    # Roll a D20
    if user_message == "!d20":
        num = random.randint(1, 20)
        if (num < 10): 
            await message.channel.send(f"You rolled a {num}! Sadly, you failed the stat check... :(")
        else: 
            await message.channel.send(f"Yay, you rolled a {num}! You passed the stat check! :D")

    # Valorant Pick Up Lines Command
    elif user_message == "!val":
        quote = random.choice(VALORANT_QUOTES)
        await message.channel.send(quote)

    # OSU Trivia Command
    elif user_message == "!osutrivia":
        await handle_osu_trivia(message)
    
    elif user_message == "!valoranttrivia":
        await handle_valorant_trivia(message)

    # React to Message
    elif user_message.lower() == "!react":
        emojis = ["😄", "👍", "🎉", "🤖"]
        emoji = random.choice(emojis)
        await message.add_reaction(emoji)

    elif user_message.lower() == "!crazy":
        await message.channel.send("Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room filled with rats. And rats make me crazy. Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room filled with rats. And rats make me crazy.")

    elif user_message.lower() == "!toothless":
        voice_channel = message.author.voice.channel
    # Only play music if user is in a voice channel
        if voice_channel:
        # Grab user's voice channel
            channel = voice_channel.name
            await message.channel.send('User is in channel: ' + channel)
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file
            vc.play(discord.FFmpegPCMAudio('Audios/toothless_dancing.mp3'), after=lambda e: print('done', e))

        # Wait until the audio is done playing
            while vc.is_playing():
                await asyncio.sleep(1)

        # Disconnect after the player has finished
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")
        
    elif user_message.lower() == "!laugh":
        voice_channel = message.author.voice.channel
    # Only play music if user is in a voice channel
        if voice_channel:
        # Grab user's voice channel
            channel = voice_channel.name
            await message.channel.send('User is in channel: ' + channel)
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file
            vc.play(discord.FFmpegPCMAudio('Audios/laugh.mp3'), after=lambda e: print('done', e))

        # Wait until the audio is done playing
            while vc.is_playing():
                await asyncio.sleep(1)

        # Disconnect after the player has finished
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")


    elif user_message.lower().startswith("!eric"):
    # Split the user message to get the number of repetitions
        parts = user_message.split()
        repetitions = 1  # Default repetitions

        if len(parts) > 1:
            try:
                repetitions = int(parts[1])  # Try to parse the number of repetitions
            # Limit the repetitions to a maximum of 10
                repetitions = min(repetitions, 10)
                if repetitions == 10:
                    await message.channel.send("Maximum repetitions capped at 10.")
            except ValueError:
                pass  # Ignore if the user input is not a valid number

        voice_state = message.author.voice
    # Check if the user is in a voice channel
        if voice_state and voice_state.channel:
            voice_channel = voice_state.channel
        # Grab the name of the voice channel
            channel_name = voice_channel.name
            await message.channel.send('User is in channel: ' + channel_name)
        
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file multiple times
            for _ in range(repetitions):
                vc.play(discord.FFmpegPCMAudio('Audios/Eric.mp3'), after=lambda e: print('done', e))
            # Wait until the audio is done playing before playing it again
                while vc.is_playing():
                    await asyncio.sleep(1)

        # Disconnect after all repetitions
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")

    elif user_message.lower().startswith("!chipichipi"):
    # Split the user message to get the number of repetitions
        parts = user_message.split()
        repetitions = 1  # Default repetitions

        if len(parts) > 1:
            try:
                repetitions = int(parts[1])  # Try to parse the number of repetitions
            # Limit the repetitions to a maximum of 10
                repetitions = min(repetitions, 10)
                if repetitions == 10:
                    await message.channel.send("Maximum repetitions capped at 10.")
            except ValueError:
                pass  # Ignore if the user input is not a valid number

        voice_state = message.author.voice
    # Check if the user is in a voice channel
        if voice_state and voice_state.channel:
            voice_channel = voice_state.channel
        # Grab the name of the voice channel
            channel_name = voice_channel.name
            await message.channel.send('User is in channel: ' + channel_name)
        
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file multiple times
            for _ in range(repetitions):
                vc.play(discord.FFmpegPCMAudio('Audios/chipichipi.mp3'), after=lambda e: print('done', e))
            # Wait until the audio is done playing before playing it again
                while vc.is_playing():
                    await asyncio.sleep(1)

        # Disconnect after all repetitions
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")


    elif user_message.lower().startswith("!jason"):
    # Split the user message to get the number of repetitions
        parts = user_message.split()
        repetitions = 1  # Default repetitions

        if len(parts) > 1:
            try:
                repetitions = int(parts[1])  # Try to parse the number of repetitions
            # Limit the repetitions to a maximum of 10
                repetitions = min(repetitions, 10)
                if repetitions == 10:
                    await message.channel.send("Maximum repetitions capped at 10.")
            except ValueError:
                pass  # Ignore if the user input is not a valid number

        voice_state = message.author.voice
    # Check if the user is in a voice channel
        if voice_state and voice_state.channel:
            voice_channel = voice_state.channel
        # Grab the name of the voice channel
            channel_name = voice_channel.name
            await message.channel.send('User is in channel: ' + channel_name)
        
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file multiple times
            for _ in range(repetitions):
                vc.play(discord.FFmpegPCMAudio('Audios/jason.mp3'), after=lambda e: print('done', e))
            # Wait until the audio is done playing before playing it again
                while vc.is_playing():
                    await asyncio.sleep(1)

        # Disconnect after all repetitions
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")
            

    elif user_message.lower().startswith("!fatherfigure"):
    # Split the user message to get the number of repetitions
        parts = user_message.split()
        repetitions = 1  # Default repetitions

        if len(parts) > 1:
            try:
                repetitions = int(parts[1])  # Try to parse the number of repetitions
            # Limit the repetitions to a maximum of 10
                repetitions = min(repetitions, 10)
                if repetitions == 10:
                    await message.channel.send("Maximum repetitions capped at 10.")
            except ValueError:
                pass  # Ignore if the user input is not a valid number

        voice_state = message.author.voice
    # Check if the user is in a voice channel
        if voice_state and voice_state.channel:
            voice_channel = voice_state.channel
        # Grab the name of the voice channel
            channel_name = voice_channel.name
            await message.channel.send('User is in channel: ' + channel_name)
        
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file multiple times
            for _ in range(repetitions):
                vc.play(discord.FFmpegPCMAudio('Audios/fatherfigure.mp3'), after=lambda e: print('done', e))
            # Wait until the audio is done playing before playing it again
                while vc.is_playing():
                    await asyncio.sleep(1)

        # Disconnect after all repetitions
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")
            

    elif user_message.lower().startswith("!shutup"):
    # Split the user message to get the number of repetitions
        parts = user_message.split()
        repetitions = 1  # Default repetitions

        if len(parts) > 1:
            try:
                repetitions = int(parts[1])  # Try to parse the number of repetitions
            # Limit the repetitions to a maximum of 10
                repetitions = min(repetitions, 10)
                if repetitions == 10:
                    await message.channel.send("Maximum repetitions capped at 10.")
            except ValueError:
                pass  # Ignore if the user input is not a valid number

        voice_state = message.author.voice
    # Check if the user is in a voice channel
        if voice_state and voice_state.channel:
            voice_channel = voice_state.channel
        # Grab the name of the voice channel
            channel_name = voice_channel.name
            await message.channel.send('User is in channel: ' + channel_name)
        
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file multiple times
            for _ in range(repetitions):
                vc.play(discord.FFmpegPCMAudio('Audios/shutup.mp3'), after=lambda e: print('done', e))
            # Wait until the audio is done playing before playing it again
                while vc.is_playing():
                    await asyncio.sleep(1)

        # Disconnect after all repetitions
            await vc.disconnect()
        else:
            await message.channel.send("❌ You need to be in a voice channel!")

    elif user_message.lower().startswith("!say"): 

        text_to_speak = " ".join(user_message.split()[1:])
        try:
            voice_channel = message.author.voice.channel
        except AttributeError:
            await message.channel.send("❌ You need to be in a voice channel!")
            return

        try:
            audio_file = text_to_speech_file(text_to_speak)
        except Exception as e:
            print(e)
            await message.channel.send("🔇 Sorry, I couldn't generate the audio file.")
            return
        

        if voice_channel:
        # Grab user's voice channel
            channel = voice_channel.name
            await message.channel.send('User is in channel: ' + channel)
        # Connect to the voice channel
            vc = await voice_channel.connect()

        # Play the audio file
            vc.play(discord.FFmpegPCMAudio(audio_file), after=lambda e: print('done', e))

        # Wait until the audio is done playing
            while vc.is_playing():
                await asyncio.sleep(1)

        # Disconnect after the player has finished
            await vc.disconnect()

            os.remove(audio_file)
            print(f"Deleted audio file: {audio_file}")
        else:
            await message.channel.send("❌ You need to be in a voice channel!")

    # Add more commands here

# OSU Trivia Command Handling
async def handle_osu_trivia(message):
    streak = 0
    highest_streak = 0
    points = 0
    while True: 
        question = random.choice(OSU_QUESTIONS)
        await message.channel.send(question["question"])

        try:
            def check(answer_message):
                return answer_message.author == message.author and answer_message.channel == message.channel

            answer_message = await client.wait_for("message", timeout=30.0, check=check)
            user_answer = answer_message.content.lower()

            if user_answer == "end":
                await message.channel.send(f"Thanks for Playing!")
                final_embed = Embed(title="🏆 Trivia Results", color=0xffd700)
                final_embed.add_field(name="Points", value=f"🥇{message.author}: {points} (Streak: {highest_streak} 🔥)  \n 🥈kale.: 7 (Streak: 2 🔥) \n 🥉nnosaj: 4 (Streak: 1 🔥) \n Ryli: 2 (Streak: 2 🔥)")
                await message.channel.send(embed=final_embed)
                break

            if user_answer == question["answer"].lower():
                streak += 1
                points += 1
                highest_streak = max(streak, highest_streak)
                await message.channel.send(f"✅ {message.author.mention}! The answer is {question['answer']}.")
            else:
                streak = 0
                await message.channel.send(f"❌ Wrong! The answer is {question['answer']}.")

        except asyncio.TimeoutError:
            streak = 0
            await message.channel.send(f"⏰ Time's up! The correct answer was: {question['answer']}")

# Valorant Trivia Command Handling
async def handle_valorant_trivia(message):
    streak = 0
    highest_streak = 0
    while True: 
        question = random.choice(VALORANT_QUESTIONS)
        await message.channel.send(question["question"])

        try:
            def check(answer_message):
                return answer_message.author == message.author and answer_message.channel == message.channel

            answer_message = await client.wait_for("message", timeout=30.0, check=check)
            user_answer = answer_message.content.lower()

            if user_answer == "end":
                await message.channel.send(f"Thanks for Playing! Your highest streak was {highest_streak} questions right in a row! 🔥")
                final_embed = Embed(title="🏆 Trivia Results", color=0xffd700)
                final_embed.add_field(name="Max Streak", value=f"{message.author} {highest_streak} 🔥")
                await message.channel.send(embed=final_embed)
                break

            if user_answer == question["answer"].lower():
                streak += 1
                highest_streak = max(streak, highest_streak)
                await message.channel.send(f"✅ {message.author.mention}! The answer is {question['answer']}.")
            else:
                streak = 0
                await message.channel.send(f"❌ Wrong! The answer is {question['answer']}.")

        except asyncio.TimeoutError:
            streak = 0
            await message.channel.send(f"⏰ Time's up! The correct answer was: {question['answer']}")

# Discord Bot Initialization
user_data = load_user_data(DATA_FILE)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=PREFIX, intents=intents)

# Regular Command Handling
@client.event
async def on_message(message):
    if message.author == client.user: 
        return
    
    # Check for prohibited words
    for word in prohibited_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send("⚠️ Content Removed")
            
            user_id = str(message.author.id)
            if user_id not in user_data:
                user_data[user_id] = {"warnings": []}

            warning_entry = {
            "reason": "Inappropriate content",
            "moderator": "Automated"  # slash commands use interaction.user
            }
            user_data[user_id]["warnings"].append(warning_entry)
            save_user_data(user_data, DATA_FILE)

            await message.channel.send(f"{message.author.mention} has been warned for: Inappropriate content")
            return
    await handle_regular_commands(message)

# Slash Commands Start Here 

# /help
@client.tree.command(name = "help", description = "This is the Help Command!")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(f"# Slash commands: \n - /help: Pulls up this list! \n - /say: Makes the bot say something in place of you! \n - /val: Have an e-girl or smoking hot man in your lobby? Use this command to get a pickup line! \n - /jasonscream: Jason's Greatest Moment \n - /eric: Eric's Greatest Moment \n - /dog: You get to learn where the name comes from!\n\n" +  "# ! Commands \n - !dicksize - How big is your johnson? \n - !val: More pickup lines for your little pookiebear \n - !crazy: Crazy? I was crazy once... \n - !osutrivia: Test your osu knowledge! \n - !toothless: toothless \n - !eric: he said a bad word \n - !chipichipi: chapachapa" , ephemeral=True)
# /hello 
@client.tree.command(name = "hello", description = "Hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!", ephemeral=True)

# /say
@client.tree.command(name = "say", description = "What do you want me to say?")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

# /val
@client.tree.command(name="val", description = "A pick-up line for your little e-kitten")
async def val(interaction:discord.Interaction): 
    quote = random.choice(VALORANT_QUOTES)
    await interaction.response.send_message(quote)

# /jasonscream
@client.tree.command(name="jasonscream", description = "AHHHHHHHH")
async def jasonscream(interaction:discord.Interaction): 
    await interaction.response.send_message("https://discord.com/channels/1021629412334108672/1097590517476376637/1104107438426312764")

# /eric
@client.tree.command(name="eric", description = "kick them off the plane")
async def eric(interaction:discord.Interaction):
    await interaction.response.send_message("https://discord.com/channels/1021629412334108672/1097590517476376637/1104110685463519262")

# /dog
@client.tree.command(name="dog", description = "whiffington")
async def dog(interaction:discord.Interaction):
    await interaction.response.send_message("https://discord.com/channels/1021629412334108672/1097590517476376637/1097594113769078804")
    
@client.tree.command(name="poll", description="Create a poll")
@app_commands.describe(question="Poll question", options="Comma-separated options (max 5)")
async def poll(interaction: discord.Interaction, question: str, options: str):
    options = [o.strip() for o in options.split(",")[:5]]
    embed = Embed(title=question, color=0x00ff00)
    reactions = []
    for i, option in enumerate(options):
        embed.add_field(name=f"Option {i+1}", value=option, inline=False)
        reactions.append(f"{i+1}\u20e3")  # Keycap emojis
    await interaction.response.send_message("Vote Now!")
    msg = await interaction.channel.send(embed=embed)
    for reaction in reactions:
        await msg.add_reaction(reaction)
    
@client.tree.command(name="serverinfo", description="Show server information")
async def serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    embed = Embed(title=f"{guild.name} Info", color=0x7289da)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Created", value=guild.created_at.strftime("%b %d, %Y"))
    embed.set_thumbnail(url=guild.icon.url)
    await interaction.response.send_message(embed=embed)
    
@client.tree.command(name="remind", description="Set a reminder")
@app_commands.describe(time="Time in minutes", message="Reminder message")
async def remind(interaction: discord.Interaction, time: int, message: str):
    await interaction.response.send_message(f"Reminder set for {time} minutes!", ephemeral=True)
    await asyncio.sleep(time * 60)
    await interaction.user.send(f"⏰ Reminder: {message}")
    
# Moderation Commands

@client.tree.command(name="warn", description="Warn a user.")
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.describe(member="The user to warn", reason="Reason for the warning")
async def warn(
    interaction: discord.Interaction,
    member: discord.Member,
    reason: str = "No reason provided"
):
    user_id = str(member.id)
    if user_id not in user_data:
        user_data[user_id] = {"warnings": []}

    warning_entry = {
        "reason": reason,
        "moderator": str(interaction.user),  # slash commands use interaction.user
    }
    user_data[user_id]["warnings"].append(warning_entry)
    save_user_data(user_data, DATA_FILE)

    # For slash commands, use interaction.response or followups, not ctx.send
    await interaction.response.send_message(f"{member.mention} has been warned for: {reason}")

@client.tree.command(name="warnings", description="View warnings for a user.")
@app_commands.checks.has_permissions(manage_messages=True)
async def warnings(interaction: discord.Interaction, member: discord.Member):
    user_id = str(member.id)
    if user_id not in user_data or "warnings" not in user_data[user_id]:
        await interaction.response.send_message(f"{member.mention} has no warnings.")
        return

    w_list = user_data[user_id]["warnings"]
    if not w_list:
        await interaction.response.send_message(f"{member.mention} has no warnings.")
        return

    lines = [f"Warnings for {member.mention}:", "-------------------------"]
    for i, w in enumerate(w_list, 1):
        reason = w.get("reason", "No reason")
        mod = w.get("moderator", "Unknown")
        lines.append(f"{i}. **Reason**: {reason} | **Mod**: {mod}")
    await interaction.response.send_message("\n".join(lines))

# Bot Initialization
@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    try: 
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

# Run the bot
client.run(TOKEN)