import discord
from discord import role 
from discord.ext import commands
import random

from discord.ext.commands.core import check
client = discord.Client()

bot = commands.Bot(command_prefix = "=", description = "miam")

@bot.event
async def on_ready():
    print("commandes opérationnellese !")
#test
@bot.command()
async def test(ctx):
    await ctx.send("miam miam !")
#infoserveur
@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    TextSalon = len(server.text_channels)
    TextVoc = len(server.voice_channels)
    DescServeur = server.description
    nmbrP = server.member_count
    NomsServeur = server.name
    message = f"Le serveur **{NomsServeur}** contient {nmbrP} personnes. \nCe serveur possède {TextSalon} salons écrit ainsi que {TextVoc} vocaux. "
    await ctx.send(message)
#clear
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()
#100 fois
@bot.command()
async def test10(ctx):
    for loop in range(100):
        message = "test 100 fois"
        await ctx.send(message)
#navigation
@bot.command()
async def nav1(message):
    roleile2 = discord.utils.get(message.guild.roles, name = "ile2")
    await message.author.add_roles(roleile2)
    await message.channel.send('Tu es maintenant sur la deuxième ile')
#fouiller
@bot.command()
async def chercher(ctx):
    if random.randint(1,100) < 50:
        embed = discord.Embed(title = " ",
                            description = "📦 ▪️ Vous avez trouvé 5 vivres !")
        embed.set_author(name = ctx.author.name, 
                        icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    if random.randint(1,100) > 50:
        embed = discord.Embed(title = " ",
                            description = "📦 ▪️ Vous avez trouvé 5 matériaux !")
        embed.set_author(name = ctx.author.name, 
                        icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

@bot.command()
async def salons(ctx):
    embed = discord.Embed(title = "**Résumé des différents salons :**",
                          description = " ")
    embed.add_field(name="**Salons textuels :**", value="<#901918991415644232> : Salon où sont indiquées les arrivées et les départs des membres du discord. \n<#901935609898229793> : Salon où ceux qui le veulent peuvent se présenter. \n<#695528614237569057> : Salon principal pour discuter de tout et n'importe quoi. \n<#902564524513701888> : Salon résumant les différents salons du discord.", inline=False)
    embed.add_field(name = "**Interfeel :**", value = "<#695528898187886672> : Salon pour parler d'Interfeel sans spoiler.\n<#901917995662733353> : Salon dédié au tome 1 d'Interfeel.\n<#901917830134497411> : Salon dédié au tome 2 d'Interfeel.\n<#901917857011597322> : Salon dédié au tome 3 d'Interfeel.\n<#902204919333941248> : Salon où Antonin Atger communique ses dernières infos importantes.", inline=False)
    embed.add_field(name = "Conseils d'écriture :", value = "<#866386910997250078> Salon général des conseils d'écriture.\n<#901962902033022986> : Salon des conseils d'écriture dédié aux personnages.\n<#901962918659256340> : Salon des conseils d'écriture dédié aux univers.\n<#901962932823416892> : Salon des conseils d'écriture dédié aux intrigues.\n<#901974460679200778> : Salon des conseils d'écriture dédié aux casse-têtes de notre sublime langue.\n<#902123460724154408> : Salon des conseils d'écriture où la communauté peux poster des extraits de sa littérature.\n<#902183526294757476> : Salon des conseils d'écriture où les gens peuvent venir se motiver.\n<#902310509599133696> : Salon des conseils d'écriture dédié aux musiques.\n<#902833017960157195> : Salon où Antonin Atger propose à la communauté différents défis littéraires.\n<#902946738300649522> : Salon où vous pouvez demander de l'aide dans le cadre du concours Nano WriMo.", inline=False)
    embed.add_field(name = "Mises en relation :", value = "<#901935221635702865> : Salon où vous pouvez présenter ce que vous avez créé, quel que soit le médié et/ou support.\n<#901174475750531172> : Salon où vous pouvez présenter vos compétences.\n<#866387013770674176> : Salon où vous pouvez demander à la communauté de bêta lire votre futur Harry Potter à l'école des Sorciers")
    embed.add_field(name = "Analyse d'oeuvres :", value= "<#901174240689139803> : Salon des analyses d'œuvres dédié aux mangas, livres et films.\n<#902235535043600444> : Salon des analyses d'œuvres dédié aux mangas.\n<#902235128481316935> : Salon des analyses d'œuvres dédié aux livres.\n<#902235309264212029> : Salon des analyses d'œuvres dédié aux séries.\n<#901933018300690523> : Vous voulez savoir ce que contient ce salon ? Très bien, ce savoir est à vous. Trouvez-le ! Il est indiqué quelque part dans le nom de ce salon !\n<#901956690876985435> : Vous pensiez trouver une description du salon, mais c'était moi, Dio !", inline=False)
    embed.add_field(name = "Salons vocaux :", value = "<#695528614237569058> : Vocal général\n<#901919988158455818> : Nos meilleurs débats One Piece seront là bas :eyes:", inline=False)
    embed.add_field(name = "Gestion du serveur :", value = "<#901939611775938591> : Salon recensant les règles du discord.\n<#901954883702382674> : Salon dédié au spam des commandes des bots.\n<#901922463225622558> : Salon où vous pouvez faire vos suggestions pour améliorer ce discord.", inline=False)
    embed.set_thumbnail(url="https://ladiescolocblog.files.wordpress.com/2020/01/interfeel-tome-2-les-resistants-1271053.png?w=606&h=312&crop=1")
    
@bot.command()
async def inscription(ctx):
	await ctx.send("Quel est le nom de priate, marine ou révolutionaire de votre personnage ?")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		nom = await bot.wait_for("message", timeout = 10, check = checkMessage)
	except:
		await ctx.send("Veuillez réitérer la commande, 10 secondes se sont écoulées.")
		return
	message = await ctx.send(f"Nom : {nom.content}\n Quel est l'épithète de votre personnage ? (Avec \"le\" \"la\" ou \"l\'\") ")

    def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

        try:
            epith = await bot.wait_for("message", timeout = 10, check = checkMessage)
        except:
            await ctx.send("Veuillez réitérer la commande, 10 secondes se sont écoulées.")
            return

    await ctx.send(f"Nom : {nom.content}\nEpithète : {epith.content}")




bot.run("process.env.TOKEN" )
