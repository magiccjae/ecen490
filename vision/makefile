CC = g++
LIB = `pkg-config --libs --cflags opencv` -ldl -lm

# the build target executable:
EXE = vision

all: $(EXE)

$(EXE): $(EXE).cpp
	$(CC) $(EXE).cpp -o $(EXE) $(LIB)

run: vision
	./vision


clean:
	$(RM) $(EXE) *.o

valgrind: $(EXE)                                          
	valgrind --tool=memcheck --leak-check=yes ./$(EXE)

