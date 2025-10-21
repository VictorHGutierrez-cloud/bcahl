from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from textwrap import wrap
import os

def draw_slide_with_image(c, title, bullets, slide_num, image_path=None):
    width, height = A4
    
    # Header with slide number
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(HexColor('#2E86AB'))
    c.drawString(20*mm, height-15*mm, f"Slide {slide_num}")
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor('#000000'))
    c.drawString(20*mm, height-35*mm, title)
    
    # Image if provided
    if image_path and os.path.exists(image_path):
        try:
            c.drawImage(image_path, 20*mm, height-200*mm, width=150*mm, height=100*mm, preserveAspectRatio=True)
            y_start = height-220*mm
        except:
            y_start = height-55*mm
    else:
        y_start = height-55*mm
    
    # Bullets
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor('#333333'))
    y = y_start
    
    for i, bullet in enumerate(bullets):
        # Bullet point
        c.setFont("Helvetica-Bold", 12)
        c.drawString(22*mm, y, "•")
        
        # Text
        c.setFont("Helvetica", 11)
        lines = wrap(bullet, 110)
        x_pos = 30*mm
        
        for line in lines:
            c.drawString(x_pos, y, line)
            y -= 6*mm
        y -= 4*mm
    
    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(HexColor('#666666'))
    c.drawString(20*mm, 15*mm, "AHL Design & Engineering - Visual Business Case | Factorial Finance | 20 Oct 2025")

def create_visual_business_report():
    file_path = "AHL_Visual_Business_Report.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)
    
    # Slide 1 - Title and Company Overview
    title = "AHL Design & Engineering SRL - Business Case Analysis"
    bullets = [
        "🏢 COMPANY: Design & Engineering Services (HVAC, Plumbing, Cleanrooms)",
        "📍 HEADQUARTERS: 30 Avenue Général Leclerc - 38200 VIENNE, France | SIREN: 921 210 027",
        "📊 PERFORMANCE (2023): Revenue €45.7M (+154%) | Profit €1.5M (+273%) | Assets €16.2M (+46%)",
        "🌍 EXPANSION: France, Morocco, North Africa | 10+ countries | 77 employees (+33%)",
        "🎯 FOCUS: Pharmaceutical and Healthcare Turnkey Projects",
        "⚠️ CHALLENGE: Rapid growth creating working capital pressure (€8.2M receivables)"
    ]
    draw_slide_with_image(c, title, bullets, 1)
    c.showPage()
    
    # Slide 2 - Financial Growth Analysis
    title = "Financial Growth Analysis - Exceptional Performance"
    bullets = [
        "🚀 REVENUE GROWTH: +154.2% (€18.0M → €45.7M) - exceptional scaling",
        "💰 PROFIT GROWTH: +273.0% (€389K → €1.5M) - strong profitability improvement",
        "📈 ASSET GROWTH: +46.2% (€11.1M → €16.2M) - solid foundation",
        "💼 EQUITY GROWTH: +36.1% (€4.0M → €5.5M) - healthy capital structure",
        "👥 EMPLOYEE GROWTH: +33% (58 → 77) - significant human capital investment",
        "🎯 MARGIN IMPROVEMENT: Net margin 2.1% → 3.2% - operational efficiency gains"
    ]
    image_path = "03_Charts_English/01_Financial_Growth_2022_vs_2023_EN.png"
    draw_slide_with_image(c, title, bullets, 2, image_path)
    c.showPage()
    
    # Slide 3 - Executive Dashboard
    title = "Executive Dashboard - Key Financial Metrics"
    bullets = [
        "💵 CASH POSITION: €5.5M available cash - strong liquidity",
        "📊 REVENUE BREAKDOWN: 99.7% services, 0.3% goods - service-focused business",
        "⚖️ FINANCIAL RATIOS: Net margin 3.2%, operational margin 4.7%",
        "📈 GROWTH RATES: Revenue +154%, Profit +273%, Assets +46%",
        "🎯 CREDIT RATING: 'Very Good' (7.7/10) - no overdue state debts",
        "⚠️ WORKING CAPITAL: €8.2M receivables (18% of revenue) - needs optimization"
    ]
    image_path = "03_Charts_English/11_Executive_Dashboard_EN.png"
    draw_slide_with_image(c, title, bullets, 3, image_path)
    c.showPage()
    
    # Slide 4 - Assets & Liabilities Analysis
    title = "Assets & Liabilities Composition Analysis"
    bullets = [
        "🏦 ASSETS STRUCTURE: 97% current assets, 3% fixed assets - highly liquid",
        "💰 CASH & EQUIVALENTS: €5.5M (35% of total assets) - excellent liquidity",
        "📋 ACCOUNTS RECEIVABLE: €8.2M (52% of current assets) - major concern",
        "🏢 LIABILITIES: 66% total debt, 34% equity - manageable leverage",
        "💳 SUPPLIER DEBTS: €6.2M (58% of total debt) - payment management needed",
        "📊 TAX DEBTS: €573K overdue taxes, €581K social security - compliance issues"
    ]
    image_path = "03_Charts_English/03_Assets_Composition_2023_EN.png"
    draw_slide_with_image(c, title, bullets, 4, image_path)
    c.showPage()
    
    # Slide 5 - Revenue & Expenses Analysis
    title = "Revenue & Expenses Composition Analysis"
    bullets = [
        "💼 REVENUE MIX: 99.7% engineering services, 0.3% goods sales",
        "📊 SERVICE REVENUE: €45.6M - core business strength",
        "💸 EXPENSE BREAKDOWN: 67% external purchases, 33% personnel costs",
        "👥 PERSONNEL COSTS: €13.2M salaries + €2.8M social charges",
        "🛒 EXTERNAL COSTS: €9.2M materials + €17.6M other external purchases",
        "📈 EFFICIENCY: Revenue per employee €593K - high productivity"
    ]
    image_path = "03_Charts_English/05_Revenue_Composition_2023_EN.png"
    draw_slide_with_image(c, title, bullets, 5, image_path)
    c.showPage()
    
    # Slide 6 - Financial Indicators & Margins
    title = "Financial Indicators & Margins Evolution"
    bullets = [
        "📊 NET MARGIN: 3.2% (2023) vs 2.1% (2022) - 52% improvement",
        "⚖️ OPERATIONAL MARGIN: 4.7% (2023) vs 2.9% (2022) - 62% improvement",
        "💰 PROFITABILITY TREND: Consistent margin improvement over time",
        "📈 GROWTH SUSTAINABILITY: Margins improving despite rapid scaling",
        "🎯 EFFICIENCY GAINS: Better cost control and operational optimization",
        "⚠️ CASH CONVERSION: Strong profits but working capital pressure"
    ]
    image_path = "03_Charts_English/09_Financial_Indicators_EN.png"
    draw_slide_with_image(c, title, bullets, 6, image_path)
    c.showPage()
    
    # Slide 7 - Debt Analysis & Liquidity
    title = "Debt Analysis & Liquidity Assessment"
    bullets = [
        "💳 DEBT STRUCTURE: €10.7M total debt (+52% vs 2022)",
        "🏪 SUPPLIER DEBTS: €6.2M (58% of total) - payment management critical",
        "🏛️ TAX DEBTS: €573K overdue taxes (+1,129%) - compliance urgency",
        "👥 SOCIAL DEBTS: €581K social security (+173%) - HR compliance needed",
        "💰 BANK DEBT: €848K (+254%) - manageable but growing",
        "💧 LIQUIDITY: €5.5M cash vs €8.2M receivables - working capital gap"
    ]
    image_path = "03_Charts_English/07_Debts_by_Category_2023_EN.png"
    draw_slide_with_image(c, title, bullets, 7, image_path)
    c.showPage()
    
    # Slide 8 - Risk Analysis
    title = "Risk Analysis & Strategic Recommendations"
    bullets = [
        "⚠️ HIGH RISK: Accounts receivable management (€8.2M at risk)",
        "📊 MEDIUM RISK: Tax compliance (€573K overdue) - penalty risk",
        "💼 MEDIUM RISK: Supplier relationship management (€6.2M debt)",
        "👥 LOW RISK: Social security compliance (€581K debt)",
        "💰 LOW RISK: Bank debt (€848K) - manageable levels",
        "🎯 OPPORTUNITY: Factorial can address all high/medium risk areas"
    ]
    image_path = "03_Charts_English/12_Risk_Analysis_EN.png"
    draw_slide_with_image(c, title, bullets, 8, image_path)
    c.showPage()
    
    # Slide 9 - Factorial Recommendations
    title = "Factorial Solution Recommendations"
    bullets = [
        "🎯 IMMEDIATE ACTIONS: Automated AR tracking, tax compliance, supplier management",
        "📊 PROJECT CONTROL: Budget tracking + time logging for accurate project margins",
        "💳 EXPENSE AUTOMATION: OCR + approval flows to reduce leakage",
        "📈 CASH FLOW: Better receivables management to improve working capital",
        "⏰ COMPLIANCE: Automated tax deadlines and social security tracking",
        "🚀 PILOT PROPOSAL: 90-day program targeting 15-25% cost reduction"
    ]
    draw_slide_with_image(c, title, bullets, 9)
    c.showPage()
    
    # Slide 10 - Implementation Roadmap
    title = "Implementation Roadmap & Expected Impact"
    bullets = [
        "📅 WEEK 1-2: Discovery & Setup | Analyze processes, configure modules",
        "📅 WEEK 3-4: Training & Go-Live | Train team, implement workflows",
        "📅 WEEK 5-8: Monitoring | Track KPIs, optimize processes",
        "📅 WEEK 9-12: Scale & Expand | Roll out to all business units",
        "🎯 SUCCESS METRICS: DSO -7 days, margin +3-5%, admin time -40%",
        "💰 ROI PROJECTION: 6-8 month payback, 15-25% cost reduction"
    ]
    draw_slide_with_image(c, title, bullets, 10)
    c.showPage()
    
    c.save()
    return file_path

# Create the PDF
pdf_path = create_visual_business_report()
print(f"Visual Business Report PDF created successfully: {pdf_path}")
