import time
import threading
import keyboard
import pydirectinput

# Настройки таймингов
PAUSE_AFTER_THROW = 0.2
PAUSE_AFTER_PICK = 0.2

is_running = False

def farm_loop():
    global is_running
    pydirectinput.PAUSE = 0.0
    
    while is_running:
        # Нажатие G (Бросок)
        pydirectinput.keyDown('g')
        time.sleep(0.04)
        pydirectinput.keyUp('g')
        
        time.sleep(PAUSE_AFTER_THROW)
        
        if not is_running: 
            break
            
        # Нажатие E (Подбор)
        pydirectinput.keyDown('e')
        time.sleep(0.05)
        pydirectinput.keyUp('e')
        
        time.sleep(PAUSE_AFTER_PICK)

def toggle_farm():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=farm_loop, daemon=True).start()
        print("Старт")
    else:
        is_running = False
        print("Стоп")

print("F8 - Старт/Стоп | ESC - Выход")

keyboard.add_hotkey('f8', toggle_farm)
keyboard.wait('esc')
