import discord
from discord.ext import commands
import math

# discord.py calls groups of commands cogs
# cogs can also be handlers for different types of events
# and respond to changes in data as they happen

# setup
class BasicCog:
    def __init__(self, bot):
        self.bot = bot

    # ping command
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    # echo command
    # commands are given a name implicitly, but you can also define this explicitly as well
    # the cooldown attribute allows you to limit how frequently the command can be used in
    # a channel, a server, or by a specific user
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command(name='echo')
    async def echo(self, ctx, *, message='_echo_'):
        await ctx.send(f'{ctx.author.mention} : {message}')

    # github command
    @commands.command(name='sqrt')
    async def sqrt(self, ctx, num: int):
        await ctx.send(_sqrt(num))

# add this cog to the bot
def setup(bot):
    bot.add_cog(BasicCog(bot))

def _sqrt(num: int):
    """
    Example of how to include methods that can be easily tested
    
    >>> _sqrt(4)
    'Sqrt(4) = 2.0'

    """

    return f'Sqrt({num}) = {math.sqrt(num)}'

# optional, but helpful for testing via the shell
if __name__ == '__main__':
    import doctest
    doctest.testmod()