distance=float(input('Введите расстояние:'))
razhod=float(input('Введите расход топлива:'))
cena=float(input('Введите цену бензина:'))
toplivo=razhod/100*distance
stoimoct=toplivo*cena
print(f'Топливо: {toplivo:.2f}')
print(f'Стоимость: {stoimoct:.2f}')

