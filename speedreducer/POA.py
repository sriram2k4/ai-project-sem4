import numpy as np

fbest, Xbest, best_so_far, iterations, best_per_iteration = [], [], [], [], []

def POA(SearchAgents, Max_iterations, lowerbound, upperbound, dimension, fitness, fhandle, fnonlin):
    
    lowerbound = np.ones(dimension) * lowerbound  # Lower limit for variables
    upperbound = np.ones(dimension) * upperbound  # Upper limit for variables
    
    # Initialization
    X = np.zeros((SearchAgents, dimension))  # Initialize X as a matrix of zeros # Eq(2)
    for i in range(dimension):
        X[:, i] = lowerbound[i] + np.random.rand(SearchAgents) * (upperbound[i] - lowerbound[i])  # Initial population # Eq(1)
    
    fit = np.zeros(SearchAgents)  # Initialize fitness array # Eq(3)
    for i in range(SearchAgents):
        L = X[i, :]
        fit[i] = fitness(fhandle, fnonlin, L)
    
    
    best_so_far = []  # Initialize list to store best fitness values over iterations
        
    for t in range(1, Max_iterations):
        iterations.append(t) # for graph
        
        location, best = min(enumerate(fit), key=lambda x: x[1])
        if t == 1:
            fbest = best
            Xbest = X[location, :]  # Accessing row 'location' from matrix X

        elif (best<fbest):
            fbest = best
            Xbest = X[location, :]  # Accessing row 'location' from matrix X
            
    
        # UPDATE location of food
        k = np.random.randint(0, SearchAgents)  # Randomly select an index k
        X_FOOD = X[k, :]  # Update X_FOOD with the selected row from X
        F_FOOD = fit[k]   # Update F_FOOD with the fitness value corresponding to the selected row
        
        for i in range(SearchAgents):
            # PHASE 1: Moving towards prey (exploration phase)
            if fit[i] > F_FOOD:
                X_new = X[i, :] + np.random.rand() * (X_FOOD - X[i, :])  # Eq(4)
            else:
                X_new = X[i, :] + np.random.rand() * (X[i, :] - X_FOOD)  # Eq(4)
        
            # Ensure X_new is within the bounds
            X_new = np.maximum(X_new, lowerbound)
            X_new = np.minimum(X_new, upperbound)
        
            # Updating X_i using equation (5)
            f_new = fitness(fhandle, fnonlin, X_new)
            if f_new <= fit[i]:
                X[i, :] = X_new
                fit[i] = f_new
                
            # PHASE 2: Winging on the water surface (exploitation phase)
            X_new = X[i, :] + 0.2 * (1 - t / Max_iterations) * (2 * np.random.rand(dimension) - 1) * X[i, :]  # Eq(6)
        
            # Ensure X_new is within the bounds
            X_new = np.maximum(X_new, lowerbound)
            X_new = np.minimum(X_new, upperbound)
        
            if f_new <= fit[i]:
                X[i,:] = X_new
                fit[i] = f_new
                
        best_so_far.append(fbest)
                
    
    return fbest, Xbest, best_so_far