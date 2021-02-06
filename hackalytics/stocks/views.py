from django.shortcuts import render
import matplotlib.pyplot as plt, mpld3

# Create your views here.
def test_plot(request):
    fig, ax = plt.subplots()
    temp = ax.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    # mpld3.show()
    return render(request, 'stocks/display_plot.html', {
        'plot': mpld3.fig_to_html(fig)
    })
