from sqlalchemy import create_engine

tushare_db = create_engine('postgresql+pg8000://earthson@localhost/trading_tushare', pool_size=128, max_overflow=0)