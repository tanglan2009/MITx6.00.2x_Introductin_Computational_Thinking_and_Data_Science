import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 5
#set size of numbers on  x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5


def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan * ((r*(1+r)**m)/((1+r)**m -1))


class MortgagePlots(object):

    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range (1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)


class Mortgage(object):
    """Abstract class for building different kinds of mortgages."""
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None          # description of mortgage

    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment = self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend
pylab.show()



# Mix- in class



















