# ----------------------------------------------
# Project ProductionTester
# V0.1
# data_logging/result_writer.py
# ----------------------------------------------

import os
from datetime import datetime


class ResultWriter:
    def __init__(self, base_path, tester_id="Tester01"):
        self.base_path = base_path
        self.tester_id = tester_id

    def _current_csv(self):
        month = datetime.now().strftime("%Y-%m")
        return f"{self.base_path}/results_{month}.csv"

    def _ensure_header(self, file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Timestamp,PPID,TesterID,Current,Temperature,Result\n")

    def write_result(self, ppid, result, data_dict):
        """
        data_dict must contain:
            - current_mA
            - temperature_C
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_path = self._current_csv()

        self._ensure_header(file_path)

        current = data_dict.get("current_mA", "")
        temp = data_dict.get("temperature_C", "")

        line = (
            f"{timestamp},"
            f"{ppid},"
            f"{self.tester_id},"
            f"{current:.3f},"
            f"{temp:.2f},"
            f"{result}\n"
        )

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(line)
