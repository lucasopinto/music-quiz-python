import time
import random

perguntas = [
    {
        "pergunta": "Qual banda lançou o álbum 'The Dark Side of the Moon'?",
        "opcoes": ["A) Led Zeppelin", "B) Pink Floyd", "C) The Who", "D) Queen"],
        "resposta": "B"
    },
    {
        "pergunta": "Quem é conhecido como o 'Rei do Pop'?",
        "opcoes": ["A) Elvis Presley", "B) Prince", "C) Michael Jackson", "D) James Brown"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual desses álbuns é do Radiohead?",
        "opcoes": ["A) OK Computer", "B) Nevermind", "C) Abbey Road", "D) Thriller"],
        "resposta": "A"
    },
    {
        "pergunta": "Quem compôs a trilha sonora original de 'Star Wars'?",
        "opcoes": ["A) Hans Zimmer", "B) John Williams", "C) Danny Elfman", "D) Ennio Morricone"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual banda brasileira lançou 'Cassia Eller' como integrante?",
        "opcoes": ["A) Legião Urbana", "B) Titãs", "C) Cassia Eller foi solo", "D) Skank"],
        "resposta": "C"
    },
]


def rodar_quiz():
    random.shuffle(perguntas)
    pontos = 0
    tempos = []

    print("=" * 50)
    print("🎵 QUIZ DE TRIVIA MUSICAL 🎵")
    print("=" * 50)
    input("Pressione ENTER para começar...\n")

    for i, item in enumerate(perguntas, start=1):
        print(f"\nPergunta {i}/{len(perguntas)}: {item['pergunta']}")
        for opcao in item["opcoes"]:
            print(f"  {opcao}")

        inicio = time.time()
        resposta = input("Sua resposta (A/B/C/D): ").strip().upper()
        fim = time.time()

        tempo_gasto = round(fim - inicio, 1)
        tempos.append(tempo_gasto)

        if resposta == item["resposta"]:
            print(f"✅ Certo! ({tempo_gasto}s)")
            pontos += 1
        else:
            print(f"❌ Errado! A resposta certa era {item['resposta']}. ({tempo_gasto}s)")

    mostrar_resultado(pontos, len(perguntas), tempos)


def mostrar_resultado(pontos, total, tempos):
    percentual = (pontos / total) * 100
    tempo_medio = round(sum(tempos) / len(tempos), 1)

    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    print(f"Pontuação: {pontos}/{total} ({percentual:.0f}%)")
    print(f"Tempo médio por resposta: {tempo_medio}s")

    if percentual >= 80:
        print("🏆 Mandou muito bem!")
    elif percentual >= 50:
        print("👍 Boa, mas dá pra melhorar!")
    else:
        print("📚 Bora estudar mais música!")


if __name__ == "__main__":
    rodar_quiz()
