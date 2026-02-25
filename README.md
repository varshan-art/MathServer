# Ex.04 Design a Website for Server Side Processing
## Date:25-02-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
gst.html

<html>
    <head>
        <title>GST Bill Calculator</title>
        <style>
        .box {
            width:500px;
            height:300px;
            border:dashed 3px blueviolet;
            padding:10px;
            position:fixed;
            top:190px;
            left:750px;
            text-align:center;
            background-color:greenyellow;
            }
        </style>
    </head>
    <body bgcolor="lightyellow">
        <div class="box">
            <h1>Total Bill Amount</h1>
            <h3>SRI VIJAY VARSHAN.G[25008956]</h3>
            <form method="POST">
                {% csrf_token %}
        <div>
            <label>Price(₹)</label>
            <input type="text" name="price" required>
        </div>
        <br>
        <div>
            <label>GST(%)</label>
            <input type="text" name="gst" required>
        </div>
        <br>
        <div>
            <input type="submit" value="Calculate">
        </div>
        <br>
        <div>
            <label>Total Bill (₹)</label>
            <input type="text" value="{{bill}}">
        </div>
            </form>
        </div>
    </body>
</html>

views.py

from django.shortcuts import render

def gst_bill(request):

    p = float(request.POST.get('price', '0'))
    g = float(request.POST.get('gst', '0'))

    bill = p + (p * g / 100) if request.method == 'POST' else 0

    print("price =", p)
    print("gst =", g)
    print("total bill =", bill)

    return render(request, 'serverapp/gst.html',
                  {'p': p, 'g': g, 'bill': bill})

urls.py

from django.contrib import admin
from django.urls import path
from serverapp import views

urlpatterns = [
    path('', views.gst_bill, name='gst_bill'),
]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-02-25 131517.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-02-25 130546.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
