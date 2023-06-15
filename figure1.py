
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
pks,trs,ShR,PTR,StR,RDR = utils.measure_shape(eeg,rejects, widthS=widthS)



# Select one recording
group = 'off'
subj = 1
x = eeg[group][subj]
rejects0=0
w = 3
# Bandpass filter in beta frequency range
xbeta = utils.firf(x,0, flo, Fs, w = 3, rmvedge=False)
# Determine rising and falling zerocrossings.
pos = xbeta > 0
zerorises = (pos[:-1] & ~pos[1:]).nonzero()[0]
pos = xbeta < 0
zerofalls = (pos[:-1] & ~pos[1:]).nonzero()[0]

#data was checked so xlims fell in non-artifact region
xlim = (9.6,10.1)
ylim = (-20,20)

l=len(x)/Fs
t = np.arange(0, l, 1 / Fs)

fig = plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(t, x,'k',linewidth=3)
plt.ylabel('Raw Signal\n Voltage ($\mu V$)',size=15)
plt.ylim(ylim)
plt.xlim(xlim)
plt.yticks(ylim,size=15)
plt.tick_params(labelsize=15)
plt.xticks(visible=False)



l=len(xbeta)/Fs
t = np.arange(0, l, 1 / Fs)

plt.subplot(3,1,2)
plt.plot(t, xbeta, 'k',linewidth=3)
plt.plot(t[zerofalls], xbeta[zerofalls], 'yo', ms=8,label='rising zerocross')
plt.plot(t[zerorises], xbeta[zerorises], 'go', ms=8,label='falling zerocross')
lgd = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=20)
plt.ylabel('Beta-filtered\n Voltage ($\mu V$)',size=15)
plt.xlim(xlim)
plt.ylim(ylim)
plt.yticks(ylim,size=15)
plt.tick_params(labelsize=15)

plt.xticks(visible=False)

l=len(x)/Fs
t = np.arange(0, l, 1 / Fs)

plt.subplot(3,1,3)
plt.plot(t, x, 'k-',linewidth=3)
plt.plot(t[pks[group][subj]],x[pks[group][subj]],'mo', ms=8, label='peak')
plt.plot(t[trs[group][subj]],x[trs[group][subj]],'co', ms=8, label='trough')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=20)
plt.ylabel('Raw Signal\n Voltage ($\mu V$)',size=15)


rise=plt.axvspan(9.88,10, color='dodgerblue', alpha=0.1,label='rise')
plt.ylim(ylim)
plt.yticks(ylim,size=15)
plt.xlim(xlim)
plt.xlabel('Time (s)',size=15)
plt.xticks(xlim,[0,.5])

plt.tick_params(labelsize=15)

plt.savefig('fig1_A.png', format='png', dpi=300)





pkidx = 205#peak id
tridx = 205#trough id

xlim = (9.88,10)
ylim=(-20,20)

plt.figure(figsize=(5,3))
plt.plot(t, x, 'k-',linewidth=3)
plt.plot(t[pks[group][subj]],x[pks[group][subj]],'mo', ms=8)
plt.plot(t[trs[group][subj]],x[trs[group][subj]],'co', ms=8)
plt.plot([t[pks[group][subj][pkidx]]-widthS/Fs,t[pks[group][subj][pkidx]]-widthS/Fs],[-1000,1000],'m-')
plt.plot([t[pks[group][subj][pkidx]]+widthS/Fs,t[pks[group][subj][pkidx]]+widthS/Fs],[-1000,1000],'m-')
plt.plot([t[trs[group][subj][tridx]]-widthS/Fs,t[trs[group][subj][tridx]]-widthS/Fs],[-1000,1000],'c-')
plt.plot([t[trs[group][subj][tridx]]+widthS/Fs,t[trs[group][subj][tridx]]+widthS/Fs],[-1000,1000],'c-')
plt.plot(t[pks[group][subj][pkidx]-widthS],x[pks[group][subj][pkidx]-widthS],'m^',ms=10)
plt.plot(t[pks[group][subj][pkidx]+widthS],x[pks[group][subj][pkidx]+widthS],'m^',ms=10)
plt.plot(t[trs[group][subj][tridx]-widthS],x[trs[group][subj][tridx]-widthS],'c^',ms=10)
plt.plot(t[trs[group][subj][tridx]+widthS],x[trs[group][subj][tridx]+widthS],'c^',ms=10)

pkidx = 206#rise id
tridx = 206#fall id
print(t[pks[group][subj][pkidx+0]])
rise=plt.axvspan(t[pks[group][subj][pkidx]],t[trs[group][subj][tridx+0]], color='gold', alpha=0.3,label='rise')
decay=plt.axvspan(t[trs[group][subj][tridx+1]],t[pks[group][subj][pkidx+0]], color='green', alpha=0.3,label='fall')
rise=plt.axvspan(9.88,9.94, color='dodgerblue', alpha=0.1)
rise=plt.axvspan(t[trs[group][subj][tridx+1]],10, color='dodgerblue', alpha=0.1)



plt.legend([rise, decay], ["rise", "fall"])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=20)
plt.yticks(ylim,size=15)
plt.xlim(xlim)
plt.ylim(ylim)
plt.xticks(xlim,[.28,.4])


plt.tick_params(labelsize=15)
plt.ylabel('Raw Signal\n Voltage ($\mu V$)',size=15)
plt.xlabel('Time (s)',size=15)
plt.tight_layout()
plt.savefig('fig1_B.png', format='png', dpi=300)
plt.show()