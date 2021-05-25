inicial=1000
x=0.05

juros_tempo=1+(x/100)#Fórmula de juros

montante=inicial
for i in range(12):
 montante*=juros_tempo

print(montante)