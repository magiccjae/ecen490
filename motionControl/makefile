CC = gcc
CFLAGS  = -Wall -std=c99
LIB = -L/usr/lib -lgsl -lgslcblas -lm

# the build target executable:
EXE = motionControl

all: $(EXE)

$(EXE): $(EXE).c
	$(CC) $(CFLAGS) -o $(EXE) $(EXE).c $(LIB)

run: motionControl
	./motionControl


clean:
	$(RM) $(EXE) *.o

valgrind: $(EXE)                                          
	valgrind --tool=memcheck --leak-check=yes ./$(EXE)

