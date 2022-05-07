#include <SPI.h>
#include <Arduino.h>
#include <MFRC522.h>
#include <ESP8266Wifi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
const char *ssid = "Đạt đẹp trai";
const char *password = "12345678";
const char *mqtt_server = "driver.cloudmqtt.com";
const char *mqtt_username = "burlgbdf";
const char *mqtt_password = "0--UiYtSUWAZ";
WiFiClient espClient;
PubSubClient client(espClient);
// Constants
#define BUZZER_PIN 4
#define SS_PIN 15
#define RST_PIN 0
// Variables
byte nuidPICC[4] = {0, 0, 0, 0};
MFRC522::MIFARE_Key key;
MFRC522 rfid = MFRC522(SS_PIN, RST_PIN);

void printHex(byte *buffer, byte bufferSize);
void readRFID(void);
void buzzer_onoff(uint8_t time)
{
  for (uint8_t i = 0; i < time; i++)
  {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(500);
    digitalWrite(BUZZER_PIN, LOW);
    delay(500);
  }
}


void setup()
{

  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  pinMode(BUZZER_PIN, OUTPUT);
  while (WiFi.status() != WL_CONNECTED)
  {
    buzzer_onoff(1);
    Serial.print(".");
    delay(500);
  }
  client.setServer(mqtt_server, 18675);
  client.connect("RedTeam12", mqtt_username, mqtt_password);
Serial.println("connected");
}
void loop()
{
  if(client.connected())
  {
    readRFID();
    delay(1000);
  }
  else
  {
    client.connect("RedTeam12", mqtt_username, mqtt_password);
  }
}
void readRFID(void)
{
  String payload = "";
  for (byte i = 0; i < 6; i++)
  {
    key.keyByte[i] = 0xFF;
  }
  if (!rfid.PICC_IsNewCardPresent())
    return;

  if (!rfid.PICC_ReadCardSerial())
    return;

  for (byte i = 0; i < 4; i++)
  {
    nuidPICC[i] = rfid.uid.uidByte[i];
    payload = payload + String(nuidPICC[i] < 0x10 ? "0" : "") + String(nuidPICC[i], HEX);

    payload = payload + " ";
  }
  payload.toUpperCase();

  printHex(rfid.uid.uidByte, rfid.uid.size);
  if (client.publish("RedTeam", payload.c_str(), true))
  {
    buzzer_onoff(1);
    delay(500);
  }
  else
  {
    buzzer_onoff(3);
  }
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}

void printHex(byte *buffer, byte bufferSize)
{
  for (byte i = 0; i < bufferSize; i++)
  {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
  Serial.println();
}