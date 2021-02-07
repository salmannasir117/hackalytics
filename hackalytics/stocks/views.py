from django.shortcuts import render
from .models import *
import pickle
from django.conf import settings
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
from bs4 import BeautifulSoup

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
    # Pickle mapping:
        # 1 -> traditional nominal 
        # 2 -> novel nominal
        # 3 -> expiremental nominal
        # 4 -> traditional converted
        # 5 -> novel converted
        # 6 -> expiremental converted
        # 7 -> traditional real
        # 8 -> novel real
        # 9 -> expiremental real
    fig = plt.figure()
    ax = fig.add_subplot(111)
    pkl = None
    x = None
    y = {}
    name = ["Nominal GDP (Raw) traditional", "Nominal GDP (Raw) novel", "Nominal GDP (Raw) experimental", "Nominal GDP (Converted) traditional", "Nominal GDP (Converted) novel", "Nominal GDP (Converted) experimental", "Real GDP traditional", "Real GDP novel", "Real GDP experimental"]
    # check if POST request occurred (submit button clicked)
    if request.POST:
        # iterate for all checkboxes
         for i in range(1, 10):
              string = 'option' + str(i)
              # check if checkbox clicked 
              if string in request.POST.getlist('checkbox'):
                   pkl = pickle.load(open("static/pickles/Pickle" + str(i) + ".pkl", 'rb'))
                   x = pkl.DATE
                   # add to data dictionary
                   y['Pickle' + str(i)] = [pkl.Predict, i, name[i - 1]]

    # plot data
    if y is not None and x is not None:
        fig = plots(x,y)    
    # html_string = mpld3.fig_to_html(fig) 
    # soup = BeautifulSoup(html_string, 'html.parser')
    # for text_tag in soup.findAll('text'):
    #     text_tag['style'] = "rgb(255,255,255)"
    
    # temp = mpld3.fig_to_html(fig).replace("<text", "<text style=\"fill:rgb(255,255,255)\"")
    # display data
    return render(request, 'stocks/display_plot.html', {
        'plot': mpld3.fig_to_html(fig)
    })

def date(day):
    month = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
        7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12: "Dec"}
    first = day.index("/")
    return month[int(day[:first])] + " " + str(day[-4:])

def get_html(day, value, series):
    return """<table border=\"1\" class=\"dataframe\">
      <thead>
          <tr style=\"text-align: right;\">
                <th></th>
                      <th>{0}</th>
                      </tr>
                            </thead>
                              <tbody>
                                  <tr>
                                        <th>Series</th>
                                              <td>{2}</td>
                                  </tr>
                                  <tr>
                                        <th>Predict</th>
                                              <td>{1}</td>
                                  </tr>
                              </tbody>
                            </table>
    """.format(day, value, series)

def plots(x, y):
    bg = '#0B0C0E'
    tx = '#FFFFFF'
    # wtx = {'labelsize':20, 'colors':'blue'}  
    dates, pred = x, y
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    # for side in ['top', 'bottom', 'left', 'right']:
    #     ax.spines[side].set_color(tx)
    # ax.xaxis.label.set_color(tx)
    # ax.yaxis.label.set_color(tx)
    years = [int(day[-4:]) + int(day[:day.index("/")]) / 12 for day in dates]
    print(dates)
    # ax.set_xlim(min(years), max(years))
    # Define some CSS to control our custom labels
    css = """
    table
    {
      border-collapse: collapse;
    }
    th
    {
      color: #ffffff;
      background-color: #000000;
    }
    td
    {
      background-color: #cccccc;
    }
    table, th, td
    {
      font-family:Arial, Helvetica, sans-serif;
      border: 1px solid black;
      text-align: right;
    }
    """
    # 1-2001 to 9-2020 months
    ax.grid(True, alpha=0.3)
    N = 236
    colors = ['r','c','m','y','w', 'dodgerblue', '#5c6370', 'chocolate','purple']
    for k, v in pred.items():
        points = ax.plot(years, v[0], '.-',  color=colors[v[1] - 1],
                        mec='k', ms=15, mew=1, alpha=.6)
        
        labels = [get_html(date(dates[i]), '${:,.2f}'.format(v[0][i]), v[2]) for i in range(N)]
        tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                          voffset=10, hoffset=10, css=css)
        plugins.connect(fig, tooltip)
    
    ax.set_xlabel('Year', size=15)
    ax.set_ylabel('Predicted Change', size=15)
    ax.set_title('Predicted Change in GDP', size=20)

    return fig

# def date(day):
#     bg = '#0B0C0E'
#     tx = '#FFFFFF'
#     month = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
#         7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12: "Dec"}

#     first = day.index("/")
#     return month[int(day[:first])] + " " + str(day[-4:])

# def plots(x, y):
#     bg = '#0B0C0E'
#     # bg = '#5c6370'
#     tx = '#FFFFFF'
    
#     dates, pred = x, y
#     fig, ax = plt.subplots(figsize=(8, 8))
#     fig.patch.set_facecolor(bg)
#     ax.set_facecolor(bg)
#     for side in ['top', 'bottom', 'left', 'right']:
#         ax.spines[side].set_color(tx)
#     # ax.xaxis.label.set_color(tx)
#     # ax.yaxis.label.set_color(tx)
#     ax.tick_params(axis='x', color=tx)
#     ax.tick_params(axis='y', color=tx)

#     # Define some CSS to control our custom labels
#     css = """
#     table
#     {
#       border-collapse: collapse;
#     }
#     th
#     {
#       color: #ffffff;
#       background-color: #000000;
#     }
#     td
#     {
#       background-color: #cccccc;
#     }
#     table, th, td
#     {
#       font-family:Arial, Helvetica, sans-serif;
#       border: 1px solid black;
#       text-align: right;
#     }
#     """
#     # 1-2001 to 9-2020 months
#     ax.grid(True, alpha=.01)
#     N = 236
#     # df = pd.DataFrame(index=range(N))
#     # df['x'] = dates.array
#     # df['y'] = pred.array

#     # labels = []
#     # for i in range(N):
#     #     label = data.loc[[i], :].T
#     #     # label = "waka waka"
#     #     # label[i].DATE = date(label[i].DATE)
#     #     label[i].Predict = '${:,.2f}'.format(label[i].Predict)
#     #     label.columns = [str(date(label[i].DATE))]
#     #     labels.append(str(label.to_html()))

#     # points = ax.plot(dates, pred, '.-', color='b',
#     #                 mec='k', ms=15, mew=1, alpha=.6)
#     colors = ['r','c','m','y','w', 'dodgerblue', '#5c6370', 'chocolate','purple']
#     i = 0
#     for key in y:
#         points = ax.plot(dates, y[key][0], '.-', color=colors[y[key][1] - 1],
#                 mec='k', mew=1, alpha=.6)
#         i += 1

#     ax.set_xlabel('Date', size=15, color='#8f96a3')
#     ax.set_ylabel('Predicted Change', size=15, color='#8f96a3')
#     ax.set_title('HTML tooltips', size=20, color='#8f96a3')
    
#     ax.spines['bottom'].set_color("red")
#     # ax.spines['top'].set_color("#8f96a30F") 
#     # ax.spines['right'].set_color("#8f96a30F")
#     ax.spines['left'].set_color("red")
    
#     ax.tick_params(axis='x', color='#8f96a3')
#     ax.tick_params(axis='y', color='#8f96a3')
#     ax.yaxis.label.set_color('#8f96a3')
#     ax.xaxis.label.set_color('#8f96a3')
#     # ax.grid(False)
#     # tooltip = plugins.PointHTMLTooltip(points[0], labels,
#     #                                   voffset=10, hoffset=10, css=css)
#     # plugins.connect(fig, tooltip)

#     # mpld3.show()
    
#     return fig