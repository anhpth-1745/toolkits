import pandas as pd 
import sweetviz as sv
import IPython


#read data
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# EDA data
my_report = sv.analyze(data)
my_report.show_html()

# show result
IPython.display.HTML('SWEETVIZ_REPORT.html')



