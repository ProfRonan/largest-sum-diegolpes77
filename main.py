def largest_sum(numbers: list[int]) -> tuple[int, int]:
    if len(numbers) < 2:
        return None

    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0], sorted_numbers[1]

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5] 
    print(largest_sum(lista1))  

    lista2 = [10, -5, 20, 15, -30]
    print(largest_sum(lista2)) 

    lista3 = [0, 0, 0, 0]
    print(largest_sum(lista3))  

    lista4 = [-10, -5, -2, -1]
    print(largest_sum(lista4))  

    lista5 = [5]
    print(largest_sum(lista5))  

    lista6 = []
    print(largest_sum(lista6))  
