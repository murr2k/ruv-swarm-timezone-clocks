import tkinter as tk
from tkinter import ttk
import math
import time
import pytz
from datetime import datetime

class AnalogClock:
    def __init__(self, parent, timezone_name, size=150):
        self.parent = parent
        self.timezone_name = timezone_name
        self.timezone = pytz.timezone(timezone_name)
        self.size = size
        self.center_x = size // 2
        self.center_y = size // 2
        self.radius = size // 2 - 10
        
        # Create frame for this clock
        self.frame = ttk.Frame(parent, padding="5")
        
        # Create canvas for the clock
        self.canvas = tk.Canvas(self.frame, width=size, height=size, bg='white')
        self.canvas.pack()
        
        # Create label for timezone name
        self.label = ttk.Label(self.frame, text=self.get_display_name(), 
                              font=('Arial', 8, 'bold'))
        self.label.pack()
        
        # Create time label
        self.time_label = ttk.Label(self.frame, text="", font=('Arial', 7))
        self.time_label.pack()
        
        self.draw_clock_face()
        self.update_time()
    
    def get_display_name(self):
        """Get a shorter display name for the timezone"""
        city_name = self.timezone_name.split('/')[-1].replace('_', ' ')
        return city_name
    
    def draw_clock_face(self):
        """Draw the static parts of the clock face"""
        # Clear canvas
        self.canvas.delete("all")
        
        # Draw outer circle
        self.canvas.create_oval(10, 10, self.size-10, self.size-10, 
                               outline='black', width=2)
        
        # Draw hour markers
        for i in range(12):
            angle = i * 30 * math.pi / 180
            x1 = self.center_x + (self.radius - 15) * math.sin(angle)
            y1 = self.center_y - (self.radius - 15) * math.cos(angle)
            x2 = self.center_x + (self.radius - 5) * math.sin(angle)
            y2 = self.center_y - (self.radius - 5) * math.cos(angle)
            
            self.canvas.create_line(x1, y1, x2, y2, width=3, fill='black')
        
        # Draw minute markers
        for i in range(60):
            if i % 5 != 0:  # Skip hour markers
                angle = i * 6 * math.pi / 180
                x1 = self.center_x + (self.radius - 8) * math.sin(angle)
                y1 = self.center_y - (self.radius - 8) * math.cos(angle)
                x2 = self.center_x + (self.radius - 3) * math.sin(angle)
                y2 = self.center_y - (self.radius - 3) * math.cos(angle)
                
                self.canvas.create_line(x1, y1, x2, y2, width=1, fill='gray')
        
        # Draw numbers
        for i in range(1, 13):
            angle = i * 30 * math.pi / 180
            x = self.center_x + (self.radius - 25) * math.sin(angle)
            y = self.center_y - (self.radius - 25) * math.cos(angle)
            
            self.canvas.create_text(x, y, text=str(i), font=('Arial', 10, 'bold'))
    
    def update_time(self):
        """Update the clock hands based on current time in timezone"""
        # Get current time in this timezone
        utc_now = datetime.now(pytz.UTC)
        local_time = utc_now.astimezone(self.timezone)
        
        # Update time label
        time_str = local_time.strftime("%H:%M:%S")
        date_str = local_time.strftime("%m/%d")
        self.time_label.config(text=f"{time_str}\n{date_str}")
        
        # Remove old hands
        self.canvas.delete("hands")
        
        # Calculate angles for hands
        hour = local_time.hour % 12
        minute = local_time.minute
        second = local_time.second
        
        # Hour hand
        hour_angle = (hour + minute/60) * 30 * math.pi / 180
        hour_x = self.center_x + (self.radius - 40) * math.sin(hour_angle)
        hour_y = self.center_y - (self.radius - 40) * math.cos(hour_angle)
        self.canvas.create_line(self.center_x, self.center_y, hour_x, hour_y, 
                               width=4, fill='black', tags="hands")
        
        # Minute hand
        minute_angle = minute * 6 * math.pi / 180
        minute_x = self.center_x + (self.radius - 20) * math.sin(minute_angle)
        minute_y = self.center_y - (self.radius - 20) * math.cos(minute_angle)
        self.canvas.create_line(self.center_x, self.center_y, minute_x, minute_y, 
                               width=3, fill='blue', tags="hands")
        
        # Second hand
        second_angle = second * 6 * math.pi / 180
        second_x = self.center_x + (self.radius - 10) * math.sin(second_angle)
        second_y = self.center_y - (self.radius - 10) * math.cos(second_angle)
        self.canvas.create_line(self.center_x, self.center_y, second_x, second_y, 
                               width=1, fill='red', tags="hands")
        
        # Center dot
        self.canvas.create_oval(self.center_x-3, self.center_y-3, 
                               self.center_x+3, self.center_y+3, 
                               fill='black', tags="hands")
    
    def pack(self, **kwargs):
        """Pack the clock frame"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """Grid the clock frame"""
        self.frame.grid(**kwargs)