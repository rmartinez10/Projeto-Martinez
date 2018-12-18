print('hello world...BBBannn')

Valprest = 143.73
Qtdprest = 1

#-------------------------------------------------------------------------
print('----------------------------------------------------------------')
print('--------------------<<<    I N I C I O    >>>-------------------')
print('----------------------------------------------------------------')
print('vou entrar no if...')
while Qtdprest < 24:
   ValSemJ = Valprest + ValsemJ
   Valtotal = Valprest * Qtdprest   
   print ('Parcela: ', Qtdprest, 'custa: ',round(Valprest,2),'TOTAL PAGO: ', round(Valtotal,2) )
   Valprest = Valprest + (Valprest * 0.073)
   Qtdprest = Qtdprest + 1
#print.format(Qtdprest,2)
#elif Qtdprest > 24:
else:
    print ('---------------------------------------'            )
    print ('-----<<    E X T R A T O    >>>--------'            )
    print ('---------------------------------------'            )
    print ('quantidade de parcelas.......: ', Qtdprest          )
    print ('valor da ultima prestacao....: ', round(Valprest,2) )
    print ('total sem juros..............: ', round(ValSemJ, 2) )
    print ('total com juros..............: ', round(Valtotal,2) )
    print ('---------------------------------------'            )
