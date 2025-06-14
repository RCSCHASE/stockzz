#!/usr/bin/env python3
"""
Script to create the LMT analysis file
Run this script to automatically create lmt_analysis.py
"""

code_content = '''#!/usr/bin/env python3
"""
Comprehensive Lockheed Martin (LMT) Stock Analysis
Using py-stocks package to gather all available data
"""

import sys
import os
sys.path.append('py-stocks')

from Stock import Stock
import pandas as pd
from datetime import datetime

def analyze_lockheed_martin():
    """Comprehensive analysis of Lockheed Martin stock using py-stocks package"""
    
    print("="*60)
    print("LOCKHEED MARTIN CORPORATION (LMT) - COMPREHENSIVE ANALYSIS")
    print("="*60)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Initialize Stock object
    lmt = Stock("LMT")
    
    # BASIC COMPANY DATA
    print("📊 COMPANY INFORMATION")
    print("-" * 30)
    
    try:
        print(f"Company Name: {lmt.get_name()}")
    except Exception as e:
        print(f"Company Name: Error retrieving - {e}")
    
    try:
        print(f"Sector: {lmt.get_sector()}")
    except Exception as e:
        print(f"Sector: Error retrieving - {e}")
    
    try:
        print(f"Industry: {lmt.get_industry()}")
    except Exception as e:
        print(f"Industry: Error retrieving - {e}")
    
    try:
        print(f"Employees: {lmt.get_employees():,}")
    except Exception as e:
        print(f"Employees: Error retrieving - {e}")
    
    try:
        address = lmt.get_address()
        print(f"Address: {address}")
    except Exception as e:
        print(f"Address: Error retrieving - {e}")
    
    try:
        print(f"Website: {lmt.get_website()}")
    except Exception as e:
        print(f"Website: Error retrieving - {e}")
    
    try:
        summary = lmt.get_summary()
        print(f"\\nCompany Summary:\\n{summary}")
    except Exception as e:
        print(f"Company Summary: Error retrieving - {e}")
    
    print("\\n" + "="*60)
    
    # CURRENT STOCK PRICE DATA
    print("💰 CURRENT STOCK METRICS")
    print("-" * 30)
    
    try:
        print(f"Current Price: ${lmt.get_current_price():.2f}")
    except Exception as e:
        print(f"Current Price: Error retrieving - {e}")
    
    try:
        print(f"Volume: {lmt.get_volume():,}")
    except Exception as e:
        print(f"Volume: Error retrieving - {e}")
    
    try:
        print(f"Average Volume: {lmt.get_average_volume():,}")
    except Exception as e:
        print(f"Average Volume: Error retrieving - {e}")
    
    try:
        dividend_yield = lmt.get_dividend_yield()
        print(f"Dividend Yield: {dividend_yield:.2%}" if dividend_yield else "Dividend Yield: N/A")
    except Exception as e:
        print(f"Dividend Yield: Error retrieving - {e}")
    
    try:
        print(f"Day High: ${lmt.get_day_high():.2f}")
    except Exception as e:
        print(f"Day High: Error retrieving - {e}")
    
    try:
        print(f"Day Low: ${lmt.get_day_low():.2f}")
    except Exception as e:
        print(f"Day Low: Error retrieving - {e}")
    
    try:
        print(f"52-Week High: ${lmt.get_52week_high():.2f}")
    except Exception as e:
        print(f"52-Week High: Error retrieving - {e}")
    
    try:
        print(f"52-Week Low: ${lmt.get_52week_low():.2f}")
    except Exception as e:
        print(f"52-Week Low: Error retrieving - {e}")
    
    print("\\n" + "="*60)
    
    # HISTORICAL DATA
    print("📈 HISTORICAL DATA (LAST MONTH)")
    print("-" * 30)
    
    try:
        last_month_data = lmt.get_last_month_data()
        print("Last Month OHLCV Data:")
        print(last_month_data.tail())
        print(f"\\nData points available: {len(last_month_data)}")
    except Exception as e:
        print(f"Last Month Data: Error retrieving - {e}")
    
    try:
        month_ema = lmt.get_month_ema()
        print(f"\\nExponential Moving Average (Last Month):")
        print(month_ema.tail())
    except Exception as e:
        print(f"Month EMA: Error retrieving - {e}")
    
    print("\\n" + "="*60)
    
    # ANALYST DATA
    print("👔 ANALYST INFORMATION")
    print("-" * 30)
    
    try:
        analyst_recs = lmt.get_analyst_recs()
        print("All Analyst Recommendations:")
        print(analyst_recs)
        print(f"\\nTotal recommendations: {len(analyst_recs)}")
    except Exception as e:
        print(f"Analyst Recommendations: Error retrieving - {e}")
    
    try:
        recent_recs = lmt.get_most_recent_recs()
        print(f"\\nMost Recent Analyst Recommendations:")
        print(recent_recs)
    except Exception as e:
        print(f"Recent Recommendations: Error retrieving - {e}")
    
    print("\\n" + "="*60)
    
    # INSTITUTIONAL DATA
    print("🏛️ INSTITUTIONAL & SUSTAINABILITY DATA")
    print("-" * 30)
    
    try:
        holders = lmt.get_holders()
        print("Institutional Holders:")
        print(holders)
    except Exception as e:
        print(f"Institutional Holders: Error retrieving - {e}")
    
    try:
        sustainability = lmt.get_sustainability_info()
        print(f"\\nSustainability Information:")
        print(sustainability)
    except Exception as e:
        print(f"Sustainability Info: Error retrieving - {e}")
    
    print("\\n" + "="*60)
    
    # NEWS DATA
    print("📰 RECENT NEWS")
    print("-" * 30)
    
    try:
        news = lmt.get_news()
        print("Recent News Articles from NASDAQ:")
        for idx, row in news.head(10).iterrows():
            print(f"• {row.get('title', 'No title')}")
            print(f"  Date: {row.get('date', 'No date')}")
            print(f"  Link: {row.get('link', 'No link')}")
            print()
    except Exception as e:
        print(f"Recent News: Error retrieving - {e}")
    
    print("="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)

if __name__ == "__main__":
    analyze_lockheed_martin()
'''

# Write the file
filename = "lmt_analysis.py"
try:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(code_content)
    print(f"✅ Successfully created {filename}")
    print(f"📁 File location: {os.path.abspath(filename)}")
    print("\\n📝 To run the analysis:")
    print(f"python {filename}")
except Exception as e:
    print(f"❌ Error creating file: {e}")