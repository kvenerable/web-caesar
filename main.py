from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']= True 



form = """ <!doctype html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans- serif;
                border-radius: 10px;
    
            }}
            textarea{{
                margin:10px 0;
                width: 100%;
                height: 120px;
    
            }}
        </style>
    </head>
   <body>
   <form method ='POST'>

   <div>
   <label for ="rotate-by">Rotate by:</label>
   </div>

   <div>
   <input type="text" name ="rot" value ="0"/>
   </div>

   <div>
   <textarea name="text">{0}</textarea>
   </div>

   <div>
   <input type ="submit" value = "Submit Query"/>
   </div>

   </form>
   </body> 
</html>   

"""




@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])  
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypt_txt = rotate_string(text, rot)


    return form.format(encrypt_txt) 


app.run()
