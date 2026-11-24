def is_valid_command(command):
    return command in ("0", "1", "2", "exit")
def can_burn(power, fuel):
    return fuel >= power
def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    new_fuel = fuel - power
    new_speed = max(0, speed + gravity - thrust_step * power)
    new_height = max(0, height - new_speed)
    return new_height, new_speed, new_fuel
def get_status(height, speed, safe_speed=2):
    if height > 0:
        return "В полете"
    if speed <= safe_speed:
        return "Посадка успешна"
    return "Авария"
def format_state(height, speed, fuel):
    return f"Высота: {height} | Скорость: {speed} | Топливо: {fuel}"
def main():
    # Параметры варианта (сейчас указан вариант 1)
    height = 20
    speed = 2
    fuel = 8
    gravity = 2
    thrust_step = 2
    print(format_state(height, speed, fuel))
    while True:
        command = input()
        if not is_valid_command(command):
            print("Ошибка команды")
            continue
        if command == "exit":
            print("Полет прерван")
            break
        power = int(command)
        if not can_burn(power, fuel):
            print("Недостаточно топлива")
            continue
        height, speed, fuel = simulate_step(
            height, speed, fuel, power, gravity, thrust_step
        )
        print(format_state(height, speed, fuel))
        status = get_status(height, speed)
        if status != "В полете":
            print(status)
            break
main()