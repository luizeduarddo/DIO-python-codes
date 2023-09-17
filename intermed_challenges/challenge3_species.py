group = input() 
class_animal = input() 
niche = input() 

if group == 'vertebrado':
    if class_animal == 'ave':
        if niche == 'carnivoro':
            print('aguia')
        elif niche == 'onivoro':
            print('pomba')
    elif class_animal =='mamifero':
        if niche == 'onivoro':
            print('homem')
        elif niche == 'herbivoro':
            print('vaca')
elif group == 'invertebrado':
    if class_animal == 'inseto':
        if niche == 'hematofago':
            print('pulga')
        elif niche == 'herbivoro':
            print('lagarta')
    elif class_animal == 'anelideo':
        if niche == 'hematofago':
            print('sanguessuga')
        elif niche == 'onivoro':
            print('minhoca')

            
