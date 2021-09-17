kaas  input('is de kaas geel? ')

if kaas =='ja':
    vraag1 = input('zit er gaten in? ')
    if vraag1 =='ja':
          vraag2 = input('is de kaas bruin? ')
          if vraag2 =='ja': 
              print('dan is het een alberthein kaas. ')
    else: 
        vraag3 = input('zit er groene plekken op de kaas? ')
    
    if vraag3 == 'ja': print('dan is het een franse kaas ')

else: 
    vraag4= input('is de kaas wit? ') 
    if vraag4 == 'ja':      
        print('dan is het een lidl kaas ')
    else : 
        vraag5 = input('heeft de kaas een blaauwe verpaking? ')
    if vraag5 == 'ja':
        print('dan is het een jumbo kaas. ')