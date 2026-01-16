class DeviceLogger:
    def __init__(self, base_path):
        self.base_path = base_path

    def _current_logfile(self):
        from datetime import datetime

        month = datetime.now().strftime("%Y-%m")
        return f"{self.base_path}/device_log_{month}.log"

    def write(self, message: str):
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} | {message}\n"
        with open(self._current_logfile(), "a", encoding="utf-8") as f:
            f.write(line)
