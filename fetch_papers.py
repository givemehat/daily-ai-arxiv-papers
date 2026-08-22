import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import os

# arXiv API URL for latest AI/ML/CV papers
ARXIV_URL = "http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CV&sortBy=submittedDate&sortOrder=descending&max_results=10"
NS = {'atom': 'http://www.w3.org/2005/Atom'}

import time
from urllib.error import HTTPError

def fetch_papers():
    print(f"Fetching papers from arXiv API...")
    req = urllib.request.Request(ARXIV_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req) as response:
                xml_data = response.read()
            break
        except HTTPError as e:
            if e.code == 429:
                wait_time = 5 * (attempt + 1)
                print(f"Rate limited (429). Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    else:
        print("Max retries reached. Exiting.")
        return []
    
    root = ET.fromstring(xml_data)
    papers = []
    
    for entry in root.findall('atom:entry', NS):
        title = entry.find('atom:title', NS).text.replace('\\n', ' ').strip()
        summary = entry.find('atom:summary', NS).text.replace('\\n', ' ').strip()
        link = entry.find("atom:link[@title='pdf']", NS)
        pdf_url = link.attrib['href'] if link is not None else entry.find('atom:id', NS).text
        
        authors = [author.find('atom:name', NS).text for author in entry.findall('atom:author', NS)]
        
        papers.append({
            'title': title,
            'authors': ', '.join(authors),
            'summary': summary,
            'url': pdf_url
        })
        
    return papers

def generate_markdown(papers):
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    md_content = f"# 🤖 Daily AI Research Papers\n\n"
    md_content += f"*Automatically fetched on {date_str}*\n\n"
    md_content += "This repository automatically fetches the latest top research papers in Artificial Intelligence, Machine Learning, and Computer Vision from arXiv every day.\n\n"
    md_content += "---\n\n"
    
    for idx, paper in enumerate(papers, 1):
        md_content += f"## {idx}. {paper['title']}\n"
        md_content += f"**Authors:** {paper['authors']}\n\n"
        md_content += f"**Summary:** {paper['summary']}\n\n"
        md_content += f"[📄 Read PDF]({paper['url']})\n\n"
        md_content += "---\n\n"
        
    return md_content

def main():
    papers = fetch_papers()
    if not papers:
        print("No papers found!")
        return
        
    print(f"Fetched {len(papers)} papers. Generating Markdown...")
    markdown_content = generate_markdown(papers)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print("README.md updated successfully!")

if __name__ == "__main__":
    main()
