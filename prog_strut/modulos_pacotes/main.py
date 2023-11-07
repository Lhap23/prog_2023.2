from cli import cli
# from cli import cli as c

def main():
    nome = cli.ler_nome()
    print("Olá", nome)
    print(cli.NUMERO_MAXIMO_ITENS)

if __name__ == "__main__":
    main()
