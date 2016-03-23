from pylab import *

phqc = np.loadtxt('ex2.txt', skiprows=2)
ph   = phqc[:, 0]

semilogy(ph, phqc[:, 11], 'b-', ph, phqc[:, 12], 'r-', ph, phqc[:, 7], 'g-', ph, phqc[:, 3], 'm-', ph, phqc[:, 8], 'c-')
semilogy(ph, phqc[:, 23], 'b-.', ph, phqc[:, 24], 'y-', ph, phqc[:,25], 'k-')
plt.xlim([1, 11])
plt.ylim([1.0e-15, 1.0e-9])
plt.xlabel('pH')
plt.ylabel('M')
plt.yticks([1e-15, 1e-13, 1e-11, 1e-9])
lgd = plt.legend(('HgCl$_2$', 'HgCl${_3}{^-}$', 'HgOHCl', 'Hg(OH)$_2$', 'HgOHCO${_3}{^-}$', 'HgRs$^+$', 'HgRs$_2$', 'HgRcoo$^+$'),loc=3)
lgd.draw_frame(False)
txt = lgd.get_texts()
plt.setp(txt, fontsize='medium')

plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.12, wspace=0.05, hspace=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 6)
savefig('ex2.pdf')
#show()
