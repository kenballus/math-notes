# Author: Ben Kallus
# Asks for two numbers, then prints their sum, difference, product, the result of raising the first to the power of the second. Also prints their quotient and remainder, if the second number is not 0.

print((n:=float(input("Enter a number: ")),m:=float(input("Enter a number: ")),"")[2]+"\n".join(f"{n} {o} {m} = {eval(f'{n}{o}{m}')}"for o in{'-','+','*','**'}|({'/','%'}if m else set())))