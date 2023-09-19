#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

void calculateFrequencies(const char *text, long length_text, double *tetrafrequencies)
{

    if (tetrafrequencies == NULL)
    {
        perror("Memory allocation failed");
        exit(1);
    }

    memset(tetrafrequencies, 0, 26 * 26 * 26 * 26 * sizeof(double));

    for (int i = 0; i < length_text - 3; i++)
    {
        int x = (text[i] - 'A') * 26 * 26 * 26 +
                (text[i + 1] - 'A') * 26 * 26 +
                (text[i + 2] - 'A') * 26 +
                (text[i + 3] - 'A');
        tetrafrequencies[x] += 1;
    }
    for (int i = 0; i < 26 * 26 * 26 * 26; i++)
    {
        tetrafrequencies[i] = tetrafrequencies[i] / (length_text - 3);
    }
}

double calculateFitness(const char *text, long length_text, double *tetrafrequencies)
{

    double result = 0;

    for (int i = 0; i < length_text - 3; i++)
    {
        int x = (text[i] - 'A') * 26 * 26 * 26 +
                (text[i + 1] - 'A') * 26 * 26 +
                (text[i + 2] - 'A') * 26 +
                (text[i + 3] - 'A');

        if (tetrafrequencies[x] == 0)
        {
            result += -15;
        }
        else
        {
            result += log(tetrafrequencies[x]);
        }
    }

    result = result / (length_text - 3);

    return result;
}


char* decrypt(char* plaintext, char* key, int key_length, char* ciphertext,int ciphertext_length){
    unsigned int i, j;
    int value;
    for (i = 0, j = 0; i < ciphertext_length; i++, j++){
        if (j >= key_length){
            j = 0;
        }
        value = (ciphertext[i]) - (key[j]);
        if (value < 0){
            value = value + 26;
        }
        plaintext[i] = value + 65;
        printf("%d\n",value + 65);
    }
    return plaintext;
}

void bruteforce(int key_lenght){
    char key[key_lenght];
    for (int i = 0; i< pow(26,key_lenght);i++)
    {
        
    }
}

int main()
{

    char *languageExample = "booksInTXT/moby_dick_cleaned.txt";
    char *languageExampleText = 0;
    long languageExampleTextLength;
    FILE *file_languageExample = fopen(languageExample, "rb");

    if (file_languageExample)
    {
        fseek(file_languageExample, 0, SEEK_END);
        languageExampleTextLength = ftell(file_languageExample);
        fseek(file_languageExample, 0, SEEK_SET);
        languageExampleText = malloc(languageExampleTextLength);
        if (languageExampleText)
        {
            fread(languageExampleText, 1, languageExampleTextLength, file_languageExample);
        }
        fclose(file_languageExample);
    }

    char *languageBaselineExample = "booksInTXT/romeo_and_juliet_cleaned.txt";
    char *languageBaselineExampleText = 0;
    long languageBaselineExampleLength;
    FILE *f_languageBaselineExample = fopen(languageBaselineExample, "rb");

    if (f_languageBaselineExample)
    {
        fseek(f_languageBaselineExample, 0, SEEK_END);
        languageBaselineExampleLength = ftell(f_languageBaselineExample);
        fseek(f_languageBaselineExample, 0, SEEK_SET);
        languageBaselineExampleText = malloc(languageBaselineExampleLength);
        if (languageBaselineExampleText)
        {
            fread(languageBaselineExampleText, 1, languageBaselineExampleLength, f_languageBaselineExample);
        }
        fclose(f_languageBaselineExample);
    }

    int array_size = 26 * 26 * 26 * 26;

    double *languageTetrafrequencies = malloc(26 * 26 * 26 * 26 * sizeof(double));

    calculateFrequencies(languageExampleText, languageExampleTextLength, languageTetrafrequencies);


    double romeo_juliet_fitness = calculateFitness(languageBaselineExampleText,languageBaselineExampleLength,languageTetrafrequencies);

    printf("Fitness of Romeo and Juliet is: %f: " , romeo_juliet_fitness);



    char *ciphertextFile = "ciphertexts/example_3.txt";
    char *ciphertext = 0;
    long ciphertextLength;
    FILE *f_ciphertextFile = fopen(ciphertextFile, "rb");

    if (f_ciphertextFile)
    {
        fseek(f_ciphertextFile, 0, SEEK_END);
        ciphertextLength = ftell(f_ciphertextFile);
        fseek(f_ciphertextFile, 0, SEEK_SET);
        ciphertext = malloc(ciphertextLength);
        if (ciphertext)
        {
            fread(ciphertext, 1, ciphertextLength, f_ciphertextFile);
        }
        fclose(f_ciphertextFile);
    }




    bruteforce();



    free(languageTetrafrequencies);

    return 0;
}
