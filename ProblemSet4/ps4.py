


import numpy
import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        return self.maxBirthProb

    def getClearProb(self):
        return self.clearProb

    def doesClear(self):
        return random.random() <= self.getClearProb()

    def reproduce(self, popDensity):
        if random.random() <= self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        raise NoChildException


class Patient(object):

    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        return self.viruses

    def getMaxPop(self):
        return self.maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        popDensity = len(self.viruses) / float(self.maxPop)
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity))
            except NoChildException:
                pass
        return len(self.viruses)


# Problem 3: simulationWithoutDrug
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    steps = 300
    trialResults = [[] for s in range(steps)]
    for __ in range(numTrials):
        viruses = [SimpleVirus(maxBirthProb, clearProb) for v in range(numViruses)]
        patient = Patient(viruses, maxPop)
        for step in range(steps):
            trialResults[step].append(patient.update())
    resultsSummary = [sum(l) / float(numTrials) for l in trialResults]
    pylab.plot(resultsSummary, label="Total Virus Population")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()


# Problem 4: a) ResistantVirus
class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.mutProb = mutProb
        self.resistances = resistances

    def isResistantTo(self, drug):
        return self.resistances.get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        if (all(self.isResistantTo(d) for d in activeDrugs) and
            random.random() <= self.getMaxBirthProb() * (1 - popDensity)):
            resistances = {k:v if random.random() > self.mutProb else not v
                           for k, v in self.resistances.items()}
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(),
                                  resistances, self.mutProb)
        raise NoChildException


# Problem 4: b) TreatedPatient
class TreatedPatient(Patient):

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugs =[]

    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        return self.drugs

    def getResistPop(self, drugResist):
        return len([v for v in self.viruses if all(v.isResistantTo(d)
                                                   for d in drugResist)])

    def update(self):
        self.viruses = [v for v in self.viruses if not v.doesClear()]
        popDensity = len(self.viruses) / float(self.maxPop)
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity,
                                                self.getPrescriptions()))
            except NoChildException:
                pass
        return len(self.viruses)


# Problem 5: simulationWithoutDrug
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    steps = 600
    treatOnStep = 300
    trialResultsTot = [[] for s in range(steps)]
    trialResultsRes = [[] for s in range(steps)]
    for __ in range(numTrials):
        viruses = [ResistantVirus(maxBirthProb, clearProb,
                                  resistances.copy(), mutProb)
                   for v in range(numViruses)]
        patient = TreatedPatient(viruses, maxPop)
        for step in range(steps):
            if step == treatOnStep:
                patient.addPrescription("guttagonol")
            patient.update()
            trialResultsTot[step].append(patient.getTotalPop())
            trialResultsRes[step].append(patient.getResistPop(["guttagonol"]))
    resultsSummaryTot = [sum(l) / float(len(l)) for l in trialResultsTot]
    resultsSummaryRes = [sum(l) / float(len(l)) for l in trialResultsRes]
    pylab.plot(resultsSummaryTot, label="Total Virus Population")
    pylab.plot(resultsSummaryRes, label="Resistant Virus Population")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend()
    pylab.show()


#print simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)



def simulationDelayedTreatment(numTrials):
    """

   Runs simulations and make histograms for problem 1.

   Runs numTrials simulations to show the relationship between delayed
       treatment and patient outcome using a histogram.

  Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
       numTrials: number of simulation runs to execute (an integer)
       """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False}
    mutProb = 0.005

    for delay in [300, 150, 75, 0]:
        totalPopOfViruses = [0] * numTrials

        for trial in range(numTrials):

            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)] * numViruses
            patient = TreatedPatient(viruses, maxPop)
            for i in range(delay):
                totalPopOfViruses[trial] = patient.update()

            patient.addPrescription('guttagonol')
            for i in range(150):
                totalPopOfViruses[trial] = patient.update()
        pylab.hist(totalPopOfViruses)
        pylab.title(delay)
        pylab.xlabel("final total virus population values")
        pylab.ylabel("number of trials belonging to each histogram bin")
        pylab.show()

#print simulationDelayedTreatment(100)

def simulationTwoDrugsDelayedTreatment(numTrials):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False, 'grimpex': False}
    mutProb = 0.005
    for delay in [300, 150, 75, 0]:
        totalPopOfViruses = [0] * numTrials

        for trial in range(numTrials):

            viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)] * numViruses
            patient = TreatedPatient(viruses, maxPop)
            for i in range(150):
                totalPopOfViruses[trial] = patient.update()

            patient.addPrescription('guttagonol')
            for i in range(delay):
                totalPopOfViruses[trial] = patient.update()
            patient.addPrescription('grimpex')
            for i in range(150):
                totalPopOfViruses[trial] = patient.update()
        pylab.hist(totalPopOfViruses)
        pylab.title(delay)
        pylab.xlabel("final total virus population values")
        pylab.ylabel("number of trials belonging to each histogram bin")
        pylab.show()
print simulationTwoDrugsDelayedTreatment(100)


