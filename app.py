from flask import Flask, render_template, request, redirect, url_for, flash
from prolog import PrologLogic

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
p = PrologLogic()

@app.route('/')
def index():
    p.retract_all_query('chosen_meal(X)')
    p.retract_all_query('chosen_bread(X)')
    p.retract_all_query('chosen_main(X)')
    p.retract_all_query('chosen_veggie(X)')
    p.retract_all_query('chosen_sauce(X)')
    p.retract_all_query('chosen_topup(X)')
    p.retract_all_query('chosen_side(X)')
    p.retract_all_query('chosen_drink(X)')

    return render_template('index.html', title="intro")

@app.route('/step-1', methods=['GET', 'POST'])
def step1():
    meals = p.get_query("ask_meal(X)")[0].get('X')
    quest = "Please Choose your Meal."

    if request.method == 'POST':
        if request.values.get("back"):
            return redirect(url_for('index'))
        elif request.values.get("submit"):
            choice = request.values.get("group")
            if choice is None:
                flash("Please make a Choice.", 'warning')
            else:
                p.assert_query('chosen_meal('+choice+')')
                return redirect(url_for('step2'))

    return render_template('radioForm.html', title="intro", radio=meals, question=quest)

@app.route('/step-2', methods=['GET', 'POST'])
def step2():
    breads = p.get_query("ask_bread(X)")[0].get('X')
    quest = "Please Choose your Bread."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_meal(X)')
            return redirect(url_for('step1'))
        elif request.values.get("submit"):
            choice = request.values.get("group")
            if choice is None:
                flash("Please make a Choice.", 'warning')
            else:
                p.assert_query('chosen_bread('+choice+')')
                return redirect(url_for('step3'))

    return render_template('radioForm.html', title="intro", radio=breads, question=quest)

@app.route('/step-3', methods=['GET', 'POST'])
def step3():
    mains = p.get_query("ask_mains(X)")[0].get('X')
    quest = "Please Choose your Main."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_bread(X)')
            return redirect(url_for('step2'))
        elif request.values.get("submit"):
            choice = request.values.get("group")
            if choice is None:
                flash("Please make a Choice.", 'warning')
            else:
                p.assert_query('chosen_main('+choice+')')
                return redirect(url_for('step4'))

    return render_template('radioForm.html', title="intro", radio=mains, question=quest)

@app.route('/step-4', methods=['GET', 'POST'])
def step4():
    veggies = p.get_query("ask_veggie(X)")[0].get('X')
    quest = "Please Choose your Veggies."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_main(X)')
            return redirect(url_for('step3'))
        elif request.values.get("submit"):
            choice = request.form.getlist("group")
            if len(choice) == 0:
                flash("Please make a Choice.", 'warning')
            else:
                for val in choice:
                    p.assert_query('chosen_veggie('+val+')')

                return redirect(url_for('step5'))

    return render_template('checkboxesForm.html', title="intro", radio=veggies, question=quest)


@app.route('/step-5', methods=['GET', 'POST'])
def step5():
    topups = p.get_query("ask_topup(X)")
    if(len(topups) == 0):
        print("value meal has no top up")
        return redirect(url_for('step6'))

    topups = topups[0].get('X')
    quest = "Please Choose your Top-ups."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_veggie(X)')
            return redirect(url_for('step4'))
        elif request.values.get("submit"):
            choice = request.form.getlist("group")
            if len(choice) == 0:
                flash("Please make a Choice.", 'warning')
            else:
                for val in choice:
                    p.assert_query('chosen_topup(' + val + ')')

                return redirect(url_for('step6'))

    return render_template('checkboxesForm.html', title="intro", radio=topups, question=quest)


@app.route('/step-6', methods=['GET', 'POST'])
def step6():
    sauces = p.get_query("ask_sauces(X)")[0].get('X')

    quest = "Please Choose your Sauces."

    if request.method == 'POST':
        if request.values.get("back"):
            topups = p.get_query("ask_topup(X)")
            if (len(topups) == 0):
                print("value meal has no top up")
                p.retract_all_query('chosen_veggie(X)')
                return redirect(url_for('step4'))
            else:
                p.retract_all_query('chosen_topup(X)')
                return redirect(url_for('step5'))
        elif request.values.get("submit"):
            choice = request.form.getlist("group")
            if len(choice) == 0:
                flash("Please make a Choice.", 'warning')
            else:
                for val in choice:
                    p.assert_query('chosen_sauce(' + val + ')')

                return redirect(url_for('step7'))

    return render_template('checkboxesForm.html', title="intro", radio=sauces, question=quest)

@app.route('/step-7', methods=['GET', 'POST'])
def step7():
    sides = p.get_query("ask_sides(X)")[0].get('X')

    quest = "Please Choose your Sides."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_sauce(X)')
            return redirect(url_for('step6'))
        elif request.values.get("submit"):
            choice = request.values.get("group")
            if choice is None:
                flash("Please make a Choice.", 'warning')
            else:
                p.assert_query('chosen_side(' + choice + ')')
                return redirect(url_for('step8'))

    return render_template('radioForm.html', title="intro", radio=sides, question=quest)

@app.route('/step-8', methods=['GET', 'POST'])
def step8():
    drinks = p.get_query("ask_drinks(X)")[0].get('X')
    quest = "Please choose your drinks."

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_side(X)')
            return redirect(url_for('step7'))
        elif request.values.get("submit"):
            choice = request.values.get("group")
            if choice is None:
                flash("Please make a Choice.", 'warning')
            else:
                p.assert_query('chosen_drink('+choice+')')
                return redirect(url_for('step9'))

    return render_template('radioForm.html', title="intro", radio=drinks, question=quest)

@app.route('/step-9', methods=['GET', 'POST'])
def step9():

    # p.assert_query('chosen_meal(value)')
    # p.assert_query('chosen_bread(parmesan)')
    # p.assert_query('chosen_main(chicken_bacon_ranch)')
    # p.assert_query('chosen_veggie(cucumbers)')
    # p.assert_query('chosen_veggie(tomatoes)')
    # p.assert_query('chosen_sauce(honey_mustard)')
    # p.assert_query('chosen_topup(avocado)')
    # p.assert_query('chosen_side(cookies)')
    # p.assert_query('chosen_drink(water)')

    choices_arr = []

    meal = {'header': 'Choice of Meal', 'value': p.get_query("show_meals(X)")[0].get('X')}
    bread = {'header': 'Choice of Bread', 'value': p.get_query("show_breads(X)")[0].get('X')}
    veggies = {'header': 'Choices of veggies', 'value': p.get_query("show_veggies(X)")[0].get('X')}
    sauces = {'header': 'Choices of Sauces', 'value': p.get_query("show_sauces(X)")[0].get('X')}
    topups = {'header': 'Choices of Top-ups', 'value': p.get_query("show_topups(X)")[0].get('X')}
    sides = {'header': 'Choices of Sides', 'value': p.get_query("show_sides(X)")[0].get('X')}
    drinks = {'header': 'Choice of drink', 'value': p.get_query("show_drinks(X)")[0].get('X')}

    choices_arr.append(meal)
    choices_arr.append(bread)
    choices_arr.append(veggies)
    choices_arr.append(sauces)
    choices_arr.append(topups)
    choices_arr.append(sides)
    choices_arr.append(drinks)

    # for choices in choices_arr:
    #     print(choices["header"])
    #     print(choices["value"])

    if request.method == 'POST':
        if request.values.get("back"):
            p.retract_all_query('chosen_drink(X)')
            return redirect(url_for('step8'))
        elif request.values.get("submit"):
            return redirect(url_for('index'))


    return render_template('summaryReport.html', title="intro", summary=choices_arr)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)