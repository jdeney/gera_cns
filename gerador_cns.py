import random
import argparse

def gerar(qtd):
    cns_set = set()
    while len(cns_set) < qtd:
        gera0 = random.randint(1, 3)
        if gera0 == 3:
            gera0 = random.randint(7, 9)
        gera1 = random.randint(1, 99999)
        gera2 = random.randint(1, 99999)
        cns = f"{gera0}{gera1:05d}{gera2:05d}"
        soma = sum(int(cns[j]) * (15 - j) for j in range(11))
        resto = soma % 11
        dv = 11 - resto
        dv = 0 if dv == 11 else dv
        if dv == 10:
            soma += 2
            resto = soma % 11
            dv = 11 - resto
            cns += f"001{dv}"
        else:
            cns += f"000{dv}"
        if len(cns) == 15:
            cns_set.add(cns)
    return list(cns_set)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gera números de CNS válidos.')
    parser.add_argument('qtd', type=int, help='Quantidade de números CNS a gerar')
    parser.add_argument('-o', '--output', type=str, default='cns_gerados.tsv', help='Nome do arquivo de saída')
    
    args = parser.parse_args()
    cns_numbers = gerar(args.qtd)
    
    with open(args.output, 'w') as f:
        f.write("CNS\n")
        for cns in cns_numbers:
            f.write(f"{cns}\n")
