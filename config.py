#Config:#
token = 'MTA0MjczOTgxNzczMTA4NDMyOA.GL2eQN.E5jgw0OuABRyMQ18-1w0CUFVsj4Dkwhbd_8b48'                
CommandPrefix = '!'    
activitytype = 'Playing'                        #Accepted Values are Watching, Listening, Playing, or Streaming.
botstatusmessage = 'Giving server owners and admins a break'        
developerid = 0000000000000000000               #Insert the userID here were the bot will send all error dms too. THE USER MUST BE IN THE SAME DISCORD SERVER THAT THE BOT IS IN!
guildID = 0000000000000000000                   #Insert the guildID of the server that the bot will be running in here.
StaffRoleID = 0000000000000000000               #Change this value to the role in the server that will give bot perms to the anti-raid commands
SystemLogsChannelID = 0000000000000000000       #Change this value to where the bot will send all logs of commands too

#Embeds#
embedcolor = 0xc9f8fa                           #Change this value to the color value of the hex code that you would like the embeds the bot sends to be (KEEP THE 0x!)

customfooter = False                            #Set this the True if you like to have a custom footer at embeds            
customfootvalue = ''                            #Place the text of the custom footers

#Anti-Raid:
GracePeriodForKicks = 600                       #Adjust this value for the bot to look for members to kick who joined during a certain amount of time before anti-raid is enabled, default is 10 minutes, seconds only 
IncludeInviteLink = False                       #Change this to True for Yes, False for No. This allows for a discord invite to be on the message that the bot sends to a member who is kicked due to anti-raid
DiscordServerInviteLink = ''                    #Place in here the link to the discord. Use https, for example: https://discord.gg/yourvanityurl
