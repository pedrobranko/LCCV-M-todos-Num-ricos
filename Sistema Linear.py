class Linsolv: 
    #Classe que possui os métodos de Gauss-Seidel e da biblioteca numpy para resolução de sistemas lineares
    def __init__(self,a,b): 
        #A entrada de dados é feita a partir da matriz dos coeficientes A e da matriz B
        self.a = a
        self.b = b        
        au = 0
        av = []
        a = self.a                
        for i in range(0,len(a)):    
            #Trecho que verifica a convergência da Matriz A pelo critério de Sassenfeld
            for j in range(0,len(a)):
                au += a[i][j]
            au -= a[i][i]    
            av.append(au/a[i][i])
            if av[i]>1:                
                self.conv = True
            else:
                self.conv = False
            au = 0
            #Fim do trecho
    def gauss_seidel(aux): 
        #Função que utiliza o método de Gauss-Seidel 
        import timeit #Função utilizada para medir o tempo
        tol = float(input('Entre com o valor da tolerância: ')) #Entrada da tolerância dada em 10^-n, n>=0
        nite = int(input('Entre com o número de tentativas: ')) #Entrada do número de tentativas        
        ti = timeit.default_timer() #Inínio da contagem de tempo 
        if aux.conv == True:
            return
        count = 0
        dist = 1        
        ax = aux.a
        b = aux.b        
        x0 = [0 for col in range(len(b))] #Cria matriz de zeros do chute inicial
        x = [0 for col in range(len(b))] #Cria matriz utilizada para retorno                 
        while dist**(1/2)>tol and count<nite: 
            #Algorítimo de Gauss-Seidel
            for i in range(0,len(b)):
                s0 = b[i]   
                s1 = 0
                for j in range(0,i):
                    s0 -= ax[i][j]*x[j]
                for j in range(i+1,len(b)):
                    s1 -= ax[i][j]*x0[j]        
                x[i] = (s0+s1)/ax[i][i]
            dist = 0    
            for i in range(0,len(b)):
                dist += ((x0[i]-x[i])**2)
            count += 1               
            for i in range(0,len(b)):
                x0[i] = x[i]
            #Fim do algorítmo
        tf = timeit.default_timer() #Fim da contagem de tempo 
        print('Tempo de execução foi de: ',tf-ti, 'segundos')              
        return x #Retorna o vetor resporta x 
    
    def np_solv(aux): 
        #Função que utiliza o método da biblioteca Numpy
        import numpy as np #Import da biblioteca numpy
        import timeit
        ti = timeit.default_timer() #Início da contagem de tempo  
        x = np.linalg.solve(aux.a,aux.b)
        tf = timeit.default_timer()  #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')        
        return x #Retorna o vetor resporta x
    
    def np_solv2(aux): 
        #Função que utiliza o Numpy para inverter a matriz A e multiplicar pela Matris B
        import numpy as np #Import da biblioteca numpy
        import timeit
        ti = timeit.default_timer() #Início da contagem de tempo  
        x = np.linalg.inv(aux.a).dot(aux.b)
        tf = timeit.default_timer()  #Fim da contagem de tempo  
        print('Tempo de execução foi de: ',tf-ti, 'segundos')
        return x #Retorna o vetor resporta x 



def matcon(n,sol): 
    #Função auxiliar que cria uma matriz aleatória convergente pelo critério de Sassenfeld. 
    #Esta função recebe como entrada o tamanho da matriz e o vetor solução X
    import random #Função random utilizada ao criar os elementos aleatórios
    mb = []
    ma = [[random.randint(0,10) for col in range(int(n))] for row in range(int(n))] #Matriz aleatória
    for i in range(0,int(n)): #For que substitui a diagonal principal por elementos que garantam a convergência
        aux = 0
        for j in range(0,int(n)):
            aux += ma[i][j]
        ma[i][i] = aux
    for i in range(0,int(n)): #For que cria o vetor B de acordo com o vetor X dado
        aux = 0
        for j in range(0,int(n)):
            aux += ma[i][j]*sol[j]
        mb.append(aux)
    return(ma,mb) #Retorna a matriz A e o vetor B

'''Parte bonus da atividade que foi solicitada '''
def fun(x): 
    #Função que retorna o valor de f(x)
    p = 2*x**2+x-3
    return p

def defun(x): 
    #Função que retorna o f'(x)
    p = 4*x+1
    return p

def newton(nite,x0,tol): 
    #Método de Newton-Raphson para zeros de funções
    count = 0
    while count < nite:
        x = x0 - fun(x0)/defun(x0)
        if abs(x-x0)<tol:
            return x
        count += 1
        x0 = x
    print('O método falhou após ',nite,' interações')
    return


'''Exemplo'''

sol = [i for i in range(0,20)] #Solução para criar a matriz aleatória 20x20
entrada = matcon(20,sol) #Criação da matriz
aux = Linsolv(entrada[0],entrada[1])
'''Como a matriz é muito grande, deve-se ter cuidado na exibição da mesma'''
a = aux.gauss_seidel()
#print(a)
b = aux.np_solv()
#print(b)
c = aux.np_solv2()
#print(c)


