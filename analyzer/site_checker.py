import requests
def check_sites(companies):
    results = []
    for company in companies:
        site = company.get("website")
        if site:
            try:
                r = requests.get(site, timeout=5)
                company["site_status"] = "OK" if r.status_code == 200 else f"Error {r.status_code}"
            except Exception:
                company["site_status"] = "Not reachable"
        else:
            company["site_status"] = "No site"
        results.append(company)
    return results
