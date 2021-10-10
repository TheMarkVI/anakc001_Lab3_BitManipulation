/*	Author: Artip Nakchinda
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab 3  Exercise 1
 *	Exercise Description: "Count the number of 1s on Ports A and B 
 *                          and output that number to Port C"
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF; // Configure port's pins as inputs
    DDRB = 0x00; PORTB = 0xFF;

    DDRC = 0xFF; PORTC = 0x00; // Configure port's pins as outputs

    unsigned char tempA = 0x00;
    unsigned char tempB = 0x00;
    
    unsigned char totalOnes = 0x00;
    
    /* Insert your solution below */
    while (1) {
        totalOnes = 0;

        tempA = PINA;
        tempB = PINB;

        for(unsigned char i = 0; i < 8; i++) {
            if((tempA >> i & 0x01) == 0x01) {
                totalOnes += 1;
            }
            if((tempB >> i & 0x01) == 0x01) {
                totalOnes += 1;
            }
        }

        PORTC = totalOnes;
    }
    return 1;
}
