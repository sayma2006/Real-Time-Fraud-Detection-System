import pandas as pd
import matplotlib.pyplot as plt
import os

# Read performance results
df = pd.read_csv("performance_results.csv")

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# -------------------------------
# Graph 1: Inference Time
# -------------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    df["Requests"],
    df["Average Response Time (ms)"],
    marker="o"
)

plt.xlabel("Number of Requests")
plt.ylabel("Average Response Time (ms)")
plt.title("Inference Time vs Number of Requests")
plt.grid(True)

plt.savefig(
    "graphs/inference_time.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -------------------------------
# Graph 2: Memory Usage
# -------------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    df["Requests"],
    df["Server Memory After (MB)"],
    marker="o"
)

plt.xlabel("Number of Requests")
plt.ylabel("Server Memory Usage (MB)")
plt.title("Memory Usage vs Number of Requests")
plt.grid(True)

plt.savefig(
    "graphs/memory_usage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Graphs created successfully!")
print("Saved inside the graphs folder.")