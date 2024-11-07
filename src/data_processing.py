import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

# Fetch data from GitLab's Handbook and Direction pages
handbook_url = "https://about.gitlab.com/handbook/"
direction_url = "https://about.gitlab.com/direction/"
handbook_company_url = "https://handbook.gitlab.com/handbook/company/"
about_company_url = "https://about.gitlab.com/company/"
context = "Inspired by companies like GitLab, which embody a “build in public” philosophy, this project aims to foster transparency, collaboration, and learning. GitLab openly shares its strategies, roadmaps, and internal processes, encouraging community feedback and improvement."

handbook_data = fetch_data(handbook_url)
direction_data = fetch_data(direction_url)
about_company_data = fetch_data(about_company_url)
handbook_company_data = fetch_data(handbook_company_url)

# Removing empty lines
handbook_data = "\n".join([line for line in handbook_data.split("\n") if line.strip()])
direction_data = "\n".join([line for line in direction_data.split("\n") if line.strip()])
about_company_data = "\n".join([line for line in about_company_data.split("\n") if line.strip()])
handbook_company_data = "\n".join([line for line in handbook_company_data.split("\n") if line.strip()])

initial_context = context + handbook_data + direction_data + about_company_data + handbook_company_data

# Print initial context with utf-8 encoding
# with open('context.txt', 'w', encoding='utf-8') as f:
#     f.write(initial_context)