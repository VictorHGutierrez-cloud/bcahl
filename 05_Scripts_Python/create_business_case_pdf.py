from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from textwrap import wrap
import os

def draw_slide(c, title, bullets, slide_num):
    width, height = landscape(A4)
    
    # Header with slide number
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(HexColor('#2E86AB'))  # Professional blue
    c.drawString(20*mm, height-15*mm, f"Slide {slide_num}")
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor('#000000'))
    c.drawString(20*mm, height-35*mm, title)
    
    # Bullets
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor('#333333'))
    y = height-55*mm
    
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
    c.drawString(20*mm, 15*mm, "AHL Design & Engineering - Business Case | Factorial Finance | Prepared: 19 Oct 2025")

def create_business_case_pdf():
    file_path = "AHL_BusinessCase_Factorial_Strategy.pdf"
    c = canvas.Canvas(file_path, pagesize=landscape(A4))
    
    # Slide 1 - Q1 Summary (company overview)
    title = "Q1 — AHL Design & Engineering: Company Snapshot"
    bullets = [
        "🏢 HEADQUARTERS: Bucharest, Romania (Str. Johann Strauss 2A) | Website: https://www.ahlde.eu",
        "🏭 INDUSTRY: HVAC, Plumbing, Cleanrooms | NACE: 4322 | Focus: Pharma, Healthcare Turnkey Projects",
        "📊 SIZE & FINANCIALS (2023): Revenue: 45.7M RON (+154%) | Net Profit: 1.45M RON (+273%) | Employees: 77",
        "🌍 EXPANSION: France, Morocco, North Africa | International operations in 10+ countries",
        "⚠️ SIGNALS: Rapid growth but receivables jumped to 8.1M RON | Working capital pressure increasing",
        "📋 SOURCES: RisCo.ro, Company website, LinkedIn, Official Romanian business registry"
    ]
    draw_slide(c, title, bullets, 1)
    c.showPage()
    
    # Slide 2 - Q1 Meeting Strategy
    title = "Q1 — Meeting Opening Strategy (First 10 Minutes)"
    bullets = [
        "🎯 ACKNOWLEDGE GROWTH: 'Congratulations on 154% revenue growth - impressive expansion!'",
        "⚠️ PIVOT TO RISK: 'Growth without proper controls creates significant financial risks'",
        "📊 USE DATA: 'Your receivables grew 127% to 8.1M RON - cash flow management is critical'",
        "❓ KEY QUESTIONS: 'Which projects drive most revenue? How do you track project profitability?'",
        "💡 PROPOSAL: '90-day Factorial Finance pilot: Projects + Expenses modules for better control'",
        "📈 CREDIBILITY: Bring official RisCo data to build trust and demonstrate thorough research"
    ]
    draw_slide(c, title, bullets, 2)
    c.showPage()
    
    # Slide 3 - Q2 Financial Analysis
    title = "Q2 — Financial Deep Dive: Critical Insights"
    bullets = [
        "🚀 REVENUE ACCELERATION: 45.7M RON in 2023 (+154% vs 2022) - scaling business lines successfully",
        "💰 WORKING CAPITAL STRESS: Receivables 8.1M RON (+127%) | Liabilities 10.7M RON | Cash flow pressure",
        "📈 PROFITABILITY: Net profit 1.45M RON (+273%) but cash conversion stretched | DSO likely 80-120 days",
        "👥 HEADCOUNT: 77 employees (+33% growth) | Labor costs material | Risk of misallocation without tracking",
        "🏆 CREDIT PROFILE: Rating 'Very Good' (7.7/10) | No overdue state debts | Opportunity to optimize before strain",
        "⚠️ URGENCY: Current manual processes cannot scale with 154% growth rate"
    ]
    draw_slide(c, title, bullets, 3)
    c.showPage()
    
    # Slide 4 - Strategic Recommendation
    title = "Strategic Recommendation: Factorial Finance as Growth Enabler"
    bullets = [
        "🔗 CAUSAL CHAIN: Project visibility → Accurate billing → Faster invoicing → Lower DSO → More cash for growth",
        "📊 PROJECT CONTROL: Budget tracking + time logging = accurate project margins | Essential for 154% growth",
        "💳 EXPENSE AUTOMATION: OCR + approval flows = reduced leakage | Connect SaaS costs to projects",
        "🎯 PILOT PROPOSAL: 30/60/90 days | 1 business unit | Target KPIs: DSO -7 days, margin +3-5%, admin time -40%",
        "📋 IMMEDIATE ASK: Share AR aging + payroll summary (12 months) to size ROI and customize solution",
        "🚀 BOTTOM LINE: Transform growth challenges into competitive advantages with proper financial controls"
    ]
    draw_slide(c, title, bullets, 4)
    c.showPage()
    
    c.save()
    return file_path

# Create the PDF
pdf_path = create_business_case_pdf()
print(f"PDF created successfully: {pdf_path}")
