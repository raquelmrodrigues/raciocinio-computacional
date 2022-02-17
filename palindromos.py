palavra = input('Digite uma palavra: ')

def palidromo(palavra):
    
    inicio = 0
    fim = len(palavra)

    for i in range(len(palavra)//2):
        if palavra[inicio] != palavra[fim]:
            return False
        inicio =+ 1 
        fim =- 1
    return True