from pylab import *

pf   = np.loadtxt('ex2.txt', skiprows=1)
pf1  = np.loadtxt('../ex2a/ex2.txt', skiprows=1)
phqc = np.loadtxt('../../../../phreeqc/speciation/dong2010/ex2.txt', skiprows=2)
ph   = phqc[:, 0]

semilogy(pf[:, 0], pf[:, 2], 'bo', pf[:, 0], pf[:, 3], 'rs', pf[:, 0], pf[:, 5], 'gd', pf[:, 0], pf[:, 6], 'm^', pf[:, 0], pf[:, 7], 'c<', pf[:, 0], pf[:, 9], 'k>', markerfacecolor = 'white')
semilogy(pf1[:, 0], pf1[:, 2], 'bo', pf1[:, 0], pf1[:, 3], 'rs', pf1[:, 0], pf1[:, 5], 'gd', pf1[:, 0], pf1[:, 6], 'm^', pf1[:, 0], pf1[:, 7], 'c<', pf1[:, 0], pf1[:, 9], 'k>')
semilogy(ph, phqc[:, 11], 'b-', ph, phqc[:, 12], 'r-', ph, phqc[:, 7], 'g-', ph, phqc[:, 3], 'm-', ph, phqc[:, 8], 'c-', ph, phqc[:, 23], 'k-')
plt.xlim([1, 11])
plt.ylim([1.0e-15, 1.0e-9])
plt.xlabel('pH')
plt.ylabel('M')
plt.yticks([1e-15, 1e-13, 1e-11, 1e-9])
lgd = plt.legend(('HgCl$_2$', 'HgCl${_3}{^-}$', 'HgOHCl', 'Hg(OH)$_2$', 'HgOHCO${_3}{^-}$', 'HgRs$^+$'),loc=3)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium')

plt.subplots_adjust(left=0.13, right=0.95, top=0.95, bottom=0.12, wspace=0.05, hspace=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6, 4.5)
savefig('ex2.pdf')
#show()
