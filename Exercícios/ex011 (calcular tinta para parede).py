# Leia as medidas da parede e calcule sua área e diga a quantidade de Litros de tinta nescessaria para pinta-la (1 litro de tinta para 2 metros quadarados).
print('-'*100)
la = float(input('Qual a largura da parede em Metros?'))
al = float(input('Qual a altura da parede em Metros?'))
ar = al*la
tin = ar / 2
print('Sua parede tem a dimenção de {} x {} e sua área é de {}m²\n' \
      'para pintar essa parede você precisará de {}l de tinta'.format(la,al,ar,tin))
print('-'*100)