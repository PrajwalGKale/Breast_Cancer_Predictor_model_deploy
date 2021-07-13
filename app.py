from flask import Flask
from flask import render_template
from flask import request
import breast_cancer_file as model
import os

app = Flask(__name__,template_folder='templates')

picFolder = os.path.join('static')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def data():
    img = os.path.join(app.config['UPLOAD_FOLDER'],'BgImg.jpg')
    fav = os.path.join(app.config['UPLOAD_FOLDER'],'favicon.png')
    return render_template("index.html",bg = img,favicon =fav)

@app.route("/second")
def second():
    img = os.path.join(app.config['UPLOAD_FOLDER'],'BgImg.jpg')
    fav = os.path.join(app.config['UPLOAD_FOLDER'],'favicon.png')
    return render_template("prediction.html",bg=img,favicon =fav)

@app.route("/third")
def third():
    p = os.path.join(app.config['UPLOAD_FOLDER'],'py.png')
    s = os.path.join(app.config['UPLOAD_FOLDER'],'1200px-Scikit_learn_logo_small.svg.png')
    f = os.path.join(app.config['UPLOAD_FOLDER'],'flask-removebg-preview.png')
    fav = os.path.join(app.config['UPLOAD_FOLDER'],'favicon.png')
    return render_template("aboutme.html",sci = s,flaski =f,py =p,favicon =fav)

@app.route("/submit",methods = ['POST'])
def submit():
    #html -> .py
    if request.method == "POST":
        radius_m = request.form["radius_mean"]
        texture_mean = request.form["texture_mean"]
        perimeter_mean	= request.form["perimeter_mean"]
        area_mean = request.form["area_mean"]
        smoothness_mean	= request.form["smoothness_mean"]
        compactness_mean = request.form["compactness_mean"]
        concavity_mean = request.form["concavity_mean"]
        concave_points_mean	 = request.form["concave_points_mean"]
        symmetry_mean	= request.form["symmetry_mean"]
        fractal_dimension_mean= request.form["fractal_dimension_mean"]
        radius_se	 = request.form["radius_se"]
        texture_se	 = request.form["texture_se"]    
        perimeter_se= request.form["perimeter_se"]	  
        area_se	   = request.form["area_se"]
        smoothness_se= request.form["smoothness_se"]
        compactness_se	= request.form["compactness_se"]
        concavity_se	= request.form["concavity_se"]
        concave_points_se= request.form["concave_points_se"]
        symmetry_se	= request.form["symmetry_se"]
        fractal_dimension_se = request.form["fractal_dimension_se"]	 
        radius_worst = request.form["radius_worst"]
        texture_worst = request.form["texture_worst"]	
        perimeter_worst	= request.form["perimeter_worst"]
        area_worst	= request.form["area_worst"]
        smoothness_worst= request.form["smoothness_worst"]	
        compactness_worst = request.form["compactness_worst"]
        concavity_worst = request.form["concavity_worst"]
        concave_points_worst= request.form["concave_points_worst"]
        symmetry_worst = request.form["symmetry_worst"]	
        fractal_dimension_worst  = request.form["fractal_dimension_worst"]	
        prediction_cancer = model.breast_cancer_model_deployment(
        radius_m,
        texture_mean,
        perimeter_mean,
        area_mean,
        smoothness_mean,
        compactness_mean,
        concavity_mean,
        concave_points_mean,
        symmetry_mean,
        fractal_dimension_mean,
        radius_se,
        texture_se,    
        perimeter_se,
        area_se,
        smoothness_se,
        compactness_se,
        concavity_se,
        concave_points_se,
        symmetry_se,
        fractal_dimension_se,
        radius_worst,
        texture_worst,
        perimeter_worst,
        area_worst,
        smoothness_worst,	
        compactness_worst,
        concavity_worst,
        concave_points_worst,
        symmetry_worst,
        fractal_dimension_worst
        )
        print("printing the real value of cancer")
        print(prediction_cancer)
        # res = np.round(accuracy_score(y_test,prediction_cancer)*100,2)
        fav = os.path.join(app.config['UPLOAD_FOLDER'],'favicon.png')
        if prediction_cancer == 1:
            img = os.path.join(app.config['UPLOAD_FOLDER'],'Malignant.png')
        elif prediction_cancer == 0:
            img = os.path.join(app.config['UPLOAD_FOLDER'],'Benign.jpg')
    Bimg = os.path.join(app.config['UPLOAD_FOLDER'],'BgImg.jpg')
    #.py -> html
    return render_template("submit.html",pred = prediction_cancer,cancer_img = img,bg = Bimg)

if __name__ == "__main__":
    app.debug = True
    app.run()
