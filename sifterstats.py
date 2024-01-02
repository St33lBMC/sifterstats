
'''
simulates the gregtech/gt++ sifter processing recipes to see if there is a difference in output
with large numbers of input materials
assumes input_size is divisible by batch_size because im lazy
results: no real difference based on observation.
         obviously would require some sort of statistical test to prove but can't be bothered?!
1/1/24
usage: python3 sifterstats.py
'''

import random

probabilities = [0.03, 0.12, 0.45, 0.14, 0.28, 0.35] #the probability of getting each output using the pure emerald crushed ore recipe
batch_size = 8 #the size of each batch produced by the gt++ multiblock sifter
input_size = 10000 #the total number of items put through both sifters
n_trials = 100 #number of times to run the experiment
rand = random

def __main__():
    sum_d_outputs = [0] * len(probabilities) # after running a single trial, add the difference in outputs to the running total
    average_d_outputs = [0] * len(probabilities)
    for i in range(n_trials):
        d_output = run_trial()
        for j in range(len(probabilities)):
            sum_d_outputs[j] = sum_d_outputs[j] + d_output[j]

    #average the difference in outputs
    for i in range(len(probabilities)):
        average_d_outputs[i] = sum_d_outputs[i] / float(n_trials)

    print("average difference in singleblock - multiblock outputs")
    print("of " + str(n_trials) + " trials running " + str(input_size) + " items each: ")
    print(average_d_outputs)

def run_trial():
    sb_outputs = [0] * len(probabilities)
    mb_outputs = [0] * len(probabilities)
    d_outputs = [0] * len(probabilities) #vector of differences sb_outputs - mb_outputs

    #simulate processing input_size items in the singleblock sifter
    for i in range(input_size):
        r = rand.random()
        for j in range(len(probabilities)):
            if r < probabilities[j]:
                sb_outputs[j] = sb_outputs[j] + 1

    #print("singleblock results")
    #print(sb_outputs)

    # simulate processing input_size items in the singleblock sifter
    for i in range(int(input_size / batch_size)):
        r = rand.random()
        for j in range(len(probabilities)):
            if r < probabilities[j]:
                mb_outputs[j] = mb_outputs[j] + batch_size

    #print("multiblock results")
    #print(mb_outputs)

    # calculate vector of differences
    for i in range(len(probabilities)):
        d_outputs[i] = sb_outputs[i] - mb_outputs[i]

    #print("difference singleblock output - multiblock output")
    #print(d_outputs)
    return d_outputs

if __name__ == "__main__":
    __main__()