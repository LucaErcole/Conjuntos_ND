#comando para ler txt
text = open("calculo_1.txt", "r")

#determinando a quantidade de operaçãoes 
a = text.readline().split(",")
plinha = []
plinha.append(int(a[0]))

#Contador while
contador = plinha[0]

#Laço de repetição das operações
while contador > 0:

    #leitura e ordenação na tabela ask para a letra da operação
    b = text.readline().rstrip('\n')
    slinha = []
    slinha.append(ord(b[0]))

    #If para a operação da união
    if slinha == [85]:

        #lendo as linhas com numeros e transformando em lista
        tlinha = text.readline()
        tlinha = tlinha.rstrip('\n')
        lista1 = tlinha.split(", ")

        qlinha = text.readline()
        qlinha = qlinha.rstrip('\n')
        lista2 = qlinha.split(", ")

        #codigo para união
        lista3 = []
        for i in lista1:
            lista3.append(i)
        for i in lista2:
            if i not in lista3:
                lista3.append(i)
        #tirando o numero de ciclos das operações
        contador = contador - 1

        #Print da operação
        print("União: Conjunto 1:", lista1,"conjunto 2:", lista2,"resultado:", lista3)

    #If para a operação da Interseção
    elif slinha == [73]:
        tlinha = text.readline()
        tlinha = tlinha.rstrip('\n')
        lista1 = tlinha.split(", ")

        qlinha = text.readline()
        qlinha = qlinha.rstrip('\n')
        lista2 = qlinha.split(", ")

        #codigo para a interseção
        lista3 = []
        for i in lista1:
            if i in lista2:
                lista3.append(i)
                
        contador = contador - 1

        print("Interseção: Conjunto 1:", lista1,"conjunto 2:", lista2,"resultado:", lista3)

    #If para a operação da Diferença
    elif slinha == [68]:
        tlinha = text.readline()
        tlinha = tlinha.rstrip('\n')
        lista1 = tlinha.split(", ")

        qlinha = text.readline()
        qlinha = qlinha.rstrip('\n')
        lista2 = qlinha.split(", ")

        #codigo para a diferença
        lista3 = []
        for i in lista1:
            if i not in lista2:
                lista3.append(i)
        for i in lista2:
            if i not in lista1:
                lista3.append(i)
                
        contador = contador - 1

        print("Diferença: Conjunto 1:", lista1,"conjunto 2:", lista2,"resultado:", lista3)

   #If para a operação do plano cartesiano
    elif slinha == [67]:
        tlinha = text.readline()
        tlinha = tlinha.rstrip('\n')
        lista1 = tlinha.split(", ")

        qlinha = text.readline()
        qlinha = qlinha.rstrip('\n')
        lista2 = qlinha.split(", ")

        #codigo para o produto cartesiano
        list3 = []
        for i in lista1:
            for l in lista2:
                lista3.append((i, l))
                
        contador = contador - 1

        print("Produto Cartesiano: Conjunto 1:", lista1,"conjunto 2:", lista2,"resultado:", lista3)
    
  
  
    

