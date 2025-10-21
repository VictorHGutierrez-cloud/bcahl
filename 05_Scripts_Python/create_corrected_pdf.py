from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def create_corrected_financial_statements_pdf():
    # Create PDF document
    filename = "AHL_DESIGN_ENGINEERING_Financial_Statements_2023_CORRECTED.pdf"
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
    elements.append(Paragraph("FINANCIAL STATEMENTS 2023 - CORRECTED ENGLISH TRANSLATION", title_style))
    elements.append(Spacer(1, 20))
    
    # BALANCE SHEET - ASSETS (ACTIF)
    elements.append(Paragraph("BALANCE SHEET - ASSETS (ACTIF)", section_style))
    
    # Period header
    period_header = Table([['Period: 01/01/2023 to 31/12/2023', 'Period: 01/01/2022 to 31/12/2022', '', '', ''],
                          ['Gross', 'Depr. & Prov.', 'Net', 'Net', '']], 
                         colWidths=[1.5*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    period_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(period_header)
    elements.append(Spacer(1, 10))
    
    # Assets table data - CORRECTED based on original French text
    assets_data = [
        ['Description', 'Gross', 'Depr. & Prov.', '2023 Net', '2022 Net'],
        ['I. FIXED ASSETS (ACTIF IMMOBILISE)', '', '', '', ''],
        ['Subscribed capital not called (01)', '', '', '', ''],
        ['Establishment expenses', '', '', '', ''],
        ['Research and development', '', '', '', ''],
        ['Concessions, patents, trademarks, software and similar rights', '26,334', '25,736', '598', '13'],
        ['Goodwill', '', '', '', ''],
        ['Other intangible assets', '', '', '', ''],
        ['Land', '', '', '', ''],
        ['Buildings', '', '', '', ''],
        ['Technical installations, equipment & industrial tools', '299,209', '160,970', '138,239', '165,982'],
        ['Other tangible assets', '', '', '', ''],
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
        ['TOTAL (II)', '16,348,653', '623,895', '15,724,758', '10,591,153'],
        ['', '', '', '', ''],
        ['Charges to be spread over several periods', '', '', '', ''],
        ['(III) Bond redemption premiums', '', '', '', ''],
        ['(IV) Conversion differences and asset evaluation differences', '', '', '', ''],
        ['(V)', '', '', '', '']
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
        ('BACKGROUND', (0, 21), (-1, 21), colors.lightblue),
        ('FONTNAME', (0, 21), (-1, 21), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 23), (-1, 23), colors.lightgrey),
        ('FONTNAME', (0, 23), (-1, 23), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 41), (-1, 41), colors.lightblue),
        ('FONTNAME', (0, 41), (-1, 41), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(assets_table)
    elements.append(Spacer(1, 20))
    
    # Page break
    elements.append(PageBreak())
    
    # LIABILITIES (PASSIF)
    elements.append(Paragraph("BALANCE SHEET - LIABILITIES (PASSIF)", section_style))
    
    # Period header for liabilities
    period_header_liab = Table([['Period: 01/01/2023 to 31/12/2023', 'Period: 01/01/2022 to 31/12/2022', ''],
                               ['Net', 'Net', '']], 
                              colWidths=[2*inch, 2*inch, 2*inch])
    period_header_liab.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(period_header_liab)
    elements.append(Spacer(1, 10))
    
    # Liabilities table data - CORRECTED based on original French text
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
    
    # Build PDF
    doc.build(elements)
    
    print(f"Corrected PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_corrected_financial_statements_pdf()
