#include <stdio.h>

int main() {
    // Define the first term and common ratio
    int first_term = 5;
    int common_ratio = 2;

    // Generate the geometric progression sequence
    int num_terms = 20;
    int x_values[num_terms];
    double seq_gp[num_terms];

    // Populate the arrays
    int current_term = first_term;
    for (int n = 0; n < num_terms; n++) {
        x_values[n] = n;
        seq_gp[n] = current_term;
        current_term *= common_ratio;
    }

    // Open the .dat file for writing
    FILE *file = fopen("data.dat", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    // Write the input values to the file
    fprintf(file, "n\tx(n)\n");
    for (int i = 0; i < num_terms; i++) {
        fprintf(file, "%d\t%lf\n", x_values[i], seq_gp[i]);
    }

    // Close the file
    fclose(file);

    return 0;
}

