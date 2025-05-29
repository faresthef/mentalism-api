from flask import Flask, request, make_response

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
    total_str = request.form.get('text', '0').replace(',', '.')
    
    try:
        total = float(total_str) * 1000
        if total in combinations:
            choice = combinations[total]
            
            # Formatage texte brut pour MysterSmith
            response_text = f"""
            🔮 RÉVÉLATION 🔮
            -----------------
            Entrée : {choice['entree']} ({choice['prix_entree']:.3f} TND)
            Plat : {choice['plat']} ({choice['prix_plat']:.3f} TND)
            Dessert : {choice['dessert']} ({choice['prix_dessert']:.3f} TND)
            Chicha : {choice['chicha']} ({choice['prix_chicha']:.3f} TND)
            -----------------
            TOTAL = {choice['total']:.3f} TND
            """
            
            # Retourne du texte brut avec le bon Content-Type
            response = make_response(response_text)
            response.headers['Content-Type'] = 'text/plain; charset=utf-8'
            return response
            
        return "Aucune combinaison trouvée pour ce total."
    except:
        return "Erreur : format invalide (exemple: 72.700)"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)