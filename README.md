
# Calculadora de Prazos Jurídicos

Este é um aplicativo simples para calcular prazos jurídicos em diversas áreas do direito. Ele permite selecionar uma área jurídica, uma data de entrada e um tipo de andamento, e retorna a data final do prazo, ajustando automaticamente para evitar finais de semana.

## Funcionalidades

- **Seleção da área jurídica**: Escolha entre Direito Civil, Penal, Trabalhista, Tributário e Empresarial.
- **Cálculo automático de prazos**: Insira uma data de início e obtenha o prazo final ajustado para evitar finais de semana.
- **Ajuste de dias úteis**: Se o prazo final cair em um final de semana, a data será ajustada para o último dia útil anterior.
- **Exibição do dia da semana**: Além da data, o aplicativo também informa o dia da semana correspondente ao fim do prazo.
- **Mensagem de ajuda**: Ao passar o mouse sobre o ícone de interrogação no canto superior direito, uma mensagem explicativa aparece, orientando o usuário sobre como usar o aplicativo.

## Requisitos

- Python 3.x
- Biblioteca `tkinter` (inclusa em versões padrão do Python)

## Instalação

1. Clone o repositório ou baixe o código.
2. Certifique-se de ter o Python instalado em seu sistema. Se necessário, faça o download [aqui](https://www.python.org/downloads/).
3. Execute o arquivo principal com o comando:


## Como usar

1. **Selecione a área do direito**: No topo da interface, há várias opções de áreas jurídicas, como Direito Civil, Direito Penal, etc. Selecione a área desejada.
   
2. **Insira a data de entrada**: No campo logo abaixo, insira a data de início do prazo no formato `dd/mm/aaaa`.

3. **Escolha o tipo de andamento**: Dependendo da área jurídica selecionada, aparecerão diferentes tipos de andamentos para calcular o prazo. Escolha o andamento que deseja calcular.

4. **Clique em 'Calcular'**: Após inserir as informações, pressione o botão "Calcular" para obter o prazo final ajustado para dias úteis. A data e o dia da semana aparecerão logo abaixo.

5. **Mensagem de ajuda**: Se precisar de ajuda, passe o mouse sobre o símbolo `❓` no canto superior direito para ver uma mensagem explicativa sobre como usar o aplicativo.

## Exemplo de uso

- Área selecionada: **Direito Civil**
- Data de entrada: **01/10/2024**
- Andamento: **Contestação**

Resultado: O prazo será calculado e exibido como **15/10/2024**, junto com o dia da semana correspondente.

## Personalização

- Você pode adicionar novas áreas do direito ou tipos de andamentos, simplesmente editando o dicionário `prazos_por_area` no código.


