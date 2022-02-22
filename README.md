# Demonstration of Probability Density Function and Log Likelihood Estimate the Drift Diffusion Model
## This code implements Wiener First Passager Time proposed by Navarro & Fuss (2009) in Python and Jupyter Notebook
## This code demonstrates how to calculate the probability density function of BOTH upper bound and lower bound 

Navarro's original matlab code in the appendix calculates the pdf when hitting the lower bound (drift rate is always negative).
This code incorporates the pdf when the decision variable hits the upper bound (drift rate is positive). In practice, use positive RT for lower bound, and negative RT for upper bound. The two bound can be two choices (choice A vs. Choice B), or can be correct and incorrect responses. 

See wfpt_twobounds.ipynb as an example. 


wfpt_navarro.py implements the probability density function of RT when other parameters (drift, boundary) are fixed.
wfpt_twobound.pynb is the jupyter notebook version.
