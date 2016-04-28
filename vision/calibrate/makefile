CC = g++
LIB = `pkg-config --libs --cflags opencv` -ldl -lm

# the build target executable:
EXE = calibrate

all: $(EXE)

$(EXE): $(EXE).cpp
	$(CC) $(EXE).cpp -o $(EXE) $(LIB)

run: calibrate
	./calibrate


clean:
	$(RM) $(EXE) *.o

valgrind: $(EXE)                                          
	valgrind --tool=memcheck --leak-check=yes ./$(EXE)

