import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def random_walk(N: int) -> int:
    """Esta funcion retorna el resultado de una caminata aleatoria en una dimension
    luego de n pasos
    
    Parameters
    ----------
    N : int
        Numero de pasos que realiza la caminata aleatoria
        
    Returns
    -------
    int
    total desplazado en pasos de tamanio 1
    """
    values = np.random.choice([-1, 1], size=N)
    return np.sum(values)

def run_random_walk_simulator(num_run: int, N: int) -> np.ndarray:
    """Esta funcion corre un total de x veces una caminata aleatoria de N pasos
    
    Parameters
    ----------
    num_run : int
        numero de veces que se va a correr la simulacion
    N: int
        tamaño que se va a tomar de la muestra para cada caminata
        
    Returns
    -------
    np.ndarray
    un arreglo de numpy con los resultados de cada caminata
    """
    result = [random_walk(N) for i in range (num_run)]
    return np.array(result)

def plot_random_histogram(num_run: int, N: int, file_name: str):
    """La funcion grafica un histograma con los resultados de correr num_run veces una caminata aleatoria en 1d
    
    Parameters
    ----------
    num_run : int
        numero de veces que se va a correr la simulacion
    N: int
        tamaño que se va a tomar de la muestra para cada caminata
    """
    
    plt.figure()
    #Plot the bins
    bins = run_random_walk_simulator(num_run, N)
    bin_count = int(np.ceil(np.log2(num_run)) + 1)
    plt.hist(bins, bin_count, density = True, label = "Data distribution")
    
    #Plot the associated gaussian
    mu = 0
    sigma = np.sqrt(N)
    
    maximo = np.max([np.abs(np.min(bins)), np.max(bins)])
    num = 400 if N<400 else N
    x = np.linspace(-maximo, maximo, num=num)
    
    
    exponential_factor = np.exp(-0.5 * (1 / sigma * (x - mu))**2)
    factor = 1 / (np.sqrt(2 * np.pi) * sigma)
    y = factor * exponential_factor
    
    plt.plot(x, y, '--', color ='black', label = "Expected gaussian")
    plt.legend()
    plt.xlabel('Number of steps')
    plt.title(f'Probability distribution of random walk with {N} steps runned {num_run} times')
    plt.savefig(file_name)
    
    return np.mean(bins), np.std(bins), mu, sigma

def run_many_times_histogram(num_run: int, N_min: int, N_max: int, steps: int, file_name: str) -> pd.DataFrame:
    """Corre varias veces el metodo para obtener el histograma con valores entre N_min y N_max con un step
    
    Parameters
    ----------
    num_run : int
        numero de veces que se va a correr la simulacion
    N_min: int
        tamaño N minimo para correr la caminata aleatoria
    N_max: int
        tamaño N maximo para correr la caminata aleatoria
    step: int
        cada cuanto se toman valores de N
        
    Returns
    -------
    pd.DataFrame
    DataFrame con los valores de N y las varianzas y media obtenidas y esperadas
    """
    N_array = np.arange(N_min, N_max, steps)
    
    means = []
    variances = []
    expected_means = []
    expected_variances = []
    
    for N in N_array:
        mean, var, expected_mean, expected_var = plot_random_histogram(num_run, N, f'{file_name}N{N}.png')
        
        means.append(mean)
        variances.append(var)
        expected_means.append(expected_mean)
        expected_variances.append(expected_var)
    
    d = {'N': N_array, 
         'mean': means, 
         'variance': variances, 
         'expected mean': expected_means, 
         'expected variances': expected_variances}
    return pd.DataFrame(data=d)

