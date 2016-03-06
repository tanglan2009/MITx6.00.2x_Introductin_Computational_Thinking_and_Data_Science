class Puzzle(object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == '0':
                self.spot = index
                return None
    def transition(self, to):
        label = self.label
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0'
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])