import json

def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    
    while K < INDICE:
        K =+ 1
        SOMA += K
        
    print(f"Valor final de SOMA: {SOMA}")
    
def is_bibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return n ==0

def verificar_fibonacci():
    numero = int(input("Informe um número: "))
    
    if is_bibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
        
    
def analisar_faturamento_diario():
    faturamento_diario = '''{
        "faturamento": [200, 300, 0, 500, 400, 0, 700, 0, 800, 100, 0, 0, 0, 900, 1000, 0, 0, 0, 200, 300, 400, 500, 0, 0, 600, 700, 800, 0, 0, 900]
    }'''
    
    dados = json.loads(faturamento_diario)
    faturamento = [valor for valor in dados["faturamento"] if valor > 0]
    
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
    
def calcular_percentual_faturamento():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    total = sum(faturamento.values())
    
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
        
def inverter_string():
    def inverter(s):
        invertida = ''
        for char in s:
            invertida = char + invertida
        return invertida
    
    string = input("Informe uma string: ")
    print(f"String invertida: {inverter(string)}")
    
def main():
    print("1) Valor da variável SOMA")
    calcular_soma()
    print("\n2) Verificar Fibonacci")
    verificar_fibonacci()
    print("\n3) Análise de faturamento diário")
    analisar_faturamento_diario()
    print("\n4) Percentual de faturamento por estado")
    calcular_percentual_faturamento()
    print("\n5) Inversão de string")
    inverter_string()

if __name__ == "__main__":
    main()