#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define the function y(n)
int y(int n) {
    return 3 * n * n + 13 * n + 10;
}

int main() {
    FILE *fp;
    fp = fopen("data1.dat", "w");

    int n_values[11];
    int y_values[11];
    int highlight_index;

    // Define the range of n
    for (int i = 0; i < 11; i++) {
        n_values[i] = i;
    }

    // Compute y(n) for each value of n
    for (int i = 0; i < 11; i++) {
        y_values[i] = y(n_values[i]);
    }

    // Find the index of n=9
    for (int i = 0; i < 11; i++) {
        if (n_values[i] == 9) {
            highlight_index = i;
            break;
        }
    }

    // Write n and y(n) values to the file
    fprintf(fp, "n y(n)\n");
    for (int i = 0; i < 11; i++) {
        fprintf(fp, "%d %d\n", n_values[i], y_values[i]);
    }

    // Write the index of n=9 to the file
    fprintf(fp, "Highlight index: %d\n", highlight_index);

    // Close the file
    fclose(fp);

    return 0;
}

