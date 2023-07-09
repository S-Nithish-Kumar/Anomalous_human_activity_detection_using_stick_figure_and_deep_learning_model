// assign pins for LEDs and buzzer
int LED1 = 3;
int LED2 = 4;
int LED3 = 5;
int Buzz = 6;
int dataFromUser; // declare a variable to receive serial data
int count=0; // declare a counter which will be used to turn ON the LEDs and buzzer sequentially
void setup() 
{
    // set the pin mode for all the LED and buzzer pins
    pinMode(LED1,OUTPUT);
    pinMode(LED2,OUTPUT);
    pinMode(LED3,OUTPUT);
    pinMode(Buzz,OUTPUT);
    Serial.begin(9600);
}

void loop()
 {
  while(Serial.available())
  {
  dataFromUser = Serial.read();
  // when the serial data is 1, it means anomalous. The counter value will be checked every time for turning the LEDs On.
  if(dataFromUser == '1' && count==0)
  {
    digitalWrite(LED1,HIGH);
    count++;
  }
  else if(dataFromUser == '1' && count==1)
  {
    digitalWrite(LED2,HIGH);
    count++;
  }
  else if(dataFromUser == '1' && count==2)
  {
    digitalWrite(LED3,HIGH);
    count++;
  }
  else if(dataFromUser == '1' && count==3)
  {
    digitalWrite(Buzz,HIGH); 
  }
  // if serial data is 2, then the activity is normal. The digital pin values of LEDs and buzzer is set to LOW and the counter is re-initialized.
  else if(dataFromUser == '2' )
  {
    digitalWrite(LED1,LOW);
    digitalWrite(LED2,LOW);
    digitalWrite(LED3,LOW);
    digitalWrite(Buzz,LOW);
    count=0;
  }
//Serial.print(dataFromUser);
}
}
