from flask import Flask, request

app = Flask(__name__)

# Menu avec les prix en MILLIMES (1 TND = 1000 millimes)
menu = {
    "entrees": {
        "Salade": 13400,
        "Brik à l'œuf": 8900,
        "Fricassé Tunisien": 6600
    },
    "plats": {
        "Couscous au Poulet": 18100,
        "Kefteji": 24300,
        "Entrecôte grillée": 21200
    },
    "desserts": {
        "Tiramisu maison": 8700,
        "Cheesecake aux fruits rouges": 10800,
        "Fondant au chocolat": 12000
    },
    "chichas": {
        "Chicha Apple": 32500,
        "Chicha Love": 44200,
        "Chicha Soltan": 53500
    }
}

# Dictionnaire pour stocker les combinaisons
combinations = {}

# Générer toutes les combinaisons possibles
for entree, p1 in menu["entrees"].items():
    for plat, p2 in menu["plats"].items():
        for dessert, p3 in menu["desserts"].items():
            for chicha, p4 in menu["chichas"].items():
                total_millimes = p1 + p2 + p3 + p4
                combinations[total_millimes] = {
                    "entree": entree,
                    "plat": plat,
                    "dessert": dessert,
                    "chicha": chicha,
                    "prix_entree": p1 / 1000,
                    "prix_plat": p2 / 1000,
                    "prix_dessert": p3 / 1000,
                    "prix_chicha": p4 / 1000,
                    "total": total_millimes / 1000
                }

@app.route('/mentalism')
def mentalism_trick():
    # Récupérer le total depuis l'URL
    total_str = request.args.get('total', '0').replace(',', '.')
    
    try:
        # Convertir en millimes
        total_tnd = float(total_str)
        total_millimes = int(total_tnd * 1000)  # Conversion en millimes
        
        if total_millimes in combinations:
            choice = combinations[total_millimes]
            return f"""
            <h1>Révélation Mentaliste 🔮</h1>
            <p>VOUS AVEZ CHOISIS :</p>
            <ul>
                <li>🥗 Entrée: {choice['entree']} ({choice['prix_entree']:.3f} TND)</li>
                <li>🍲 Plat: {choice['plat']} ({choice['prix_plat']:.3f} TND)</li>
                <li>🍰 Dessert: {choice['dessert']} ({choice['prix_dessert']:.3f} TND)</li>
                <li>💨 Chicha: {choice['chicha']} ({choice['prix_chicha']:.3f} TND)</li>
            </ul>
            <p>--------------------------</p>
            <h3>TOTAL = {choice['total']:.3f} TND</h3>
            """
        else:
            return f"Aucune combinaison trouvée pour {total_str} TND. Vérifiez la somme.", 404
    except:
        return "Format invalide. Utilisez un nombre (ex: 72.700)", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)