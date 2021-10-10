/*	Author: Artip Nakchinda
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab 3  Exercise 2
 *	Exercise Description: 
 *      - Fuel level sensor: PA3 - PA0
 *      - IF fuel level == 1 || 2, PC5 = 1
 *      - IF fuel level == 3 || 4, PC5..PC4 = 1;
 *      - IF fuel level == 5 || 6, PC5..PC3 = 1;
 *      - IF fuel level == 7 || 8 || 9, PC5..PC2 = 1;
 *      - IF fuel level <= 4, PC6 = 1 (low fuel);
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
    // Inputs
    DDRA = 0x00; PORTA = 0xFF; // 0000 3210

    // Outputs
    DDRC = 0xFF; PORTC = 0x00; // 0654 3210 

    unsigned char tempA = 0x00;
    
    unsigned char fuelSensor = 0x00;
    
    /* Insert your solution below */
    while (1) {
        fuelSensor = 0;
        tempA = PINA;

        // - Fuel level sensor: PA3 - PA0 | 7654 3210
        //                                  0000 1111
        // - IF fuel level <= 4, PC6 = 1 (low fuel);
        // - IF fuel level == 13 || 14 || 15, PC5..PC0 = 1;
        // 0011 1111
        if((tempA & 0x0F) == 0x0F || (tempA & 0x0E) == 0x0E || (tempA & 0x0D) == 0x0D) {
            fuelSensor = 0x3F;
        } 

        // - IF fuel level == 10 || 11 || 12, PC5..PC1 = 1;
        // 10 : 1010
        // 0011 1110
        else if((tempA & 0x0C) == 0x0C || (tempA & 0x0B) == 0x0B || (tempA & 0x0A) == 0x0A) {
            fuelSensor = 0x3E;
        } 

        // - IF fuel level == 7 || 8 || 9, PC5..PC2 = 1;
        // 7 = 0111 | 8 = 1000 | 9 = 1001
        // 0011 1100 
        else if((tempA & 0x07) == 0x07 || (tempA & 0x08) == 0x08 || (tempA & 0x09) == 0x09) {
            fuelSensor = 0x3C;
        } 

        // - IF fuel level == 5 || 6, PC5..PC3 = 1;
        // 0011 1000
        else if((tempA & 0x05) == 0x05 || (tempA & 0x06) == 0x06) {
            fuelSensor = 0x38;
        } 

        // - IF fuel level == 3 || 4, PC5..PC4 = 1, PC6 = 1
        // 0111 0000
        else if((tempA & 0x03) == 0x03 || (tempA & 0x04) == 0x04) {
            fuelSensor = 0x70;
        }

        // - IF fuel level == 1 || 2, PC5 = 1, PC6 = 1
        // 0110 0000
        else if((tempA & 0x01) == 0x01 || (tempA & 0x02) == 0x02) {
            fuelSensor = 0x60;
        }
        else {
            // 0100 0000, only low fuel sensor is on.
            fuelSensor = 0x40;
        }

        PORTC = fuelSensor;
    }
    return 1;
}
