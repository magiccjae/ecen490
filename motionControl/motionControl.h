#ifndef __HOTPLATE_H__
#define __HOTPLATE_H__

void printMatrix(gsl_matrix*, int, int);
gsl_matrix* measurementMatrix();
gsl_matrix* rotationMatrix(float, float);
gsl_matrix* pointToVelocity(float, float, float, float, float, float, float);
gsl_matrix* linearToAngular(gsl_matrix*, gsl_matrix*, gsl_matrix*);
float rowSum(gsl_matrix*, gsl_matrix*, int);

#endif
