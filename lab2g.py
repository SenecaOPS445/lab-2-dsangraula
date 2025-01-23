#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    try:
        timer = int(sys.argv[1]) 
    except ValueError:
        print("Error: Timer value must be a valid integer.")
        print(f"Usage: {sys.argv[0]} [timer]")
        sys.exit(0)  
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')

