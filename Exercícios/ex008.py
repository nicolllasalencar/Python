#converta a uma medida de metros para outras
M = float(input('Uma distacia em metros:'))
km = M/1000
hm = M/100
dam = M/10
dm = M*10
cm = M*100
mm = M*1000
print('a medidada de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(M,km,hm,dam,dm,cm,mm))