import random

def push(pila, elemento):
    if len(pila)==0:
        return None
    else:
        return pila.append(elemento)
    
def pop(pila):
    if len(pila)==0:
        return None
    else:
        return pila.pop()

def main():
    parentesi_aperte=["{", "[", "("]
    parentesi_chiuse=["}", "]", ")"]
    dizionario={"{":"}", "[":"]", "(":")"}
    stringa="[{1+[2+3]*5}"
    pila= []
    errore=False
    pos=-1
    for carattere in stringa:
        pos+=1
        if carattere in parentesi_aperte:
            parentesi=push(pila, carattere)
            if parentesi!=None:
                if dizionario[parentesi]!=carattere:
                    errore=True
                    break
            else:
                errore=True
                break
        if carattere in parentesi_chiuse:
            parentesi=pop(pila)
            if parentesi!=None:
                if dizionario[parentesi]!=carattere:
                    errore=True
                    break
            else:
                errore=True
                break
    if errore:
        print(f"Errore! in posizione {pos}")
    else:
        print("corretto")   
            
                   
    
if __name__=="__main__":
    main()