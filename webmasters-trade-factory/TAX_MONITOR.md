# 📊 Webmasters LLC | Automated Tax Monitor Document
**Prepared for:** Sterling-CFO (Financial Manager Persona Node)
**Business Origin:** Missouri, USA (Webmasters LLC Registered)

## 🏢 1. Missouri State Tax Rules (In-State Sales)
*   **The Rule:** Missouri does not charge sales tax on digital software leases, website rentals, or cloud SaaS items.
*   **Missouri Buyers:** You do not charge or collect sales tax for clients located inside Missouri.
*   **Physical Media Exception:** If you deliver code on a physical USB drive or disc, it becomes physical property and becomes taxable. Always deliver digitally online.

---

## 🇺🇸 2. Out-of-State Sales Tax Matrix
When selling to auto shops across state lines, you only collect tax if you hit that state's "Economic Nexus" limit (typically $100,000 in sales or 200 separate transactions).

### 🟥 Fully Taxable States (Cloud Software / Leases)
*   New York, Washington, Pennsylvania, Arizona, Massachusetts, Utah.

### 🟨 Partially Taxable States
*   **Texas:** Only taxes 80% of the software lease price.
*   **Connecticut:** Charges a lower tax rate if the buyer is a registered business.

### 🟩 Strictly Non-Taxable States
*   California (Exempt until 2027), Florida, Virginia, Missouri.

---

## 💳 3. What Stripe Does (Automated Tracking)
Your Stripe integration includes built-in tools to automate this entire tracking framework:

*   **Location Sourcing:** Stripe automatically reads the client's credit card and billing address to find their exact tax region.
*   **Threshold Monitoring:** Stripe watches your sales volume in every state and displays dashboard warnings when you approach a state's economic limit.
*   **Automatic Checkout Tax:** Once activated and mapped to a digital product code, Stripe automatically calculates and adds the correct state tax onto the client invoice at checkout.
