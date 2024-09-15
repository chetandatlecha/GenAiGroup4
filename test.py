from llama_index.graph_stores.neo4j import Neo4jGraphStore
username = "neo4j"
password = "gen-ai-team-4"
# url = "bolt://44.211.44.239:7687"
url="bolt://localhost:7687"
database = "neo4j"
graph_store = Neo4jGraphStore(
    username=username,
    password=password,
    url=url,
    database=database,
)
print(graph_store)