class ELEMENTO:
    def __init__(self, id=None, prior=None):
        self.id = id
        self.prior = prior

    def __str__(self):
        '''
        Sobrescreve o método str que formata o print do objeto
        :return:
        '''
        return "{} {}".format(self.id, self.prior)


class FILADEPRIORIDADE:
    def __init__(self, A=[], maxElementos=4000, m=0):
        '''

        :param A:
        :param maxElementos:
        :param m:
        '''
        self.A = A
        self.maxElementos = maxElementos
        self.m = m
        self.A = [ELEMENTO(-1, -1.0)]

    def __str__(self):
        result = ""
        if self.m > 0:
            for i in range(1,self.m+1):
                result = result + str(self.A[i]) + " "
        else:
            result = str(self.A[0])
        return result


    def Heap_Max(self):
        '''
        devolve o elemento que possui a maior prioridade do vetor A o
        qual contém m elementos. Se não existem elementos na fila de prioridade, o método
        deve devolver -1 -1,0. O consumo desse método deve ser O(1).
        '''
        if self.m > 0:            #Θ(1)
            result = self.A[1]    #O(1)
        else:                     #O(1)
            result = self.A[0]    #O(1)
        return result             #Θ(1)
        '''
        O(1)
        '''


    def Heap_Extract_Max(self):
        '''
        remove e devolve o elemento que possui a maior prioridade
        do vetor A e que contém m elementos. Se não existem elementos na fila de
        prioridade, o método deve devolver -1 -1,0. O consumo desse método deve ser O(lg m).
        '''
        if self.m > 0:              #Θ(1)
            self.m = self.m - 1     #O(1)
            max = self.A.pop(1)     #O(1)
            self.Max_Heapify(1)     #O(lg m)
        else:                       #O(1)
            max = self.A[0]         #O(1)

        return max                  #Θ(1)
        '''
        O(lg n)
        '''

    def Heap_Insert(self, elemento):
        '''
        insere o elemento no vetor A que contém m
        elementos. Se é possível inserir o elemento, o método devolve T. Caso contrário,
        devolve F. O consumo desse método deve ser O(lg m).
        '''
        # valor da prioridade, validar os 90000
        if self.m < self.maxElementos:                                    #Θ(1)
            prior, elemento.prior = elemento.prior, -1*self.maxElementos  #O(1)
            self.m = self.m + 1                                           #O(1)
            self.A.insert(self.m, elemento)                               #O(1)
            self.Heap_Increase_Key(self.m, prior)                         #O(lg m)
            return "T"                                                    #O(1)
        else:                                                             #O(1)
            return "F"                                                    #O(1)

        '''
        O(1) + O(lg m)
        '''



    def Heap_Print(self, A, m):
        '''
        imprime o vetor A que contém m elementos
        '''
        result = ""                                         #Θ(1)
        if self.m > 0:                                      #Θ(1)
            for i in range(1,self.m+1):                     #O(m)
                result = result + str(self.A[i]) + " "      #O(m)
        else:                                               #O(1)
            result = str(self.A[0])                         #O(1)
        return result                                       #Θ(1)
        '''
        T(m): O(m)
        '''



    def Max_Heapify(self, i):
        '''
         recebe o vetor A e o índice i, tal que as árvores com raízes nos
        filhos esquerdo e direito do nó i são max-heaps e o único elemento que não está na
        posição certa na sub árvore enraizada em i é o elemento de índice i. O método deve
        converter o quase max-heap enraizado em i em um max-heap. Esse método pode
        ser utilizado como método auxiliar do Heap-Extract-Max.
        '''
        e = 2*i                                                       #Θ(1)
        d = 2*i+1                                                     #Θ(1)
        if e <= self.m and self.A[e].prior > self.A[i].prior:         #Θ(1)
            maior = e                                                 #O(1)
        else:                                                         #Θ(1)
            maior = i                                                 #)(1)
        if d <= self.m and self.A[d].prior > self.A[maior].prior:     #Θ(1)
            maior = d                                                 #O(1)

        if maior != i:                                                #Θ(1)
            self.A[i], self.A[maior] = self.A[maior], self.A[i]       #O(1)
            self.Max_Heapify(maior)                                   #T(h-1)

        '''        
        T(h)≤T(h-1)+Θ(1) #varios Θ(1) e O(1) 
        T(h)=O(h) # agora deixar em função de m
        Como h = ⌊lg(m/i)⌋, propriedade de heap
        T(h)=O(h)=O(⌊lg(m/i)⌋)=O(lg(m/i))=O(lg(m))
        '''

    def get_parent(self, i):
        if ((i > 1)):
            return i // 2
        return 0

    def Heap_Increase_Key(self, i, prior):
        '''
        aumenta o valor da prioridade para prior do elemento
        que está na posição i do vetor A e o realoca na posição certa no heap, caso
        necessário. Pode ser utilizado como método auxiliar do Heap-Insert. O consumo
        desse método deve ser O(lg m).
        '''#-1 -1,0
        self.A[i].prior = prior           #Θ(1)
        while ((i > 1) and(self.A[self.get_parent(i)].prior < self.A[i].prior)):          #T(h) = O(h)
            self.A[i], self.A[self.get_parent(i)] = self.A[self.get_parent(i)], self.A[i] #T(h)
            i = self.get_parent(i)                                                        #T(h)
        return

        '''
        Pior dos casos é aumentar a prioridade de uma folha para acima da raíz;
        nesse caso vai percorrer h - 1.
        T(h)≤T(h-1)+Θ(1) #varios Θ(1) e O(1) 
        T(h)=O(h) # agora deixar em função de m
        Como h = ⌊lg(m/i)⌋, propriedade de heap
        T(h)=O(h)=O(⌊lg(m/i)⌋)=O(lg(m/i))=O(lg(m))
        '''


def main():
    '''
    No programa principal deve ser criada uma fila de prioridades vazia com maxElementos=4000.
    '''
    fila_de_prioridade = FILADEPRIORIDADE()
    qtd_iteracoes = input("Digite o número de operações que deseja realizar:")

    for iteracao in range(int(qtd_iteracoes)):
        comando = input("Digite a operação, caso tenha argumentos digite-os com 1 espaçamento dividindo:")
        args = comando.split(" ")
        if args[0] == "1":
            print(fila_de_prioridade.Heap_Max())
        elif args[0] == "2":
            print(fila_de_prioridade.Heap_Extract_Max())
        elif args[0] == "3":
            id = int(args[1])
            prior = float(args[2])
            print(fila_de_prioridade.Heap_Insert(ELEMENTO(id, prior)))
        elif args[0] == "4":
            print(fila_de_prioridade)




if __name__ == "__main__":
    main()