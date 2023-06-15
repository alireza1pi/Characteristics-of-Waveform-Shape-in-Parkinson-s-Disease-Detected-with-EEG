import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pac

import seaborn as sns
sns.set_style('white')

import imp
import shape
import utils

imp.reload(utils)



widthS = 3
Fs, t, S, Sc, flo, fhi = utils.loadmeta()
eeg,rejects = utils.loadPD()
pac = utils.measure_pac(eeg,rejects, flo, fhi, Fs=Fs)
pks,trs,ShR,PTR,StR,RDR = utils.measure_shape(eeg,rejects, widthS=widthS)





#sharpness ratio and steepness ratio data is pooled to find correlation
allpt = np.log10(np.hstack((PTR['off'],PTR['on'])))
allrd = np.log10(np.hstack((RDR['off'],RDR['on'])))

print(sp.stats.spearmanr(allpt,allrd))


print(sp.stats.spearmanr(PTR['off'][15:30], RDR['off'][15:30]))
print(sp.stats.spearmanr(PTR['on'][15:30], RDR['on'][15:30]))




M = .3
mb = np.polyfit(allpt, allrd,1)
xs = np.array([-M,M])
yfit = mb[1] + xs*mb[0]
plt.figure(figsize=(8,6.5))

colors='plasma'#inferno#plasma#viridis#bone#pink
faces='.98'
alphas=1
sizes=90
lw=0.6

fsize=24

plt.fill_between([0,M], [0,0], [M,M], facecolor=faces, alpha=alphas, interpolate=True)
plt.fill_between([-M,0], [0,0], [-M,-M], facecolor=faces, alpha=alphas, interpolate=True)
plt.fill_between([0,M], [0,0], [-M,-M], facecolor='dodgerblue', alpha=0.1, interpolate=True)
plt.fill_between([-M,0], [0,0], [M,M], facecolor=faces, alpha=alphas, interpolate=True)
plt.plot(xs, yfit, 'k--',linewidth=1)
plt.plot([-M,M],[0,0],'k-',alpha=.3)
plt.plot([0,0],[-M,M],'k-',alpha=.3)
plt.xlabel('log peak-to-trough ratio',size=fsize)
plt.ylabel('log rise-to-fall ratio',size=fsize)
plt.xlim((-M,M))
plt.ylim((-M,M))
plt.xticks([-M,0,M],size=fsize)
plt.yticks([-M,0,M],size=fsize)
plt.legend(loc='best',fontsize=fsize)

plt.scatter(np.log10(PTR['off']), np.log10(RDR['off']),\
            c=pac['off'], s=sizes,cmap=colors,alpha=1,linewidths=lw,edgecolors='black',label="OFF", marker="o")
plt.scatter(np.log10(PTR['on']), np.log10(RDR['on']),\
            c=pac['on'], s=sizes,cmap=colors,alpha=1,linewidths=lw,edgecolors='black',label="ON",marker="s")#label="on"
# plt.scatter(np.log10(PTR['C']), np.log10(RDR['C']),\
#             c=pac['C'], s=sizes,cmap=colors,alpha=1,linewidths=lw,edgecolors='black',label="CONTROL",marker="o")#label="on"



colorb=plt.colorbar(label='Modulation Index')
colorb.ax.tick_params(labelsize=fsize)
colorb.set_label(label='Modulation Index',size=fsize)
plt.legend(loc='best',fontsize=fsize)


plt.tight_layout()
plt.savefig('Fig5A_23.png', format='png', dpi=1000)






import matplotlib.pyplot as plt
import numpy as np

Ncycles = 4
cw = np.array([0,.01,.05,.1,.2,1,.9,.8,.7,.6,.5,.4,.3,.2,.1,.05,.01])
cw = np.tile(cw,(Ncycles))
tc = np.arange(len(cw))

iw = np.array([0,.8,.9,.95,.99,1,.99,.95,.9,.8,.7,.6,.5,.4,.3,.2,.1])
iw = -iw + 1
iw = np.tile(iw,(Ncycles))
ti = np.arange(len(cw))
lineg='.35'

plt.figure(figsize=(5,5))
plt.subplot(2,2,2)
plt.plot(tc,cw,lineg,linewidth=3)
plt.xticks([],[],visible=False)
plt.ylim((-.1,1.1))
plt.yticks([],[],visible=False)
plt.xlim((0,len(tc)))

plt.subplot(2,2,4)
plt.plot(ti,iw,lineg,linewidth=3)
plt.fill_between([0,100],[-5,-5],[100,0], facecolor='dodgerblue', alpha=0.1, interpolate=True)
plt.xticks([],[],visible=False)
plt.yticks([],[],visible=False)
plt.xlabel('time',size=20)
plt.ylim((-.1,1.1))
plt.xlim((0,len(tc)))

plt.subplot(2,2,3)
plt.plot(tc,-cw,lineg,linewidth=3)
plt.ylabel('Voltage',size=20)
plt.xlabel('time',size=20)
plt.xticks([],[],visible=False)
plt.ylim((-1.1,.1))
plt.yticks([],[],visible=False)
plt.xlim((0,len(tc)))

plt.subplot(2,2,1)
plt.plot(ti,-iw,lineg,linewidth=3)
plt.xticks([],[],visible=False)
plt.ylabel('Voltage',size=20)
plt.yticks([],[],visible=False)
plt.ylim((-1.1,.1))
plt.xlim((0,len(tc)))
plt.tight_layout()

plt.show()