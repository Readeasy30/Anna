#!/usr/bin/env python3
# Automated Persistent Tunnel Connection Manager
# Context Boundary: wholelychit

import os
import sys
import time
import subprocess
from android-ops.notifier import SystemNotifier

def manage_tunnel_lifecycle():
    notifier = SystemNotifier()
    retry_delay = 15
    max_consecutive_failures = 5
    failure_count = 0
    
    notifier.dispatch_alert("INFO", "Tunnel-Automation", "Booting background connection monitor pipeline...")
    
    # Target Cloudflare Quick Tunnel command for headless background runtime execution
    tunnel_cmd = ["npx", "wrangler", "tunnel", "--url", "http://localhost:8080"]

    while True:
        try:
            notifier.dispatch_alert("INFO", "Tunnel-Automation", "Spawning secure proxy tunnel instance...")
            
            # Start tunnel as a headless background process
            process = subprocess.Popen(
                tunnel_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            
            # Monitor process actively while it stays alive
            while process.poll() is None:
                time.sleep(5)
                
            # If loop drops out here, the process terminated unexpectedly
            failure_count += 1
            notifier.dispatch_alert("WARNING", "Tunnel-Automation", f"Tunnel disconnected abruptly. Fault Count: {failure_count}/{max_consecutive_failures}")
            
            if failure_count >= max_consecutive_failures:
                notifier.dispatch_alert("CRITICAL", "Tunnel-Automation", "Max connection thresholds breached. Entering cooling hold state...")
                time.sleep(300) # 5-minute cool off before re-attempting core initialization
                failure_count = 0
            else:
                time.sleep(retry_delay)
                
        except KeyboardInterrupt:
            notifier.dispatch_alert("INFO", "Tunnel-Automation", "Manual termination command received. Teardown active.")
            break
        except Exception as e:
            notifier.dispatch_alert("ERROR", "Tunnel-Automation", f"Process supervisor anomaly detected: {str(e)}")
            time.sleep(retry_delay)

if __name__ == "__main__":
    # Ensure correct working directory bounds are mapped npx executions
    os.chdir("C:\\Users\\Wholelychit\\Anna-agent")
    manage_tunnel_lifecycle()
