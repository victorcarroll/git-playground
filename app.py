from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/') #redirect root to the url or route mapped to the index function
def root():
    return redirect(url_for('index'))

@app.route('/items', methods = ["GET", "POST", "PUT"])
def index():
    if request.method == 'POST':
        new_item = session.add_item(request.form['Title'])  ## Title is the name used in new.html
##      session._DEFAULT_ITEMS.append(new_item) #append to list instead calling session
        return redirect(url_for('index'))
### tried using PUT doesnt save input from form :(
    elif request.method == 'PUT':
        found_id = session.get_item(id)
        passed_id = request.form['Id']
        updated_status = request.form['Status_update']
        a = session.get_item(found_id)
        item = {'id': passed_id, 'status': updated_status, 'title': a['title']}
        update_item = session.save_item(item['id'])
        return redirect(url_for('index'))
    return render_template('index.html', Items=session.get_items())

@app.route('/items/new')
def new():
    return render_template('new.html')

@app.route('/GetItem/<id>') ## Trying to update the item
def show(id):
    found_id = session.get_item(id)
    return render_template('show.html', Items=found_id)   ##Items=found_id is to pass found_id to the variable called Items

@app.route('/GetItem/<id>/delete')
def delete(id):
    found_id = session.get_item(id)
    print(found_id, type(found_id))
    item = session.delete_item(found_id['id'])
    return redirect(url_for('index'))

@app.route('/GetItem/<id>/update', methods = ["GET", "POST"])
def update(id):
    found_id = session.get_item(id)
    return render_template('update.html', Items=found_id)

##FIXED BELOW. THANKS!

@app.route('/items/updated', methods = ["GET", "POST"])
def updated():
    if request.method == 'POST':
        passed_id = int(request.form['Id'])
        updated_status = request.form['Status_update']
        a = session.get_item(passed_id)
        item = {'id': passed_id, 'status': updated_status, 'title': a['title']}
        update_item = session.save_item(item)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

