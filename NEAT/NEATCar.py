########################################
##### N.E.A.T. Robot Car Algorithm #####
########################################

### Imports ###

import random

### Variables ###

population = 10
maxGeneration = 10
#inputs = 400
#outputs = {"leftSlow" : 0, "leftMedium" : 0, "leftFast" : 0, "rightSlow" : 0, "rightMedium" : 0, "rightFast" : 0,}
inputs = 2
outputs = {"True" : 0, "False" : 0}
pool = {}
pool["species"] = {}
pool["generation"] = 0
pool["innovation"] = 0
pool["currentSpecies"] = 1
pool["currentGenome"] = 1
pool["mutationRates"] = {"bias" : 0.4, "link" : 0.5, "node" : 0.5, "disable" : 0.4, "enable" : 0.2}
pool["maxFitness"] = 0

### Functions ###

def getInputs():
    return

def randomNeuron(neurons, num):
    if num == -1:
        neuron = 1000
        while neuron >= 1000:
            neuron = random.choice(neurons.keys())
    else:
        if num < inputs:
            num = inputs-1
        neuron = num
        while neuron <= num:
            neuron = random.choice(neurons.keys())
    return neuron
    
def newInnovation():
    newestInnovation = pool["innovation"]
    return newestInnovation

def bias(genome):
    
    return genome

def link(genome):
    neuron1 = randomNeuron(genome["network"]["neurons"], -1)
    neuron2 = randomNeuron(genome["network"]["neurons"], neuron1)
    
    used = False
    for gene in genome["genes"]:
        if neuron1 == gene["into"] and neuron2 == gene["out"]:
            used = True
                
    if used == False:
        genome["genes"].append({"into" : neuron1, "out" : neuron2, "weight" : 1, "enable" : True, "innovation" : newInnovation()})
        
    return genome["genes"]

def node(genome):
    
    return genome

def disable(genome):
    
    return genome

def enable(genome):
    
    return genome

def mutate(genome):
    mutations = {"bias" : bias, "link" : link, "node" : node, "disable" : node, "enable" : node}
    for name, func in mutations.iteritems():
        tf = True
        while tf == True:
            if random.random() <= pool["mutationRates"][name]:
                func(genome)
            else:
                tf = False
    return genome
    
def generateNetwork(genome):
    network = {"neurons" : {}}
    
    for i in range(inputs):
        network["neurons"][i] = {"incoming" : [], "value" : 0.0}
        
    for o in range(len(outputs)):
        network["neurons"][o+1000] = {"incoming" : [], "value" : 0.0}
    
    for gene in genome["genes"]:
        if gene["enable"] == True:
            neurons = network["neurons"]
            try:
                if not neurons[gene["out"]]:
                    print "um..."
            except:
                neurons[gene["out"]] = {"incoming" : [], "value" : 0.0}

            neurons[gene["out"]]["incoming"].append(gene)
            
            try:
                if not network["neurons"][gene["into"]]:
                    print "um..."
            except:
                network["neurons"][gene["into"]] = {"incoming" : [], "value" : 0.0}
                
    return network

def addToSpecie(genome, num):
    pool["species"]["genome"+str(num)] = genome
    
def runSimulation(genome):
    fitness = 1
    return fitness

### Class 1 ###

def initialize():
    for i in range(population):
        basic = {"genes" : [], "network" : {}, "maxNeurons" : inputs + len(outputs), "fitness" : 0, "rank" : 0}
        basic["network"] = generateNetwork(basic)
        basic["genes"] = link(basic)
        basic["network"] = generateNetwork(basic)
        addToSpecie(basic, i)

def showOff():
    for i in pool.keys():
        if i == "species":
            for g in pool[i]:
                print g + " = " + str(pool[i][g])
        else:
            print i + " = " + str(pool[i])

def evaluateNetworks():
    for s in pool["species"].keys():
        for g in pool["species"][s].keys():
            genome = pool["species"][s][g]
            fitness = runSimulation(genome)
            genome["fitness"] = fitness
    return

def dataSave():
    datafile = open("NetData.txt", "w")
    datafile.write("Generation: " + str(pool["generation"]))
    
    datafile.write()

def newGeneration():
    return

### Algorithm ###

initialize()

while pool["generation"] < maxGeneration:
    evaluateNetworks()
    dataSave()
    newGeneration()
    pool["generation"]+=1

showOff()

### The End ###