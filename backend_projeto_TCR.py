import math
#Funcao para verificar se o Sistema pode ser resolvivel pro TCR.
def eh_resolvivel(nums, mods):
    for i in range(len(mods)-1):
        for j in range(i+1, len(mods)):
            if math.gcd(mods[i], mods[j])!=1:
                return False
        
    return True

#funcao para calcular os inversos de cada modulo parcial.
def calcula_inversos(nums, mods):
    all_d = []
    for i in range(len(nums)):
        d = 0
        while True:
            if ((nums[i]%mods[i]) * d)%mods[i] == 1:
                all_d.append(d)
                break
            d+=1
    return all_d


def main():
    nums = list(map(int, input("Insira todos os restos: ").split()))
    mods = list(map(int, input("Insira todos os mods: ").split()))
    
    if not eh_resolvivel(nums, mods):
        print("nao e possivel resolucionar")
        exit(0)
    
    M = 0 #Modulo Global
    for mod in mods:
        if M:
            M *= mod
        else:
            M = mod   

    all_c = []  #Guarda todos os modulos parciais.
    for mod in mods:
        c = M / mod
        all_c.append(c)
        
    all_d = calcula_inversos(all_c, mods)
    
    total_sum = 0
    for i in range(len(nums)):
        total_sum+= nums[i] * all_c[i] * all_d[i]
        
    print(f"{int(total_sum%M)}=mod{M}")

main()                