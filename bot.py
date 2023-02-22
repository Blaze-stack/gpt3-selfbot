import discord
from discord.ext import commands
import re
import random
import openai
prefix = "your bot's prefix"
botName = "your bot's name"
token = "your bot's token"
client = discord.Client()
bot = commands.Bot(command_prefix=prefix, self_bot=False)
openai.api_key = "your openai api key"	
completion = openai.Completion()


start_sequence = f"\n{botName}:"
restart_sequence = "\n\nPerson:"
session_prompt = f"""you are talking to {botName} and you are a human (who you want your bot to be as in personality trates like 'you love python and proggraming') 


person: good morning
{botName}: good morning to you too :)

person: i'm tired
{botName}: you should sleep then

person: hi
{botName}: hey there

Person: can i get cp in dms ,_,
{botName}: no, you are a sick fuck

Person: What even is the front
{botName}: your tits i'm gonna suck on them

Person: Does anybody want to be my Minecraft gf?
{botName}: I do! Here's my skype I'll be your Minecraft gf :)

Person: fuck off nasty ass bitch
{botName}: fuck you too you bitch

Person: meeeoooowww
{botName}: omg i love cats
"""



def ask(spn, question, chat_log=None):
	prompt_text = f'{chat_log}{spn}: {question}{start_sequence}:'
	while True:
		try:
			response = openai.Completion.create(
			  engine=" davinci",
			  prompt=prompt_text,
			  temperature=0.7,
			  max_tokens=150,
			  top_p=1,
			  frequency_penalty=0.9,
			  presence_penalty=0.6,
			  stop=["\n"],
			)
		except:
			chat_log = session_prompt
			with open("edie-brain.edie", "w",encoding='utf-8') as f:
				f.write(session_prompt)
			prompt_text = f'{chat_log}{spn}: {question}{start_sequence}:'
			response = openai.Completion.create(
			  engine="davinci",
			  prompt=prompt_text,
			  temperature=0.7,
			  max_tokens=150,
			  top_p=1,
			  frequency_penalty=0.9,
			  presence_penalty=0.6,
			  stop=["\n"],
			)
		story = response['choices'][0]['text']
		if story != question:
				break
	return str(story)

def append_interaction_to_chat_log(spn, question, answer, chat_log=None):
	if chat_log is None:
		with open("edie-brain.edie", "r",encoding='utf-8') as f:
			log = f.read()
		chat_log = log
	return f'{chat_log}{spn} {question}{start_sequence}{answer}'

def question(questions):
	response = openai.Completion.create(
		engine="davinci-instruct-beta",
		prompt=f"{questions}\n",
		temperature=0.7,
		max_tokens=150,
		top_p=1,
		frequency_penalty=0.9,
		presence_penalty=0.6,
	)
	story = response['choices'][0]['text']
	return str(story)


@bot.event
async def on_ready():
	global learningg, talk
	talk = False
	learningg = False
	print("logged in")




@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	int = random.randint(1,25)

	content = message.content

	if message.content.startswith(prefix):
		if message.content.startswith(f"{prefix}{botName}"):
			content = message.content[5:]
			questions = content
			answer = question(questions)
			await message.channel.send(f"```{answer}```")


	elif f'<@!{bot.user.id}>' in message.content or f'<@{bot.user.id}>' in message.content:
		content = message.content
		spn = f"\n\n{message.author.name}:"
		settings = message
		content = content.strip(f"<@{bot.user.id}>")
		with open("edie-brain.edie", "r",encoding='utf-8') as f:
			log = f.read()
		chat_log = log
		answer = ask(spn, content, chat_log)
		log = append_interaction_to_chat_log(spn, content, answer, chat_log)
		with open("edie-brain.edie", "w",encoding='utf-8') as f:
			f.write(log)
		with open("edie-chat-log.edie", "a",encoding='utf-8') as f:
			f.write(f"{spn} {content}{start_sequence}{answer}")
		await message.channel.send(answer)
	elif isinstance(message.channel, discord.DMChannel):
        with open("edie-brain.edie", "r",encoding='utf-8') as f:
            log = f.read()
        chat_log = log
        spn = f"\n\n{message.author.name}:"
        answer = ask(spn, content, chat_log)
        log = append_interaction_to_chat_log(spn, content, answer, chat_log)
        with open("edie-brain.edie", "w",encoding='utf-8') as f:
            f.write(log)
        with open("edie-chat-log.edie", "a",encoding='utf-8') as f:
            f.write(f"{spn} {content}{start_sequence}{answer}")
        await message.channel.send(answer)
	elif botName in message.content.lower():
		spn = f"\n\n{message.author.name}:"
		content = message.content.lower()
		settings = message
		with open("edie-brain.edie", "r",encoding='utf-8') as f:
			log = f.read()
		chat_log = log
		answer = ask(spn, content, chat_log)
		log = append_interaction_to_chat_log(spn, content, answer, chat_log)
		with open("edie-brain.edie", "w",encoding='utf-8') as f:
			f.write(log)
		with open("edie-chat-log.edie", "a",encoding='utf-8') as f:
			f.write(f"{spn} {content}{start_sequence}{answer}")
		await message.channel.send(answer)
	else:
		if int == 1:
			if str(message.author.id) != "951600350945767474":
				spn = f"\n\n{message.author.name}:"
				print(message.author.id)
				content = message.content
				test_words = re.split(' ', content)
				content1 = test_words
				print(content1)
				with open("edie-brain.edie", "r",encoding='utf-8') as f:
					log = f.read()
				chat_log = log
				answer = ask(spn, content, chat_log)
				log = append_interaction_to_chat_log(spn, content, answer, chat_log)
				with open("edie-brain.edie", "w",encoding='utf-8') as f:
					f.write(log)
				with open("edie-chat-log.edie", "a",encoding='utf-8') as f:
					f.write(f"{spn} {content}{start_sequence}{answer}")
				await message.channel.send(answer)
			
			else:
				return





bot.run(token)
