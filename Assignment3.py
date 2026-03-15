from collections import deque

# 1. Initialize
application_inbox = deque()      # Queue (FIFO)
processed_history = []           # Stack (LIFO)

# 2. Ingest Data
raw_data = ["e.g. TechCorp", "bio-gen", "  AlphaTech ", "NextGen  "]

for item in raw_data:
    clean_item = item.lower().strip()
    application_inbox.append(clean_item)

# 3. Process (FIFO)
while application_inbox:
    company = application_inbox.popleft()   # remove first item in queue
    print("Approving:", company)
    processed_history.append(company)       # push to stack

# 4. Undo (LIFO)
if processed_history:
    last_item = processed_history.pop()     # remove last item
    print("Reverting approval for:", last_item)