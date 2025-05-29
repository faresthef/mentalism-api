from flask import Flask, request, jsonify

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

@app.route('/mentalism', methods=['POST'])
def mentalism():
    # Récupère le texte depuis MysterSmith
    total_str = request.form.get('text', '0').replace(',', '.')
    
    try:
        total = float(total_str) * 1000  # Conversion en millimes
        if total in combinations:
            choice = combinations[total]
            
            # Formatage spécial pour MysterSmith
            return jsonify({
                "status": "success",
                "display": f"""
                🥗 Entrée: {choice['entree']} ({choice['prix_entree']:.3f} TND)
                🍲 Plat: {choice['plat']} ({choice['prix_plat']:.3f} TND)
                🍰 Dessert: {choice['dessert']} ({choice['prix_dessert']:.3f} TND)
                💨 Chicha: {choice['chicha']} ({choice['prix_chicha']:.3f} TND)
                ──────────────
                TOTAL = {choice['total']:.3f} TND
                """,
                "quick_replies": ["72.700", "58.300", "89.100"]  # Suggestions optionnelles
            })
        else:
            return jsonify({
                "status": "error",
                "display": "Aucune combinaison trouvée. Vérifiez le total."
            })
    except:
        return jsonify({
            "status": "error", 
            "display": "Format invalide. Exemple: 72.700"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)