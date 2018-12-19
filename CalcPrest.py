print('hello world...BBBannn')

Valprest = 143.73
ValSemJ  = 0
Qtdprest = 1
ValJuros = 0.0073

from datetime import date
Dataatu = date.today()
Datatexto = '{}/{}/{}'.format(Dataatu.day,Dataatu.month,Dataatu.year)

#-------------------------------------------------------------------------
print('----------------------------------------------------------------')
print('--------------------<<<    I N I C I O    >>>-------------------')
print('----------------------------------------------------------------')
print('vou entrar no if...')
Valprim = Valprest
while Qtdprest < 24:
   ValSemJ = ValSemJ + Valprest
   Valtotal = Valprest * Qtdprest   
   print ('Parcela: ', Qtdprest, 'custa: ',round(Valprest,2),'TOTAL PAGO: ', round(Valtotal,2) )
   Valprest = Valprest + (Valprest * ValJuros)
   Qtdprest = Qtdprest + 1
#print.format(Qtdprest,2)
#elif Qtdprest > 24:
else:
    Totjuros = Valtotal - ValSemJ
    print ('---------------------------------------'            )
    print ('-----<<    E X T R A T O    >>>--------'            )
    print ('---------------------------------------'            )
    print ('data.........................: ', Datatexto         )
    print ('Taxa de juros................: ', ValJuros          )
    print ('quantidade de parcelas.......: ', Qtdprest          )
    print ('---------------------------------------'            )
    print ('valor da primeira prestacao..: ', round(Valprim,2 ) )
    print ('valor da ultima prestacao....: ', round(Valprest,2) )
    print ('---------------------------------------'            )
    print ('total sem juros..............: ', round(ValSemJ, 2) )
    print ('total com juros..............: ', round(Valtotal,2) )
    print ('total de juros pago..........: ', round(Valtotal,2) )
    print ('---------------------------------------'            ) 
