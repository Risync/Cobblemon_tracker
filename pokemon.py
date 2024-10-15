from system.lib import minescript as mc
import time
import sys

pokemon = ' '.join(sys.argv[1:]).lower()

while True:  
    nearby_pokemon = mc.entities()

    for entity in nearby_pokemon:
        pokemon_name = (entity.name).lower()
        pokeposition = [round(xyz) for xyz in entity.position]
        
        if pokemon_name == pokemon:
            mc.echo(pokemon_name, pokeposition)

    time.sleep(5)
