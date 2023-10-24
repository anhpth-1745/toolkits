import pandas as pd 
import sweetviz as sv
import IPython
from pandasgui import show import pandas as pd


# use sweetviz
## read data
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

## EDA data
my_report = sv.analyze(data)
my_report.show_html()

## show result
IPython.display.HTML('SWEETVIZ_REPORT.html')


# use pandasGui

## load data
train = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv") 

## show visualize
gui = show(train)
