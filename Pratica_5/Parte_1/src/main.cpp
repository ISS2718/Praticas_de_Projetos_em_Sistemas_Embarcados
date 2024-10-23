#include <Arduino.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED 2  // Define o pino do LED

TaskHandle_t task1Handle = NULL;  // Handle para a Task 1
TaskHandle_t task2Handle = NULL;  // Handle para a Task 2

// Declaração das funções das tasks
void vTask1(void * pvParameters);
void vTask2(void * pvParameters);

void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial a 9600 bps

  // Cria a Task 1, que pisca o LED, com prioridade 5 no core 0
  xTaskCreatePinnedToCore(vTask1, "Blink", 2048, NULL, 5, NULL, 0);
  
  // Cria a Task 2, que imprime a contagem na Serial, com prioridade 0 no core 1
  xTaskCreatePinnedToCore(vTask2, "Contagem", 2048, NULL, 0, NULL, 1);
}

void loop() {
  vTaskDelay(3000);  // Atraso de 3 segundos na função loop
}

// Função da Task 1: Pisca o LED a cada 200ms
void vTask1(void * pvParameters){
  pinMode(LED, OUTPUT);  // Configura o pino do LED como saída
  while(1){
    digitalWrite(LED, !digitalRead(LED));  // Alterna o estado do LED
    vTaskDelay(pdMS_TO_TICKS(200));  // Atraso de 200ms
  }
}

// Função da Task 2: Imprime a contagem na Serial a cada 1 segundo
void vTask2(void * pvParameters){
  int cont = 0;  // Variável de contagem
  while(1){
    Serial.println("Contando... " + String(cont++));  // Imprime a contagem na Serial
    vTaskDelay(pdMS_TO_TICKS(1000));  // Atraso de 1 segundo
  }
}