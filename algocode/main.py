import POA
import fun_info as f
import plotter as p

# --------------------------------------------------------------------------------------------------------------------------------------------------
Fun_name = "F1"  # test function 
SearchAgents = 30  # number of Pelicans (population members)
Max_iterations = 1000  # maximum number of iterations

# Object function information
fitness, lowerbound, upperbound, dimension = f.fun_info(Fun_name)
	
# Calculating the solution of the given problem using POA
Best_score, Best_pos, POA_curve = POA.POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness)

# Displaying results
print(f"The best solution obtained by POA for {Fun_name} is: \n{Best_pos}")
print(f"The best optimal value of the objective function found by POA for {Fun_name} is: {Best_score}")

iterations = [i for i in range(1, Max_iterations)]
p.plot_func(iterations, POA_curve, Fun_name)

# --------------------------------------------------------------------------------------------------------------------------------------------------