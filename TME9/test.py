import ir_datasets

dataset = ir_datasets.load("gov2")
for doc in dataset.docs_iter():
    doc # namedtuple<doc_id, url, http_headers, body, body_content_type>