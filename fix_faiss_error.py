import json

with open("rag-using-langchain.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = cell["source"]
        if not source: continue
        new_source = []
        for line in source:
            if "vector_store.get_by_ids(" in line:
                new_source.append("# FAISS does not support get_by_ids directly.\n")
                new_source.append("# Instead, we can get an ID from the mapping and search the docstore:\n")
                new_source.append("sample_id = list(vector_store.index_to_docstore_id.values())[0]\n")
                new_source.append("vector_store.docstore.search(sample_id)\n")
            else:
                new_source.append(line)
        cell["source"] = new_source

with open("rag-using-langchain.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
