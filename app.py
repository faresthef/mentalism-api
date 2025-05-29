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
@app.route('/mentalism', methods=['GET', 'POST'])
def mentalism():
    # Récupération du total
    total_str = request.form.get('total', request.args.get('total', '0')).replace(',', '.').strip()
    
    try:
        total = int(float(total_str) * 1000)  # Conversion précise en millimes
        
        if total in combinations:
            choice = combinations[total]
            
            # Format reçu minimaliste
            receipt = f"""
            Révélation Mentaliste
            ---------------------
            Vous avez choisi :
            {choice['entree']} - Prix : {choice['prix_entree']:.3f} DTN
            {choice['plat']} - Prix : {choice['prix_plat']:.3f} DTN
            {choice['dessert']} - Prix : {choice['prix_dessert']:.3f} DTN
            {choice['chicha']} - Prix : {choice['prix_chicha']:.3f} DTN
            ---------------------
            TOTAL = {choice['total']:.3f} DTN
            """
            
            return jsonify({
                "myster_smith_display": receipt,
                "myster_smith_format": "fixed_width"  # Pour une police monospace
            })
            
        return jsonify({
            "myster_smith_display": f"Aucune combinaison pour {total_str} DTN"
        })
        
    except Exception as e:
        return jsonify({
            "myster_smith_display": f"Erreur : Entrez un nombre valide (ex: 72.700)"
        })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)