//YWROBOT
//Compatible with the Arduino IDE 1.0
//Library version:1.1
#include <LiquidCrystal_I2C.h>
// 아날로그 0, 1 5v gnd 에 연결

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
int count = 0;
int diod_pin = A1;
void setup()
{
  lcd.init();                      // LCD 초기화
  // Print a message to the LCD.
  lcd.noBacklight();                // 백라이트 켜기
  lcd.setCursor(0,0);             // 1번째, 1라인
  lcd.print("Hello");
  lcd.setCursor(0,1);             // 1번째, 2라인
  lcd.print("I'm Mommybot!");
  
  Serial.begin(9600);
  Serial.println("Im Start");
}


void loop()
{  
    int sensorValue = analogRead(diod_pin);
    //int outputValue = map(sensorValue, 0, 1023, 0, 255);

   // lcd.backlight();
    while(!Serial){}
    while(!Serial.available() ){}
    String text = Serial.readString();

    Serial.println(text);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("   WARNING!");
    lcd.setCursor(0,1);
    lcd.print(text);
    for(int i = 0; i<100; i++){
      lcd.noBacklight();
      delay(50);
      lcd.backlight();
      delay(50);
    }
    lcd.noBacklight();
}
