# Aula do dia 15/06/23

#   Como criar uma classe em python:
class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def apresentar(self):
        print('Ola meu nome é', self.nome)
        
    def envelhecer(self, anos):
        self.idade += anos 
        #self.idade = self.idade + anos
        print('Tenho', self.idade, 'anos.')
        
    def mostrarcpf(self):
        print('Este é o meu cpf', self.cpf)
        
pessoa1 = Pessoa('Layla', 22, '868.647.857-86')
pessoa2 = Pessoa('Victor', 27, '486.488.646-54')
pessoa3 = Pessoa('Duana', 22, '685.396.946-54')

pessoa1.apresentar()
#para a pesssoa envelhecer basta escrever 
pessoa1.envelhecer(10) # o numero dentro dos parenteses ira ser adicionado a idade 
# mostrar o cpf
pessoa1.mostrarcpf()

pessoa2.apresentar()
pessoa2.envelhecer(10)
pessoa2.mostrarcpf()

pessoa3.apresentar()
pessoa3.envelhecer(10)
pessoa3.mostrarcpf()

