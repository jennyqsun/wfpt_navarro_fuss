import numpy as np
import matplotlib.pyplot as plt


# likelihood of a drift of 3 given different RT and ndt of 3

def wfpt(t,v, t0,a,z,err=1e-29):

    tt = (t - t0) / (a**2)
    if t< 0:
        tt = (-t -t0) / (a**2)

    if t < 0:
        print('sign flipped')
        v=-v
        # t=-t
    w = z/a

    ks = 2 + np.sqrt(-2*tt * np.log(2*np.sqrt(2*np.pi*tt)*err))
    ks = np.max((ks, np.sqrt(tt)+1))

    K=10
    k = np.arange(-4,6)
    p = np.cumsum((w+2*k)*np.exp(-((w+2*k)**2)/2/tt))
    p = p[-1]/np.sqrt(2*np.pi*tt**3)

    pp = p * np.exp(-v*a*w - (v**2)*t/2)/(a**2)

    return (pp)

#####################
#likelihood of drift given RT
######################
pdf1 = []
for i in np.linspace(0.31,10,300):
    prob = wfpt(i,-1, 0.3, 2, 2/2, err=1e-29)
    pdf1.append(prob)
plt.plot(np.linspace(0.31,10,300), pdf1)
plt.xlabel('Reaction time (Positive)')
plt.ylabel('L ( delta = -0.5 | RT)')
plt.title('L ( delta = -0.5 | RT incorrect)')
plt.show()


pdf2 = []
for i in np.linspace(0.31,10,300):
    prob = wfpt(i,1,0.3, 2, 2/2, err=1e-29)
    pdf2.append(prob)

plt.plot(np.linspace(0.31,10,300), pdf2)
plt.xlabel('Reaction time (Negative')
plt.ylabel('L ( delta = -0.5 | RT incorrect)')
plt.title('L ( delta = -0.5 | RT incorrect)')
plt.show()


#############################
#probability of RT given drift
##############################

pdf = []
for i in np.linspace(-6,0,300):
    prob = wfpt(0.634,i,0.3, 2, 2/2, err=1e-29)
    pdf.append(prob)

plt.plot(np.linspace(-6,0,300), pdf)
plt.xlabel('Drift')
plt.ylabel('P ( RT = 0.63 | Drift)')
plt.title('P ( RT = 0.63 | Drift)')
plt.show()


pdf = []
for i in np.linspace(-6,0,300):
    prob =wfpt(-0.634,i,0.3, 2, 2/2, err=1e-29)
    pdf.append(prob)

plt.plot(np.linspace(-6,0,300), pdf)
plt.xlabel('Drift')
plt.ylabel('P ( RT = - 0.8 | Drift)')
plt.title('P ( RT = - 0.8 | Drift)')
plt.show()







pdf = []
for i in np.linspace(0.3,4,300):
    prob_small= wfpt(0.64,-0.5,0.3,i,i/2,err=1e-29)
    pdf.append(prob_small)
plt.plot(np.linspace(0.3,4,300), pdf)
plt.show()


pdf = []
for i in np.linspace(0.3,4,300):
    prob_small= wfpt(-0.64,-0.5,0.3,i,i/2,err=1e-29)
    pdf.append(prob_small)
plt.plot(np.linspace(0.3,4,300), pdf)
plt.show()



plt.title('probability density function when drift rate=1\n starting point=0.5\n boundary seperation=2')
plt.xlabel('Decision Time')
plt.ylabel('Density')
xy = np.linspace(0.1,3,300)[np.argmax(pdf_small)], pdf_small[np.argmax(pdf_small)]
plt.plot(xy[0],xy[1], 'ro')
plt.annotate('time: %.2f'%xy[0], xy=xy, xytext=(0.5,0.9),
            arrowprops=dict(facecolor='black', shrink=0.1), fontsize=15)
plt.show()
