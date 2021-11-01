import pandas

df = pandas.DataFrame([[2, 4, 6],[10, 20, 30]]) # default
df = pandas.DataFrame([[2, 4, 6],[10, 20, 30]], columns=["price", "age", "value"]) # name columns
df = pandas.DataFrame([[2, 4, 6],[10, 20, 30]], columns=["price", "age", "value"], index=["First", "Second"]) #name rows
df_2 = pandas.DataFrame([{"name":"john"}, {"name":"mike"}]) # dictionary
df_2 = pandas.DataFrame([{"name":"john", "surname":"novelt"}, {"name":"jack"}]) # add more columns
type(df_2) # pandas.core.frame.DataFrame
dir(df_2) # list of methods
df.mean() # get average
type(df.price) # pandas.core.series.Series
df.price.mean()
df.price.max()

"""
    pip3 install jupyter

    or

    Jupyter in the cloud

    If you do not want to install Jupyter or you cannot install it, you can use Jupyter in the cloud. 
    Google offers a ready-to-use Jupyter notebook here: https://colab.research.google.com/#create=true
"""