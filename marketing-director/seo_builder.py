import os

class SEODirector:
    def __init__(self):
        self.showroom_path = "C:/Users/Wholelychit/Anna-agent/website-factory-core/index.html"
        # High-converting keywords tailored for your business solutions
        self.seo_tags = """
    <!-- Premium SEO Optimization Strings -->
    <meta name="description" content="Deploy highly capable, open-source AI employees in 73 hours. Premium automated workforce solutions provided by Webmasters LLC.">
    <meta name="keywords" content="Webmasters LLC, AI Avatars, Autonomous Agents, Open Source AI, Business Automation, 24-Hour Deployment">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Webmasters LLC | AI Employee Showroom">
    <meta property="og:description" content="Scale operations instantly with Level 1 to Level 4 autonomous digital workers.">
    <meta property="og:type" content="website">
"""

    def inject_seo_tags(self):
        print("📢 Initiating search engine optimization sweep...")
        
        if not os.path.exists(self.showroom_path):
            print("❌ Target error: Showroom index.html file not found in factory core.")
            return

        # Read your current showroom HTML file content
        with open(self.showroom_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Check if the SEO tags are already there to avoid duplicates
        if "Premium SEO Optimization" in html_content:
            print("✅ Status clear: Showroom page already contains active SEO tags.")
            return

        # Safely insert the optimization meta tags right under the <head> tag block
        if "<head>" in html_content:
            updated_html = html_content.replace("<head>", f"<head>\n{self.seo_tags}")
            
            with open(self.showroom_path, "w", encoding="utf-8") as f:
                f.write(updated_html)
            print("💾 Success: Premium SEO meta metadata injected into your showroom storefront page!")
        else:
            print("⚠️ Parsing warning: Valid HTML5 <head> token boundary marker not identified.")

if __name__ == "__main__":
    director = SEODirector()
    director.inject_seo_tags()
