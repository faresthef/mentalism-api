from flask import Flask, request, jsonify
from datetime import datetime

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
    total_str = request.form.get('total', '0') if request.method == 'POST' else request.args.get('total', '0')
    total_str = total_str.replace(',', '.').strip()

    try:
        total = int(float(total_str) * 1000)
        
        if total in combinations:
            choice = combinations[total]
            
            # Réponse stylisée avec animations
            return jsonify({
                "myster_smith_display": f"""
                <div style='
                    font-family: "Helvetica Neue", sans-serif;
                    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                    color: white;
                    padding: 25px;
                    border-radius: 20px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                    max-width: 100%;
                    animation: fadeIn 1s ease-in-out;
                '>
                    <h1 style="text-align: center; margin-bottom: 25px; font-size: 1.8em;">
                        ✨ Votre Menu Secret ✨
                    </h1>
                    
                    <div style='
                        background: rgba(255,255,255,0.15);
                        padding: 15px;
                        border-radius: 12px;
                        margin-bottom: 15px;
                        backdrop-filter: blur(10px);
                    '>
                        <div style='display: flex; justify-content: space-between;'>
                            <span>🥗 Entrée:</span>
                            <span>{choice['entree']} <strong>{choice['prix_entree']:.3f} TND</strong></span>
                        </div>
                    </div>
                    
                    <!-- Répétez le même bloc pour Plat, Dessert, Chicha -->
                    
                    <div style='
                        margin-top: 30px;
                        padding-top: 15px;
                        border-top: 1px dashed rgba(255,255,255,0.3);
                        text-align: center;
                        font-size: 1.3em;
                    '>
                        TOTAL: <strong>{choice['total']:.3f} TND</strong>
                    </div>
                    
                    <div style='
                        text-align: center;
                        margin-top: 20px;
                        font-size: 0.8em;
                        opacity: 0.7;
                    '>
                        {datetime.now().strftime("Revelation • %d/%m/%Y %H:%M")}
                    </div>
                </div>
                """,
                "myster_smith_animation": "fadeIn",
                "myster_smith_delay": 1500
            })
            
        else:
            return jsonify({
                "myster_smith_display": """
                <div style='
                    /* Style d'erreur élégant */
                '>
                    Aucune combinaison trouvée
                </div>
                """
            })
            
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": 400
        })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)