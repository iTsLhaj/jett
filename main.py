from rich.console import Console
from rich.theme import Theme
from typing import List, Union
from asyncio import sleep

import discord
import dotenv
import os


dotenv.load_dotenv()
console_theme = Theme({
	"mag": "magenta"
})
console = Console(theme=console_theme)
command_pref = ':'
the_speech = "a ser ya trikt lkhera w zna w trami m7sna w sbabet mkhelta w l97ab memghta ya trikt ma9ala wadal mn t97bin w tl3bin w hzan rjlin lkhmis w tnin yatrikt lft lm7for w zab lm3bor w hzan l9lwa mn lor ya trikt l97ab w j3ab w sef 3nd lbab ytrikt l7sira w tbzira w lbota sghira ya trikt l97ob w l3ob w doran f drob w hzan zbob w srwal mt9ob wzek 3amer 7bob ya trikt l3bid w l7wa f l3id ya trik lkar ghadi w l7wa badi dserti aweld l97ba"

class Client(discord.Client):

	async def hbt_t9wwd(self, message: discord.Message) -> discord.Member:

		mentions: List[discord.User | discord.Member] = message.mentions
		# console.log(mentions.__len__())
		if mentions.__len__() > 1:
			await message.reply("one at a time !")
		else:
			await message.reply(f"khrj t9wwd {mentions[0].mention} hh!")
			return mentions[0]

	async def on_ready(self):
		console.log(f" ☁️  [mag]{self.application.name} is ready ![/mag]")

	async def on_message(self, message: discord.Message):

		# the part were i check if the bot is mentioned !
		mentions: List[discord.User | discord.Member] = message.mentions
		for mentioned in mentions:

			# the part were i check if the owner.id isn't mentioned !
			if mentioned.id == self.application.id and message.author.id != self.application.owner.id:
				await message.reply(the_speech)
				break

		# the part were i execute commands !
		if message.content.startswith(command_pref):

			try:
				# the part were i kick ppl !
				if message.content[1:6] == "kick ":

					if message.author.voice == None:
						if message.author.id == self.application.owner.id:
							await message.reply("rah khask dkhole shi voice channel n3am as 👉👈 !")
						else:
							await message.reply("fin? dkhole ya zbi Lshi voice channel, so i can join in !")
					else:
						channel: Union[discord.VoiceChannel, discord.StageChannel] = message.author.voice.channel
						voice: discord.VoiceProtocol = await channel.connect()
						source = discord.FFmpegPCMAudio(source='kicking_audio.wav')
						voice.play(source)
						while voice.is_playing():
							await sleep(.1)
						await voice.disconnect()

					user: discord.Member = await self.hbt_t9wwd(message)
					await user.kick(reason="charlomanti hh")

			except KeyError:
				await message.reply("command not found !")

intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(token=os.environ["CLIENT_TOKEN"])
