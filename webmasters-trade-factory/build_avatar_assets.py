import os
import json

class AvatarAssetBuilder:
    def __init__(self):
        self.workspace = "C:/Users/Wholelychit/Anna-agent/webmasters-trade-factory"
        
        # Define the exact tool components each avatar needs to work without errors
        self.assets = {
            "Anna-WebsiteManager": ["product_catalog.json", "sales_pitch_templates.json"],
            "Maximus-Scraper": ["scraped_raw_cache.json", "national_zip_codes.csv"],
            "Sterling-CFO": ["stripe_ledger_log.json", "payout_forecast.json"],
            "Samantha-Compliance": ["compliance_archive.json", "legal_disclosures_boilerplate.txt"]
        }

    def build_all_required_assets(self):
        print("=======================================================")
        print("🏗️ FABRICATING AUTOMATED ASSET MATRICES FOR LEVEL 4 WORKFORCE")
        print("=======================================================")
        
        # 1. Create a dedicated structural folder to house avatar processing notes
        runtime_dir = os.path.join(self.workspace, "avatar_runtime_data")
        os.makedirs(runtime_dir, exist_ok=True)
        print(f"📁 Initialized secure processing wing path at: {runtime_dir}")

        # 2. Build the baseline data files for each specific avatar
        for avatar, files in self.assets.items():
            print(f"\n⚙️ Staging structural environment for: [{avatar.upper()}]")
            for file_name in files:
                target_file_path = os.path.join(runtime_dir, file_name)
                
                if not os.path.exists(target_file_path):
                    # If it's a JSON database skeleton, write clean bracket layouts
                    if file_name.endswith(".json"):
                        default_structure = {"meta": {"owner": "Gerry Lattray", "assigned_to": avatar}, "data": []}
                        with open(target_file_path, "w", encoding="utf-8") as f:
                            json.dump(default_structure, f, indent=4)
                    else:
                        # Otherwise write an empty structural placeholder text sheet
                        with open(target_file_path, "w", encoding="utf-8") as f:
                            f.write("")
                    print(f"📄 Created clean inventory block: {file_name}")
                else:
                    print(f"✅ Clear: {file_name} already initialized on disk.")

        print("\n=======================================================")
        print("✅ Success: All 4 Avatar work components are built and armed.")
        print("=======================================================")

if __name__ == "__main__":
    builder = AvatarAssetBuilder()
    builder.build_all_required_assets()
