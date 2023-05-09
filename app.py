from flask import Flask, render_template, url_for, request, redirect
from database import engine, conn , text 



app = Flask(__name__)

"""def load_data_from_db(product_type=None):
    with engine.connect() as conn:
        if product_type:
            query = text("SELECT * FROM products WHERE product_type = :product_type")
            result = conn.execute(query, {"product_type": product_type})
        else:
            query = text("SELECT * FROM products")
            result = conn.execute(query)

        print("SQL query: ", query)  # print the generated SQL query
        print("Result: ", result)  # print the result variable
        if result is not None:
           products = [dict(row) for row in result.fetchall()]
        else:
            products = []
        return products """


def load_data_from_db(product_type=None):
    with engine.connect() as conn:
        if product_type:
            query = text("SELECT * FROM products WHERE product_type = :product_type")
            result = conn.execute(query, {"product_type": product_type})
        else:
            query = text("SELECT * FROM products")
            result = conn.execute(query)

        if result is not None:
            products = []
            for row in result.fetchall():
                product = dict(id=row[0], price=row[1],name=row[2],description=row[3], image_url=row[4], product_type=row[5] )
                image_url = f"/static/assets/images/{product['image_url']}"
                product_url = f"/product/{product['id']}"  # URL for the single-product page
                product['image_url'] = image_url
                product['product_url'] = product_url
                products.append(product)
        else:
            products = []

        return products
    
@app.route("/")
def index():
  products_list = load_data_from_db()
  return render_template('/index.html', products = products_list )#inside this index.html when you load you load all the data in db  

@app.route("/about")
def about(): 
  return render_template('about.html')

@app.route("/products")
def products():
  products_list = load_data_from_db()
  return render_template('/products.html', products = products_list)

@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/single-product")
def view_product():
    return render_template('single-product.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  # Create MySQL connection
    if request.method == 'POST' :
      if 'signIn' in request.form:
        if 'email' in request.form and 'password' in request.form : #and 'username' in request.form
          # Get form data
          email = request.form.get('email')
          #username = request.form.get('username')
          password = request.form.get('password')
          conn = engine.connect()
          result = conn.execute(f"SELECT * FROM users WHERE  email = '{email}' AND password = '{password}'")
          user = result.fetchone()
          # Check if user exists
          if user:
            # User authenticated
              return 'User authenticated'
          else:
            # Authentication failed
             return 'Please Sing up '

          #   Render login form
        return render_template('login.html')
      elif 'signUp' in request.form:
            if 'username' in request.form and 'password' in request.form and 'email' in request.form :
                username = request.form.get('username')
                password = request.form.get('password')
                email = request.form.get('email')
                conn = engine.connect()
                # Check if user already exists
                check_user = conn.execute(text("SELECT COUNT(*) FROM users WHERE username=:username"), username=username)
                if check_user.fetchone()[0] > 0:
                    return 'User already exists'
                # Insert user information into database
                else:
                    create_user = conn.execute(text("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)"), username=username, password=password, email=email)
                    conn.close()
                    return 'User created'
        # Render login form
            return render_template('login.html')
    # Render sign up page
    return render_template('/login.html')

#@app.route("/login", methods=["POST", "GET"]) 
#def login():
  #if request.method == "POST":
   #   user = request.form["nm"]
   #   return redirect(url_for("user", usr=user))
  #else:
   #    return render_template('/login.html')
#@app.route("/")
#def user(usr):
 # return f"<h1>{usr}<h2>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) #this debug help to auto loade upade in code 
