from flask import Flask,render_template
import requests,json
app= Flask(__name__)

# Api Key
api_key ="ac48a1607d4d402:b7pe75pech23c6q"

# Get data from API
url = f'https://api.tradingeconomics.com/search/sweden?category=markets&c={api_key}'
data = requests.get(url).json()
# print(data)

# print first list
# first = data[0]
# second = data[1]
# # second_first_category = first[0]['Symbol']
# print(first['Name'])
# print(second_first_category)

# print(first)
# print(data)


@app.route("/")
def display_data_from_API():

    return render_template("table.html",data=data)

if __name__ == '__main__':
    app.run(debug=True)