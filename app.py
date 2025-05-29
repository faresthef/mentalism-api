from flask import Flask, request, render_template_string

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
    total_str = request.args.get('total', '0').replace(',', '.').strip()
    
    try:
        total = int(float(total_str) * 1000)
        if total in combinations:
            choice = combinations[total]
            
            # Template HTML minimaliste pour navigateur
            receipt_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Révélation Mentaliste</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {
                        font-family: 'Courier New', monospace;
                        max-width: 500px;
                        margin: 0 auto;
                        padding: 20px;
                        color: #333;
                    }
                    h1 {
                        text-align: center;
                        font-size: 1.5em;
                        border-bottom: 2px dashed #333;
                        padding-bottom: 10px;
                    }
                    .item {
                        display: flex;
                        justify-content: space-between;
                        margin: 8px 0;
                    }
                    .total {
                        font-weight: bold;
                        border-top: 2px dashed #333;
                        margin-top: 15px;
                        padding-top: 10px;
                    }
                </style>
            </head>
            <body>
                <h1>RÉVÉLATION MENTALISTE</h1>
                
                <div class="item">
                    <span>Entrée :</span>
                    <span>{{ entree }} - {{ prix_entree }} DTN</span>
                </div>
                
                <div class="item">
                    <span>Plat :</span>
                    <span>{{ plat }} - {{ prix_plat }} DTN</span>
                </div>
                
                <div class="item">
                    <span>Dessert :</span>
                    <span>{{ dessert }} - {{ prix_dessert }} DTN</span>
                </div>
                
                <div class="item">
                    <span>Chicha :</span>
                    <span>{{ chicha }} - {{ prix_chicha }} DTN</span>
                </div>
                
                <div class="total">
                    <span>TOTAL :</span>
                    <span>{{ total }} DTN</span>
                </div>
            </body>
            </html>
            """
            
            return render_template_string(receipt_html,
                entree=choice['entree'],
                plat=choice['plat'],
                dessert=choice['dessert'],
                chicha=choice['chicha'],
                prix_entree=f"{choice['prix_entree']:.3f}",
                prix_plat=f"{choice['prix_plat']:.3f}",
                prix_dessert=f"{choice['prix_dessert']:.3f}",
                prix_chicha=f"{choice['prix_chicha']:.3f}",
                total=f"{choice['total']:.3f}"
            )
            
        return "Aucune combinaison trouvée pour " + total_str + " DTN"
        
    except Exception as e:
        return f"Erreur : {str(e)}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)