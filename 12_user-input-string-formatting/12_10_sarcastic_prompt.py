# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("What is an honest opinion you hold?: ")

honesty = ""
for char in range(len(opinion)):
    if not char % 2:
        honesty = honesty + opinion[char].upper()

    else:
        honesty = honesty + opinion[char].lower()

print(str(honesty))