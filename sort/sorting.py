# O(1)
def array_search():
    print('Array search:')
    Pokemons = ["皮卡丘","胖丁","傑尼龜","卡比獸","呆呆獸","妙蛙種子","拉普拉斯"]
    n = 0
    print(Pokemons[n])

# O(n)
def simple_sort():
    print('Simple Sort:')
    Pokemons = ["皮卡丘","胖丁","傑尼龜","卡比獸","呆呆獸","妙蛙種子","拉普拉斯"]
    Find = "拉普拉斯"

    for Pokemon in Pokemons:
        if Pokemon is Find:
            print(Pokemon)
            break
        else:
            print("Not here")
