
class TempGoopieThrusterData:
    def __init__(self):
        self.thrusterData = []

        self.addData()

    def addData(self):
        self.thrusterData.append({"thruster": ['SW'], "time": "5"})
        self.thrusterData.append({"thruster": ['SE'], "time": "5"})
        self.thrusterData.append({"thruster":['SW','SE'], "time":"10"})

    def getThrusterData(self):
        return self.thrusterData