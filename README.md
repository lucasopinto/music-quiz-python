# 🎵 Music Trivia Quiz (Python)

🇧🇷 [Português](#-português) | 🇺🇸 [English](#-english)

---

## 🇧🇷 Português

### O que o projeto faz
Quiz de perguntas sobre música que roda no terminal. As perguntas aparecem em ordem aleatória, o programa mede o tempo de cada resposta e, no final, mostra a pontuação, o percentual de acertos, o tempo médio e uma mensagem de acordo com o desempenho.

### Tecnologias
- Python 3
- Bibliotecas padrão: `random` (embaralhar perguntas) e `time` (medir tempo de resposta)

### Como executar
```bash
git clone https://github.com/lucasopinto/music-quiz-python.git
cd music-quiz-python
python music_quiz.py
```
Responda com A, B, C ou D. Não é preciso instalar dependências.

### O que aprendi
- Estruturar dados com listas de dicionários (pergunta, opções e resposta)
- Usar laços, `enumerate` e condicionais para controlar o fluxo do jogo
- Medir tempo de execução com `time.time()`
- Separar a lógica em funções (`rodar_quiz`, `mostrar_resultado`)
- Normalizar a entrada do usuário com `strip()` e `upper()`

### Próximos passos
- Guardar perguntas e placares em um banco SQLite

---

## 🇺🇸 English

### What it does
A terminal-based music trivia quiz. Questions are shuffled, the response time for each answer is measured, and at the end it shows the score, accuracy percentage, average response time and a feedback message.

### Tech stack
- Python 3
- Standard library: `random` (shuffle questions) and `time` (response timing)

### How to run
```bash
git clone https://github.com/lucasopinto/music-quiz-python.git
cd music-quiz-python
python music_quiz.py
```
Answer with A, B, C or D. No dependencies required.

### What I learned
- Structuring data as lists of dictionaries
- Controlling program flow with loops, `enumerate` and conditionals
- Measuring elapsed time with `time.time()`
- Splitting logic into functions
- Normalizing user input with `strip()` and `upper()`

### Next steps
- Store questions and scores in a SQLite database
