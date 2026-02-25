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