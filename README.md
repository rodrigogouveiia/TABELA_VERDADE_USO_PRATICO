# Sistema de Validação Bancária com Tabela Verdade

Projeto desenvolvido em Python para demonstração prática do conceito de **Lógica Proposicional**, na construção de uma **Tabela Verdade Completa** com 8 combinações `P` `Q` `R`($2^3$).

## 🔒 Variáveis Proposicionais e Regras

O algoritmo mapeia três condições de segurança e validação de dados:
*   **P (Maioridade):** O cliente possui idade igual ou superior a 18 anos?
*   **Q (Biometria):** A selfie do reconhecimento facial foi validada com sucesso?
*   **R (Abertura):** O sistema interno conseguiu gerar o número da conta digital?

A regra determina que **SE** o cliente é maior de idade **E** possui biometria válida, **ENTÃO** a conta deve obrigatoriamente ser aberta. Se os pré-requisitos forem cumpridos e a conta não for criada, a tabela verdade aponta uma quebra, sinalizada no sistema como `ERRO DO BANCO!`.

---

## 🛠️ Tecnologias Utilizadas
*   **Python 3** 
*  Para esse projeto, ao invés do uso da ferramenta `itertools` para automação da combinação das variáveis `P` `Q` `R`, optei pelo uso manual de **loops** `for`... `in`
