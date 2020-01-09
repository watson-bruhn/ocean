# Programme to create a QUBO to select a sub portfolio of stocks from an index that best matches the index return

# Get index and portfolio sizes
#index_size = int(input('How big is the index:'))
#portfolio_size = int(input('How many stocks do you want to select:'))
index_size = 50
portfolio_size = 10

# Create a set of returns
import numpy as np
stock_prices = np.random.rand(index_size+1,2)

# Scale prices so the sum of the stocks equals the index (need to edit)
stock_prices[0,0] *= 100

stock_prices[1:,0] /= stock_prices[1:,0].sum()
stock_prices[1:,0] *= stock_prices[0,0]

stock_prices[1:,1] *= 2
stock_prices[1:,1] = stock_prices[1:,1] * stock_prices[1:,0]

stock_prices[0,1] = stock_prices[1:,1].sum()

# Calculate stock returns
stock_returns = stock_prices[:,1] - stock_prices[:,0]
for i in range(1,index_size+1):
    stock_returns[i] = stock_returns[i] - (stock_returns[0]/portfolio_size)

# Display generated outcomes
print('\nStocks\n')
print(stock_prices)
print('\nReturns\n')
print(stock_returns)

# Build QUBOT matrix
q_matrix = np.zeros((index_size,index_size))
q_matrix += (1-2*portfolio_size)*np.identity(index_size)
q_matrix += 2*(1-np.tri(index_size))

print('\nQUBOT matrix\n')
print(q_matrix)

# Generate stock influence matrix
#abs_stock_returns = np.absolute(stock_returns[1:])
i_matrix = np.outer(stock_returns[1:],stock_returns[1:])
i_matrix /= np.amax(i_matrix)*2
i_matrix = np.multiply(i_matrix,np.identity(index_size)+2*(1-np.tri(index_size)))

print('\nInfluence matrix\n')
print(i_matrix)

# Build Hamiltonian
Hamiltonian = q_matrix + i_matrix

print('\nHamiltonian\n')
print(Hamiltonian)

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
f.write("response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=1000)\r\n")
f.write("for datum in response.data():\r\n")
f.write("    print(datum)\r\n")

# Show output for small arrays
#Output_Array = np.zeros((2**index_size,index_size+2))
#i = 0
#for i in range(0,2**index_size):
#    Output_Array[i,0] = i
#    for j in range(1,index_size+1):
#        if len(bin(i)) > j + 1:
#            Output_Array[i,j] = int(str(bin(i))[-j])
#        else:
#            Output_Array[i,j] = 0
#    Output_Array[i,index_size+1] = portfolio_size*portfolio_size + np.matmul(np.transpose(Output_Array[i,1:index_size+1]),np.matmul(Hamiltonian,Output_Array[i,1:index_size+1]))

#print('\nOutput array\n')
#print(Output_Array)

quit()

print('\n\n\nQuantum Time\n\n\n')

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
# >>> Set Q for the problem QUBO
linear = {('x0', 'x0'): Hamiltonian[0,0], ('x1', 'x1'): Hamiltonian[1,1], ('x2', 'x2'): Hamiltonian[2,2]}
quadratic = {('x0', 'x1'): Hamiltonian[0,1], ('x0', 'x2'): Hamiltonian[0,2], ('x1', 'x2'): Hamiltonian[1,2]}
Q = dict(linear)
Q.update(quadratic)
# >>> Minor-embed and sample 1000 times on a default D-Wave system
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=1000)
for datum in response.data():
    print(datum)
#for sample, energy, num_occurrences in response.data():
#    print(sample, "Energy: ", energy, "Occurrences: ", num_occurrences)
