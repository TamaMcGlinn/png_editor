CC := gcc
OUT := test-libpng
CFLAGS = -std=c++17 -Wall -fpermissive
LFLAGS = -lpng

$(OUT): main.cc
	$(CC) $< $(CFLAGS) $(LFLAGS) -o $(OUT)
