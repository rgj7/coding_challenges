// codeabbey, problem 55
// solution by whoisrgj

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct word word_t;
struct word {
    char *str;
    int count;
    word_t *next;
};

// initializes a new word node
word_t *initWord(char *str) {
     word_t *newWord;
     newWord = (word_t*) malloc(sizeof(word_t));
     newWord->str = (char*) malloc(sizeof(char)*(strlen(str)+1));
     strcpy(newWord->str, str);
     newWord->count = 1;
     newWord->next = NULL;
     //fprintf(stdout, "new word: %s\n", newWord->str);
     return newWord;
}

// adds in alphabetical order ascending
void add(word_t **head, char *str) {
    word_t *newWord, *current;
    newWord = initWord(str);
    current = *head;
    
    // if list empty or if needed to be inserted before head
    if(*head == NULL || strncmp(str, (*head)->str, 3) < 0) {
        *head = newWord;
        (*head)->next = current;
    } else {
        while(current != NULL) {
            if(strncmp(current->str, str, 3) == 0) {
                current->count++;
                return;   
            } else if((strncmp(current->str, str, 3) < 0)
                && (current->next == NULL || (strncmp(current->next->str, str, 3) > 0))) {
                newWord->next = current->next;
                current->next = newWord;
                return;
            }
            current = current->next;
        }
    }
}

// print list
void printList(word_t *head, int min) {
    word_t *current;
    current = head;
    while(current != NULL) {
        if(current->count > min)
            fprintf(stdout, "%s ", current->str);
        current = current->next;
    }
    fprintf(stdout, "\n");
}

// free the list
void freeList(word_t *head) {
    word_t *current, *prev;
    current = head;
    
    while(current != NULL) {
        prev = current;
        current = current->next;
        free(prev);
    }
}

int main(int argc, char *argv[]) {
    char buf[4];
    word_t *head = NULL;
    
    for( ; ; ) {
        fscanf(stdin, "%3s", buf);
        if(strncmp(buf, "end", 3) == 0)
            break;
        add(&head, buf);
    }
    
    printList(head, 1);
    freeList(head);

    return 0;
}