from src.tools.tools import web_search,scrape_url
from src.pipelines.pipeline import run_research_pipeline
# output = web_search.invoke("Latest news on AI research")
# print(output)

# results = scrape_url.invoke("https://arize.com/ai-research-papers/")
# print(results)

topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)
