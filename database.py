from sqlalchemy import create_engine, text

db_connection_strign = 'mysql+pymysql://05cbizdhu0xgsma7jpan:pscale_pw_rSoUH2g7mou1wPobtGlHcBvsqjfwl4ZOw7BNbMbNEQA@aws.connect.psdb.cloud/testcreate?charset=utf8mb4'
# Create a database engine for ssl
 
engine = create_engine(db_connection_strign,
                       connect_args={"ssl": {
                         "ss_ca": "/etc/ssl/cert.pem"
                       }})
 
# Create MySQL connection just for trying
#==========================================                       
#the functions of with is help you to connection with db  that and exit connetion done.
#the conn is just name_variable , this will help you to execut this commands in database  "select * from  you table"
#with engine.connect() as conn:
 # result = conn.execute(text("select * from products"))
  #print(result.all())
# Create MySQL connection to sing up 
#===============================================================
conn = engine.connect()
#db = SQLAlchemy(app)

#class products(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(50))
   # price = db.Column(db.Float)
    #images = db.Column(db.String(100))
        # Execute SQL query
#result = conn.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
