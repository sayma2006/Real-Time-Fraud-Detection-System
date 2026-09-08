import requests
import time
import psutil
import csv

API_URL = "http://127.0.0.1:8000/predict"

transaction = {
    "amount": 850.75,
    "transaction_hour": 2,
    "merchant_category": "Travel",
    "foreign_transaction": 1,
    "location_mismatch": 1,
    "device_trust_score": 25,
    "velocity_last_24h": 10,
    "cardholder_age": 35
}

loads = [10, 50, 100, 500, 1000]


def get_server_process():
    """Find the FastAPI/Uvicorn server process."""
    for process in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            cmdline = " ".join(process.info["cmdline"] or []).lower()

            if "uvicorn" in cmdline and "app:app" in cmdline:
                return psutil.Process(process.info["pid"])

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    raise RuntimeError("FastAPI server process not found.")


results = []

for load in loads:

    server = get_server_process()

    memory_before = server.memory_info().rss / (1024 * 1024)

    start_time = time.perf_counter()

    for _ in range(load):
        response = requests.post(
            API_URL,
            json=transaction
        )

        response.raise_for_status()

    end_time = time.perf_counter()

    server = get_server_process()

    memory_after = server.memory_info().rss / (1024 * 1024)

    total_time = end_time - start_time

    average_time = (total_time / load) * 1000

    throughput = load / total_time

    memory_change = memory_after - memory_before

    results.append([
        load,
        round(average_time, 2),
        round(throughput, 2),
        round(memory_before, 2),
        round(memory_after, 2),
        round(memory_change, 2)
    ])

    print(f"\nLoad: {load} requests")
    print(f"Average Response Time: {average_time:.2f} ms")
    print(f"Throughput: {throughput:.2f} requests/sec")
    print(f"Server Memory Before: {memory_before:.2f} MB")
    print(f"Server Memory After: {memory_after:.2f} MB")
    print(f"Memory Change: {memory_change:.2f} MB")


with open("performance_results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Requests",
        "Average Response Time (ms)",
        "Throughput (requests/sec)",
        "Server Memory Before (MB)",
        "Server Memory After (MB)",
        "Memory Change (MB)"
    ])

    writer.writerows(results)


print("\nPerformance testing completed.")
print("Results saved to performance_results.csv")