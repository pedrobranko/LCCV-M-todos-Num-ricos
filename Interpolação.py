class Interp: 
    #Classe que possui os métodos de interpolação de Lagrange e da biblioteca Scipy
    def __init__(self,x,fx):
        #A entrada é feita pelo conjunto de pares ordenados x,fx
        self.x = x
        self.fx = fx        
    def lagrange(aux):
        #Método de Lagrange
        import timeit #Função utilizada para medir o tempo
        ti = timeit.default_timer() #Início da contagem de tempo
        def produto(f): #Função que representa o algorítimo de Lagrange           
            p = 0
            for i in range(0,len(aux.x)):
                s = 1
                for k in range(0,len(aux.x)):
                    if k != i:
                        s = s*(f-aux.x[k])/(aux.x[i]-aux.x[k])
                p = p+aux.fx[i]*s
            return p #Retorna o polinômio 
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')
        return produto #Retorna a função do polinômio
    
    def sci_lag(aux):
        #Método do Scipy
        import timeit #Função utilizada para medir o tempo
        from scipy.interpolate import lagrange #Import da biblioteca Scipy
        ti = timeit.default_timer() #Início da contagem de tempo
        poli = lagrange(aux.x,aux.fx) 
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')
        return poli #Retorna a função do polinômio
    
    def esp(aux,n):
        #Função que cria um vetor com N pontos de x igualmente espaçados
        a = []
        count = 0
        for i in range(0,n):
            count += (aux.x[len(aux.x)-1]-aux.x[0])/(n)
            a.append(count)
        return a


'''Exemplo'''

import matplotlib.pyplot as plt #Biblioteca de impressão
a = Interp([0,0.25,0.5,0.75,1],[1,1.2840,1.6487,2.1170,2.7183]) #Criação do objeto
print('[Lagrange]')
j = a.lagrange()
print('[Scipy]')
k = a.sci_lag()
x = a.esp(20) #Cria um vetor com os elementos de x
lag = [j(x[i]) for i in range(len(x))] #Cria um vetor com os elementos de y da função Lagrange
sci = [k(x[i]) for i in range(len(x))] #Cria um vetor com os elementos de y da função Scipy
plt.plot(x,sci,'b-', x,lag,'ro') #Imprime ambas, em pontos vermelhos Scipy e a linha azul Lagrange











