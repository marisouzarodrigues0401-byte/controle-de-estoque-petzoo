# seed_itens.py
# Script para cadastrar vários itens de uma vez no estoque.
# Todos com unidade "un".

from app import create_app, db
from app.models import Item

app = create_app()

ITENS = [
    # ======= CEREAIS / FARINHAS / MASSAS =======
    {"nome": "Arroz",              "categoria": "Cereais"},
    {"nome": "Farinha de mandioca","categoria": "Cereais"},
    {"nome": "Farinha de milho",   "categoria": "Cereais"},
    {"nome": "Farinha de rosca",   "categoria": "Cereais"},
    {"nome": "Farinha de trigo",   "categoria": "Cereais"},
    {"nome": "Fubá",               "categoria": "Cereais"},
    {"nome": "Macarrão",           "categoria": "Cereais"},
    {"nome": "Pão de queijo",      "categoria": "Cereais"},
    {"nome": "Pipoca",             "categoria": "Cereais"},

    # ======= LEGUMINOSAS / GRÃOS =======
    {"nome": "Feijão carioca",     "categoria": "Leguminosas"},
    {"nome": "Ervilha",            "categoria": "Leguminosas"},
    {"nome": "Milho verde",        "categoria": "Leguminosas"},

    # ======= OLEAGINOSAS / ÓLEOS =======
    {"nome": "Azeite Galo",        "categoria": "Oleaginosas"},
    {"nome": "Óleo",               "categoria": "Oleaginosas"},
    {"nome": "Óleo lata",          "categoria": "Oleaginosas"},
    {"nome": "Óleo Maria",         "categoria": "Oleaginosas"},

    # ======= EDULCORANTES / AÇÚCARES =======
    {"nome": "Açúcar",             "categoria": "Edulcorantes"},
    {"nome": "Adoçante",           "categoria": "Edulcorantes"},
    {"nome": "Achocolatado",       "categoria": "Edulcorantes"},

    # ======= TEMPEROS / MOLHOS =======
    {"nome": "Ajinomoto",          "categoria": "Temperos"},
    {"nome": "Barbecue",           "categoria": "Temperos"},
    {"nome": "Caldo de carne",     "categoria": "Temperos"},
    {"nome": "Canela",             "categoria": "Temperos"},
    {"nome": "Ketchup grande",     "categoria": "Temperos"},
    {"nome": "Ketchup bom",        "categoria": "Temperos"},
    {"nome": "Ketchup escola",     "categoria": "Temperos"},
    {"nome": "Molho de tomate",    "categoria": "Temperos"},
    {"nome": "Molho para salada",  "categoria": "Temperos"},
    {"nome": "Mostarda público",   "categoria": "Temperos"},
    {"nome": "Mostarda escola",    "categoria": "Temperos"},
    {"nome": "Orégano",            "categoria": "Temperos"},
    {"nome": "Sazon",              "categoria": "Temperos"},
    {"nome": "Sal",                "categoria": "Temperos"},
    {"nome": "Sal grosso",         "categoria": "Temperos"},
    {"nome": "Shoyu",              "categoria": "Temperos"},
    {"nome": "Tabasco",            "categoria": "Temperos"},
    {"nome": "Vinagre",            "categoria": "Temperos"},
    {"nome": "Vinagre balsâmico",  "categoria": "Temperos"},

    # ======= GORDURAS / CREMES =======
    {"nome": "Creme de leite",     "categoria": "Gorduras"},
    {"nome": "Doce de leite",      "categoria": "Gorduras"},
    {"nome": "Margarina funcional","categoria": "Gorduras"},
    {"nome": "Margarina pública",  "categoria": "Gorduras"},

    # ======= SECOS / ENLATADOS / DIVERSOS =======
    {"nome": "Azeitona",           "categoria": "Secos"},
    {"nome": "Brigadeiro",         "categoria": "Secos"},
    {"nome": "Bolo cenoura",       "categoria": "Secos"},
    {"nome": "Bolo chocolate",     "categoria": "Secos"},
    {"nome": "Batata palha",       "categoria": "Secos"},
    {"nome": "Chá mate",           "categoria": "Secos"},
    {"nome": "Café",               "categoria": "Secos"},
    {"nome": "Fermento para pão",  "categoria": "Secos"},
    {"nome": "Fermento em pó",     "categoria": "Secos"},
    {"nome": "Gelatina",           "categoria": "Secos"},
    {"nome": "Leite",              "categoria": "Secos"},
    {"nome": "Maionese",           "categoria": "Secos"},
    {"nome": "Nescau / Nescau escola","categoria": "Secos"},
    {"nome": "Ovos",               "categoria": "Secos"},
    {"nome": "Queijo ralado",      "categoria": "Secos"},

    # ======= BEBIDAS / SUCOS =======
    {"nome": "Suco funcional",     "categoria": "Bebidas"},
    {"nome": "Suco uva",           "categoria": "Bebidas"},
    {"nome": "Suco limão",         "categoria": "Bebidas"},
    {"nome": "Suco laranja",       "categoria": "Bebidas"},

    # ======= CARNES / FRIOS =======
    {"nome": "Ave codorna",        "categoria": "Carnes"},
    {"nome": "Bacon",              "categoria": "Carnes"},
    {"nome": "Batata frita",       "categoria": "Carnes"},
    {"nome": "Calabresa",          "categoria": "Carnes"},
    {"nome": "Carne moída",        "categoria": "Carnes"},
    {"nome": "Carne seca",         "categoria": "Carnes"},
    {"nome": "Filé de frango",     "categoria": "Carnes"},
    {"nome": "Mussarela",          "categoria": "Carnes"},
    {"nome": "Presunto",           "categoria": "Carnes"},
    {"nome": "Salsicha",           "categoria": "Carnes"},
    {"nome": "Tomate seco",        "categoria": "Carnes"},
    {"nome": "Picanha",            "categoria": "Carnes"},
    {"nome": "Contra filé",        "categoria": "Carnes"},
    {"nome": "Miolo de alcatra",   "categoria": "Carnes"},
    {"nome": "Coração",            "categoria": "Carnes"},
    {"nome": "Frango",             "categoria": "Carnes"},
    {"nome": "Linguiça",           "categoria": "Carnes"},
    {"nome": "Costela",            "categoria": "Carnes"},
    {"nome": "Torresmo",           "categoria": "Carnes"},
    {"nome": "Retalho",            "categoria": "Carnes"},

    # ======= LATICÍNIOS / OUTROS ALIMENTOS =======
    {"nome": "Geleia",             "categoria": "Laticínios"},
    {"nome": "Requeijão",          "categoria": "Laticínios"},
    {"nome": "Sorvete",            "categoria": "Laticínios"},
    {"nome": "Palmito",            "categoria": "Laticínios"},
    {"nome": "Paio",               "categoria": "Laticínios"},
    {"nome": "Pastel",             "categoria": "Laticínios"},

    # ======= FRUTAS E LEGUMES =======
    {"nome": "Abacaxi",            "categoria": "Frutas e Legumes"},
    {"nome": "Abobrinha",          "categoria": "Frutas e Legumes"},
    {"nome": "Alface",             "categoria": "Frutas e Legumes"},
    {"nome": "Alho",               "categoria": "Frutas e Legumes"},
    {"nome": "Banana",             "categoria": "Frutas e Legumes"},
    {"nome": "Batata",             "categoria": "Frutas e Legumes"},
    {"nome": "Berinjela",          "categoria": "Frutas e Legumes"},
    {"nome": "Beterraba",          "categoria": "Frutas e Legumes"},
    {"nome": "Cebola",             "categoria": "Frutas e Legumes"},
    {"nome": "Cenoura",            "categoria": "Frutas e Legumes"},
    {"nome": "Cheiro verde",       "categoria": "Frutas e Legumes"},
    {"nome": "Coco",               "categoria": "Frutas e Legumes"},
    {"nome": "Goiaba",             "categoria": "Frutas e Legumes"},
    {"nome": "Laranja",            "categoria": "Frutas e Legumes"},
    {"nome": "Limão",              "categoria": "Frutas e Legumes"},
    {"nome": "Mamão",              "categoria": "Frutas e Legumes"},
    {"nome": "Mandioquinha",       "categoria": "Frutas e Legumes"},
    {"nome": "Maçã",               "categoria": "Frutas e Legumes"},
    {"nome": "Manga",              "categoria": "Frutas e Legumes"},
    {"nome": "Melão",              "categoria": "Frutas e Legumes"},
    {"nome": "Morango",            "categoria": "Frutas e Legumes"},
    {"nome": "Pepino",             "categoria": "Frutas e Legumes"},
    {"nome": "Pimentão amarelo",   "categoria": "Frutas e Legumes"},
    {"nome": "Pimentão verde",     "categoria": "Frutas e Legumes"},
    {"nome": "Pimentão vermelho",  "categoria": "Frutas e Legumes"},
    {"nome": "Rúcula",             "categoria": "Frutas e Legumes"},
    {"nome": "Salsa",              "categoria": "Frutas e Legumes"},
    {"nome": "Tomate",             "categoria": "Frutas e Legumes"},
    {"nome": "Tomate cereja",      "categoria": "Frutas e Legumes"},

    # ======= DESCARTÁVEIS =======
    {"nome": "Copo sobremesa",     "categoria": "Descartáveis"},
    {"nome": "Copo café",          "categoria": "Descartáveis"},
    {"nome": "Copo gelatina",      "categoria": "Descartáveis"},
    {"nome": "Copo 180 ml",        "categoria": "Descartáveis"},
    {"nome": "Embalagem de bolo",  "categoria": "Descartáveis"},
    {"nome": "Filme PVC",          "categoria": "Descartáveis"},
    {"nome": "Forminha brigadeiro","categoria": "Descartáveis"},
    {"nome": "Forminha bolo",      "categoria": "Descartáveis"},
    {"nome": "Guardanapo",         "categoria": "Descartáveis"},
    {"nome": "Palito de dente",    "categoria": "Descartáveis"},
    {"nome": "Papel alumínio",     "categoria": "Descartáveis"},
    {"nome": "Pazinha para café",  "categoria": "Descartáveis"},
    {"nome": "Saquinho sanduíche", "categoria": "Descartáveis"},
    {"nome": "Pano",               "categoria": "Descartáveis"},
    {"nome": "Touca",              "categoria": "Descartáveis"},
    {"nome": "Luva",               "categoria": "Descartáveis"},
    {"nome": "Canudo",             "categoria": "Descartáveis"},

    # ======= LIMPEZA / HIGIENE =======
    {"nome": "Álcool gel",         "categoria": "Limpeza"},
    {"nome": "Álcool 70",          "categoria": "Limpeza"},
    {"nome": "Álcool perfumado",   "categoria": "Limpeza"},
    {"nome": "Amaciante",          "categoria": "Limpeza"},
    {"nome": "Bombril",            "categoria": "Limpeza"},
    {"nome": "Candida",            "categoria": "Limpeza"},
    {"nome": "Cera",               "categoria": "Limpeza"},
    {"nome": "Desinfetante",       "categoria": "Limpeza"},
    {"nome": "Detergente",         "categoria": "Limpeza"},
    {"nome": "Esponja",            "categoria": "Limpeza"},
    {"nome": "Interfolha",         "categoria": "Limpeza"},
    {"nome": "Lustra móveis",      "categoria": "Limpeza"},
    {"nome": "Papel higiênico",    "categoria": "Limpeza"},
    {"nome": "Papel toalha",       "categoria": "Limpeza"},
    {"nome": "Removedor",          "categoria": "Limpeza"},
    {"nome": "Sabão pedra",        "categoria": "Limpeza"},
    {"nome": "Sabão em pó",        "categoria": "Limpeza"},
    {"nome": "Sabonete líquido",   "categoria": "Limpeza"},
    {"nome": "Saco lixo 100L",     "categoria": "Limpeza"},
    {"nome": "Saco lixo 60L",      "categoria": "Limpeza"},
    {"nome": "Vela",               "categoria": "Limpeza"},
]


def main():
    with app.app_context():
        total = 0
        for dados in ITENS:
            nome = dados["nome"]

            # Verifica se já existe item com esse nome
            existente = Item.query.filter_by(nome=nome).first()
            if existente:
                continue

            item = Item(
                nome=nome,
                categoria=dados.get("categoria", "Outros"),
                unidade="un",            # aqui está o "un" que você pediu
                estoque_atual=0,
                estoque_minimo=0,
                observacoes=""
            )
            db.session.add(item)
            total += 1

        db.session.commit()
        print(f"Itens inseridos: {total}")


if __name__ == "__main__":
    main()
