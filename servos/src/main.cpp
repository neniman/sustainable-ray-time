#include <Servo.h>
#include <Wire.h>


Servo servoblau; //Erstellt für das Programm ein Servo mit dem Namen „servoblau“
Servo servomiddle; //Erstellt für das Programm ein Servo mit dem Namen „servoblau“
Servo servobottom; //Erstellt für das Programm ein Servo mit dem Namen „servoblau“
int incomingByte = 0;


void setup()
{
	servoblau.attach(8);
	servomiddle.attach(7);
	servobottom.attach(6);

	Serial.begin(115200);
	Serial.println("Hello!");
}



void loop()
{
	if (Serial.available() > 0) {

		incomingByte = Serial.read(); // read the incoming byte:

		Serial.print(" I received:");

		Serial.println(incomingByte);
		if (incomingByte == 49){
			servoblau.write(180);
			delay(1000);
			servoblau.write(0);
		} else if (incomingByte == 50) {
			servomiddle.write(180);
			delay(1000);
			servomiddle.write(0);
		} else if (incomingByte == 51) {
			servobottom.write(180);
			delay(1000);
			servobottom.write(0);
		}

	}
}
