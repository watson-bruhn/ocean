# Programme to create a QUBO to select a sub portfolio of stocks from an index that best matches the index return

index_size = 10
portfolio_size = 5
influence_scale = 1
sample = 1000

# Generate a set of random returns (in this case a random set of numbers from -100 to +100 to represent differences from stocks to the index)
import numpy as np

stock_returns = np.random.rand(index_size) # Generate random numbers between 0-1
stock_returns -= 0.5 # Scale to -1 to 1
stock_returns *= 2
stock_returns *= 100 # Scale by 100 for ease of reading

print('\nReturns\n')
print(stock_returns)

# Build penalty matrix to limit the number of stocks selected to the defined portfolio size
p_matrix = np.zeros((index_size,index_size))
p_matrix += (1-2*portfolio_size)*np.identity(index_size)
p_matrix += 2*(1-np.tri(index_size))
p_matrix *= 1

print('\nPenalty matrix\n')
print(p_matrix)

# Generate stock influence matrix (sum x_i ** 2 + sum s * X_i * x_j)
i_matrix = np.outer(stock_returns,stock_returns)
i_matrix += np.triu(i_matrix,1)
i_matrix -= np.tril(i_matrix,-1)

# Scale the influence matrices
i_matrix /= np.amax(i_matrix) # scale terms to -1 <= x <= 1
i_matrix *= influence_scale

print('\nInfluence matrix\n')
print(i_matrix)

# Build Hamiltonian
Hamiltonian = p_matrix + i_matrix

print('\nHamiltonian\n')
print(Hamiltonian)

chain_strength = np.amax(Hamiltonian) - np.amin(Hamiltonian)

# Create Quantum computation file
f= open("quantum.py","w+")
f.truncate(0)
f.write("from dwave.system.samplers import DWaveSampler\r\n")
f.write("from dwave.system.composites import EmbeddingComposite\r\n")
f.write("linear = {")
for i in range(0,index_size):
    if i == index_size-1:
        f.write("('x%d', 'x%d'): %f" % (i, i, Hamiltonian[i,i]))
    else:
        f.write("('x%d', 'x%d'): %f, " % (i, i, Hamiltonian[i,i]))
f.write("}\r\n")
f.write("quadratic = {")
for i in range(0,index_size):
    for j in range(i+1,index_size):
        if i == index_size-2 and j == index_size-1:
            f.write("('x%d', 'x%d'): %f" % (i, j, Hamiltonian[i,j]))
        else:
            f.write("('x%d', 'x%d'): %f, " % (i, j, Hamiltonian[i,j]))
f.write("}\r\n")
#quadratic = {('x0', 'x1'): Hamiltonian[0,1], ('x0', 'x2'): Hamiltonian[0,2], ('x1', 'x2'): Hamiltonian[1,2]}
f.write("Q = dict(linear)\r\n")
f.write("Q.update(quadratic)\r\n")
f.write("response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, chain_strength=%d, num_reads=%d)\r\n" % (chain_strength,sample))
f.write("from datetime import datetime\r\n")
f.write("g= open(\"output\",\"w+\")\r\n")
f.write("g.truncate(0)\r\n")
f.write("for datum in response.data():\r\n")
f.write("   g.write(str(datum))\r\n")

g= open("returns","w+")
g.truncate(0)
for i in range(0,index_size):
    g.write(str(stock_returns[i]))
    g.write(",")
