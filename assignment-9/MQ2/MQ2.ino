#define MQ2_PIN 34   
int gasValue = 0;

void setup() {
  Serial.begin(115200);  
  Serial.println("MQ-2 Gas Sensor Setup Done");
}

void loop() {
  gasValue = analogRead(MQ2_PIN); 

  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  if (gasValue > 300) 
  {   
    Serial.println("Smoke Detected!");
  } 
  else 
  {
    Serial.println("Smoke not present");
  }

  delay(1000); 
}
