from index import *

@bot.command()
async def embed(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author
    
    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title="Isso é uma Embed", description="É apenas um teste", colour=discord.Colour.yellow())
    embed.set_author(name=f"{name}", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://www.google.com/search?q=discord&tbm=isch&ved=2ahUKEwiihOyUqaOAAxW1ALkGHam0Bd8Q2-cCegQIABAA&oq=discord&gs_lcp=CgNpbWcQAzIHCAAQigUQQzIICAAQgAQQsQMyCggAEIoFELEDEEMyBwgAEIoFEEMyCAgAEIAEELEDMgcIABCKBRBDMggIABCABBCxAzIHCAAQigUQQzIFCAAQgAQyBQgAEIAEOgQIIxAnUJEQWNAWYIgYaABwAHgAgAFsiAGTBpIBAzQuNJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=jFK8ZKKOKbWB5OUPqemW-A0&bih=927&biw=958&rlz=1C1CHZN_pt-BRBR985BR985#imgrc=uTo-IigMPbCTpM")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name="Campo 1", value="Este campo é um valor")
    embed.add_field(name="Campo 2", value="Este campo é verdadeiro!", inline=True)
    embed.add_field(name="Campo 3", value="Este campo é falso!", inline=False)
    embed.set_footer(text=f"{name} Fez essa Embed!")

    await ctx.send(embed=embed)
