# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ 
    # PC5..PC0 = 1;
    {'description': 'Fuel is full (PINA is 15)',
    'steps': [ {'inputs': [('PINA', 0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3F)],
    },
    {'description': 'Fuel is full (PINA is 14)',
    'steps': [ {'inputs': [('PINA', 0x0E)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3F)],
    },
    {'description': 'Fuel is full (PINA is 13)',
    'steps': [ {'inputs': [('PINA', 0x0D)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3F)],
    },
    
    # PC5..PC1 = 1;
    {'description': 'Fuel is not low (PINA is 12)',
    'steps': [ {'inputs': [('PINA', 0x0C)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3E)],
    },
    {'description': 'Fuel is not low (PINA is 11)',
    'steps': [ {'inputs': [('PINA', 0x0B)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3E)],
    },
    {'description': 'Fuel is not low (PINA is 10)',
    'steps': [ {'inputs': [('PINA', 0x0A)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3E)],
    },

    # PC5..PC2 = 1
    {'description': 'Fuel is not low (PINA is 9)',
    'steps': [ {'inputs': [('PINA', 0x09)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3C)],
    },
    {'description': 'Fuel is not low (PINA is 8)',
    'steps': [ {'inputs': [('PINA', 0x08)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3C)],
    },
    {'description': 'Fuel is not low (PINA is 7)',
    'steps': [ {'inputs': [('PINA', 0x07)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x3C)],
    },

    # PC5..PC3 = 1
    {'description': 'Fuel is not low (PINA is 6)',
    'steps': [ {'inputs': [('PINA', 0x06)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x38)],
    },
    {'description': 'Fuel is not low (PINA is 5)',
    'steps': [ {'inputs': [('PINA', 0x05)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x38)],
    },

    # PC6..PC4 = 1;
    {'description': 'Fuel is low (PINA is 4)',
    'steps': [ {'inputs': [('PINA', 0x04)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x70)],
    },
    {'description': 'Fuel is low (PINA is 3)',
    'steps': [ {'inputs': [('PINA', 0x03)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x70)],
    },

    # PC6..PC5 = 1;
    {'description': 'Fuel is low (PINA is 2)',
    'steps': [ {'inputs': [('PINA', 0x02)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x60)],
    },
    {'description': 'Fuel is low (PINA is 1)',
    'steps': [ {'inputs': [('PINA', 0x01)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x60)],
    },

    # PC6 = 1;
    {'description': 'Fuel is low/empty (PINA is 0)',
    'steps': [ {'inputs': [('PINA', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x40)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
watch = ['PINA', 'PORTC']

