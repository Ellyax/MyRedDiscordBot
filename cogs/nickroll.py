import discord
from random import *
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice as rndchoice
import os
# -- coding: utf-8 --

class NickRoll:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    #@checks.admin_or_permissions(administrator=True)
    async def nickroll(self, member : discord.Member):
        """Change the <member> nickname"""
        modif = 1
        if int(member.id) == 308898820450680834: #Toxic Testeur
            nick_list = ["Le Testeur", "Toxic", "Toxic Testeur"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 117289772224872453: #Forskeren
            nick_list =  ["Forskeren", "Forskefoutre", "Manque1Rein", "KickedOutByHisMom", "Flibidi",
            "Hitler", "El Nazi", "Foutre au Sucre", "Francouille", "Forskerein", 
            "Franco de porc", "je m’excuser", "Web developer", "Répèpète"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 110178544310583296: #Count Orlok
            nick_list = ["Lama", "Count Orlok", "Cunt Lama", "ILoveTheNewLinkinPark", 
            "Graforlok", "Ellamasticot", "Ellyax's First Fan", "Naheulband", 
            "Marcel boy", "Blamatoscope", "Lamaaaaaaa", "Mom’s Madeleine", 
            "Angular master", "Gragas slave", "3 bières flambées", "Cookie",
            "Sailor Moon"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 110470292274446336: #Toxic Bob
            #new_nick = "Test"
            modif = 0
            await self.bot.say("Sry bro I can't change the Admin Name, he's more powerful than me :/")
        elif int(member.id) == 95587875130703872: #Thug Life
            nick_list = ["Jeune et Dynamique", "Thug Life", "E-boy", "Eweno Galleto",
            "DullEvergreen9", "Worst Nasus EUW", "T bon Tu montes", "El pedo", "Teenage party",
            "Diamond", "Asleep"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 136186758609108992: #Stratis
            nick_list = ["Roti de porc", "Stratis", "Un truc vraiment stylé", 
            "Le tueur du Brabant", "Salamalek", "Glace kiwi", "Compote de pomme"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 119888092369780736: #Isaac
            nick_list = ["Isaac luck", "Deep throat", "Monsieur 60cm", 
            "Lolli predator", "Wiki porn", "Freine groupe", "Mic = Garderie", 
            "Aram d’homme", "MonsieurGratuit", "Urivabo", "SuceCarpentouze", 
            "GunnarConnard", "PairiDaiza", "beeg.com", "MagdaleneMain", "PreziGod"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 118856858764050432: #Chakal
            nick_list = ["Avaleur de foutre", "30cm inside", "Voix passive", "Lama’s bitch",
            "Baaaaah", "Mais j’vous emmerde", "Lamaaaaaaaa"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 118800995575660544: #Sulfaoh
            nick_list = ["Excuse moi drama", "TV allumée", "360 noscope", "Sulfatron", 
            "Sulfisteur", "Sulfachiasse"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 119816804209000448: #Kevin
            nick_list = ["Le polak", "Mister rage quit", "Pas invité", "Drama", "Vodka cerise",
            "Sulfaoh pardon", "Still Bachelor", "Moskow", "DramaMaster"]
            new_nick = randomPick(nick_list)
        elif int(member.id) == 123447121532813312: #Remy
            nick_list = ["PudgeGod", "322", "L'homme de l'Ombre", "NyxAssassin420", "Lee Sin God",
            "GraouhGraouh", "Shokalol", "Je suis Boulez"]
            new_nick = randomPick(nick_list)
        else:
            modif = 0
            await self.bot.say("Yo this user sucks bro, no nicknames are planned for him")

        if modif == 1:
            await self.bot.change_nickname(member, new_nick)
            await self.bot.say("Hey , your new nickname is " + member.mention)

        
def randomPick (liste):
    max = len(liste)-1
    random_index = randint(0, max)
    return liste[random_index]
        

def setup(bot):
    bot.add_cog(NickRoll(bot))