from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3

# Create your views here.
def test_plot(request):
    fig, ax = plt.subplots()
    temp = ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20, color='#ffffff')
    ax.spines['bottom'].set_color('#FF0000')
    ax.spines['top'].set_color('#FF0000') 
    # ax.spines['right'].set_color('ffffff')
    # ax.spines['left'].set_color('ffffff')
    ax.set_facecolor("#0b0c0e")
    # mpld3.show()
    return render(request, 'stocks/display_plot.html', {
        'plot': mpld3.fig_to_html(fig)
    })

def test_bootstrap(request):
    return render(request, 'stocks/bootstrap_demo.html', {})
