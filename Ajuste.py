class Ajuste:
    #Classe que possui métodos de ajuste polinomial e retorna o valor dos coeficientes do polinômio
    def __init__(self,n,x,fx):
        #Entrada dos valores na forma de n (Grau do polinômio) e pares ordenados x,fx
        self.n = n
        self.x = x
        self.fx = fx
        
    def apol(cla):
        #Método dos Mínimos Quadrados para Polinômios
        import timeit #Função utilizada para medir o tempo
        ti = timeit.default_timer() #Início da contagem de tempo        
        a = []
        b = []
        ma = []
        aux = 0
        maux = []
        for i in range(0,2*(len(cla.x)+1)):
            for j in range(0,len(cla.x)):
                aux += cla.x[j]**(i)
            a.append(aux)
            aux = 0
        for i in range(0,cla.n):
            for j in range(0,len(x)):
                aux += cla.fx[j]*cla.x[j]**i
            b.append(aux)
            aux = 0
        for i in range(0,cla.n):
            for j in range(0,cla.n):
                maux.append(a[i+j])
            ma.append(maux)
            maux = []
            #Ao fim, um sistema linear do tipo AX = B é gerado  
        
        def gauss(a,b):
            #Como foi gerado um sistema linear, foi implementada o método da 
            #eliminação de Gauss para resolve-lo, pois este método tem melhor precisão
            for k in range(0,len(b)-1):
                for i in range(k+1,len(b)):
                    m = a[i][k]/a[k][k]
                    a[i][k] = 0
                    for j in range(k+1,len(b)):
                        a[i][j] = a[i][j] - m*a[k][j]
                    b[i] = b[i] - m*b[k]            
            x = [0 for col in range(len(b))]
            x[len(b)-1] = b[len(b)-1]/a[len(b)-1][len(b)-1]            
            for i in range(len(b)-2,-1,-1):
                soma = 0
                for j in range(i+1,len(b)):
                    soma = soma + a[i][j]*x[j]
                x[i] = (b[i]-soma)/a[i][i]
            x.reverse()
            return x     
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')
        return gauss(ma,b) #Ao fim, os coeficientes do polinômio são retornados  
        
    def scip_sol(cla):
        #Método de determinação dos coeficientes do polinômio de ajuste a partir
        #da biblioteca Scipy
        import timeit #Função utilizada para medir o tempo
        from scipy.optimize import curve_fit #Função de ajuste da biblioteca scipy
        ti = timeit.default_timer() #Início da contagem de tempo
        def fun(x,a,b,c,d):
            #Função característica do ajuste, neste caso, um polinômio de grau 4
            return a*x**3 + b*x**2 + c*x + d        
        popt,pcov = curve_fit(fun,cla.x,cla.fx)
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')            
        return popt #Ao fim, os coeficientes do polinômio são retornados  


'''Exemplo'''

x = [0,0.25,0.5,0.75,1] 
fx = [1,1.2840,1.6487,2.1170,2.7183] 
a = Ajuste(4,x,fx)
print('[Mínimos Quadrados]')
j = a.scip_sol()
print('\nOs coeficientes são: ',j)
print('\n[Scipy]')
g = a.apol()
print('\nOs coeficientes são: ',g)



