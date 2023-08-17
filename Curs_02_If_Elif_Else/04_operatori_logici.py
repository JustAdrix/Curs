# OPERATORI_LOGICI

# "and" - echivalent cu "si"
# atat "acesta" cat si "celalalt" valoare de adevar
# este un operator care verifica toate elementele de pe linie - valoarea lor de adevar

acesta, celalalt = True, True
print("acesta and celalalt: ", acesta and celalalt)  #  True and True => True
acesta, celalalt = True, False
print("acesta and celalalt: ", acesta and celalalt)   #  True and False => False
acesta, celalalt = False, True
print("acesta and celalalt: ", acesta and celalalt)    #  False and True => False
acesta, celalalt = False, False
print("acesta and celalalt: ", acesta and celalalt)    #  False and False => False

print("-"*40)

# operatorul "or" (SAU)
# fie alpha, fie beta valoare de adevar (oricare din ele)
alpha, beta = True, True
print("alpha or beta: ", alpha or beta)    #  True or True => True
alpha, beta = True, False
print("alpha or beta: ", alpha or beta)    #  True or False => True
alpha, beta = False, True
print("alpha or beta: ", alpha or beta)    #  False or True => True
alpha, beta = False, False
print("alpha or beta: ", alpha or beta)    #  False or False => False


#operatori logici
# and: Acest operator returnează True dacă ambele condiții evaluate sunt adevărate.
# Altfel, returnează False.
#

x = 5
print(x > 3 and x < 10) # Outputs True


# or: Acest operator returnează True dacă cel puțin
# una dintre condițiile evaluate este adevărată. Altfel, returnează False.

x = 5
print(x > 3 or x > 10) # Outputs True


# not: Acest operator neghează rezultatul condiției pe care o evaluează.
# Dacă condiția este adevărată, not va returna False și viceversa.

x = 5
print(not(x > 3 and x < 10)) # Outputs False



