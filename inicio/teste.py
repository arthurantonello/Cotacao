import pandas_market_calendars as mcal
import datetime

nyse = mcal.get_calendar('NYSE')
hoje = datetime.date.today()
hoje_str = hoje.isoformat()
abertura_bolsa = nyse.schedule(start_date= hoje_str, end_date= hoje_str)
bolsa_hoje = abertura_bolsa.index.date



print(bolsa_hoje)