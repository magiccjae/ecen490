#include <math.h>
#include <stdio.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_cblas.h>

#include "motionControl.h"

void printMatrix(gsl_matrix* m, int row, int col) {
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            printf("%g ", gsl_matrix_get(m, i, j));
        }
        printf("\n");
    }
}

gsl_matrix* measurementMatrix() {
    gsl_matrix *m = gsl_matrix_alloc (3, 3);

    gsl_matrix_set (m, 0, 0, -.5);
    gsl_matrix_set (m, 0, 1, .866);
    gsl_matrix_set (m, 0, 2, (.866*6.9282 - -.5*4));
    gsl_matrix_set (m, 1, 0, -.5);
    gsl_matrix_set (m, 1, 1, -.866);
    gsl_matrix_set (m, 1, 2, (.866*6.9282 - -.5*4));
    gsl_matrix_set (m, 2, 0, 1);
    gsl_matrix_set (m, 2, 1, 0);
    gsl_matrix_set (m, 2, 2, 8);

    return m;
}

gsl_matrix* rotationMatrix(float omegaWorld, float omegaBody) {
    gsl_matrix *m = gsl_matrix_alloc (3, 3);

    float theta = omegaWorld - omegaBody; // TODO check if radians or degrees

    gsl_matrix_set (m, 0, 0, cos(theta));
    gsl_matrix_set (m, 0, 1, sin(theta));
    gsl_matrix_set (m, 0, 2, 0);
    gsl_matrix_set (m, 1, 0, -sin(theta));
    gsl_matrix_set (m, 1, 1, cos(theta));
    gsl_matrix_set (m, 1, 2, 0);
    gsl_matrix_set (m, 2, 0, 0);
    gsl_matrix_set (m, 2, 1, 0);
    gsl_matrix_set (m, 2, 2, 1);

    return m;
}

gsl_matrix* pointToVelocity(float cX, float cY, float cOmega, float dX, float dY, float dOmega, float time) { //d stands for desired
    gsl_matrix *m = gsl_matrix_alloc (3, 1);

    float vX = (dX - cX) / time;
    float vY = (dY - cY) / time;
    float omega = (dOmega - cOmega) / time;

    gsl_matrix_set (m, 0, 0, vX);
    gsl_matrix_set (m, 1, 0, vY);
    gsl_matrix_set (m, 2, 0, omega);

    return m;
}

gsl_matrix* linearToAngular(gsl_matrix* R, gsl_matrix* M, gsl_matrix* V) {
    gsl_matrix_transpose(R);

    int signum;

    gsl_matrix * inverseR = gsl_matrix_alloc (3, 3);
    gsl_permutation * perm = gsl_permutation_alloc (3);

    gsl_linalg_LU_decomp (M, perm, &signum);
    gsl_linalg_LU_invert (M, perm, inverseR);

    gsl_matrix_mul_elements (inverseR, M);
    gsl_matrix* result = inverseR;

    float omega1 = rowSum(result, V, 0);
    float omega2 = rowSum(result, V, 1);
    float omega3 = rowSum(result, V, 2);

    gsl_matrix * final = gsl_matrix_alloc (3, 1);
    gsl_matrix_set (final, 0, 0, omega1);
    gsl_matrix_set (final, 1, 0, omega2);
    gsl_matrix_set (final, 2, 0, omega3);

    gsl_matrix_free(inverseR);
    gsl_permutation_free(perm);
    return final;
}

float rowSum(gsl_matrix* result, gsl_matrix* V, int row) {
    float sum = 0;
    for(int i = 0; i < 3; i++) {
        sum += gsl_matrix_get(result, row, i) * gsl_matrix_get(V, i, 0);
    }
    return sum;
}

int main (void) {
    gsl_matrix* M = measurementMatrix();
    gsl_matrix* R = rotationMatrix(1, 2);
    gsl_matrix* V = pointToVelocity(0, 0, 0, 1, 1, 0, 1);

    gsl_matrix* final = linearToAngular(R, M, V);

    printMatrix(final, 3, 1);
    gsl_matrix_free (M);
    gsl_matrix_free (R);
    gsl_matrix_free (V);
    gsl_matrix_free (final);

    return 0;
}

