###Version 3 du calculateur d'IP // Avril 2016 ###
Obool=True
while Obool :
    vMo=255
    ipt=input('Veuillez entrer votre adresse IPV4 \n')
    ip=ipt.split(".")

    pO=int(ip[0])
    dO=int(ip[1])
    tO=int(ip[2])
    qO=int(ip[3])

    def po():
        if pO>=224 and pO<=255:
            print("\nLes adresses commençant par ", pO, \
    " ne sont pas couramment utilisées")
        elif pO<0 or pO>255 :
            print("\nLa valeur entrée pour le PREMIER octet n'est PAS valable")


    def po_class():
        po()
        if pO>=0 and pO<=127:
            print("C'est une adresse de classe A")
        elif pO>=128 and pO<=191:
            print("C'est une adresse de classe B")
        elif pO>=192 and pO<=223:
            print("C'est une adresse de classe C")


    def do_class():
        if dO<0 or dO>255 :
            print("\nLa valeur entrée pour le DEUXIÈME octet n'est PAS valable")


    def to_class():
        if tO<0 or tO>255 :
            print("\nLa valeur entrée pour le TROISIÈME octet n'est PAS valable")


    def qo_class():
        if qO<0 or qO>255 :
            print("\nLa valeur entrée pour le QUATRIÈME octet n'est PAS valable")

    po_class()
    while pO >255 is not True or pO <0 is not True :
        pO=int(input("Entrez à nouveau le premier octet de votre adresse IPV4\n"))
        po_class()

    do_class()
    while dO >255 is not True or dO <0 is not True:
        
        dO=int(input("Entrez à nouveau le deuxième octet de votre adresse IPV4\n"))
        do_class()

    to_class()
    while tO >255 is not True or tO <0 is not True:
        
        tO=int(input("Entrez à nouveau le troisième octet de votre adresse IPV4\n"))
        to_class()

    qo_class()
    while qO >255 is not True or qO <0 is not True:
        
        qO=int(input("Entrez à nouveau le dernier octet de votre adresse IPV4\n"))
        qo_class()

    vbR=vMo-qO  #Pour le broadcast /24
    vBr=vMo-tO  #Pour le broadcast /16
    Vbr=vMo-dO  #Pour le broadcast /8
    #Bien entendu il faut utiliser les 3 pour le broadcast /8
    
    pObin8=pO%2
    pObin7=int((pO/2)%2)
    pObin6=int((pO/2**2)%2)
    pObin5=int((pO/2**3)%2)
    pObin4=int((pO/2**4)%2)
    pObin3=int((pO/2**5)%2)
    pObin2=int((pO/2**6)%2)
    pObin1=int((pO/2**7)%2)
    pObinL=str(pObin1), str(pObin2), str(pObin3), str(pObin4), str(pObin5), str(pObin6), str(pObin7), str(pObin8)
    pObinT="".join(pObinL)
    pObinlist=[int(pObin1*2**7), int(pObin2*2**6), int(pObin3*2**5), int(pObin4*2**4), int(pObin5*2**3), int(pObin6*2**2), int(pObin7*2**1), int(pObin8*2**0)]



    dObin8=dO%2
    dObin7=int((dO/2)%2)
    dObin6=int((dO/2**2)%2)
    dObin5=int((dO/2**3)%2)
    dObin4=int((dO/2**4)%2)
    dObin3=int((dO/2**5)%2)
    dObin2=int((dO/2**6)%2)
    dObin1=int((dO/2**7)%2)
    dObinL=str(dObin1), str(dObin2), str(dObin3), str(dObin4), str(dObin5), str(dObin6), str(dObin7), str(dObin8)
    dObinT="".join(dObinL)
    dObinlist=[int(dObin1*2**7), int(dObin2*2**6), int(dObin3*2**5), int(dObin4*2**4), int(dObin5*2**3), int(dObin6*2**2), int(dObin7*2**1), int(dObin8*2**0)]


    tObin8=tO%2
    tObin7=int((tO/2)%2)
    tObin6=int((tO/2**2)%2)
    tObin5=int((tO/2**3)%2)
    tObin4=int((tO/2**4)%2)
    tObin3=int((tO/2**5)%2)
    tObin2=int((tO/2**6)%2)
    tObin1=int((tO/2**7)%2)
    tObinL=str(tObin1), str(tObin2), str(tObin3), str(tObin4), str(tObin5), str(tObin6), str(tObin7), str(tObin8)
    tObinT="".join(tObinL)
    tObinlist=[int(tObin1*2**7), int(tObin2*2**6), int(tObin3*2**5), int(tObin4*2**4), int(tObin5*2**3), int(tObin6*2**2), int(tObin7*2**1), int(tObin8*2**0)]


    qObin8=qO%2
    qObin7=int((qO/2)%2)
    qObin6=int((qO/2**2)%2)
    qObin5=int((qO/2**3)%2)
    qObin4=int((qO/2**4)%2)
    qObin3=int((qO/2**5)%2)
    qObin2=int((qO/2**6)%2)
    qObin1=int((qO/2**7)%2)
    qObinL=str(qObin1), str(qObin2), str(qObin3), str(qObin4), str(qObin5), str(qObin6), str(qObin7), str(qObin8)
    qObinT="".join(qObinL)
    qObinlist=[int(qObin1*2**7), int(qObin2*2**6), int(qObin3*2**5), int(qObin4*2**4), int(qObin5*2**3), int(qObin6*2**2), int(qObin7*2**1), int(qObin8*2**0)]

        
    print("\n\nVotre adresse IP est "), print(pO, dO, tO, qO, sep=".")
    if pO==255 and dO==255 and tO==255 and qO==255:
        print('L\'envoi de requêtes planétaire n\'est pas autorisé')

    mT=int(input("\nVeuillez entrer votre masque en format CIDR (sans mettre le /)""\n /"))


    nppO=(8-mT)-1

    npdO=(16-mT)-1

    nptO=(24-mT)-1

    npqO=(32-mT)-1



    def mT_class():
        mT=int(input("\nVeuillez entrer votre masque en format CIDR (sans mettre le /)""\n /"))
       

    while mT<1 or mT>31:            
            print("Notation non valable, la valeur doit être comprise entre 1 et 31")
            mT=int(input("\nVeuillez entrer votre masque en format CIDR (sans mettre le /)""\n /"))
            nppO=(8-mT)-1
            npdO=(16-mT)-1
            nptO=(24-mT)-1
            npqO=(32-mT)-1




    print("\nSous forme binaire votre adresse IP équivaut à :\n" \
          + pObinT + "." + dObinT+"." + tObinT +"." + qObinT+"\n")
            
    if mT<=7 :
        for nmpO in range(2**0,2**(nppO+1)):
            pass
        print("Votre adresse réseau est: " +(str(sum(pObinlist[0:mT])))+3*".0" + " /"+str(mT))
        print("Votre adresse broadcast est: " +str(sum(pObinlist[0:mT])+nmpO)+3*("." +str(vMo))+" /"+str(mT))
        

    if mT==8:
        if dO==255 and tO==255 and qO==255:
            print("Il s'agit de l'adresse de broadcast du réseau : " +str(pO) +3*".0" + " /" +str(mT))

        else:
            print("L'adresse de votre machine est :" + str(pO)+"." + str(dO)+"."+ str(tO)\
              +"."+str(qO)+" /" + str(mT))
            print("Votre adresse réseau est :" +str(pO) +"." + str(dO-dO) +"." + str(tO-tO) \
              +"." + str(qO-qO)+" /" + str(mT))
            print("Votre adresse de Broadcast est :" +str(pO) +"." + str(Vbr+dO) +"." + str(vBr+tO) \
              +"." + str(vbR+qO)+" /"+ str(mT))

    if mT>8 and mT<=15 :
        for nmdO in range(2**0,2**(npdO+1)):
            pass
        print("Votre adresse réseau est: " +str(pO)+"." +str(sum(dObinlist[0:mT-8]))+2*".0" + " /"+str(mT))
        print("Votre adresse broadcast est: "+str(pO)+"." +str(sum(dObinlist[0:mT-8])+nmdO)+2*("." +str(vMo))+" /"+str(mT))
        print(nmdO)


    if mT==16:
        if tO==255 and qO==255:
            print("Il s'agit de l'adresse de broadcast du réseau : "  +str(pO) +"." + str(dO) + 2*".0" + " /" +str(mT))

        elif tO==0 and qO==0:
            print("Il s'agit d'une adresse réseau")
            print("Votre adresse de Broadcast est :" +str(pO) +"." + str(dO) + 2*("."+(str(vMo))) \
             + " /" + str(mT))

        else:
            print("L'adresse de votre machine est :" + str(pO)+"." + str(dO)+"."+ str(tO)\
              +"."+str(qO)+" /" + str(mT))
            print("Votre adresse réseau est :" +str(pO) +"." + str(dO) +"." + str(tO-tO) \
              +"." + str(qO-qO)+" /" + str(mT))
            print("Votre adresse de Broadcast est :" +str(pO) +"." + str(dO) + 2*("."+(str(vMo))) \
             + " /" + str(mT))

    if mT>16 and mT<=23 :
        for nmtO in range(2**0,2**(nptO+1)):
            pass
        print("Votre adresse réseau est: " +str(pO)+"."+str(dO)+"." +str(sum(tObinlist[0:mT-16]))+1*".0" + " /"+str(mT))
        print("Votre adresse broadcast est: "+str(pO)+"."+str(dO)+"." +str(sum(tObinlist[0:mT-16])+nmtO)+1*("." +str(vMo))+" /"+str(mT))


    if mT==24:
        if qO==255:
            print("Il s'agit de l'adresse de broadcast du réseau : " +str(pO)+"." + str(dO)+"." + str(tO)+"." + "0 /24")
        elif qO==0:
            print("Il s'agit d'une adresse réseau")
            print("Votre adresse de Broadcast est :" +str(pO) +"." + str(dO) +"." + str(tO) \
              +"." + str(vbR+qO)+" /"+ str(mT))
        else:
            print("L'adresse de votre machine est :" + str(pO)+"." + str(dO)+"."+ str(tO)\
              +"."+str(qO)+" /" + str(mT))
            print("Votre adresse réseau est :" +str(pO) +"." + str(dO) +"." + str(tO) \
              +"." + str(qO-qO)+" /" + str(mT))
            print("Votre adresse de Broadcast est :" +str(pO) +"." + str(dO) +"." + str(tO) \
              +"." + str(vbR+qO)+" /"+ str(mT))

    if mT>24 and mT<=31 :
        for nmqO in range(2**0,2**(npqO+1)):
            pass
        print("Votre adresse réseau est: " +str(pO)+"."+str(dO)+"."+str(tO)+"." +str(sum(qObinlist[0:mT-24])) + " /"+str(mT))
        print("Votre adresse broadcast est: "+str(pO)+"."+str(dO)+"." + str(tO)+"." +str(sum(qObinlist[0:mT-24])+nmqO)+" /"+str(mT))

    print("\nVous avez : " +str((2**(32-mT)-2)) + " possibilités d'adressage dans ce réseau avec le masque /" + str(mT)+"\n" )



    reponse=input("\nVoulez-vous continuer ? O/N ?")
    if reponse == "O" or reponse == "o":
        Obool=True
    elif reponse == "N" or reponse == "n" or reponse !="O" or reponse !="o" :
        Obool=False

        



