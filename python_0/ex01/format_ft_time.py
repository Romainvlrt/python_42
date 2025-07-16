import time
from datetime import datetime

timestamp = time.time()
formated = f"{timestamp:,.4f}"
scientific = f"{timestamp:.2e}"
today = datetime.now().strftime("%b %d %Y") 

print("Seconds since January 1, 1970:", formated, "or", scientific, "in scientific notation")
print(today)