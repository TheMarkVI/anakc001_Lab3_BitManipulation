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
tests = [ {'description': 'No 1s on ports A or B',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x00)],
    },
    {'description': 'Port A = 0x01, PortB = 0x00, PortC == 0x01',
    'steps': [ {'inputs': [('PINA', 0x01), ('PINB', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x01)],
    },
    {'description': 'Port A = 0x00, PortB = 0x01, PortC == 0x01',
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x01)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x01)],
    },
    {'description': 'Port A = 0x01, PortB = 0x01, PortC == 0x02',
    'steps': [ {'inputs': [('PINA', 0x01), ('PINB', 0x01)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x02)],
    },
    {'description': 'Port A = 0xFF, PortB = 0xFF, PortC == 0x10',
    'steps': [ {'inputs': [('PINA', 0xFF), ('PINB', 0xFF)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x10)],
    },
    {'description': 'Port A = 0xA0, PortB = 0x5A, PortC == 0x06', # A = 1010 0000 | B = 0101 1010 | C = 0x06
    'steps': [ {'inputs': [('PINA', 0xA0), ('PINB', 0x5A)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x06)],
    },
    {'description': 'Port A = 0xF0, PortB = 0x00, PortC == 0x04', # A = 1111 0000 | B = 0000 0000 | C = 0x04
    'steps': [ {'inputs': [('PINA', 0xF0), ('PINB', 0x00)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x04)],
    },
    {'description': 'Port A = 0x00, PortB = 0x0F, PortC == 0x04', # A = 0000 0000 | B = 0000 1111 | C = 0x04
    'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x0F)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x04)],
    },
    {'description': 'Port A = 0xAB, PortB = 0xCD, PortC == 0x04', # A = 1010 1011 | B = 1100 1101 | C = 0x10
    'steps': [ {'inputs': [('PINA', 0xAB), ('PINB', 0xCD)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x0A)],
    },
    ]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
watch = ['PORTC']

