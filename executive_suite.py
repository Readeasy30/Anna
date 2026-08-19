import json
import os
import random
from datetime import datetime

class ExecutiveSuiteManager:
    def __init__(self):
        self.workspace = "C:/Users/Wholelychit/Anna-agent/webmasters-trade-factory"
        self.leads_db = "showroom_leads.json"
        self.error_log_file = "scraper_error_log.txt"
        
        # Simulated User-Agent header rotation strings to fool target site block rules
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]

    def run_maximus_sales_scraper(self, target_trade="Auto Repair"):
        """Maximus programmatically scrapes shops with full exception-handling skip rules"""
        print("\n🔎 [Maximus-Scraper] Initiating protected market research sweep...")
        
        # Targets for your week-1 run. Note: Shop #2 is a dummy blocker site to test the skip rule
        mock_targets = [
            {"name": "Ozark Precision Auto", "url": "http://ozarkprecisionauto.com", "phone": "417-555-0122", "city": "Springfield"},
            {"name": "Stuck-Up Fake Auto Parts", "url": "http://blockedmechanictest.com", "phone": "417-555-9999", "city": "Branson"},
            {"name": "Tri-Lakes Service Center", "url": "http://trilakesservice.com", "phone": "417-555-0144", "city": "Branson"}
        ]
        
        # Load your central leads tracker file
        database = {"showroom_meta": {}, "leads": []}
        if os.path.exists(self.leads_db):
            with open(self.leads_db, "r", encoding="utf-8") as f:
                try: database = json.load(f)
                except: pass

        existing_names = [lead["shop_name"] for lead in database["leads"]]

        for shop in mock_targets:
            # ADVISOR 1 UPGRADE RULE: Test if a target website triggers a block exception
            if "blockedmechanictest.com" in shop["url"]:
                # Trigger automated defense crash isolation
                error_msg = f"[{datetime.now()}] HTTP 403 Forbidden: Cloudflare WAF bot block triggered at {shop['url']}. Rotating User-Agents...\n"
                with open(os.path.join(self.workspace, self.error_log_file), "a", encoding="utf-8") as err_log:
                    err_log.write(error_msg)
                
                print(f"⚠️ [Maximus-Scraper] Website Block Encountered at {shop['name']}! Exception logged. Skipping node safely...")
                continue # Instantly skips to the next item line without crashing the engine loop

            # If the site passes or is clean, log the lead normally
            if shop["name"] not in existing_names:
                new_lead = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "shop_name": shop["name"],
                    "phone": shop["phone"],
                    "trade": target_trade,
                    "city": shop["city"],
                    "pipeline_status": "staged_for_outreach",
                    "assigned_executive": "Anna-WebsiteManager",
                    "browser_header_used": random.choice(self.user_agents)
                }
                database["leads"].append(new_lead)
                print(f"📌 [Maximus-Scraper] Discovered and logged: {shop['name']} ({shop['city']})")

        with open(self.leads_db, "w", encoding="utf-8") as f:
            json.dump(database, f, indent=4)

    def run_samantha_marketing_push(self):
        """Samantha reads clean files and writes outbound ad content layouts"""
        print("\n📢 [Samantha-Compliance] Vetting pipeline records to build marketing content...")
        if not os.path.exists(self.leads_db): return
        with open(self.leads_db, "r", encoding="utf-8") as f: database = json.load(f)

        for lead in database["leads"]:
            if lead.get("pipeline_status") == "staged_for_outreach":
                campaign_text = f"# Ad Matrix for {lead['shop_name']}\nLocation: {lead['city']}, MO\n\n### Outreach text:\n'Hey {lead['shop_name']}, we have an ultra-fast framework ready for your shop in {lead['city']}!'"
                out_path = os.path.join(self.workspace, f"campaign_{lead['shop_name'].lower().replace(' ', '_')}.md")
                with open(out_path, "w", encoding="utf-8") as f: f.write(campaign_text)
                lead["pipeline_status"] = "campaign_ready"
                print(f"💾 [Samantha-Compliance] Marketing campaign file created for {lead['shop_name']}")

        with open(self.leads_db, "w", encoding="utf-8") as f: json.dump(database, f, indent=4)

    def execute_factory_sweep(self):
        print("=======================================================")
        print("🏭 RUNTIME SUITE NODE | ADVISOR 1 EXCEPTION OVERRIDES ACTIVE")
        print("=======================================================")
        self.run_maximus_sales_scraper()
        self.run_samantha_marketing_push()

if __name__ == "__main__":
    manager = ExecutiveSuiteManager()
    manager.execute_factory_sweep()
