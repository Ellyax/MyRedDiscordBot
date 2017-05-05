import discord
from random import *
from discord.ext import commands
from .utils.dataIO import fileIO
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice as rndchoice
from .utils.chat_formatting import box
import os
# -- coding: utf-8 --

class NickRoll:
    def __init__(self, bot):
        self.bot = bot
        self.filename = 'data/nickroll/nickroll.json'
        self.nickrolls = dataIO.load_json(self.filename)
       
    async def save_nickrolls(self):
        dataIO.save_json(self.filename, self.nickrolls)
    
    @commands.command(pass_context=True, no_pm=True, name='nickroll')
    #@checks.admin_or_permissions(administrator=True)
    async def nickroll(self, context, member : discord.Member):
        """
            Generate a random nickname for this <member> from his nickame list.
            To add a new nickname to his list, type !addnick <member> <new_nickname>
        """
        server = context.message.server
        author = context.message.author
        nicklist = []
        memberid = member.id
        themember = member
        member = str(member)
        if int(memberid) == 110470292274446336:
            await self.bot.say("Sry bro I can't change the Admin Name, he's more powerful than me :/")
        elif int(memberid) == 307177980407578624:
            await self.bot.say("Don't even think about it, u fgt")    
        elif server.id in self.nickrolls:
            nicklist = self.nickrolls[server.id][member.lower()]['nick_list']
            randompick = randomPick(nicklist)
            await self.bot.change_nickname(themember, randompick)
            await self.bot.say("Hey , your new nickname is " + themember.mention)
        else:
            await self.bot.say("Yo this user sucks bro, no nicknames are planned for him")
            await self.bot.say("Use the command !addnick <member> <new_nickname> to create a new nickname for this member")
            
    @commands.command(pass_context=True, name='nickadd')
    async def nickadd(self, context, member : discord.Member, nick):
        """
            Add a new nickname <nick> for the user <member>
        """
        server = context.message.server
        memberid = member.id
        member = str(member)
        if int(memberid) == 110470292274446336:
            await self.bot.say("Sry bro I can't change the Admin Name, he's more powerful than me :/")
        #Check si il existe une liste de users/nicks pour ce serveur
        else:
            if server.id not in self.nickrolls:
                self.nickrolls[server.id] = {}
            #Check si le <member> est deja dans la liste
            if member.lower() not in self.nickrolls[server.id]:
                try:
                    int(member)
                    #await self.bot.say(member.id)
                except:
                    self.nickrolls[server.id][member.lower()] = {}
                    newnicklist = [nick]
                    self.nickrolls[server.id][member.lower()]['nick_list'] = newnicklist
                    await self.save_nickrolls()
                    message = 'New user and nickname added.'
                else:
                    message = 'Meh ca marche pas ta merde'
            else:
                nicklist = self.nickrolls[server.id][member.lower()]['nick_list'] 
                nicklist.append(nick)
                self.nickrolls[server.id][member.lower()]['nick_list'] = nicklist
                await self.save_nickrolls()
                message = 'New nickname added.'
            await self.bot.say(message)
        
    @commands.command(pass_context=True, name='nicklist')
    async def nicklist(self, context, member : discord.Member):
        """
            Add a new nickname <nick> for the user <member>
        """
        server = context.message.server
        memberid = member.id
        member = str(member)
        nicklist = self.nickrolls[server.id][member.lower()]['nick_list']
        msg = "+ Available Nickname list\n\n" + "\n\n".join(sorted(nicklist))
        msg = box(msg, lang="diff")
        
        await self.bot.say(msg)
        
def randomPick (liste):
    max = len(liste)-1
    random_index = randint(0, max)
    return liste[random_index]
    
    
def check_file():
    data = {}
    f = 'data/nickroll/nickroll.json'
    if not dataIO.is_valid_json(f):
        print('Creating default nickroll.json...')
        dataIO.save_json(f, data)
        
        
def check_folder():
    if not os.path.exists('data/nickroll'):
        print('Creating data/nickroll folder...')
        os.makedirs('data/nickroll')        

        
def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(NickRoll(bot))
    
    
    
    
"""    
    @commands.command()
    #@checks.admin_or_permissions(administrator=True)
    async def nickroll(self, member : discord.Member):
        #Change the <member> nickname
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
"""