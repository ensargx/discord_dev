import responses
import discord
import os

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)
        await message.channel.send("Error: " + str(e))



def run_discord_bot():
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = discord.Client(intents=discord.Intents.all())

    tree = discord.app_commands.CommandTree(client)

    @tree.command()
    async def hello(interation: discord.Interaction, name: str = 'world'):
        """Say hello to the world, or to a specific person.
        
        Args:
            name (str): The name of the person to say hello to.
        """
        await interation.response.send_message(f'Hello {name}!')

    @tree.command()
    async def ping(interation: discord.Interaction, user: discord.User = None):
        """Ping!
        
        Bak ne güzel olmuş.
        """
        await interation.response.send_message('Pong!')
    

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        await tree.sync()    

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = message.author.name
        user_message = str(message.content)
        channel = message.channel

        print(f"Message from {username} in {channel}: {user_message}")

        if not channel.name == "genel":
            return

        if message.attachments:
            print(f"Attachments found in {username}'s message in {channel}!")
            await message.channel.send("Attachments Found!")
            # print attachment details
            for attachment in message.attachments:
                print(f"Attachment: {attachment.filename}")
            # Save attachments to a folder called "attachments"
            for attachment in message.attachments:
                await attachment.save(f"attachments/{attachment.filename}")
            # Delete the message
            await message.delete()
            print(f"Attachments from {username} in {channel} deleted!")            
            return

        if user_message == "delete":
            await message.delete()
            print(f"Message from {username} in {channel} deleted!")
            await message.channel.send("Message deleted!")
            return

        await send_message(message, user_message, False)

    client.run(TOKEN)