from flask import Flask, request, make_response
import json
app = Flask(__name__)

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

combinations = {}

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
def mentalism():
    total_str = request.args.get('total', '0').replace(',', '.')
    
    try:
        total = float(total_str) * 1000  # Conversion en millimes
        if total in combinations:
            choice = combinations[total]
            
            # Création du HTML à afficher
            html_response = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background: #121212;
                        color: white;
                        padding: 20px;
                        text-align: center;
                    }}
                    .menu-item {{
                        margin: 15px 0;
                        font-size: 1.2em;
                    }}
                    .total {{
                        font-weight: bold;
                        font-size: 1.5em;
                        margin-top: 30px;
                    }}
                </style>
            </head>
            <body>
                <h1>🔮 Révélation Mentaliste</h1>
                
                <div class="menu-item"> Entrée: {choice['entree']} ({choice['prix_entree']:.3f} TND)</div>
                <div class="menu-item"> Plat: {choice['plat']} ({choice['prix_plat']:.3f} TND)</div>
                <div class="menu-item"> Dessert: {choice['dessert']} ({choice['prix_dessert']:.3f} TND)</div>
                <div class="menu-item"> Chicha: {choice['chicha']} ({choice['prix_chicha']:.3f} TND)</div>
                
                <div class="total">TOTAL = {choice['total']:.3f} TND</div>
            </body>
            </html>
            """
            
            # Retourne directement le HTML
            return html_response
        else:
            return "Aucune combinaison trouvée pour ce total."
    except:
        return "Erreur : format invalide (utilisez un nombre comme 72.700)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)