import dde_client as ddec

columns = ['DATE', 'TIME', 'BID', 'ASK']

QUOTE_client = ddec.DDEClient('MT4', 'QUOTE')
QUOTE_client.advise("BTCUSD")


response = QUOTE_client.request("BTCUSD")

if response is not None : 
    datum = response.split()
    
    
    print '         '.join(columns)
    print '   '.join(datum)
