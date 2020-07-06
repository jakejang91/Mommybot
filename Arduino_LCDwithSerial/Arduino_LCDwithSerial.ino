//YWROBOT
//Compatible with the Arduino IDE 1.0
//Library version:1.1
#include <LiquidCrystal_I2C.h>
// Connecting to  0, 1 5v gnd

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
int count = 0;
int diod_pin = A1;
void setup()
{
  lcd.init();                      // LCD Initializing
  // Print a message to the LCD.
  lcd.noBacklight();                // Turn on Backlight
  lcd.setCursor(0,0);             // First char, First line
  lcd.print("Hello");
  lcd.setCursor(0,1);             // First char, Second Line
  lcd.print("I'm Mommybot!");
  
  Serial.begin(9600);
  Serial.println("Im Start");
}


void loop()
{  
    int sensorValue = analogRead(diod_pin);
    //int outputValue = map(sensorValue, 0, 1023, 0, 255);

   // lcd.backlight();
    while(!Serial){} // wait unitil serial is working
    while(!Serial.available() ){} // wait unitil serial is working
    String text = Serial.readString(); // Get string from Serial port

    Serial.println(text);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("   WARNING!");
    lcd.setCursor(0,1);
    lcd.print(text);            // print text
    for(int i = 0; i<100; i++){ // Blink
      lcd.noBacklight();
      delay(50);
      lcd.backlight();
      delay(50);
    }
    lcd.noBacklight();
}
