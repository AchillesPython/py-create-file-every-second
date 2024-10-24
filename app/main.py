from datetime import datetime
from time import sleep


def create_log_file() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as file:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    create_log_file()
