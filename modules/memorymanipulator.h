#include <stdio.h>
#include <stdlib.h>

void *alocateProcessInMemoryDynamic(size_t size){
    void *ptr = malloc(size);
    if (ptr == NULL) {
        printf("Erro: falha na alocação de memória.\n");
        exit(1);  // Encerrar o programa se não houver memória suficiente
    }
    return ptr;
}