from llama_index.graph_stores.neo4j import Neo4jGraphStore
graph_store = Neo4jGraphStore(url="neo4j://localhost:7687", username="neo4j", password="gen-ai-team-4")
print(graph_store)