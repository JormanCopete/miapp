lenguajes = ["Python","Csharp","PHP","GO","JAVA","Javascript"]



"""i = 1
while i <= 10:
    print(i)
    i = i + 1"""


"""i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i = i + 1"""

#for lenguaje in lenguajes:
#    print(lenguaje)    

personas = [ [1,"Carlos",25],   [2,"Tomas",15], [3,"Mauricio",36]  ]
for i in range(len(personas)):
    for j in range(len(personas[i])):  # 1,"Carlos",25]
        print(personas[i][j])