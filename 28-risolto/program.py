
''' 
    Un modo comune di memorizzare tabelle e' come liste di dizionari. 
    Ogni riga della tabella corrisponde ad un dizionario le cui chiavi sono i nomi delle colonne della tabella.
    Questa collezione di dizionari e' poi memorizzata in una lista.
    Ad esempio la tabella
    
    nome  | anno | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

puo' essere memorizzata come 
[{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

'''


def es28(tabella, colonna, valore):
    ''' 
    Si implementi la funzione es28(tabella, colonna, valore) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    - un valore
    restituisce la  sottotabella che si ottiene eliminando dalla tabella la colonna 
    indicata e le righe che in quella colonna avevano valori diversi da valore.
    La tabella originaria non deve essere modificata e nella nuova tabella 
    le righe devono conservare il vecchio ordinamento.
    Ad esempio con  tabella = [{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                      {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]
    al termine di es28(dati, 'anno', 1981) verra' restituita la tabella
    [{'nome': 'Bruno','tel': 5558432}]
    '''
    
    tabella2 = [] #inizializzo una tabella vuota.
    
    for line in tabella: #per ogni riga della tabella...        
        
        if line[colonna] == valore: #...se il valore della colonna data è uguale al valore dato...          
            
            new_line = {} #...si crea una nuova riga vuota.            
            
            for a, b in line.items(): #itero per ogni chiave e valore della riga               
                
                if a != colonna: #e se la chiave è diversa dalla colonna data, allora si può aggiungere alla riga
                  new_line[a] = b            
            
            tabella2.append(new_line) #infine aggiungo la nuova riga creata alla tabella vuota
   
    return tabella2          

es28([{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},
                  {'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}], 'anno', 1981)
