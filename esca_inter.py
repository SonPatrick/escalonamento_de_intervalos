def escalona(s, f):
    #------------------Atributo das Atividades---------------------
    #tempo de inicio
    s = s
    #tempo de fim
    f = f
    #-------------------------------------------------------------

    #-----------------Atividades válidas--------------------------
    valida_s = []
    valida_f = []
    #-------------------------------------------------------------
    n = len(s)
    pivot_s = 0
    pivot_f = f[0]

    #-----------------Define a primeira atividade---------------------
    for i in range(n):
        if f[i] < pivot_f:
            pivot_s = s[i]
            pivot_f = f[i]
    #----------------------------------------------------------------

    #------------------insere na lista da atividades a primeira atividade-------------------------
    valida_s.append(pivot_s)
    valida_f.append(pivot_f)
    #--------------------------------------------------------------------------------------------
    j = 0 #contador
    #-------------------Organiza as atividades------------------------
    for i in range(0, n, 1):
        if s[i] >= valida_f[j]:
            valida_s.append(s[i])
            valida_f.append(f[i])
            j += 1
    #---------------------------------------------------------------
    print(valida_s)
    print(valida_f)
    return 0