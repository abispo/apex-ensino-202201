
if __name__ == '__main__':

    # O Python possui diversos operadores:
    # Aritméticos: + - * / % ** //

    # Atribuição: = += -= *= /=
    # a = a + 1     -> a += 1

    # Comparação: == != > < >= <=
    nome = "ok"
    print(f"1 == 1 -> {1 == 1}")
    print(f"5 != 3 -> {5 != 3}")
    print(f"10 > 13 -> {10 > 13}")
    print(f"12 <= 12 -> {12 <= 12}")
    # Utilizamos acima uma f-string.

    # Operadores lógicos
    # O resultado das operações lógicas sempre retorna um valor booleano (True ou False)
    # and -> Retorna True se os dois lados da expressão forem verdadeiros
    print(f"5 < 6 and 10 > 20 -> {5 < 6 and 10 > 20}")
    # True  and     True    ->  True
    # True  and     False   ->  False
    # False and     True    ->  False
    # False and     False   ->  False

    # or -> Retorna True se qualquer um dos lados da comparação for verdadeiro
    # True  or     True    ->  True
    # True  or     False   ->  True
    # False or     True    ->  True
    # False or     False   ->  False
    print(f"5 < 6 or 10 > 20 -> {5 < 6 or 10 > 20}")
    print(f"5 > 6 or 10 > 20 -> {5 > 6 or 10 > 20}")

    # not -> Retorna True se a expressão for False e False se a expressão for true (operador negação)
    # not   True    ->  False
    # not   False   ->  True
    print(f"not 5 > 6 -> {not 5 > 6 }")

    # Operadores de identidade (is, is not)
    # Operadores de pertencimento (in, not in)

