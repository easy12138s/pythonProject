import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set your Azure Cognitive Services endpoint and key
endpoint = "YOUR_ENDPOINT"
key = "YOUR_KEY"

# Instantiate a Text Analytics client
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Text for analysis
documents = [
    "I love the weather today! It makes me so happy.",
    "The movie was not good. I did not enjoy it at all.",
    "Microsoft is a technology company based in Redmond, Washington.",
    "The new product launch was a success. Customers are excited about it."
]

# Perform sentiment analysis
response = text_analytics_client.analyze_sentiment(documents=documents)[0]
for idx, doc in enumerate(response):
    print("Document: {}".format(documents[idx]))
    print("Sentiment: {}".format(doc.sentiment))
    print()

```python
# Perform entity recognition
response = text_analytics_client.recognize_entities(documents=documents)[0]
for idx, doc in enumerate(response):
    print("Document: {}".format(documents[idx]))
    print("Entities:")
    for entity in doc.entities:
        print("\tText: {}, Type: {}".format(entity.text, entity.category))
    print()
# Perform key phrase extraction
response = text_analytics_client.extract_key_phrases(documents=documents)[0]
for idx, doc in enumerate(response):
    print("Document: {}".format(documents[idx]))
    print("Key Phrases:")
    for phrase in doc.key_phrases:
        print("\t{}".format(phrase))
    print()
