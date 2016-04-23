from pylab import *

pf   = np.loadtxt('ex2/ex2.txt', skiprows=1)
phqc = np.loadtxt('../../../phreeqc/speciation/dong2010/ex2.txt', skiprows=2)
ph   = phqc[:, 0]

hgtot = 4.0e-10 / 100.0
plt.subplot(1, 2, 1)
plt.plot(pf[:, 0], pf[:, 2]/hgtot, 'bo', pf[:, 0], pf[:, 3]/hgtot, 'r+', pf[:, 0], pf[:, 5]/hgtot, 'gx', pf[:, 0], pf[:, 6]/hgtot, 'ms', pf[:, 0], pf[:, 7]/hgtot, 'cd', pf[:, 0], pf[:, 9]/hgtot, 'k^')
plt.plot(ph, phqc[:, 11]/hgtot, 'b-', ph, phqc[:, 12]/hgtot, 'r-', ph, phqc[:, 7]/hgtot, 'g-', ph, phqc[:, 3]/hgtot, 'm-', ph, phqc[:, 8]/hgtot, 'c-', ph, phqc[:, 23]/hgtot, 'k-')
plt.xlim([1, 11])
plt.ylim([-10, 110])
plt.xlabel('pH')
plt.ylabel('%')
lgd = plt.legend(('HgCl$_2$', 'HgCl${_3}{^-}$', 'HgOHCl', 'Hg(OH)$_2$', 'HgOHCO${_3}{^-}$', 'HgRs$^+$'),loc=6)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium')

pf   = np.loadtxt('ex3/ex3.txt', skiprows=1)
phqc = np.loadtxt('../../../phreeqc/speciation/Dong2010/ex3.txt', skiprows=2)
ph   = phqc[:, 0]
tot  = 5.0e-12 / 100.0

ax2 = plt.subplot(1, 2, 2)
plot(pf[:, 0], pf[:, 1]/tot, 'bo', pf[:, 0], pf[:, 2]/tot, 'rs', pf[:, 0], pf[:, 3]/tot, 'gd', pf[:, 0], pf[:, 4]/tot, 'm^')
plot(ph, phqc[:, 26]/tot, 'b-', ph, phqc[:, 27]/tot, 'r-', ph, phqc[:, 28]/tot, 'g-', ph, phqc[:, 29]/tot, 'm-')
plt.xlim([1, 11])
plt.ylim([-10, 110])
plt.xlabel('pH')
lgd = plt.legend(('CH$_3$Hg$^+$', 'CH$_3$HgCl', 'CH$_3$HgRs', 'CH$_3$HgOH'),loc=6)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium')
plt.setp(ax2.get_yticklabels(),visible=False)


plt.subplots_adjust(left=0.06, right=0.98, top=0.95, bottom=0.12, wspace=0.05, hspace=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 4.5)
savefig('ex23.pdf')
savefig('ex23.png')
show()


