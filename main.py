import random_walk as rw
import os

def display_menu():
    print('-'*100)
    print('-'*35 + 'Running random walk simulator' + '-'*36)
    print('-'*100)
    print()

    while True:
        print('Select the option you want')
        print()
        print('1. Run random walk with N steps')
        print('2. Run many times random walk')
        print('3. Run many times the random walk with many N')
        print('4. Exit')

        option = int(input('Select an option: '))

        if option == 1:
            N = int(input('Selet number N of steps: '))
            print('-'*100)
            x = rw.random_walk(N)
            print(f'the final position x where the random walker is located is {x}')
        
        if option == 2:
            N = int(input('Selet number N of steps: '))
            num_run = int(input('Number of times to run the simulation: '))
            file_name = input('name of the file to save the histogram ')
            print('-'*100)

            if not os.path.exists('./histograms'):
                os.makedirs('./histograms')
            
            mean, var, expected_mean, expected_var = rw.plot_random_histogram(num_run, N, f'./histograms/{file_name}.png')

            print(f'the mean is {mean} while it was expected {expected_mean}')
            print(f'the variance is {var} while it was expected {expected_var}')

            print(f'the histogram was stored in the path ./histograms/{file_name}')
        if option == 3:
            N_min = int(input('Selet minimum number steps: '))
            N_max = int(input('Selet maximum number steps: '))
            steps = int(input('Selet each many N values are taken: '))
            num_run = int(input('Number of times to run the simulation: '))
            dir_name = input('name of the file to save the histogram ')
            print('-'*100)

            if not os.path.exists('./histograms'):
                os.makedirs('./histograms')

            if not os.path.exists(f'./histograms/{dir_name}'):
                os.makedirs(f'./histograms/{dir_name}')
                
            a = rw.run_many_times_histogram(num_run, 
                N_min, 
                N_max,
                steps,
                f'./histograms/{dir_name}/'
            )

            print(a)
            print(f'the histogram was stored in the path ./histograms/{dir_name}')
        
        if option == 4:
            return

        print('-'*100)
        print()

if __name__ == '__main__':
    display_menu()