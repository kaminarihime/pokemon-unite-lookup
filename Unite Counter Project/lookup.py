import json

with open('pokemon_data.json', 'r') as file:
    pokemon_data = json.load(file)

pokemon = input("Enter the name of the Pokemon: ").strip()

found = False
for poke in pokemon_data:
    if poke.lower() == pokemon.lower():
        info = pokemon_data[poke]
        synergy = info.get("synergizes_with") or info.get("synergizes with") or info.get("synergies")
        countered_by = info.get("is_countered_by") or info.get("is countered by") or info.get("counters")
        strong_against = info.get("strong_against") or info.get("strong against") or info.get("strong")

        print(f"\n{poke}:")
        print("  - Works well with:", ", ".join(synergy) if synergy else "None listed")
        print("  - Is strong against:", ", ".join(strong_against) if strong_against else "None listed")
        print("  - Is countered by:", ", ".join(countered_by) if countered_by else "None listed")
        found = True
        break

if not found:
    print("Either the Pokemon is not found or the spelling is incorrect. Please try again.")
