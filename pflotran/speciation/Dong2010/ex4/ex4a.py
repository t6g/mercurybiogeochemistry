from pylab import *

pf   = np.loadtxt('ex4a.txt', skiprows=2)
phqc = np.loadtxt('../../../../phreeqc/speciation//Dong2010/ex4.txt', skiprows=2)
incr = phqc[:, 0]
xx = incr * 1e9
xp = pf[:, 0] * 1e9

ax1 = subplot(2, 1, 1)
#plot(xx, np.divide(phq0[:, 1], incr)*100.0, 'b-', xx, np.divide(phq0[:, 2], incr)*100.0, 'r-', xx, np.divide(phq0[:, 3], incr)*100.0, 'g-')
plot(xx, np.divide(phqc[:, 1], incr)*100.0, 'b-', xx, np.divide(phqc[:, 2], incr)*100.0, 'r-', xx, np.divide(phqc[:, 3], incr)*100.0, 'g-')
plot(xp, np.divide(pf[:, 2], pf[:, 0])*100.0, 'b+', xp, np.divide(pf[:, 3], pf[:, 0])*100.0, 'rx', xp, np.divide(pf[:, 1], pf[:, 0])*100.0, 'go')
ylim([0, 110])

ylabel('%Hg$^{2+}$')
lgd = plt.legend(('HgL$^+$', 'HgL$_2$', 'Hg(OH)$_2$'),loc=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
setp(txt, fontsize='medium')
ylim([0, 100])
setp(ax1.get_xticklabels(), visible=False)


cl = 4.0e-9
ax2 = subplot(2, 1, 2)
plot(xx, phqc[:, 1]/cl*100.0, 'b-', xx, phqc[:, 2]/cl*100.0, 'r-', xx, phqc[:,22]/cl*100.0, 'k-')
plot(xx, phqc[:, 7]/cl*100.0, 'g-.', xx, phqc[:, 9]/cl*100.0, 'm:')
plot(xp, pf[:, 2]/cl*100.0, 'bx', xp, pf[:, 3]/cl*100.0, 'r+', xp, pf[:, 4]/cl*100.0, 'ko', xp, pf[:, 5]/cl*100.0, 'gs', xp, pf[:, 6]/cl*100.0, 'm^', )
ylim([0, 100])
lgd = plt.legend(('HgL$^+$', 'HgL$_2$', 'HL', 'ZnL$^+$', 'CuL$^+$'),loc=1)
lgd.draw_frame(False)
txt = lgd.get_texts()
setp(txt, fontsize='medium')
xlabel('[Hg$^{2+}$] (nM)')
ylabel('%L')

plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.12, wspace=0.05, hspace=0.05)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6, 9)
savefig('ex4a.pdf')
#show()
