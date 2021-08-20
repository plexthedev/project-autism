import requests
import json
import os
import asyncio
from PIL import Image,ImageFont,ImageDraw, ImageFilter

import discord
from discord.ext import commands

class GatoText(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gatotext(self, ctx, *, text=""):
        if (len(text) > 0):
            imagePath = "./resources/images/cat.png"
            fontPath = "./resources/fonts/Arial.ttf"
            exitPath = "./temp/gatotext.png"

            gtx = 593/2
            gty = 593 - 150
            fontSize = 100

            for suckmydick in text:
                fontSize -= 2
                gty += 1
                if (fontSize <= 0):
                    await ctx.reply("bro message too long pipe down", mention_author=False)
                    return


            coords = (gtx, gty)
            Img = Image.open(imagePath)
            Draw = ImageDraw.Draw(Img)
            Font = ImageFont.truetype(fontPath, fontSize)
            Draw.text(coords, text, (255, 255, 255), font=Font, anchor="mt")
            Img.save(exitPath)

            await ctx.reply(file = discord.File(exitPath), mention_author=False)

        else:
            await ctx.reply("ERROR: No text given", mention_author=False)

def setup(client):
    client.add_cog(GatoText(client))