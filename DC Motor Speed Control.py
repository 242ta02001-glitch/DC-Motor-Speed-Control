# DC Motor Speed Control System
# EEE Student GitHub Project

import time

# Motor specifications
MAX_RPM = 3000
MIN_RPM = 0


def calculate_rpm(pwm):
    """Calculate motor RPM from PWM percentage."""
    return (pwm / 100) * MAX_RPM


def motor_status(pwm):
    """Determine motor operating status."""
    if pwm == 0:
        return "STOPPED"
    elif pwm < 30:
        return "LOW SPEED"
    elif pwm < 70:
        return "MEDIUM SPEED"
    else:
        return "HIGH SPEED"


def display_motor_data(pwm):
    """Display motor information."""

    rpm = calculate_rpm(pwm)
    status = motor_status(pwm)

    print("\n" + "=" * 40)
    print("       DC MOTOR SPEED CONTROL")
    print("=" * 40)
    print(f"PWM Duty Cycle : {pwm}%")
    print(f"Motor Speed    : {rpm:.0f} RPM")
    print(f"Motor Status   : {status}")
    print("=" * 40)


def main():

    print("DC Motor Speed Control System")
    print("--------------------------------")

    while True:

        try:
            pwm = float(input("\nEnter PWM value (0-100): "))

            if pwm < 0 or pwm > 100:
                print("Please enter a value between 0 and 100.")
                continue

            display_motor_data(pwm)

            choice = input("\nChange speed? (y/n): ").lower()

            if choice != "y":
                print("\nMotor control system stopped.")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
