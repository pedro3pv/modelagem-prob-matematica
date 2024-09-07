#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    int n;
    int *column;
    int operation[4];
}File;

File *initFile(long size) {
    File *file = (File *)malloc(sizeof(File));
    if (file == NULL) {
        printf("Error! Memory not allocated for File structure.");
        exit(1);
    }

    file->n = size;
    file->column = (int *)malloc(size * sizeof(int));
    if (file->column == NULL) {
        printf("Error! Memory not allocated for column array.");
        free(file);
        exit(1);
    }

    return file;
}

int *convertCharIntoIntArray(char *line, long n) {
    int *int_arr;
    int i, offset, index;
    // alloc mem for int arr
    int_arr = malloc(sizeof(int) * (strlen(line) / n));
    if (int_arr == NULL) {
        printf("Error! Memory not allocated for int array.");
        exit(1);
    }
    index = 0;
    // using sscanf() "convert" string to int
    while (sscanf(line, "%d%n", &i, &offset) == 1) {
        // offset increments ptr to lines
        line += offset;
        int_arr[index++] = i;
    }
    return int_arr;
}

void convertStrToOperations(char *line){

}


File *readFile() {
    FILE *fptr;

    fptr = fopen("matriz.txt", "r");
    if (fptr == NULL) {
        fprintf(stderr, "Error! File not found.");
        exit(1);
    }

    char buffer[256];
    if (fgets(buffer, sizeof(buffer), fptr) == NULL) {
        fprintf(stderr, "Error! Failed to read the file.");
        fclose(fptr);
        exit(1);
    }

    long size = atol(buffer);
    File *file = initFile(size);
    printf("Size: %ld\n", size);

    for (int i = 0; i < size; i++) {
        if (fgets(buffer, sizeof(buffer), fptr) == NULL) {
            fprintf(stderr, "Error! Failed to read the line.");
            free(file->column);
            free(file);
            fclose(fptr);
            exit(1);
        }
        printf("Line: %s", buffer);
        file->column[i] = *convertCharIntoIntArray(buffer, file->n);
    }

    fclose(fptr);
    return file;
}

void freeFile(File *file) {
    free(file->column);
    free(file);
}