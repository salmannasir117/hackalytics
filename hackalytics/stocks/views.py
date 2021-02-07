from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3
from .models import *
import pickle
from django.conf import settings

# Create your views here.
# Demonstrate ability to display matplotlib graph as d3 graph on website
def test_plot(request):
    fig, ax = plt.subplots()
    temp = ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20, color='#ffffff')
    ax.spines['bottom'].set_color('#FF0000')
    ax.spines['top'].set_color('#FF0000') 
    ax.set_facecolor("#0b0c0e")
    return render(request, 'stocks/display_plot.html', {
        'plot': mpld3.fig_to_html(fig)
    })

# Handle the clicks of the checkboxes  
def handle_checkboxes(request):
    # create matplotlib variables
    fig = plt.figure()
    ax = fig.add_subplot(111)
    pkl = None
    y = {}

    # check if POST request occurred (submit button clicked)
    if request.POST:
        # iterate for all checkboxes
         for i in range(1, 10):
              string = 'option' + str(i)
              # check if checkbox clicked 
              if string in request.POST.getlist('checkbox'):
                   pkl = pickle.load(open("static/pickles/NotSuspicious" + str(i) + ".pkl", 'rb'))
                   x = pkl.DATE
                   # add to data dictionary
                   y['NotSus' + str(i)] = pkl.Predict

    # plot data
    for key in y:
         ax.plot(x, y[key])
    
    # display data
    return render(request, 'stocks/display_plot.html', {
        'plot': mpld3.fig_to_html(fig)
    })