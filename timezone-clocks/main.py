import tkinter as tk
from tkinter import ttk
import pytz
from analog_clock import AnalogClock

class TimezoneClockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("24 Timezone Analog Clocks")
        self.root.geometry("1200x800")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # List of 24 major timezones representing different hours
        self.timezones = [
            'Pacific/Midway',      # UTC-11
            'Pacific/Honolulu',    # UTC-10
            'US/Alaska',           # UTC-9
            'US/Pacific',          # UTC-8
            'US/Mountain',         # UTC-7
            'US/Central',          # UTC-6
            'US/Eastern',          # UTC-5
            'America/Caracas',     # UTC-4
            'America/Argentina/Buenos_Aires',  # UTC-3
            'America/Sao_Paulo',   # UTC-3
            'Atlantic/South_Georgia',  # UTC-2
            'Atlantic/Azores',     # UTC-1
            'UTC',                 # UTC+0
            'Europe/London',       # UTC+0/+1
            'Europe/Paris',        # UTC+1
            'Africa/Cairo',        # UTC+2 (Fixed: was Europe/Cairo)
            'Europe/Moscow',       # UTC+3
            'Asia/Dubai',          # UTC+4
            'Asia/Karachi',        # UTC+5
            'Asia/Dhaka',          # UTC+6
            'Asia/Bangkok',        # UTC+7
            'Asia/Shanghai',       # UTC+8
            'Asia/Tokyo',          # UTC+9
            'Australia/Sydney',    # UTC+10
            'Pacific/Noumea',      # UTC+11
            'Pacific/Auckland',    # UTC+12
        ]
        
        # Take first 24 timezones and validate them
        self.timezones = self.timezones[:24]
        self.validate_timezones()
        
        self.clocks = []
        self.create_widgets()
        self.update_all_clocks()
    
    def validate_timezones(self):
        """Validate all timezones and replace invalid ones"""
        valid_timezones = []
        all_timezones = list(pytz.all_timezones)
        
        for tz in self.timezones:
            if tz in all_timezones:
                valid_timezones.append(tz)
            else:
                print(f"Warning: Invalid timezone '{tz}', skipping...")
        
        # Fill up to 24 with additional valid timezones if needed
        backup_timezones = [
            'America/New_York', 'America/Los_Angeles', 'America/Chicago',
            'America/Denver', 'Europe/Berlin', 'Europe/Rome', 'Asia/Kolkata',
            'Asia/Singapore', 'Australia/Melbourne', 'Pacific/Fiji'
        ]
        
        for backup_tz in backup_timezones:
            if len(valid_timezones) >= 24:
                break
            if backup_tz not in valid_timezones and backup_tz in all_timezones:
                valid_timezones.append(backup_tz)
        
        self.timezones = valid_timezones[:24]
        print(f"Using {len(self.timezones)} valid timezones")
    
    def create_widgets(self):
        """Create all the clock widgets"""
        # Create main frame with scrollbar
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create title
        title_label = ttk.Label(main_frame, text="24 Timezone Analog Clocks", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=10)
        
        # Create canvas and scrollbar for scrolling
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create grid of clocks (6 columns, 4 rows)
        for i, timezone in enumerate(self.timezones):
            row = i // 6
            col = i % 6
            
            try:
                # Validate timezone before creating clock
                pytz.timezone(timezone)  # This will raise exception if invalid
                clock = AnalogClock(scrollable_frame, timezone, size=150)
                clock.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                self.clocks.append(clock)
                print(f"Created clock for {timezone}")
            except Exception as e:
                print(f"Error creating clock for {timezone}: {e}")
                # Create a placeholder label instead
                error_frame = ttk.Frame(scrollable_frame, padding="5")
                error_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                error_label = ttk.Label(error_frame, text=f"Error:\n{timezone.split('/')[-1]}", 
                                       font=('Arial', 8), foreground='red')
                error_label.pack()
        
        # Configure grid weights
        for i in range(6):
            scrollable_frame.columnconfigure(i, weight=1)
        for i in range(4):
            scrollable_frame.rowconfigure(i, weight=1)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def update_all_clocks(self):
        """Update all clocks every second"""
        for clock in self.clocks:
            try:
                clock.update_time()
            except Exception as e:
                print(f"Error updating clock: {e}")
        
        # Schedule next update
        self.root.after(1000, self.update_all_clocks)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = TimezoneClockApp()
    app.run()