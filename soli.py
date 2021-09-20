evrvaring = int(input('hoeveel jaren praktijkervaring heb je? '))
diploma   = input('wat is je hoogtse diploma? ')
hoed      = input('heb jij een grote hoed? ')
geslacht  = input('ben je een man of een voruw? ')
if geslacht =='man': 
    snor = int(input('hoe breed is jou snor in cm? '))
else :
    haar = input('heb je roodkrul haar dat  langer is dan 20cm ? ')   
lengte   = float(input('hoelang ben jij in cm ? '))
gewicht  = float(input('hoeveel weeg je in kilogram? '))
certifi  = input('heb je een certificaat van overleven met gevaarlijke personeel? ')



if evrvaring >=4 and (diploma == "mbo4" or diploma == "hbo" or diploma == 'uni' or diploma == 'universiteit') and hoed == "ja" and (snor >=10 or haar=='ja') and lengte >=150 and gewicht >=90 and certifi =="ja":
    print('jij voeldoet aan de eisen, we nemen zo snel mogelijk contact met je op. ')
else :
    print('jij voeldoet heelaas niet aan onze stricte eisen, dus je kan bij ons heelaas niet werken. ')
    


     
