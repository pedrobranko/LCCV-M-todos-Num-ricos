class Integ:
    #Classe que possui métodos de integração numérica implementada e da 
    #biblioteca scipy
    def __init__(self,fun,b,a,n):
        #A entrada consiste na função a ser integrada (fun), o intervalo de
        #integração (b e a) e a quantidade de intervalos (n)
        self.b = b
        self.a = a
        self.n = n
        self.fun = fun        

    def int_trap(aux):
        #Função que utiliza o algoritimo de Newton-Cotes
        import timeit #Função utilizada para medir o tempo
        ti = timeit.default_timer() #Início da contagem de tempo
        x = []
        for i in range(aux.a,aux.n+1):
            x.append(i*(aux.b-aux.a)/(aux.n))
        inte = 0 
        part = 0
        for j in range(1,len(x)-1):
            part += 2*aux.fun(x[j])    
        inte = (x[1]-x[0])/2*(fun(x[len(x)-1])+fun(x[0])+part)
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')  
        return inte #Retorna o valor da integral
    
    def int_sc(aux):
        #Função que utiliza a biblioteca numpy e scipy
        import timeit #Função utilizada para medir o tempo        
        import numpy as np
        from scipy import integrate
        ti = timeit.default_timer() #Início da contagem de tempo
        x = np.linspace(aux.a,aux.b,aux.n)
        y = fun(x)
        inte = integrate.trapz(y,x)
        tf = timeit.default_timer() #Fim da contagem de tempo
        print('Tempo de execução foi de: ',tf-ti, 'segundos')
        return inte #Retorna o valor da integral
   
    
'''Exemplo'''    
def fun(x):
    #Função que representa o f(x) que será integrado
    p = 2*x**2+x-3
    return p
a = Integ(fun,1,0,50)
print('[Método Implementado]')
print('Integral :',a.int_trap())
print('\n[Método Scipy]')
print('Integral :',a.int_sc())