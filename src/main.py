print("Sistema Kanban Inicializado")

import time
from machine import Pin, ADC

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)  

btn = Pin(25, Pin.IN, Pin.PULL_UP)

contador_pecas = 0
estado_anterior_bloqueado = False
tempo_bloqueio_inicio = 0
micro_parada_registrada = False

print("Contador de Producao Inicializado")

ultimo_estado_btn = btn.value()
ultimo_tempo_debounce = time.ticks_ms()

while True:
    current_time = time.ticks_ms()
    
    lux_val = ldr.read() 

    bloqueado = (lux_val < 600)
    
    if bloqueado:
        if not estado_anterior_bloqueado:
            estado_anterior_bloqueado = True
            tempo_bloqueio_inicio = current_time
            micro_parada_registrada = False
        else:
            if not micro_parada_registrada and (time.ticks_diff(current_time, tempo_bloqueio_inicio) > 5000):
                print("Alerta: Micro-parada detectada!")
                micro_parada_registrada = True
    else:
        if estado_anterior_bloqueado:
            contador_pecas += 1
            print(f"Peca detectada! Total: {contador_pecas}")
            estado_anterior_bloqueado = False

    leitura_atual = btn.value()
    if leitura_atual != ultimo_estado_btn:
        if time.ticks_diff(current_time, ultimo_tempo_debounce) > 30:
            ultimo_tempo_debounce = current_time
            if ultimo_estado_btn == 1 and leitura_atual == 0:
                contador_pecas = 0
                print("Turno resetado com sucesso. Contadores zerados.")
                # Pequena pausa para estabilizar a leitura do Wokwi CLI e evitar timeout pós-reset
                time.sleep(0.5)
            ultimo_estado_btn = leitura_atual

    time.sleep(0.01)