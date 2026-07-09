import random
import re

# Seu banco de dados de frases personalizado
msg = [
    "Ainda vou add mensagens aqui, lol!",
    "Pensando ainda...",
    "Trabalhando...",
]

def update_readme():
    frase_do_dia = random.choice(msg)
    
    with open("README.md", "r", encoding="utf-8") as file:
        conteudo = file.read()

    # regex para mostrar texto.
    padrao = r"(<!-- VARIABLE:START -->)(.*?)(<!-- VARIABLE:END -->)"
    novo_conteudo = re.sub(padrao, f"\\1\n\n> {frase_do_dia}\n\n\\3", conteudo, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(novo_conteudo)

if __name__ == "__main__":
    update_readme()
