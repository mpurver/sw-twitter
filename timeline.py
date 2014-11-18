"""Timeline plot generator for tweet streams."""
from opster import command
import pandas as pd
import matplotlib.pyplot as plt

@command()
def timeline(
        input_file,
        output=('o', 'timeline.png', 'The output file name.'),
):
    """Generate a timeline plot for a stream of tweets."""
    print('input_file is: {}'.format(input_file))
    print('output is: {}'.format(output))

    # read the input data into pandas format
    dataFrame = pd.io.parsers.read_csv(input_file, 
                                       sep=' ',
                                       names=['Date','Count'], 
                                       parse_dates=True, 
                                       index_col=0)
    print dataFrame.head()

    # plot and save
    dataFrame.plot()
    plt.savefig(output)

if __name__ == '__main__':
    timeline.command()
        
