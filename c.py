class MPNeuron:
    inputs = []
    weights = []
    threshold = 0
    def __init__(self):
        inputs = [1,1,1]
        weights = [1,1,1]
        threshold = 2.5
    
    def MP_Neuron_Input(self,inputs,weights,threshold):
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        sum = 0
        for i in range(len(inputs)):
            sum = sum + self.inputs[i]*self.weights[i]
        if sum >= self.threshold:
            print("1\n")
        else:
            print("0\n")

neuron = MPNeuron()
weights = [-1,-1,-1]
for i in range(2):
    for j in range(2):
        for k in range(2):
            inputs = [i,j,k]
            neuron.MP_Neuron_Input(inputs,weights,-2.5)
            neuron.MP_Neuron_Evaluate()



