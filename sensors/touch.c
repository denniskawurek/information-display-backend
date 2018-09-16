/*
 * Calls a script every time the sensor is touched.
 * Installation instructions:
 * 1 - Download the latest bcm2835 library: http://www.airspayce.com/mikem/bcm2835/
 * 2 - Extract: tar xvfz bcm2835-1.5.tar.gz
 * 3 - cd bcm2835-1.5
 * 4 - ./configure
 * 5 - make
 * 6 - sudo make install
 *
 * Compile with:
 * gcc -o touch touch.c -l bcm2835
 */

#include <bcm2835.h>
#include <stdio.h>
#include <stdlib.h>

#define PIN RPI_GPIO_P1_19 // set the physical pin

void clickRight();

int main(int argc, char **argv)
{
    if (!bcm2835_init()) {
	printf("Initializing failed. Try again.\n");
        return 1;
    }

    bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_INPT);
    //  with a pullup
    bcm2835_gpio_set_pud(PIN, BCM2835_GPIO_PUD_UP);

    while (1) {
        uint8_t value = bcm2835_gpio_lev(PIN);
        printf("read from pin: %d\n", value);

        if(value == 1) {
    		system("/home/pi/code/information-display/information-display-backend/sensors/sh/rightClick.sh");
    	}
    	delay(250);
    }
    bcm2835_close();
    return 0;
}
