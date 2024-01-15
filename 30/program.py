

def es30(fname1,fname2,fname3):
    ''' 
    Si implementi la funzione es30(fname1,fname2,fname3) prende in input l'indirizzo di tre file di testo.
    Il primo file di testo contiene un messaggio codificato dove ogni carattere e' stato 
    sostituito da un intero di tre cifre.
    Tutti i caratteri non numerici devono essere trasferiti come sono.
    Nel secondo file  e' possibile ritrovare le corrispondenze numeri-caratteri tra i numeri 
    del testo e il rispettivo carattere. 
    Piu' precisamente questo secondo file e' organizzato in righe,  in ciascuna riga sono 
    presenti un carattere  e un intero  di tre cifre  che gli corrisponde nel file di testo separati da almeno uno spazio.
    Numeri diversi possono far riferimento ad uno stesso carattere e non tutti i numeri che appaiono in fname1
    sono necessariamente presenti nel file di decodifica.
    La funzione es30 deve decodificare il messaggio presente nel primo file grazie 
    alle informazioni contenute nel secondo.
    I numeri non presenti nel secondo file vanno decodificati con il simbolo '?'.
    Il messaggio decodificato va poi salvato nel terzo file.
    La funzione infine restituisce il numero di caratteri decodificati con il valore '?' presenti nel file decodificato.
    Ad esempio se 
    - il file fname1 contiene il testo '991118991991345      103    091027003091103?'
    - il file fname2 contiene il testo 'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 '
    il testo decodificato da registrare in file3 sara': 'tutt? a n?nna?' e la funzione restituisce il numero 2.
    Potete assumere che i caratteri numerici appaiano sempre raggruppati in triplette.
    '''
    with open(fname1) as fr1:
        text = fr1.read()
        text_list = []
        for i in text.split():
            text_list.append(' ') 
            for j in range(0, len(i), 3):
                text_list.append(i[j:j+3])

    with open(fname2) as fr2:
        text2 = fr2.read().split('\n')

        translation = {}
        for i in text2:
            text_clean = i.strip()
            translation[text_clean[1::].strip()] = text_clean[0] 

    count = 0
    translated = []
    for i in text_list:
        if len(i) != 3:
            translated.append(i)
        if i not in translation.keys() and i != ' ' and len(i) == 3:
            translated.append('?')
            count += 1
        else:
            for key, value in translation.items():
                if i == key:
                    translated.append(value)
     
    with open(fname3, 'w') as fr3:
        fr3.write(''.join(translated).strip())
    
    return count
            
            



















