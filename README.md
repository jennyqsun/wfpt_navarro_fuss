# Demonstration of pdf of reaction time of the Drift Diffusion Model and the log likliehood function given RT
# implementing the first-passage times in Wiener diffusion models proposed by Navarro & Fuss (2009)
## This code demonstrates how to calculate the probability density function of BOTH upper bound and lower bound

wfpt_navarro.py implements the probability density function of RT when other parameters (drift, boundary) are fixed.
wfpt_twobound.pynb is the jupyter notebook version.

Navarro's original matlab code only calculates the pdf when hitting the lower bound (RT is positive, drift rate is negative).
This code incorporates the pdf when the decision variable hits the upper bound (RT is negative, drift rate is positive).

See wfpt_twobound.ipynb to demonstrate examples. 