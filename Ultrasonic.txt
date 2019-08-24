int trigPin=4;
int echoPin=2;  
float Time;
float speedOfSound=346.0;
double Distance=0.0; 

void setup() 
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop()
{  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2000); 
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trigPin, LOW); 
  Time = pulseIn(echoPin, HIGH);  
  Distance=(Time)*(speedOfSound)/(10000);  
  Serial.println(Distance);
  delay(100);
}
