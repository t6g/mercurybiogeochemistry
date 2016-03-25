from pylab import *

pf   = np.loadtxt('ex3.txt', skiprows=1)
phqc = np.loadtxt('../../../../phreeqc/speciation/Dong2010/ex3.txt', skiprows=2)
ph   = phqc[:, 0]
tot  = 5.0e-12 / 100.0

plot(pf[:, 0], pf[:, 1]/tot, 'bo', pf[:, 0], pf[:, 2]/tot, 'rs', pf[:, 0], pf[:, 3]/tot, 'gd', pf[:, 0], pf[:, 4]/tot, 'm^')
plot(ph, phqc[:, 26]/tot, 'b-', ph, phqc[:, 27]/tot, 'r-', ph, phqc[:, 28]/tot, 'g-', ph, phqc[:, 29]/tot, 'm-')
plt.xlim([1, 11])
plt.ylim([0, 110])
plt.xlabel('pH')
plt.ylabel('%')
#plt.yticks([1e-15, 1e-13, 1e-11, 1e-9])
lgd = plt.legend(('CH$_3$Hg$^+$', 'CH$_3$HgCl', 'CH$_3$HgRs', 'CH$_3$HgOH'),loc=3)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium')

plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.12, wspace=0.05, hspace=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6, 4.5)
savefig('ex3.pdf')
#show()
