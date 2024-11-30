from flask import render_template ,url_for,flash,redirect,request
from Foodimg2Ing import app
from Foodimg2Ing.output import output
import os


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/', methods=['POST', 'GET'])
def predict():
    # Get the uploaded file
    imagefile = request.files['imagefile']
    
    # Define the directory where the image will be saved
    upload_folder = os.path.join(app.root_path, 'static', 'images', 'demo_imgs')
    
    # Create the directory if it doesn't exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder, exist_ok=True)
    
    # Define the image path
    image_path = os.path.join(upload_folder, imagefile.filename)
    
    # Save the uploaded image
    imagefile.save(image_path)
    
    # Generate the image URL
    img = "/images/demo_imgs/" + imagefile.filename
    
    # Process the image (your model output logic)
    title, ingredients, recipe = output(image_path)
    
    # Return the result in the template
    return render_template('predict.html', title=title, ingredients=ingredients, recipe=recipe, img=img)


@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile=os.path.join(app.root_path,'static\\images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title,ingredients,recipe = output(imagefile)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)