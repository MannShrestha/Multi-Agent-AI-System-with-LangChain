from src.tools.tools import web_search,scrape_url

# output = web_search.invoke("Latest news on AI research")
# print(output)

results = scrape_url.invoke("https://arize.com/ai-research-papers/")
print(results)
