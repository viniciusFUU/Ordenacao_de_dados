def shellSort(nums):
    contador = 0

    while contador < len(nums):
        for i in range(len(nums)-1, 0, -1):
            valorAtual=nums[i]
            valorComparado=nums[i-1]
            if valorAtual < valorComparado:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        
        contador+=1
    
    return nums


lista = [5, 4, 7, 9, 6, 3, 1, 2, 8]
print(shellSort(lista))