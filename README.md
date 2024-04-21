# Document Similarity API

## Description
This Flask API calculates the cosine similarity between a list of documents and returns the similarity matrix along with the path to the saved heatmap image.

## Usage
Send a POST request to `/api/similarity` with a JSON payload containing a list of documents. The API will respond with a JSON object containing the similarity matrix and the path to the saved heatmap image.

### Example Request
```json
{
  "documents": [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
  ]
}
