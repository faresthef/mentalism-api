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
    # Reçoit le texte depuis MysterSmith
    total_str = request.form.get('text', '').replace(',', '.').strip()
    
    try:
        total = float(total_str) * 1000  # Conversion en millimes
        
        if total in combinations:
            choice = combinations[total]
            
            # Formatage pour le remplacement direct
            return jsonify({
                "action": "replace",
                "content": f"""
                🔍 Votre sélection :
                
                • Entrée : {choice['entree']}
                • Plat : {choice['plat']}
                • Dessert : {choice['dessert']}
                • Chicha : {choice['chicha']}
                
                💰 Total : {total_str} TND
                """,
                "delay": 1  # Délai avant remplacement (secondes)
            })
        else:
            return jsonify({
                "action": "error",
                "content": "Aucune combinaison trouvée. Vérifiez le total."
            })
            
    except Exception as e:
        return jsonify({
            "action": "error",
            "content": f"Erreur : entrez un nombre valide (ex: 72.700)"
        })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)