#include <stdio.h>
#include <stdlib.h> // Usado para funções de utilidade geral como exit()

/**
 * @brief Solicita uma mensagem ao usuário, lê um número inteiro e o retorna.
 * Esta função também valida a entrada para garantir que seja um número.
 *
 * @param mensagem A mensagem a ser exibida para o usuário (ex: "Digite um número: ").
 * @return O número inteiro que foi lido com sucesso.
 */
int lerNumero(const char* mensagem) {
    int numero;
    printf("%s", mensagem);

    // Verifica o retorno de scanf. Se for diferente de 1, a leitura falhou.
    while (scanf("%d", &numero) != 1) {
        printf("Entrada inválida. Por favor, digite um número inteiro: ");

        // Limpa o buffer de entrada. Isso é crucial para evitar um loop infinito
        // caso o usuário digite um caractere em vez de um número.
        int c;
        while ((c = getchar()) != '\n' && c != EOF);
    }
    return numero;
}

/**
 * @brief Soma dois números inteiros.
 *
 * @param a O primeiro número.
 * @param b O segundo número.
 * @return O resultado da soma de a e b.
 */
int somar(int a, int b) {
    return a + b;
}

/**
 * @brief Exibe o resultado formatado da soma no console.
 *
 * @param resultado O valor da soma a ser exibido.
 */
void exibirResultado(int resultado) {
    printf("A soma dos dois números é: %d\n", resultado);
}


// --- Função Principal ---
// O ponto de entrada do programa.
int main() {
    // --- Declaração de Variáveis ---
    // É uma boa prática declarar as variáveis no início do escopo.
    int numero1, numero2, resultadoSoma;

    // --- Entrada de Dados ---
    // A função `main` agora orquestra as chamadas para as funções auxiliares.
    // Cada função tem uma responsabilidade única.
    numero1 = lerNumero("Digite o primeiro número: ");
    numero2 = lerNumero("Digite o segundo número: ");

    // --- Processamento ---
    // A lógica de negócio (o cálculo) está isolada em sua própria função.
    resultadoSoma = somar(numero1, numero2);

    // --- Saída de Dados ---
    // A apresentação do resultado também é feita por uma função dedicada.
    exibirResultado(resultadoSoma);

    // Retorna 0 para o sistema operacional, indicando que o programa
    // foi executado com sucesso.
    return 0;
}
