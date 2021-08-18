import matplotlib.pyplot as plt
def plotPieChart(positive, w_positive, s_positive, negative, w_negative, s_negative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positivo [' + str(positive) + '%]', 'Levemente Positivo [' + str(w_positive) + '%]','Fortemente Positivo [' + str(s_positive) + '%]', 'Neutro [' + str(neutral) + '%]',
                  'Negativo [' + str(negative) + '%]', 'Levemente Negativo [' + str(w_negative) + '%]', 'Fortemente Negativo [' + str(s_negative) + '%]']
        sizes = [positive, w_positive, s_positive, neutral, negative, w_negative, s_negative]
        colors = ['green','yellow','blue', 'purple', 'aqua','red','brown']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('Como as pessoas estão reagindo a ' + searchTerm + ' analizando ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
