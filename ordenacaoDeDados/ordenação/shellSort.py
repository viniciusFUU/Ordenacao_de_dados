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


lista = [51, 46, 73, 90, 66, 38, 13, 22, 87]
print(shellSort(lista))