import pylab
# pylab.figure(1)  # make figure 1 the current figure
# pylab.plot([1, 2, 3, 4], [1, 2, 3, 4]) #draw on figure 1
# pylab.figure(2)  #make figure 2 current figure
# pylab.plot([1, 4, 2, 3], [5, 6, 7, 8]) # draw on figure 2
# pylab.savefig('Figure_Eric')        # save figure 2
# pylab.figure(1) # go back to working on figure 1
# pylab.plot([5, 6, 10 ,3])   #draw again on figure 1
# pylab.savefig('Figure_Grimson') #save figure 1
#
# pylab.show()  # show figure on screen


principal = 10000       # initial investment
interestRate = 0.05
years = 20
values = []
for i in range (years + 1):
    values.append(principal)
    principal += principal * interestRate
#pylab.plot(range(years + 1), values)
pylab.plot([1, 2, 3, 4], [1, 2, 3, 4], linewidth = 1)
pylab.title('5% Growth, Compounded Annually', fontsize = 20)
pylab.xlabel('Years of Compounding', fontsize = 10)
pylab.ylabel('Value of Principal ($)', fontsize = 10)
pylab.show()


#  .rc file  for rc settings