# Specialization [![Build Status](https://travis-ci.org/HarrisonGregg/Specialization.svg?branch=master)](https://travis-ci.org/HarrisonGregg/Specialization)

Connective Media education technology specialization project 

## API Documentation

### Get Topics
GET /topics/

Response:
```json
[
    {
        "name": "Bananas",
        "pk": 1
    }
]
```

### Add Topic
POST /topics/

Body:
```json
{
    "name": "Bananas"
}
```

Response:
```json
{
    "name": "Bananas",
    "pk": 1
}
```

### Get Links for Topic
GET /topicLinks/{topic}/

Response:
```json
[
    {
    	"title":"Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Banana",
        "score": 7,
        "pk": 1,
        "topic": 1
    }
]
```

### Add Link
POST /links/

Body:
```json
{
	"title":"Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Banana",
    "topic": 1
}
```

Response:
```json
{
	"title":"Wikipedia",
	"url": "https://en.wikipedia.org/wiki/Cavendish_banananananana",
	"score": 0,
	"pk": 5,
	"topic": 1
}
```

### Update link
PUT /links/{linkId}/

Body:
```json
{
	"title":"Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}
```

Response:
```json
{
	"title":"Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}
```

### Upvote link
PUT /upvote/{linkId}/

Response:
```json
{
	"title":"Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}
```

### Downvote link
PUT /downvote/{linkId}/

Response:
```json
{
	"title":"Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}
```

### Delete Link
DELETE /links/{linkId}/

