import random

# 50 Famous Architects and Their Iconic Buildings
architects = {
    "Frank Lloyd Wright": "Fallingwater",
    "Le Corbusier": "Villa Savoye",
    "Zaha Hadid": "Heydar Aliyev Center",
    "Frank Gehry": "Guggenheim Museum Bilbao",
    "Norman Foster": "The Gherkin (30 St Mary Axe)",
    "Renzo Piano": "The Shard",
    "Tadao Ando": "Church of the Light",
    "Rem Koolhaas": "CCTV Headquarters",
    "Mies van der Rohe": "Barcelona Pavilion",
    "Louis Kahn": "Salk Institute",
    "Eero Saarinen": "TWA Terminal",
    "Santiago Calatrava": "Turning Torso",
    "Bjarke Ingels": "8 House",
    "Jean Nouvel": "Louvre Abu Dhabi",
    "I. M. Pei": "Louvre Pyramid",
    "Richard Rogers": "Pompidou Centre",
    "Oscar Niemeyer": "Cathedral of Brasília",
    "Philip Johnson": "Glass House",
    "Peter Zumthor": "Therme Vals",
    "David Adjaye": "National Museum of African American History and Culture",
    "Moshe Safdie": "Habitat 67",
    "Alvar Aalto": "Paimio Sanatorium",
    "Kenzo Tange": "Tokyo Metropolitan Government Building",
    "Toyo Ito": "Sendai Mediatheque",
    "Daniel Libeskind": "Jewish Museum Berlin",
    "Jean Gang": "Aqua Tower",
    "Shigeru Ban": "Cardboard Cathedral",
    "Fumihiko Maki": "4 World Trade Center",
    "Herzog & de Meuron": "Tate Modern",
    "Dominique Perrault": "Bibliothèque nationale de France",
    "César Pelli": "Petronas Towers",
    "Arata Isozaki": "Qatar National Convention Centre",
    "Marcel Breuer": "Whitney Museum of American Art",
    "Antoni Gaudí": "Sagrada Família",
    "Carlo Scarpa": "Brion Cemetery",
    "Eileen Gray": "E-1027 House",
    "Glenn Murcutt": "Magney House",
    "Kazuyo Sejima": "Rolex Learning Center",
    "SANAA": "New Museum of Contemporary Art",
    "John Pawson": "Nový Dvůr Monastery",
    "Luis Barragán": "Casa Gilardi",
    "Minoru Yamasaki": "World Trade Center (original)",
    "Enric Miralles": "Scottish Parliament Building",
    "Gordon Bunshaft": "Lever House",
    "Aldo Rossi": "Modena Cemetery",
    "Charles Correa": "Jawahar Kala Kendra",
    "Frei Otto": "Munich Olympic Stadium",
    "Giancarlo De Carlo": "University College, Urbino",
    "Michael Graves": "Portland Building",
    "Rafael Moneo": "Cathedral of Our Lady of the Angels"
}

cocktails = [
    "Margarita", "Old Fashioned", "Negroni", "Cosmopolitan", "Mojito",
    "Whiskey Sour", "Mai Tai", "Bloody Mary", "Daiquiri", "Gin & Tonic",
    "Pina Colada", "Espresso Martini", "Long Island Iced Tea", "Caipirinha",
    "Aperol Spritz", "Tom Collins", "Paloma", "Manhattan", "Tequila Sunrise",
    "Rum Punch"
]

perfumes = [
    "Chanel No.5", "Dior Sauvage", "Gucci Bloom", "YSL Black Opium",
    "Tom Ford Oud Wood", "Jo Malone Peony & Blush Suede", "Bleu de Chanel",
    "Armani Code", "Le Labo Santal 33", "Viktor & Rolf Flowerbomb",
    "Versace Eros", "Dolce & Gabbana Light Blue", "Byredo Gypsy Water",
    "Maison Margiela Replica 'Jazz Club'", "Prada L'Homme"
]

# Funny commentary templates
commentary = [
    "Ah, a refined taste! Clearly, you sketch in 3D while sipping design philosophy.",
    "You must dream in concrete and glass. Time to celebrate your genius!",
    "A bold choice — like your taste in cocktails and fragrances.",
    "Your inner architect just did a mic drop.",
    "You clearly enjoy your buildings with a side of drama and elegance!"
]

# Display the list of architects
print("🏛️  Famous Architects and Their Iconic Buildings 🏗️\n")
for i, (architect, building) in enumerate(architects.items(), 1):
    print(f"{i}. {architect} — {building}")

# User input
choice = input("\nEnter the name of your favorite architect: ").strip()

# Process the choice
if choice in architects:
    cocktail = random.choice(cocktails)
    perfume = random.choice(perfumes)
    reaction = random.choice(commentary)
    print(f"\n🎨 {reaction}")
    print(f"You picked {choice}, known for the {architects[choice]}.")
    print(f"\n🍸 Your cocktail of the day: {cocktail}")
    print(f"💐 Your matching perfume: {perfume}")
    print("\nNow go design something magnificent — but maybe after that drink! 😉")
else:
    print("\nHmm, that name isn't on the list. Maybe you’re an avant-garde visionary? 🍹")
