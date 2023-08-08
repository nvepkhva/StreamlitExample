import streamlit as st
import numpy as np

st.title( 'Central Limit Theorem Example' )

st.sidebar.markdown( '''
The Central Limit Theorem assumes you have a collection $X_1,\ldots,X_n$
of random variables that you will sum to create a new random variable
$X=\sum_{i=1}^n X_i$.  Here we will sum several
uniform random variables on the interval $[0,1]$.
You may choose the value of $n$ here.
''' )

num_random_variables_to_sum = st.sidebar.slider(
    "How many uniform random variables should we include in the sum?",
    1, 100, 10, 1 )

st.sidebar.markdown( '''
The Central Limit Theorem says that the new random variable $X$ will
be approximately normally distributed.  To visualize this, we will sample
many values from $X$ and create a histogram.  It should look more and more
like a bell curve as we increase $n$.
''' )

sample_size = st.sidebar.slider(
    "How large of a sample should we use to create the histogram?",
    100, 10000, 1000, 100 )

def my_random_variable ():
    return np.random.rand( num_random_variables_to_sum ).sum()

import matplotlib.pyplot as plt
sample = [ my_random_variable() for i in range(sample_size) ]
plt.hist( sample, bins=30 )
plt.title( f'Histogram of a sample of size {sample_size} from X' )
plt.xlabel( f'X = the sum of {num_random_variables_to_sum} uniform random variables on [0,1]' )
plt.ylabel( 'Frequency' )
st.pyplot(plt.gcf())

st.write( f'''
Because each $\\mu_{{X_i}}=0.5$ and $n={num_random_variables_to_sum}$,
we conclude $\\mu_X=0.5\\times{num_random_variables_to_sum}={num_random_variables_to_sum*0.5}$.

Mean of our sample is $\\bar{{x}}={np.mean( sample )}\\approx{num_random_variables_to_sum*0.5}$.
''' )


st.write( '''

# This would be a heading

Don't forget that you can use Python triple quotes to make a string
last over several lines, so that you can write as much as you want.

![A hilarious photo](BiasVariance.PNG)

''' )

