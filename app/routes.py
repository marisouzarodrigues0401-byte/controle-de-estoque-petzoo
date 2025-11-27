from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Item
from .services.settings_service import get_settings, update_settings
# Consumo padrão em unidade/semana por pessoa
# Ajuste esses valores para a realidade do Petzoo
CONSUMO_PADRAO = {
    "arroz": 0.06,        # 0,06 kg por pessoa/semana
    "feijão": 0.02,       # 0,02 kg por pessoa/semana
    "feijao": 0.02,       # sem acento, só pra garantir
    "macarrão": 0.05,
    "frango": 0.15,
    "carne bovina": 0.18,
    "carne suína": 0.15,
    "salada": 0.08,
}


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def dashboard():
    settings = get_settings()
    return render_template("dashboard.html", settings=settings)


@main_bp.route("/configuracoes", methods=["GET", "POST"])
def configuracoes():
    settings = get_settings()
    if request.method == "POST":
        city = request.form.get("city")
        api_key = request.form.get("api_key")
        rain_impact_factor = request.form.get("rain_impact_factor")
        sunny_message = request.form.get("sunny_message")
        rain_message = request.form.get("rain_message")

        try:
            rain_impact_factor = float(rain_impact_factor)
        except (TypeError, ValueError):
            flash("Informe um número válido para o fator de impacto.", "error")
            return render_template("settings.html", settings=settings)

        update_settings(
            city=city,
            api_key=api_key,
            rain_impact_factor=rain_impact_factor,
            sunny_message=sunny_message,
            rain_message=rain_message,
        )
        flash("Configurações atualizadas com sucesso!", "success")
        return redirect(url_for("main.configuracoes"))

    return render_template("settings.html", settings=settings)


@main_bp.route("/estoque")
def estoque():
    items = Item.query.order_by(Item.nome).all()

    # cria lista de itens com estoque baixo
    itens_baixos = [item for item in items if item.estoque_atual < item.estoque_minimo]

    return render_template("estoque.html", items=items, itens_baixos=itens_baixos)


@main_bp.route("/estoque/novo", methods=["GET", "POST"])
def novo_item():
    if request.method == "POST":
        nome = request.form.get("nome")
        categoria = request.form.get("categoria")
        unidade = request.form.get("unidade")
        observacoes = request.form.get("observacoes")
        try:
            estoque_atual = int(request.form.get("estoque_atual") or 0)
            estoque_minimo = int(request.form.get("estoque_minimo") or 0)
        except ValueError:
            flash("Informe números válidos para os estoques.", "error")
            return render_template("estoque_form.html", item=None)

        if not nome:
            flash("O nome do item é obrigatório.", "error")
            return render_template("estoque_form.html", item=None)

        item = Item(
            nome=nome,
            categoria=categoria,
            unidade=unidade,
            estoque_atual=estoque_atual,
            estoque_minimo=estoque_minimo,
            observacoes=observacoes,
        )
        db.session.add(item)
        db.session.commit()
        flash("Item cadastrado com sucesso!", "success")
        return redirect(url_for("main.estoque"))

    return render_template("estoque_form.html", item=None)


@main_bp.route("/estoque/<int:item_id>/editar", methods=["GET", "POST"])
def editar_item(item_id: int):
    item = Item.query.get_or_404(item_id)
    if request.method == "POST":
        nome = request.form.get("nome")
        if not nome:
            flash("O nome do item é obrigatório.", "error")
            return render_template("estoque_form.html", item=item)

        item.nome = nome
        item.categoria = request.form.get("categoria")
        item.unidade = request.form.get("unidade")
        item.observacoes = request.form.get("observacoes")
        try:
            item.estoque_atual = int(request.form.get("estoque_atual") or 0)
            item.estoque_minimo = int(request.form.get("estoque_minimo") or 0)
        except ValueError:
            flash("Informe números válidos para os estoques.", "error")
            return render_template("estoque_form.html", item=item)

        db.session.commit()
        flash("Item atualizado com sucesso!", "success")
        return redirect(url_for("main.estoque"))

    return render_template("estoque_form.html", item=item)


@main_bp.route("/estoque/<int:item_id>/deletar", methods=["POST"])
def deletar_item(item_id: int):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Item removido com sucesso!", "success")
    return redirect(url_for("main.estoque"))
from flask import render_template, request
from app.models import Item

@main_bp.route("/planejamento", methods=["GET", "POST"])
def planejamento():
    from app.models import Item  # garante que o Item está importado

    # pega os itens do estoque
    items = Item.query.order_by(Item.nome).all()
    resultados = None
    pessoas = None

    # monta um dicionário com o consumo padrão por item_id
    consumos_padrao = {}
    for item in items:
        chave = item.nome.lower()
        valor = CONSUMO_PADRAO.get(chave)
        if valor is not None:
            consumos_padrao[item.id] = valor

    if request.method == "POST":
        pessoas_raw = request.form.get("pessoas") or "0"
        try:
            pessoas = int(pessoas_raw)
        except ValueError:
            pessoas = 0

        resultados = []

        for item in items:
            campo = f"consumo_{item.id}"
            valor = request.form.get(campo)

            # 1) Se o usuário digitou algo, usa o que ele digitou
            if valor:
                try:
                    por_pessoa = float(valor.replace(",", "."))
                except ValueError:
                    # se digitou porcaria, ignora esse item
                    continue
            else:
                # 2) Se não digitou nada, tenta usar o padrão
                default = consumos_padrao.get(item.id)
                if default is None:
                    # sem padrão → ignora o item
                    continue
                por_pessoa = float(default)

            necessario = por_pessoa * pessoas
            # ajusta o nome do campo para o que você usa no modelo
            atual = item.estoque_atual or 0
            diferenca = necessario - atual

            resultados.append({
                "item": item,
                "por_pessoa": por_pessoa,
                "necessario": necessario,
                "atual": atual,
                "comprar": diferenca if diferenca > 0 else 0,
                "sobrando": -diferenca if diferenca < 0 else 0,
            })

    return render_template(
        "planejamento.html",
        items=items,
        resultados=resultados,
        pessoas=pessoas,
        consumos_padrao=consumos_padrao,
    )
    @main_bp.route("/lista-compras")
def lista_compras():
    items = Item.query.order_by(Item.nome).all()

    itens_urgentes = [
        item for item in items
        if item.estoque_atual < item.estoque_minimo
    ]

    itens_urgentes.sort(key=lambda i: (i.estoque_atual - i.estoque_minimo))

    return render_template("lista_compras.html", itens_urgentes=itens_urgentes)

@main_bp.route("/lista-compras")
def lista_compras():
    items = Item.query.order_by(Item.nome).all()

    # seleciona só itens abaixo do mínimo
    itens_urgentes = [
        item for item in items 
        if item.estoque_atual < item.estoque_minimo
    ]

    # ordena colocando os mais críticos no topo
    itens_urgentes.sort(key=lambda i: (i.estoque_atual - i.estoque_minimo))

    return render_template("lista_compras.html", itens_urgentes=itens_urgentes)
