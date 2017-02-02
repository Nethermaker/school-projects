import random
import discord
from discord.ext import commands

Tactical = ['Cloak', 'Pulse Blade', 'Grapple', 'Stim', 'A-wall', 'Phase Shift',
            'Holo Pilot']
Primary = ['R201', 'Hemlock', 'G2', 'Flatline', 'Car', 'Alternator', 'Volt',
           'R-97', 'Spitfire', 'Lstar', 'Devotion', 'Krabar', 'Double Take',
           'DMR', 'EVA-8', 'Mastiff', 'Cold War', 'Softball', 'SMR', 'EPG']
Secondary = ['Archer', 'MGL', 'Thunderbolt', 'Charge Laser', 'RE - 45',
             'P2016', 'Wingman Elite', 'Mozambique', 'Wingman']
Ordnance = ['Frag Grenade', 'Arc Grenade', 'Firestar', 'Gravity Star',
            'Electric Smoke Grenade', 'Satchel']
Kit1 = ['Power Cell', 'Fast Regen', 'Ordance Expert', 'Phase Embark']
Kit2 = ['Kill Report', 'Wallhang', 'Hover', 'Low Profile']
Titan = ['Ion', 'Tone', 'Legion', 'Ronin', 'Scorch', 'Northstar']
Ion_kits = ['Entangled Energy', 'Zero-Point Tripwire', 'Vortex Amplifier',
            'Grand Cannon', 'Refraction Lens']
Scorch_kits = ['Wildfire Launcher', 'Tempered Plating', 'Inferno Shield',
               'Fuel for the Fire', 'Scorched Earth']
Northstar_kits = ['Piercing Shot', 'Enhanced Payload', 'Twin Traps',
                  'Viper Thrusters', 'Threat Optics']
Ronin_kits = ['Ricochet Rounds', 'Thunderstorm', 'Temporal Anomaly',
              'Highlander', 'Phase Reflex']
Tone_kits = ['Enhanced Tracker Rounds', 'Reinforced Particle Wall',
             'Pulse-Echo', 'Rocket Barrage', 'Burst Loader']
Legion_kits = ['Enhanced Ammo Capacity', 'Sensor Array', 'Bulwark',
               'Leigh-Weight Alloys', 'Hidden Compartment']


class loadouts:
    """Titanfall 2 loadout generator"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loadout(self):
        """Generates random loadout"""

        list = '\n'.join(loadout())

        await self.bot.say(list)


def loadout():
    list = []
    list.append('Tactical: ' + str(random.choice(Tactical)))
    list.append('Primary: ' + str(random.choice(Primary)))
    list.append('Secondary: ' + str(random.choice(Secondary)))
    list.append('Ordanance: ' + str(random.choice(Ordnance)))
    list.append('Kit 1: ' + str(random.choice(Kit1)))
    list.append('Kit 2: ' + str(random.choice(Kit2)))
    random_titan = str(random.choice(Titan))
    if random_titan = 'Ion':
        titan_kit = str(random.choice(Ion_kits))
    elif random_titan = 'Scorch':
        titan_kit = str(random.choice(Scorch_kits))
    elif random_titan = 'Northstar':
        titan_kit = str(random.choice(Northstar_kits))
    elif random_titan = 'Ronin':
        titan_kit = str(random.choice(Ronin_kits))
    elif random_titan = 'Tone':
        titan_kit = str(random.choice(Tone_kits))
    elif random_titan = 'Legion':
        titan_kit = str(random.choice(Legion_kits))
    list.append('Titan: ' + random_titan)
    list.append('Titan Kit: ' + titan_kit)
    
    return list


def setup(bot):
    """Adds the cog"""
    bot.add_cog(loadouts(bot))
