'''
Created on Dec 19, 2018

@author: K3NN!
'''

from NumProgression.Progression import Progression
from NumProgression.ArithmeticProgression import ArithmenthicProgression
from NumProgression.GeometricProgression import GeometricProgression
from NumProgression.FibonacciProgression import Fibonacci




if __name__ == '__main__':
    print( 'Default progression:' )
    Progression().print_progression(10)
    print( 'Arithmetic progression with increment 5:' )
    ArithmenthicProgression(5).print_progression(7)
    print( 'Arithmetic progression with increment 5 and start 2:' )
    ArithmenthicProgression(5, 2).print_progression(10)
    print( 'Geometric progression with default base:' )
    GeometricProgression().print_progression(10)
    print( 'Geometric progression with base 3:' )
    GeometricProgression(3).print_progression(10)
    print('Fibonacci progression with default start Values:' )
    Fibonacci( ).print_progression(10)
    print('Fibonacci progression with start values 4 and 6:' )
    Fibonacci(4, 6).print_progression(10)

    