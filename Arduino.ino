#include <Servo.h>
int photoin = 5;
int ldrin = 6;
int ldrout = 7;
int LED01 = 0;
int LED02 = 8;
int utk09;
int utk08;
int icin = 2;
int icout = 10;
int gnd = 1;
int vcc = 3;
int echo = 11;
int trig = 12;
int LED03 = 13;
int time;
int distance;
Servo myservo;


void setup(){
    pinMode(photoin,INPUT);
    pinMode(LED01,OUTPUT);
    pinMode(LED02,OUTPUT);
    pinMode(ldrout,INPUT);
    pinMode(icin,OUTPUT);
    pinMode(icout,OUTPUT);
    pinMode(gnd,OUTPUT);
    pinMode(vcc,OUTPUT);
    pinMode(echo,INPUT);
    pinMode(trig,OUTPUT);
    pinMode(LED03,OUTPUT);
    myservo.attach(4);
}

void loop(){
    digitalWrite(vcc,HIGH);
    digitalWrite(gnd,LOW);
    digitalWrite(icin,HIGH);
    digitalWrite(icout,LOW);
    utk09=digitalRead(photoin);
    if (utk09==HIGH)
      digitalWrite(LED01,HIGH);
      
     else if (utk09==LOW)
      digitalWrite(LED01,LOW);
    utk08=digitalRead(ldrout);
    if (utk08==HIGH)
      digitalWrite(LED02,HIGH);
     else if (utk08==LOW)
      digitalWrite(LED02,LOW);
    Serial.begin(9600);
    digitalWrite(trig,HIGH);
    delayMicroseconds(1000);
    digitalWrite(trig,LOW);
    time=digitalRead(echo);
    distance=time/2/29;
    Serial.print(distance);
    delay(20);
    Serial.print("cm");

    if (distance>50)
      digitalWrite(LED03,HIGH);
     else if (distance<50)
      digitalWrite(LED03,LOW);

    if (digitalRead(LED03)==HIGH)
      myservo.write(0);
      
     else if (digitalRead(LED03)==LOW)
      
      myservo.write(180);
      delay(20);
      myservo.write(0);
      delay(20);
      myservo.write(180);
      delay(20);
}
