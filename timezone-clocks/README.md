# 24 Timezone Analog Clocks

A Windows GUI application that displays 24 analog clocks showing different time zones around the world.

## Features

- 24 analog clocks arranged in a 6x4 grid
- Real-time updates every second
- Each clock shows a different timezone
- Displays both analog clock face and digital time
- Scrollable interface for easy viewing
- Timezone names and dates displayed

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pytz library for timezone handling

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Timezones Included

The application displays clocks for 24 major timezones representing different UTC offsets:

- Pacific/Midway (UTC-11)
- Pacific/Honolulu (UTC-10)
- US/Alaska (UTC-9)
- US/Pacific (UTC-8)
- US/Mountain (UTC-7)
- US/Central (UTC-6)
- US/Eastern (UTC-5)
- America/Caracas (UTC-4)
- America/Argentina/Buenos_Aires (UTC-3)
- America/Sao_Paulo (UTC-3)
- Atlantic/South_Georgia (UTC-2)
- Atlantic/Azores (UTC-1)
- UTC (UTC+0)
- Europe/London (UTC+0/+1)
- Europe/Paris (UTC+1)
- Africa/Cairo (UTC+2)
- Europe/Moscow (UTC+3)
- Asia/Dubai (UTC+4)
- Asia/Karachi (UTC+5)
- Asia/Dhaka (UTC+6)
- Asia/Bangkok (UTC+7)
- Asia/Shanghai (UTC+8)
- Asia/Tokyo (UTC+9)
- Australia/Sydney (UTC+10)

## Controls

- Use mouse wheel to scroll through the clocks
- Each clock updates automatically every second
- Clock hands: Black (hour), Blue (minute), Red (second)

## Structure

- `main.py`: Main application window and timezone management
- `analog_clock.py`: Individual analog clock widget implementation
- `requirements.txt`: Python dependencies