import pinecone
from sentence_transformers import SentenceTransformer
from helpers import chunks

# Replace this with your Pinecone API key
API_KEY = "<YOUR API KEY HERE>"

new_index_name = "paradise-index"

file_path = "paradise_lost.txt"

lines = []
print("Fetching lines from text file...")
with open(file_path, "r") as file:
    print("File open...")
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and not line.startswith("[") and not (line.startswith("Book") and len(line) < 15):
            lines.append(line)
print("Lines fetched")

# Load pre-trained SentenceTransformer model
print("Loading pre-trained SentenceTransformer model...")
model = SentenceTransformer('all-mpnet-base-v2')
print("Success")

# Generate sentence embeddings
print("Generating sentence embeddings...")
sentence_embeddings = model.encode(lines)
print("Success")

print("Number of lines:", len(lines))
print("Dimension of sentence embeddings:", sentence_embeddings.shape[1])

print("Getting vectors as a list of lists...")
embeddings = sentence_embeddings.tolist()
print("Success")

print("Zipping up 'lines' and 'embeddings' into a list of 'vectors' ready to insert into pinecone...")
vectors = list(zip(lines, embeddings))
print("Success")

print("initialising Pinecone connection...")
pinecone.init(api_key=API_KEY, environment="us-west1-gcp-free")
print("Pinecone initialised")

print(f"Creating 768-dimensional index called '{new_index_name}'...")
pinecone.create_index(new_index_name, dimension=768)
print("Success")

print("Checking Pinecone for active indexes...")
active_indexes = pinecone.list_indexes()
print("Active indexes:")
print(active_indexes)

print(f"Getting description for '{new_index_name}'...")
index_description = pinecone.describe_index(new_index_name)
print("Description:")
print(index_description)

print(f"Getting '{new_index_name}' as object...")
pinecone_index = pinecone.Index(new_index_name)
print("Success")

print("Upserting vectors in chunks of 100...")
counter = 1
for chunk in chunks(vectors, 100):
    print(f"Upserting chunk {counter}...")
    upsert_response = pinecone_index.upsert(
        vectors=chunk
        )
    print("done")
    counter += 1
print("Success")

query_strings = [
    # Semantic search for concepts:
    "Agricultural details",
    "Anatomical details",
    "Technological innovation",

    # Semantic search for famous movie quotes:
    "I'm gonna make him an offer he can't refuse",
    "Frankly my dear, I don't give a damn",
    "I've a feeling we're not in Kansas any more",

    # Semantic search for Star Wars movie titles:
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith",
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi",
    "The Force Awakens",
    "The Last Jedi",
    "The Rise of Skywalker"
]

query_vector = model.encode(query_strings).tolist()

print("Searching for similar...")
query_results = pinecone_index.query(
    queries=query_vector,
    top_k=5,
    include_values=True
    )

for i in range(len(query_results.results)):
    print(f'\n\nSimilar results for "{query_strings[i]}":')
    for match in query_results.results[i].matches:   
        print(f'"{match.id}" ({round(match.score*100, 2)}% similar)')
