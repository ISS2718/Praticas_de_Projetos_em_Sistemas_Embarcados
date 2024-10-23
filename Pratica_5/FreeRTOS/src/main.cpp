#include <Arduino.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED 2

TaskHandle_t task1Handle = NULL;
TaskHandle_t task2Handle = NULL;


void vTask1(void * pvParameters);
void vTask2(void * pvParameters);

void setup() {
  Serial.begin(9600);

  xTaskCreatePinnedToCore(vTask1, "Blink", 2048, NULL, 5, NULL, 0);
  xTaskCreatePinnedToCore(vTask2, "Contagem", 2048, NULL, 0, NULL, 1);
}

void loop() {
  vTaskDelay(3000);
}

void vTask1(void * pvParameters){
  pinMode(LED, OUTPUT);
  while(1){
    digitalWrite(LED, !digitalRead(LED));
    vTaskDelay(pdMS_TO_TICKS(200));
  }
}

void vTask2(void * pvParameters){
  int cont = 0;
  while(1){
    Serial.println("Contando... " + String(cont++));
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}
