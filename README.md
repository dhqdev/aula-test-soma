Calculadora de Soma em C

Este projeto é uma implementação simples de um programa em C que solicita dois números inteiros ao usuário, calcula a soma e exibe o resultado. O foco principal não é a complexidade do cálculo, mas sim demonstrar uma estrutura de código limpa, modular e robusta, aplicando boas práticas de programação.

✨ Features
Entrada de Dados Interativa: O programa solicita que o usuário insira dois números.

Validação de Entrada: Garante que o usuário digite apenas números inteiros. Se um texto ou outro caractere for inserido, o programa solicitará a entrada novamente até que seja válida.

Código Modular: O programa é dividido em funções com responsabilidades únicas (ler, somar, exibir), tornando o código mais legível e fácil de manter.

Separação de Preocupações: A lógica de entrada, processamento e saída de dados é claramente separada.

📂 Estrutura do Código
O código é organizado em quatro funções principais, cada uma com um propósito bem definido:

int main()

É o ponto de entrada do programa.

Sua função é orquestrar a execução, chamando as outras funções na ordem correta.

Atua como um "sumário" do que o programa faz: lê os dados, processa e exibe o resultado.

int lerNumero(const char* mensagem)

Responsabilidade: Ler e validar um número inteiro fornecido pelo usuário.

Recebe uma mensagem para exibir (ex: "Digite o primeiro número: ").

Contém um loop que só termina quando o usuário insere um número válido, limpando o buffer de entrada para evitar erros.

int somar(int a, int b)

Responsabilidade: Realizar o cálculo da soma.

É uma função "pura": recebe dois números como entrada e retorna o resultado, sem interagir com o usuário ou outras partes do sistema.

void exibirResultado(int resultado)

Responsabilidade: Formatar e exibir o resultado final no console.

Isola a lógica de apresentação, facilitando futuras alterações no texto de saída sem mexer no resto do código.

🚀 Como Compilar e Executar
Para compilar e executar este projeto, você precisará de um compilador C, como o GCC.

Salve o código: Salve o código em um arquivo chamado programa_soma.c.

Abra o terminal: Navegue até o diretório onde você salvou o arquivo.

Compile o código: Execute o seguinte comando para compilar o programa.

Bash

gcc programa_soma.c -o soma_app
gcc é o comando do compilador.

programa_soma.c é o seu arquivo de código-fonte.

-o soma_app define o nome do arquivo executável de saída (você pode escolher outro nome se preferir).

Execute o programa: Após a compilação bem-sucedida, execute o programa com o comando:


Exemplo de Uso
Digite o primeiro número: 10
Digite o segundo número: 25
A soma dos dois números é: 35
Exemplo com Validação de Entrada
Digite o primeiro número: abc
Entrada inválida. Por favor, digite um número inteiro: 50
Digite o segundo número: 100
A soma dos dois números é: 150
💡 Boas Práticas Aplicadas
Este código serve como um exemplo de aplicação dos seguintes princípios:

Modularidade: O problema foi dividido em "módulos" (funções) menores e mais gerenciáveis.

Princípio da Responsabilidade Única (SRP): Cada função tem uma única e bem definida responsabilidade. A função somar só soma, a lerNumero só lê e valida.

Robustez: O tratamento de erros na entrada de dados torna o programa mais resistente a falhas causadas por entradas inesperadas do usuário.

Legibilidade: O uso de nomes de funções e variáveis claras, juntamente com a estrutura modular, torna a função main extremamente fácil de ler e entender.
