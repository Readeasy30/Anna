import json
import os

class AvatarVisualRegistry:
    def __init__(self):
        self.workspace = "C:/Users/Wholelychit/Anna-agent/webmasters-trade-factory"
        self.db_path = "avatar_knowledge_manifest.json"

    def inject_visual_profiles(self):
        if not os.path.exists(self.db_path):
            print("⚠️ Base database file not found. Generating fresh copy...")
            data = {}
        else:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        # Inject the exact visual look configurations into the avatar profiles
        data["website_manager"]["visuals"] = {"sex": "Female", "look": "Sharp Business Attire & Glasses", "color": "#38bdf8", "build": "Fit, Average Height"}
        data["market_scraper"]["visuals"] = {"sex": "Male", "look": "Clean-Cut, Short Beard, Dark Jacket", "color": "#475569", "build": "Tall, Solid Frame"}
        data["financial_auditor"]["visuals"] = {"sex": "Male", "look": "Tailored Corporate Suit, Silver Hair", "color": "#10b981", "build": "Lean, Distinguished"}
        data["compliance_officer"]["visuals"] = {"sex": "Female", "look": "Elegant Professional Blazer, Neat Hair", "color": "#be123c", "build": "Sharp Posture, Balanced"}

        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("🎨 Success: Visual looks, colors, and builds successfully locked into the avatar system registry!")

if __name__ == "__main__":
    registry = AvatarVisualRegistry()
    registry.inject_visual_profiles()
