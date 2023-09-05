import pyfiglet
from termcolor import colored

# Dicionário de cores em português
cores = {
    "azul": "blue",
    "magenta": "magenta",
    "ciano": "cyan",
    "branco": "white",
    "nenhum": None
}

# Lista de fontes disponíveis
fontes = [
    "standard",
    "banner",
    "big",
    "block",
    "bubble",
    "digital",
    "ivrit",
    "mini",
    "script",
    "shadow",
    "slant",
    "smscript",
    "smshadow",
    "smslant",
]

def generate_banner(text, color, font):
    if color in cores:
        color = cores[color]
    else:
        color = None

    if font not in fontes:
        font = "standard"

    banner = pyfiglet.figlet_format(text, font=font)
    if color:
        colored_banner = colored(banner, color)
        return colored_banner
    else:
        return banner

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Banners!")

    while True:
        text = input("\nDigite o texto para o banner (ou 'sair' para sair, 'menu' para ver as opções): ").strip().lower()
        if text == 'sair':
            break
        elif text == 'menu':
            print("\nOpções de cores:")
            for cor in cores.keys():
                print(cor.capitalize())

            print("\nOpções de fontes:")
            for i, fonte in enumerate(fontes):
                print(f"{i + 1}: {fonte.capitalize()}")

            continue  # Volte ao início do loop

        cor = input("Escolha uma cor ou 'nenhum' para padrão: ").strip().lower()
        fonte_choice = input("Escolha um número de fonte (ou pressione Enter para padrão): ").strip()

        if cor not in cores:
            cor = "nenhum"

        try:
            fonte_choice = int(fonte_choice)
            if 1 <= fonte_choice <= len(fontes):
                fonte = fontes[fonte_choice - 1]
            else:
                fonte = "standard"
        except ValueError:
            fonte = "standard"

        banner = generate_banner(text, cor, fonte)
        print("\nBanner gerado:")
        print(banner)
