for i in range(2,21):
    table = ''
    for j in range(0,11):
        table += f"{1} x {j} = {i*j}\n"
    with open(f'table/{i}.txt', 'w') as f:
        f.write(table)