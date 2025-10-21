from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def create_financial_statements_pdf():
    # Create PDF document
    filename = "AHL_DESIGN_ENGINEERING_Financial_Statements_2023_English.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=72, leftMargin=72, 
                          topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Section header style
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    # Table header style
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER
    )
    
    # Table data style
    table_data_style = ParagraphStyle(
        'TableData',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Helvetica',
        alignment=TA_LEFT
    )
    
    # Number style
    number_style = ParagraphStyle(
        'Number',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Helvetica',
        alignment=TA_RIGHT
    )
    
    # Add title
    elements.append(Paragraph("AHL DESIGN & ENGINEERING SRL", title_style))
    elements.append(Paragraph("FINANCIAL STATEMENTS 2023 - ENGLISH TRANSCRIPTION", subtitle_style))
    elements.append(Spacer(1, 20))
    
    # BALANCE SHEET - ASSETS
    elements.append(Paragraph("BALANCE SHEET - ASSETS (ACTIF)", section_style))
    
    # Assets table data
    assets_data = [
        ['Description', '2023 Gross', 'Depr. & Prov.', '2023 Net', '2022 Net'],
        ['I. FIXED ASSETS (ACTIF IMMOBILISE)', '', '', '', ''],
        ['Establishment expenses', '', '', '', ''],
        ['Research and development', '', '', '', ''],
        ['Concessions, patents, trademarks, software', '26,334', '25,736', '598', '13'],
        ['Goodwill', '', '', '', ''],
        ['Other intangible assets', '', '', '', ''],
        ['Land', '', '', '', ''],
        ['Buildings', '', '', '', ''],
        ['Technical installations, equipment & tools', '299,209', '160,970', '138,239', '165,982'],
        ['Assets under construction', '', '', '', ''],
        ['Advances & down payments', '', '', '', ''],
        ['Equity-accounted investments', '', '', '', ''],
        ['Other investments', '', '', '', ''],
        ['Receivables related to investments', '', '', '', ''],
        ['Other fixed securities', '', '', '', ''],
        ['Loans', '', '', '', ''],
        ['Other financial assets', '351,854', '351,854', '330,711', ''],
        ['', '', '', '', ''],
        ['TOTAL (I)', '677,397', '186,706', '490,691', '498,020'],
        ['', '', '', '', ''],
        ['II. CURRENT ASSETS (ACTIF CIRCULANT)', '', '', '', ''],
        ['Raw materials, supplies', '', '', '', ''],
        ['Goods in production', '', '', '', ''],
        ['Work in progress for services', '', '', '', ''],
        ['Intermediate and finished products', '705,862', '', '', ''],
        ['Merchandise', '', '', '', ''],
        ['Advances & down payments paid on orders', '109,370', '109,370', '567,648', ''],
        ['Customers and related accounts', '8,779,122', '623,895', '8,155,227', '3,586,631'],
        ['Other receivables', '', '', '', ''],
        ['Suppliers debtors', '', '', '', ''],
        ['Personnel', '', '', '', ''],
        ['Social organizations', '69,444', '69,444', '', ''],
        ['State, taxes on profits', '69,203', '69,203', '69,203', ''],
        ['State, taxes on turnover', '1,610,060', '1,610,060', '2,357,072', ''],
        ['Others', '22,414', '22,414', '11,096', ''],
        ['Subscribed and called-up capital, not paid', '', '', '', ''],
        ['Marketable securities', '', '', '', ''],
        ['Financial instruments and tokens held', '', '', '', ''],
        ['Cash and cash equivalents', '5,462,543', '5,462,543', '3,216,207', ''],
        ['Prepaid expenses', '226,497', '226,497', '77,434', ''],
        ['', '', '', '', ''],
        ['TOTAL (II)', '16,348,653', '623,895', '15,724,758', '10,591,153']
    ]
    
    # Create assets table
    assets_table = Table(assets_data, colWidths=[3*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    assets_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 19), (-1, 19), colors.lightblue),
        ('FONTNAME', (0, 19), (-1, 19), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 21), (-1, 21), colors.lightgrey),
        ('FONTNAME', (0, 21), (-1, 21), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 44), (-1, 44), colors.lightblue),
        ('FONTNAME', (0, 44), (-1, 44), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(assets_table)
    elements.append(Spacer(1, 20))
    
    # Page break
    elements.append(PageBreak())
    
    # LIABILITIES
    elements.append(Paragraph("BALANCE SHEET - LIABILITIES (PASSIF)", section_style))
    
    # Liabilities table data
    liabilities_data = [
        ['Description', '2023 Net', '2022 Net'],
        ['I. SHAREHOLDERS\' EQUITY (CAPITAUX PROPRES)', '', ''],
        ['Issue premiums, merger premiums, contribution premiums', '', ''],
        ['Revaluation differences', '', ''],
        ['Legal reserve', '', ''],
        ['Statutory or contractual reserves', '', ''],
        ['Regulatory reserves', '', ''],
        ['Other reserves', '', ''],
        ['Brought forward balance', '', ''],
        ['Result of the period', '5,400', '1,080'],
        ['Investment grants', '4,014,845', '1,452,607'],
        ['Regulatory provisions', '5,473,932', '848,377'],
        ['Income from participatory securities issues', '', ''],
        ['Conditional advances', '2,535,039', '6,200,374'],
        ['', '', ''],
        ['TOTAL (I)', '581,529', '573,733'],
        ['', '', ''],
        ['II. PROVISIONS FOR RISKS AND CHARGES', '', ''],
        ['Provisions for risks', '', ''],
        ['Provisions for charges', '2,465', '10,741,517'],
        ['', '', ''],
        ['TOTAL (II)', '16,215,449', ''],
        ['', '', ''],
        ['III. DEBT (EMPRUNTS ET DETTES)', '', ''],
        ['Convertible bonds', '', ''],
        ['Other convertible bonds', '', ''],
        ['Borrowings from credit institutions', '', ''],
        ['Borrowings', '', ''],
        ['Overdrafts, bank facilities', '', ''],
        ['Various financial borrowings and debts', '', ''],
        ['Others', '5,400', '1,080'],
        ['Partners', '3,625,525', '389,321'],
        ['Advances & down payments received on orders', '4,021,326', '239,564'],
        ['Supplier debts and related accounts', '98,810', '2,415,458'],
        ['Tax and social debts', '', ''],
        ['Personnel', '', ''],
        ['Social organizations', '4,012,516', '212,686'],
        ['State, taxes on profits', '46,668', '42,145'],
        ['State, taxes on turnover', '7,067,847', '11,089,173'],
        ['State, guaranteed obligations and other taxes payable', '', ''],
        ['Debts on fixed assets and related accounts', '', ''],
        ['Other debts', '', ''],
        ['Financial instruments', '', ''],
        ['Prepaid income', '', ''],
        ['', '', ''],
        ['TOTAL (III)', '', ''],
        ['TOTAL (IV)', '', ''],
        ['Conversion differences and liability evaluation differences (V)', '', ''],
        ['', '', ''],
        ['TOTAL ASSETS (I to V)', '', '']
    ]
    
    # Create liabilities table
    liabilities_table = Table(liabilities_data, colWidths=[4*inch, 1.5*inch, 1.5*inch])
    liabilities_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 15), (-1, 15), colors.lightblue),
        ('FONTNAME', (0, 15), (-1, 15), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 17), (-1, 17), colors.lightgrey),
        ('FONTNAME', (0, 17), (-1, 17), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 21), (-1, 21), colors.lightblue),
        ('FONTNAME', (0, 21), (-1, 21), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 23), (-1, 23), colors.lightgrey),
        ('FONTNAME', (0, 23), (-1, 23), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(liabilities_table)
    elements.append(Spacer(1, 20))
    
    # Page break
    elements.append(PageBreak())
    
    # PROFIT AND LOSS STATEMENT
    elements.append(Paragraph("PROFIT AND LOSS STATEMENT (COMPTE DE RESULTAT)", section_style))
    
    # P&L table data
    pnl_data = [
        ['Description', '2023 France', '2023 Export', '2023 Total', '2022 Total'],
        ['I. OPERATING INCOME', '', '', '', ''],
        ['Sales of merchandise', '119,722', '119,722', '28,723', ''],
        ['Sales of production', '45,626,970', '45,626,970', '17,968,685', ''],
        ['Net Turnover', '45,746,692', '45,746,692', '17,997,408', ''],
        ['Stock production', '-705,862', '705,862', '', ''],
        ['Immobilized production', '', '', '', ''],
        ['Operating subsidies', '', '', '', ''],
        ['Reversals of depreciation and provisions', '', '', '', ''],
        ['Other income', '28,699', '25,221', '', ''],
        ['', '', '', '', ''],
        ['TOTAL OPERATING INCOME (I)', '45,068,929', '18,728,491', '', ''],
        ['', '', '', '', ''],
        ['II. OPERATING EXPENSES', '', '', '', ''],
        ['Purchases of merchandise (including customs duties)', '166', '', '', ''],
        ['Stock variation (merchandise)', '', '', '', ''],
        ['Purchases of raw materials and other supplies', '9,170,811', '3,590,970', '', ''],
        ['Stock variation (raw materials and other supplies)', '', '', '', ''],
        ['Other purchases and external charges', '17,633,929', '10,523,976', '', ''],
        ['Taxes and similar payments', '29,272', '22,122', '', ''],
        ['Wages and salaries', '13,156,204', '3,892,973', '', ''],
        ['Social charges', '2,823,344', '91,512', '', ''],
        ['Depreciation on fixed assets', '58,359', '44,296', '', ''],
        ['Provisions on fixed assets', '', '', '', ''],
        ['Provisions on current assets', '', '', '', ''],
        ['Provisions for risks and charges', '', '', '', ''],
        ['Other charges', '36,396', '19,553', '', ''],
        ['', '', '', '', ''],
        ['TOTAL OPERATING EXPENSES (II)', '42,908,249', '18,185,568', '', ''],
        ['', '', '', '', ''],
        ['OPERATING RESULT (I-II)', '2,160,680', '542,923', '', ''],
        ['', '', '', '', ''],
        ['III. FINANCIAL INCOME', '', '', '', ''],
        ['Equity share of results (joint ventures)', '', '', '', ''],
        ['Profit or loss transferred', '0', '', '', ''],
        ['Loss to be borne or transferred', '0', '', '', ''],
        ['Income from investment securities', '', '', '', ''],
        ['Income from other marketable securities and receivables', '', '', '', ''],
        ['Other interest and similar income', '14,187', '', '', ''],
        ['Reversals of provisions and charge transfers', '', '', '', ''],
        ['Positive exchange differences', '420,951', '261,153', '', ''],
        ['Net income on sales of marketable securities', '', '', '', ''],
        ['', '', '', '', ''],
        ['TOTAL FINANCIAL INCOME (IV)', '420,985', '261,340', '', ''],
        ['', '', '', '', ''],
        ['IV. FINANCIAL EXPENSES', '', '', '', ''],
        ['Financial provisions for depreciation and provisions', '', '', '', ''],
        ['Interest and similar charges', '8,289', '10,733', '', ''],
        ['Negative exchange differences', '506,971', '333,690', '', ''],
        ['Charges on sales of marketable securities', '', '', '', ''],
        ['', '', '', '', ''],
        ['TOTAL FINANCIAL EXPENSES (VI)', '515,260', '344,423', '', ''],
        ['', '', '', '', ''],
        ['FINANCIAL RESULT (V-VI)', '-94,275', '-83,083', '', ''],
        ['', '', '', '', ''],
        ['CURRENT RESULT BEFORE TAXES', '1,066,405', '459,840', '', ''],
        ['', '', '', '', ''],
        ['V. EXCEPTIONAL INCOME', '', '', '', ''],
        ['Exceptional income on management operations', '', '', '', ''],
        ['Exceptional income on capital operations', '', '', '', ''],
        ['Reversals of provisions and charge transfers', '', '', '', ''],
        ['', '', '', '', ''],
        ['TOTAL EXCEPTIONAL INCOME (VII)', '0', '0', '', ''],
        ['', '', '', '', ''],
        ['VI. EXCEPTIONAL EXPENSES', '', '', '', ''],
        ['Exceptional expenses on management operations', '187,223', '918', '', ''],
        ['Exceptional expenses on capital operations', '', '', '', ''],
        ['Exceptional provisions for depreciation and provisions', '', '', '', ''],
        ['', '', '', '', ''],
        ['TOTAL EXCEPTIONAL EXPENSES (VIII)', '187,223', '918', '', ''],
        ['', '', '', '', ''],
        ['EXCEPTIONAL RESULT (VII - VIII)', '-187,223', '-918', '', ''],
        ['', '', '', '', ''],
        ['Employee profit-sharing (IX)', '', '', '', ''],
        ['Taxes on profits (X)', '426,577', '69,601', '', ''],
        ['', '', '', '', ''],
        ['TOTAL INCOME (I + III + VII)', '45,489,914', '18,989,831', '', ''],
        ['TOTAL EXPENSES (II + IV + VI + VIII + IX + X)', '44,037,309', '18,600,510', '', ''],
        ['', '', '', '', ''],
        ['NET RESULT', '1,452,605', '389,321', '', ''],
        ['Profit', 'Profit', '', '', ''],
        ['Including equipment leasing', '', '', '', ''],
        ['Including real estate leasing', '', '', '', '']
    ]
    
    # Create P&L table
    pnl_table = Table(pnl_data, colWidths=[2.5*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    pnl_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 11), (-1, 11), colors.lightblue),
        ('FONTNAME', (0, 11), (-1, 11), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 13), (-1, 13), colors.lightgrey),
        ('FONTNAME', (0, 13), (-1, 13), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 28), (-1, 28), colors.lightblue),
        ('FONTNAME', (0, 28), (-1, 28), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 30), (-1, 30), colors.lightgreen),
        ('FONTNAME', (0, 30), (-1, 30), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 32), (-1, 32), colors.lightgrey),
        ('FONTNAME', (0, 32), (-1, 32), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 42), (-1, 42), colors.lightblue),
        ('FONTNAME', (0, 42), (-1, 42), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 44), (-1, 44), colors.lightgrey),
        ('FONTNAME', (0, 44), (-1, 44), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 50), (-1, 50), colors.lightgreen),
        ('FONTNAME', (0, 50), (-1, 50), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 52), (-1, 52), colors.lightgrey),
        ('FONTNAME', (0, 52), (-1, 52), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 58), (-1, 58), colors.lightblue),
        ('FONTNAME', (0, 58), (-1, 58), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 60), (-1, 60), colors.lightgrey),
        ('FONTNAME', (0, 60), (-1, 60), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 66), (-1, 66), colors.lightgreen),
        ('FONTNAME', (0, 66), (-1, 66), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 68), (-1, 68), colors.lightgrey),
        ('FONTNAME', (0, 68), (-1, 68), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 74), (-1, 74), colors.lightgreen),
        ('FONTNAME', (0, 74), (-1, 74), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 76), (-1, 76), colors.lightgreen),
        ('FONTNAME', (0, 76), (-1, 76), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(pnl_table)
    
    # Build PDF
    doc.build(elements)
    
    print(f"PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_financial_statements_pdf()
