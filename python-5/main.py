from datetime import datetime

records = [
    {'source': '48-996355555', 'destination':
        '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination':
        '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination':
        '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination':
        '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination':
        '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination':
        '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination':
        '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination':
        '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination':
        '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination':
        '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination':
        '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination':
        '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def calculo_tarifa(records):

    ligacao_total = []

    for r in records:
        cliente = r['source']
        tempo = (r['end'] - r['start']) // 60
        inicio = datetime.fromtimestamp(r['start'])
        fim = datetime.fromtimestamp(r['end'])

        if 6 < inicio.hour < 22 and 6 < fim.hour < 22:
            preco = tempo*0.09 + 0.36

        elif 6 > inicio.hour or inicio.hour > 22:
            if 6 > fim.hour or fim.hour > 22:
                preco = 0.36
            else:
                dia = fim.replace(hour=6, minute=0, second=0)
                minutos_dia = int(((fim - dia).total_seconds()) / 60)
                preco = ((tempo - minutos_dia) * 0.09 + 0.36) + 0.36
        else:
            noite = inicio.replace(hour=22, minute=0, second=0)
            minutos_noite = int(((fim - noite).total_seconds()) / 60)
            preco = ((tempo - minutos_noite) * 0.09 + 0.36) + 0.36

        ligacao_total.append({'source': cliente, 'total': preco})
    return ligacao_total


def classify_by_phone_number(records):

    total = calculo_tarifa(records)
    final = []

    for t in total:
        if len(final) == 0:
            final.append({'source': t['source'], 'total': t['total']})
        else:
            contagem = 0
            for i in final:
                if t['source'] is i['source']:
                    i['total'] += t['total']
                    contagem = 1
                    break
            if contagem == 0:
                final.append({'source': t['source'], 'total': t['total']})

        for s in final:
            s['total'] = round(s['total'], 2)

    return sorted(final, key=lambda i: i['total'], reverse=True)
