hostname= '157.230.209.171'
username = 'noether_2032'
password = '7oEURIsR0mCmX3FvB24xnUPeGjCDGctQ'


def get_connection(db, user=username, host=hostname, password= password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
def get_db_url(username, password, hostname, db):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db}'
url = get_db_url(username, password, hostname, db = 'telco_churn')