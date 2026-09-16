# Beau-T-Cloud Website Development Script
## Frappe / ERPNext v16 — Cursor Master Prompt

> **Current status**
>
> - ERPNext / Frappe v16 site already exists
> - ERPNext is already installed
> - Custom app `beautcloud_website` has already been created
> - Do **not** create a new site
> - Do **not** reinstall ERPNext
> - Work only inside the existing `beautcloud_website` app

---

# 1. Open the App in Cursor

Open this folder in Cursor:

```bash
/home/frappe/frappe-bench/apps/beautcloud_website
```

Before using the master prompt, confirm the app is installed on your existing site:

```bash
cd /home/frappe/frappe-bench

bench --site YOUR_EXISTING_SITE_NAME list-apps
```

You should see:

```text
frappe
erpnext
beautcloud_website
```

If `beautcloud_website` is not listed, install only the custom app:

```bash
bench --site YOUR_EXISTING_SITE_NAME install-app beautcloud_website
```

Replace `YOUR_EXISTING_SITE_NAME` with your actual Frappe site name.

---

# 2. Cursor Master Prompt

Copy everything below into Cursor.

---

```text
You are working inside an existing Frappe / ERPNext v16 custom application.

APP NAME:
beautcloud_website

PRODUCT:
Beau-T-Cloud

PRODUCTION DOMAIN:
https://beautcloud.com

COMPANY:
Printechs

IMPORTANT CURRENT STATUS:

- The Frappe / ERPNext v16 site already exists.
- ERPNext is already installed.
- The custom app beautcloud_website already exists.
- Do NOT create a new Frappe site.
- Do NOT install ERPNext again.
- Do NOT run bench new-site.
- Do NOT run bench new-app.
- Do NOT modify Frappe core.
- Do NOT modify ERPNext core.
- Work only inside the beautcloud_website custom app.

==================================================
PROJECT GOAL
==================================================

Build the complete production-quality public website for:

Beau-T-Cloud

Beau-T-Cloud is a cloud-based Salon and Beauty Business
Management Operating System.

The website should be:

- premium
- elegant
- modern
- beauty-focused
- professional
- SEO-friendly
- mobile responsive
- fast
- easy to maintain
- suitable for Saudi Arabia and GCC markets

The site must not look like a generic ERP website.

The product UI should be the main visual focus.

==================================================
TECHNOLOGY
==================================================

Use only Frappe / ERPNext v16-compatible approaches.

Use:

- Frappe v16 Website
- Jinja templates
- server-rendered pages
- HTML5
- CSS / SCSS
- Vanilla JavaScript
- Frappe APIs when needed
- reusable template includes
- semantic HTML
- responsive design

Do NOT create a React SPA.

Do NOT create client-side routing.

Do NOT add unnecessary JavaScript frameworks.

Do NOT use external dependencies unless they are genuinely required.

==================================================
BRAND
==================================================

Brand name:

Beau-T-Cloud

Official writing:

Beau-T-Cloud

Logo wording may remain:

BEAU-T-CLOUD

Primary brand color:

#FF1B9A

Hover / secondary pink:

#FF6ED1

Light background:

#FCEFF5

White:

#FFFFFF

Dark plum:

#2E1A2F

Optional neutral colors:

#FAFAFA
#F5F5F5
#747474

Typography:

Headings:
Montserrat

Body:
Inter

Fallback:
Arial, sans-serif

Recommended color usage:

70% white / light
20% dark plum
10% pink

Do NOT make large portions of the website bright pink.

Design personality:

- premium
- beautiful
- refined
- clean
- spacious
- modern SaaS
- professional B2B
- beauty industry focused

Avoid:

- neon design
- sci-fi effects
- excessive gradients
- excessive glassmorphism
- generic Bootstrap appearance
- generic ERP appearance
- excessive animation
- childish beauty design

==================================================
MAIN POSITIONING
==================================================

Main H1:

Run your beauty business beautifully.

Supporting message:

One Cloud. Every Part of Your Beauty Business.

Main product description:

Beau-T-Cloud is a connected cloud platform for salons,
spas and beauty businesses that brings appointments,
clients, staff, POS, inventory, memberships, loyalty
and business insights together in one system.

==================================================
NO FAKE CONTENT
==================================================

Never generate or publish:

- fake customer statistics
- fake customer names
- fake testimonials
- fake founders
- fake company history
- fake awards
- fake reviews
- fake case studies
- fake uptime guarantees
- fake security certifications
- fake country counts
- fake appointment counts
- fake revenue numbers
- fabricated partner logos

If factual information has not been provided,
use a neutral placeholder or omit the claim.

==================================================
SITE STRUCTURE
==================================================

Create the following public routes:

/

/features

/features/appointment-management
/features/online-booking
/features/salon-pos
/features/client-crm
/features/staff-management
/features/inventory-management
/features/memberships-loyalty
/features/multi-location
/features/reports-analytics

/solutions

/solutions/hair-salon
/solutions/beauty-salon
/solutions/nail-salon
/solutions/spa
/solutions/barbershop
/solutions/multi-branch

/product-tour
/pricing
/about
/contact
/book-demo

Also prepare structure for future:

/resources
/blog
/privacy-policy
/terms

Do not create fake blog posts.

==================================================
SUGGESTED APP STRUCTURE
==================================================

Keep everything inside the custom app.

Recommended structure:

beautcloud_website/
    beautcloud_website/
        hooks.py

        public/
            css/
                beautcloud.css

            js/
                beautcloud.js

            images/
                logo/
                hero/
                screenshots/
                features/
                solutions/
                icons/

        templates/
            includes/
                navbar.html
                footer.html
                demo_cta.html
                feature_card.html
                section_heading.html

            layouts/
                beautcloud.html

        www/
            index.html

            features/
                index.html
                appointment-management.html
                online-booking.html
                salon-pos.html
                client-crm.html
                staff-management.html
                inventory-management.html
                memberships-loyalty.html
                multi-location.html
                reports-analytics.html

            solutions/
                index.html
                hair-salon.html
                beauty-salon.html
                nail-salon.html
                spa.html
                barbershop.html
                multi-branch.html

            product-tour.html
            pricing.html
            about.html
            contact.html
            book-demo.html

Do not duplicate navbar/footer markup across pages.

Use reusable includes.

==================================================
GLOBAL NAVIGATION
==================================================

Create a reusable sticky navigation bar.

Left:

Beau-T-Cloud logo

Main navigation:

Product
Solutions
Pricing
Resources
About

Right side:

Login
Book a Demo

Product dropdown:

Appointment Management
Online Booking
Client CRM
Salon POS
Staff & Commission
Inventory Management
Memberships & Loyalty
Multi-Location
Reports & Analytics

Solutions dropdown:

Hair Salons
Beauty Salons
Nail Studios
Spas
Barbershops
Multi-Branch Groups

Navigation requirements:

- sticky
- responsive
- mobile hamburger
- keyboard accessible
- proper focus states
- dropdowns work on desktop
- mobile menu works cleanly
- navigation becomes slightly compact after scroll

Do not use overly complex animation.

==================================================
HOME PAGE
==================================================

Build the homepage in the following order.

--------------------------------------------------
SECTION 1 — HERO
--------------------------------------------------

Eyebrow:

THE OPERATING SYSTEM FOR MODERN BEAUTY BUSINESSES

H1:

Run your beauty business beautifully.

Description:

Manage appointments, clients, staff, POS, inventory,
memberships, loyalty and multiple locations from one
connected cloud platform.

Primary CTA:

Book a Demo

Secondary CTA:

Explore the Platform

Trust points:

Cloud-Based
Multi-Location
Real-Time Insights

Hero visual:

The software UI must be the main hero.

Prepare these asset locations:

/assets/beautcloud_website/images/screenshots/dashboard.webp
/assets/beautcloud_website/images/screenshots/calendar.webp
/assets/beautcloud_website/images/screenshots/mobile-booking.webp

If the real images do not exist yet,
show elegant branded UI placeholders.

Do not use random dashboard screenshots from another product.

--------------------------------------------------
SECTION 2 — BUSINESS TYPES
--------------------------------------------------

Heading:

Built for every kind of beauty business

Cards:

Hair Salon
Beauty Salon
Nail Studio
Spa & Wellness
Barbershop
Multi-Branch Beauty Group

Each card must link to the relevant solution page.

--------------------------------------------------
SECTION 3 — CONNECTED CUSTOMER JOURNEY
--------------------------------------------------

Heading:

One Cloud. Every Part of Your Beauty Business.

Show a connected journey:

Book
→
Welcome
→
Serve
→
Pay
→
Reward
→
Rebook

Use subtle Beau-T-Cloud-inspired connection lines.

Do not use futuristic glowing circuit effects.

--------------------------------------------------
SECTION 4 — APPOINTMENTS & ONLINE BOOKING
--------------------------------------------------

Feature items:

Smart calendar
Online booking
Employee availability
Service duration
Rooms / resources
Waiting list
Rescheduling
Appointment reminders

Include a large screenshot area.

--------------------------------------------------
SECTION 5 — CLIENT CRM
--------------------------------------------------

Feature items:

Customer profile
Visit history
Service history
Preferences
Retail purchase history
Packages
Membership
Loyalty
Notes

Show a premium CRM screenshot area.

--------------------------------------------------
SECTION 6 — SALON POS & PAYMENTS
--------------------------------------------------

Feature items:

Services
Retail products
Discounts
Packages
Memberships
Gift cards
Multiple payment methods
Returns
Receipts

Do not claim support for a specific payment gateway unless confirmed.

--------------------------------------------------
SECTION 7 — STAFF & COMMISSION
--------------------------------------------------

Feature items:

Staff roster
Attendance
Working hours
Service commission
Retail commission
Targets
Performance
Productivity

--------------------------------------------------
SECTION 8 — INVENTORY & RETAIL
--------------------------------------------------

Feature items:

Retail inventory
Professional-use inventory
Purchasing
Stock transfers
Low-stock alerts
Branch stock
Stock movement

--------------------------------------------------
SECTION 9 — MULTI-LOCATION MANAGEMENT
--------------------------------------------------

Heading:

One salon or an entire beauty group.

Description:

Manage every location independently while maintaining
real-time management visibility across the entire business.

Dashboard examples:

Revenue
Appointments
Staff
Inventory
Customers
Branch performance

This section should feel enterprise-grade.

--------------------------------------------------
SECTION 10 — ANALYTICS
--------------------------------------------------

Show a branded management dashboard concept with:

Today's Revenue
Today's Appointments
Occupancy
Average Ticket
New Customers
Repeat Customers
Top Services
Top Employees
Retail Sales
Branch Comparison

Use SAR in examples.

Do not invent real company results.

--------------------------------------------------
SECTION 11 — SAUDI ARABIA & GCC
--------------------------------------------------

Heading:

Built for Beauty Businesses in Saudi Arabia and the GCC

Feature areas:

Arabic & English
SAR / GCC currencies
VAT-ready workflows
Multi-branch operations
WhatsApp/SMS readiness
Local payment integrations
Local implementation and support

Important:

Do not claim an integration is already operational unless confirmed.

Do not advertise ZATCA integration unless specifically approved later.

--------------------------------------------------
SECTION 12 — GETTING STARTED
--------------------------------------------------

Heading:

Getting started is simple.

Steps:

1. Book a Demo
2. Configure Your Business
3. Start Managing Smarter

--------------------------------------------------
SECTION 13 — FAQ
--------------------------------------------------

Create accessible accordion FAQ components.

Topics:

Cloud software
Multi-location
Data migration
Training
Data ownership
User access
Mobile access
Support

Do not make unsupported legal or security promises.

--------------------------------------------------
SECTION 14 — FINAL CTA
--------------------------------------------------

Heading:

Ready to run your beauty business beautifully?

Buttons:

Book a Demo
Contact Us

==================================================
FEATURE PAGES
==================================================

Create dedicated SEO pages for each major feature.

Every feature page should include:

1. Hero
2. Business problem
3. Beau-T-Cloud solution
4. Key capabilities
5. Product screenshot
6. Business benefits
7. Related features
8. Book a Demo CTA
9. FAQ when useful

Required pages:

Appointment Management
Online Booking
Salon POS
Client CRM
Staff & Commission
Inventory Management
Memberships & Loyalty
Multi-Location
Reports & Analytics

Avoid repeating identical copy across all pages.

==================================================
SOLUTION PAGES
==================================================

Create dedicated pages for:

Hair Salons
Beauty Salons
Nail Studios
Spas
Barbershops
Multi-Branch Beauty Groups

Each page should explain:

- the operational challenges for that business type
- how Beau-T-Cloud helps
- relevant feature modules
- typical workflow
- multi-location capability when relevant
- Book a Demo CTA

Do not invent customer results.

==================================================
BOOK A DEMO FORM
==================================================

Create a professional Book a Demo form.

Fields:

Full Name
Business Name
Email
Mobile
Country
City
Business Type
Number of Branches
Number of Employees
Current Software
Message

Required:

Full Name
Business Name
Mobile or Email

==================================================
ERPNext LEAD INTEGRATION
==================================================

When the Book a Demo form is submitted,
create an ERPNext Lead.

Use a secure Frappe whitelisted server-side method.

Recommended mapping:

lead_name = Full Name
company_name = Business Name
email_id = Email
mobile_no = Mobile
source = Beau-T-Cloud Website

For:

Country
City
Business Type
Number of Branches
Number of Employees
Current Software
Message

either:

- map to suitable existing/custom Lead fields
or
- append cleanly to Lead notes/comments

Do not create unnecessary custom fields automatically
without first checking whether suitable fields already exist.

Validate all submitted data server-side.

Protect against:

- XSS
- empty submissions
- invalid email
- invalid phone input
- rapid repeat submissions
- spam
- accidental duplicate submissions

Never expose direct database operations in browser JavaScript.

Return a polished success message.

==================================================
CONTACT PAGE
==================================================

Create a clean contact page.

Use configurable contact information.

Do not hardcode fake:

- emails
- telephone numbers
- locations
- addresses

Prepare clearly marked variables/placeholders
so real contact details can be added later.

==================================================
PRICING PAGE
==================================================

Create the page structure.

Important:

Do not invent subscription prices.

Until actual pricing is provided,
use a consultation/demo-oriented structure such as:

Plans for every stage of your beauty business

Single Location
Growing Business
Multi-Location / Enterprise

Use:

Contact Sales
Book a Demo

instead of fake prices.

==================================================
ABOUT PAGE
==================================================

Do not invent a Beau-T-Cloud founder story.

Position Beau-T-Cloud factually as a Printechs solution.

Use verified text only.

Suggested direction:

Beau-T-Cloud is developed to help modern salons,
spas and beauty businesses simplify daily operations
and gain better control over customers, appointments,
staff, sales, inventory and business performance.

Do not add founding dates or customer counts unless provided.

==================================================
FOOTER
==================================================

Create a premium reusable footer.

Include:

Beau-T-Cloud logo

Columns:

Product
Solutions
Company
Resources
Legal

Bottom text:

© current year Beau-T-Cloud.
A Printechs solution.

Use the current year dynamically.

Do not hardcode fake contact information.

==================================================
SEO
==================================================

Every page must have:

- unique SEO title
- unique meta description
- canonical URL
- OpenGraph title
- OpenGraph description
- OpenGraph image support
- Twitter card support

Homepage SEO title:

Beauty Salon Management Software Saudi Arabia | Beau-T-Cloud

Homepage meta description:

Beau-T-Cloud is an all-in-one salon and beauty business
management platform for appointments, clients, POS,
staff, inventory, memberships, loyalty and multi-location
operations.

Use:

- one H1 per page
- logical H2/H3 hierarchy
- descriptive internal links
- descriptive image alt text

Create JSON-LD where appropriate:

SoftwareApplication
Organization
FAQPage

Do not add:

- fake AggregateRating
- fake Review schema
- fake customer counts

==================================================
SEO URL RULES
==================================================

Keep URLs:

- lowercase
- short
- readable
- descriptive
- hyphenated

Do not use query-string routes for core content pages.

==================================================
PERFORMANCE
==================================================

Target:

Lighthouse Performance > 90
Accessibility > 90
SEO > 95
Best Practices > 90

Use:

- WebP / AVIF where practical
- image lazy loading
- responsive image dimensions
- minimal JS
- CSS variables
- reusable CSS
- proper cacheable assets
- no large frontend frameworks
- no unnecessary animation libraries

Avoid layout shift.

Define image width and height where possible.

==================================================
ACCESSIBILITY
==================================================

Implement:

- semantic landmarks
- keyboard navigation
- visible focus states
- form labels
- accessible dropdowns
- accessible accordions
- meaningful alt text
- adequate color contrast
- ARIA only where needed

Respect:

prefers-reduced-motion

==================================================
RESPONSIVE DESIGN
==================================================

Test these widths:

375px
390px
430px
768px
1024px
1440px
1920px

Mobile must be intentionally designed.

Do not simply shrink desktop layouts.

==================================================
ANIMATION
==================================================

Use only subtle animation:

- small fade-in
- gentle slide
- small hover lift
- subtle UI movement

Avoid:

- excessive parallax
- bouncing elements
- glowing effects
- heavy scroll animation
- large animation libraries

==================================================
FRAPPE / ERPNext v16 RULES
==================================================

Before editing:

- inspect the existing app
- inspect hooks.py
- inspect current templates
- inspect existing www files
- inspect Frappe v16 website conventions already available in this bench

Follow Frappe v16 conventions.

Do not assume older Frappe v14/v15 behavior when v16 differs.

Do not modify:

frappe/
erpnext/

Only modify:

beautcloud_website/

If a framework-specific implementation is uncertain,
inspect the installed Frappe v16 code or documentation patterns
available in the current bench before implementing.

==================================================
BUILD & VALIDATION
==================================================

After each major phase run:

bench build --app beautcloud_website

If the build fails:

- stop
- show the exact error
- identify the relevant file
- fix only what is required
- rerun the build

Do not hide build errors.

When appropriate, also recommend:

bench --site YOUR_SITE_NAME clear-cache

and:

bench --site YOUR_SITE_NAME clear-website-cache

Do not automatically run destructive database commands.

Do not automatically run production setup.

Do not automatically change Nginx.

Do not automatically install SSL.

==================================================
IMPLEMENTATION PHASES
==================================================

PHASE 1 — INSPECTION ONLY

First inspect the current beautcloud_website app.

Report:

1. current app directory structure
2. current hooks.py
3. current public assets
4. existing templates
5. existing www pages
6. files that need to be created
7. files that need to be modified
8. any Frappe v16-specific considerations

Do not write code yet.

Stop after Phase 1 and wait for approval.

==================================================

PHASE 2 — GLOBAL DESIGN + HOME PAGE

After approval, create:

- CSS design system
- base layout
- navbar
- dropdown navigation
- mobile navigation
- footer
- reusable components
- complete homepage

After Phase 2 run:

bench build --app beautcloud_website

Report the result.

==================================================

PHASE 3 — FEATURE PAGES

Build all feature pages.

Use reusable templates/components.

Add page-specific SEO.

Run build and report.

==================================================

PHASE 4 — SOLUTION PAGES

Build all solution pages.

Use reusable templates/components.

Add page-specific SEO.

Run build and report.

==================================================

PHASE 5 — BOOK DEMO + ERPNext LEAD

Create:

- Book a Demo page
- frontend form
- server-side validation
- secure whitelisted Frappe method
- ERPNext Lead creation
- success/error UX

Do not expose database logic to browser code.

Run build and report.

==================================================

PHASE 6 — OTHER PAGES

Build:

- Product Tour
- Pricing
- About
- Contact

Add required metadata.

Run build and report.

==================================================

PHASE 7 — SEO / ACCESSIBILITY / PERFORMANCE

Complete:

- SEO metadata
- canonical tags
- OpenGraph
- Twitter metadata
- JSON-LD
- accessibility
- responsive review
- image optimization
- performance cleanup

Run build and report.

==================================================

PHASE 8 — FINAL REVIEW

Review the complete app.

Provide:

- complete list of created files
- complete list of modified files
- routes created
- remaining placeholders
- screenshots still required
- contact details still required
- pricing information still required
- integrations not yet confirmed
- production deployment steps
- final test checklist

Do not perform production deployment automatically.

==================================================
START NOW
==================================================

Start with:

PHASE 1 — INSPECTION ONLY.

Do not code yet.
```

---

# 3. After Cursor Completes Phase 1

After reviewing Cursor's Phase 1 report, send:

```text
Proceed with Phase 2.

Build the global Beau-T-Cloud design system, reusable base layout,
navbar, mobile navigation, dropdowns, footer and complete homepage.

Follow the approved Beau-T-Cloud brand colors and Frappe v16 conventions.

Do not modify Frappe or ERPNext core.

After completion run:

bench build --app beautcloud_website

Show me the build result and any errors before moving to Phase 3.
```

---

# 4. Phase 3 Prompt

```text
Proceed with Phase 3.

Build all Beau-T-Cloud feature pages:

- Appointment Management
- Online Booking
- Salon POS
- Client CRM
- Staff & Commission
- Inventory Management
- Memberships & Loyalty
- Multi-Location
- Reports & Analytics

Use reusable templates and components.

Each page must have unique SEO content.

Do not use fake statistics or testimonials.

After completion run:

bench build --app beautcloud_website

Report the result before moving to Phase 4.
```

---

# 5. Phase 4 Prompt

```text
Proceed with Phase 4.

Build all solution pages:

- Hair Salons
- Beauty Salons
- Nail Studios
- Spas
- Barbershops
- Multi-Branch Beauty Groups

Each page should explain the relevant business workflow,
problems solved and Beau-T-Cloud capabilities.

Use unique SEO title and description for every page.

After completion run:

bench build --app beautcloud_website

Report the result before moving to Phase 5.
```

---

# 6. Phase 5 Prompt

```text
Proceed with Phase 5.

Build the Book a Demo form and ERPNext Lead integration.

Use a secure Frappe v16 whitelisted server-side method.

Fields:

Full Name
Business Name
Email
Mobile
Country
City
Business Type
Number of Branches
Number of Employees
Current Software
Message

Create an ERPNext Lead.

Do not expose database operations in browser JavaScript.

Validate server-side.

Add appropriate protection against spam and rapid duplicate submission.

After completion run:

bench build --app beautcloud_website

Explain exactly how I can test the form and verify the Lead in ERPNext.
```

---

# 7. Phase 6 Prompt

```text
Proceed with Phase 6.

Build:

- Product Tour
- Pricing
- About
- Contact

Do not invent pricing.

Use Contact Sales / Book a Demo until actual pricing is supplied.

Do not invent Beau-T-Cloud history, founders or customer numbers.

After completion run:

bench build --app beautcloud_website

Report the result.
```

---

# 8. Phase 7 Prompt

```text
Proceed with Phase 7.

Complete the website's:

- SEO metadata
- canonical URLs
- OpenGraph metadata
- Twitter card metadata
- JSON-LD
- accessibility
- mobile responsiveness
- image loading optimization
- performance improvements
- internal linking

Do not create fake review/rating schema.

After completion run:

bench build --app beautcloud_website

Provide the final validation report.
```

---

# 9. Phase 8 Prompt

```text
Proceed with Phase 8.

Perform a final review of the complete Beau-T-Cloud website app.

Provide:

1. all routes created
2. all files created
3. all files modified
4. remaining image placeholders
5. screenshots I still need to provide
6. contact information I still need to provide
7. pricing information still missing
8. integrations that are still unconfirmed
9. SEO status
10. mobile status
11. accessibility status
12. build result
13. final manual testing checklist
14. production deployment checklist

Do not deploy automatically.
```

---

# 10. Useful Bench Commands During Development

Replace `YOUR_EXISTING_SITE_NAME` with your actual site name.

```bash
cd /home/frappe/frappe-bench
```

Build the app:

```bash
bench build --app beautcloud_website
```

Clear normal cache:

```bash
bench --site YOUR_EXISTING_SITE_NAME clear-cache
```

Clear website cache:

```bash
bench --site YOUR_EXISTING_SITE_NAME clear-website-cache
```

Check installed apps:

```bash
bench --site YOUR_EXISTING_SITE_NAME list-apps
```

Check versions:

```bash
bench version
```

Start development server if this is a development bench:

```bash
bench start
```

---

# 11. Important Development Rule

Do **not** ask Cursor to complete all phases in one pass.

Recommended process:

```text
Phase 1
↓
Review
↓
Phase 2
↓
Test
↓
Phase 3
↓
Test
↓
Phase 4
↓
Test
↓
Phase 5
↓
Test Lead Creation
↓
Phase 6
↓
Phase 7
↓
Phase 8
```

This will make the Frappe v16 implementation easier to debug and maintain.

---

# 12. Production Domain

Final production domain:

```text
https://beautcloud.com
```

Recommended canonical URL:

```text
https://beautcloud.com
```

Recommended redirect:

```text
https://www.beautcloud.com
→
https://beautcloud.com
```

Do not perform DNS, Nginx or SSL changes from Cursor unless explicitly requested later.

---

# 13. Beau-T-Cloud Brand Summary

```text
Product:
Beau-T-Cloud

Main Headline:
Run your beauty business beautifully.

Supporting Line:
One Cloud. Every Part of Your Beauty Business.

Primary:
#FF1B9A

Secondary Pink:
#FF6ED1

Light:
#FCEFF5

Dark:
#2E1A2F

Domain:
beautcloud.com

Website App:
beautcloud_website

Framework:
Frappe / ERPNext v16
```
