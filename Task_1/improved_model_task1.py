import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

def load_jsonl(path):
    with open(path, 'r') as f:
        return [json.loads(line) for line in f]

train_data = load_jsonl('data/train.jsonl')
test_data = load_jsonl('data/test.jsonl')

train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

train_df['text'] = train_df['postText'].apply(lambda x: x[0])
test_df['text'] = test_df['postText'].apply(lambda x: x[0])

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])
pipeline.fit(train_df['text'], train_df['tags'].apply(lambda x: x[0]))

preds = pipeline.predict(test_df['text'])

output_path = 'Task_1/classification_result.jsonl'
with open(output_path, 'w') as f:
    for idx, pred in zip(test_df['id'], preds):
        result = {'id': idx, 'tags': pred}
        f.write(json.dumps(result) + '\n')

print(f"Predictions saved to {output_path}")
