from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def create_financial_statements_pdf():
    # Create PDF document
    filename = "AHL_DESIGN_ENGINEERING_Financial_Statements_2023_English.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, 
                          rightMargin=50, leftMargin=50, 
                          topMargin=50, bottomMargin=50)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Section header style
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    # Add title
    elements.append(Paragraph("AHL DESIGN & ENGINEERING SRL", title_style))
    elements.append(Paragraph("FINANCIAL STATEMENTS 2023 - ENGLISH TRANSCRIPTION", title_style))
    elements.append(Spacer(1, 20))
    
    # BALANCE SHEET - ASSETS
    elements.append(Paragraph("BALANCE SHEET - ASSETS (ACTIF)", section_style))
    
    # Assets table data - simplified
    assets_data = [
        ['Description', '2023 Gross', 'Depr. & Prov.', '2023 Net', '2022 Net'],
        ['I. FIXED ASSETS (ACTIF IMMOBILISE)', '', '', '', ''],
        ['Concessions, patents, trademarks, software', '26,334', '25,736', '598', '13'],
        ['Technical installations, equipment & tools', '299,209', '160,970', '138,239', '165,982'],
        ['Other financial assets', '351,854', '351,854', '330,711', ''],
        ['TOTAL (I)', '677,397', '186,706', '490,691', '498,020'],
        ['', '', '', '', ''],
        ['II. CURRENT ASSETS (ACTIF CIRCULANT)', '', '', '', ''],
        ['Intermediate and finished products', '705,862', '', '', ''],
        ['Advances & down payments paid on orders', '109,370', '109,370', '567,648', ''],
        ['Customers and related accounts', '8,779,122', '623,895', '8,155,227', '3,586,631'],
        ['Social organizations', '69,444', '69,444', '', ''],
        ['State, taxes on profits', '69,203', '69,203', '69,203', ''],
        ['State, taxes on turnover', '1,610,060', '1,610,060', '2,357,072', ''],
        ['Others', '22,414', '22,414', '11,096', ''],
        ['Cash and cash equivalents', '5,462,543', '5,462,543', '3,216,207', ''],
        ['Prepaid expenses', '226,497', '226,497', '77,434', ''],
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
        ('BACKGROUND', (0, 5), (-1, 5), colors.lightblue),
        ('FONTNAME', (0, 5), (-1, 5), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 7), (-1, 7), colors.lightgrey),
        ('FONTNAME', (0, 7), (-1, 7), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 17), (-1, 17), colors.lightblue),
        ('FONTNAME', (0, 17), (-1, 17), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(assets_table)
    elements.append(Spacer(1, 20))
    
    # Page break
    elements.append(PageBreak())
    
    # LIABILITIES
    elements.append(Paragraph("BALANCE SHEET - LIABILITIES (PASSIF)", section_style))
    
    # Liabilities table data - simplified
    liabilities_data = [
        ['Description', '2023 Net', '2022 Net'],
        ['I. SHAREHOLDERS\' EQUITY (CAPITAUX PROPRES)', '', ''],
        ['Result of the period', '5,400', '1,080'],
        ['Investment grants', '4,014,845', '1,452,607'],
        ['Regulatory provisions', '5,473,932', '848,377'],
        ['Conditional advances', '2,535,039', '6,200,374'],
        ['TOTAL (I)', '581,529', '573,733'],
        ['', '', ''],
        ['II. PROVISIONS FOR RISKS AND CHARGES', '', ''],
        ['Provisions for charges', '2,465', '10,741,517'],
        ['TOTAL (II)', '16,215,449', ''],
        ['', '', ''],
        ['III. DEBT (EMPRUNTS ET DETTES)', '', ''],
        ['Others', '5,400', '1,080'],
        ['Partners', '3,625,525', '389,321'],
        ['Advances & down payments received on orders', '4,021,326', '239,564'],
        ['Supplier debts and related accounts', '98,810', '2,415,458'],
        ['Social organizations', '4,012,516', '212,686'],
        ['State, taxes on profits', '46,668', '42,145'],
        ['State, taxes on turnover', '7,067,847', '11,089,173'],
        ['TOTAL (III)', '', ''],
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
        ('BACKGROUND', (0, 6), (-1, 6), colors.lightblue),
        ('FONTNAME', (0, 6), (-1, 6), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 8), (-1, 8), colors.lightgrey),
        ('FONTNAME', (0, 8), (-1, 8), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 10), (-1, 10), colors.lightblue),
        ('FONTNAME', (0, 10), (-1, 10), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 12), (-1, 12), colors.lightgrey),
        ('FONTNAME', (0, 12), (-1, 12), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(liabilities_table)
    elements.append(Spacer(1, 20))
    
    # Page break
    elements.append(PageBreak())
    
    # PROFIT AND LOSS STATEMENT
    elements.append(Paragraph("PROFIT AND LOSS STATEMENT (COMPTE DE RESULTAT)", section_style))
    
    # P&L table data - simplified
    pnl_data = [
        ['Description', '2023 Total', '2022 Total'],
        ['I. OPERATING INCOME', '', ''],
        ['Sales of merchandise', '119,722', '28,723'],
        ['Sales of production', '45,626,970', '17,968,685'],
        ['Net Turnover', '45,746,692', '17,997,408'],
        ['Stock production', '-705,862', '705,862'],
        ['Other income', '28,699', '25,221'],
        ['TOTAL OPERATING INCOME (I)', '45,068,929', '18,728,491'],
        ['', '', ''],
        ['II. OPERATING EXPENSES', '', ''],
        ['Purchases of merchandise', '166', ''],
        ['Purchases of raw materials and other supplies', '9,170,811', '3,590,970'],
        ['Other purchases and external charges', '17,633,929', '10,523,976'],
        ['Taxes and similar payments', '29,272', '22,122'],
        ['Wages and salaries', '13,156,204', '3,892,973'],
        ['Social charges', '2,823,344', '91,512'],
        ['Depreciation on fixed assets', '58,359', '44,296'],
        ['Other charges', '36,396', '19,553'],
        ['TOTAL OPERATING EXPENSES (II)', '42,908,249', '18,185,568'],
        ['', '', ''],
        ['OPERATING RESULT (I-II)', '2,160,680', '542,923'],
        ['', '', ''],
        ['III. FINANCIAL INCOME', '', ''],
        ['Other interest and similar income', '14,187', ''],
        ['Positive exchange differences', '420,951', '261,153'],
        ['TOTAL FINANCIAL INCOME (IV)', '420,985', '261,340'],
        ['', '', ''],
        ['IV. FINANCIAL EXPENSES', '', ''],
        ['Interest and similar charges', '8,289', '10,733'],
        ['Negative exchange differences', '506,971', '333,690'],
        ['TOTAL FINANCIAL EXPENSES (VI)', '515,260', '344,423'],
        ['', '', ''],
        ['FINANCIAL RESULT (V-VI)', '-94,275', '-83,083'],
        ['', '', ''],
        ['CURRENT RESULT BEFORE TAXES', '1,066,405', '459,840'],
        ['', '', ''],
        ['V. EXCEPTIONAL INCOME', '', ''],
        ['TOTAL EXCEPTIONAL INCOME (VII)', '0', '0'],
        ['', '', ''],
        ['VI. EXCEPTIONAL EXPENSES', '', ''],
        ['Exceptional expenses on management operations', '187,223', '918'],
        ['TOTAL EXCEPTIONAL EXPENSES (VIII)', '187,223', '918'],
        ['', '', ''],
        ['EXCEPTIONAL RESULT (VII - VIII)', '-187,223', '-918'],
        ['', '', ''],
        ['Taxes on profits (X)', '426,577', '69,601'],
        ['', '', ''],
        ['TOTAL INCOME (I + III + VII)', '45,489,914', '18,989,831'],
        ['TOTAL EXPENSES (II + IV + VI + VIII + IX + X)', '44,037,309', '18,600,510'],
        ['', '', ''],
        ['NET RESULT', '1,452,605', '389,321'],
        ['Profit', 'Profit', '']
    ]
    
    # Create P&L table
    pnl_table = Table(pnl_data, colWidths=[4*inch, 1.5*inch, 1.5*inch])
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
        ('BACKGROUND', (0, 7), (-1, 7), colors.lightblue),
        ('FONTNAME', (0, 7), (-1, 7), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 9), (-1, 9), colors.lightgrey),
        ('FONTNAME', (0, 9), (-1, 9), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 19), (-1, 19), colors.lightblue),
        ('FONTNAME', (0, 19), (-1, 19), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 21), (-1, 21), colors.lightgreen),
        ('FONTNAME', (0, 21), (-1, 21), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 23), (-1, 23), colors.lightgrey),
        ('FONTNAME', (0, 23), (-1, 23), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 26), (-1, 26), colors.lightblue),
        ('FONTNAME', (0, 26), (-1, 26), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 28), (-1, 28), colors.lightgrey),
        ('FONTNAME', (0, 28), (-1, 28), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 32), (-1, 32), colors.lightgreen),
        ('FONTNAME', (0, 32), (-1, 32), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 34), (-1, 34), colors.lightgrey),
        ('FONTNAME', (0, 34), (-1, 34), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 37), (-1, 37), colors.lightblue),
        ('FONTNAME', (0, 37), (-1, 37), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 39), (-1, 39), colors.lightgrey),
        ('FONTNAME', (0, 39), (-1, 39), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 42), (-1, 42), colors.lightgreen),
        ('FONTNAME', (0, 42), (-1, 42), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 44), (-1, 44), colors.lightgrey),
        ('FONTNAME', (0, 44), (-1, 44), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 48), (-1, 48), colors.lightgreen),
        ('FONTNAME', (0, 48), (-1, 48), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 50), (-1, 50), colors.lightgreen),
        ('FONTNAME', (0, 50), (-1, 50), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(pnl_table)
    
    # Build PDF
    doc.build(elements)
    
    print(f"PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_financial_statements_pdf()
