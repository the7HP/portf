from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# saving data in text file
def write_to_file(data):
 	with open ('databse.txt', mode='a') as databse:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		file = databse.write(f'\n{email},{subject},{message}')

# saving data in Excel file_sheet
def write_to_csv(data):
 	with open ('databse.txt', mode='a') as databse2:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		csv_writer = csv.writer(databse2, delimiter=",", newline="", quotechar='"', quoting=csv.QUOTE_MINIMAL)
 		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():	
    if request.method == "POST":
    	try:
	    	data = request.form.to_dict()
	    	write_to_csv(data)
	    	# submit krvi atle bija form ma redirect kare
	    	return redirect('/thankyou.html') 
    	except:
    		return 'data is not saved'
 
    else:
    	return 'not Done........Sorry'

