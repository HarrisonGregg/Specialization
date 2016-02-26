# Specialization
Connective Media education technology specialization project 

## API Documentation

### Get Links for Topic
GET /topicLinks/<topic>
Response:
[
    {
        "url": "https://en.wikipedia.org/wiki/Banana",
        "score": 7,
        "pk": 1,
        "topic": 1
    }
]

### Add Link
POST /links/
Body:
{
    "url": "https://en.wikipedia.org/wiki/Banana",
    "topic": 1
}
Response:
{
	"url": "https://en.wikipedia.org/wiki/Cavendish_banananananana",
	"score": 0,
	"pk": 5,
	"topic": 1
}

### Update link
PUT /links/<linkId>
Body:
{
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}
Response:
{
    "url": "https://en.wikipedia.org/wiki/Cavendish_bananas",
    "score": 7,
    "pk": 2,
    "topic": 1
}

### Delete Link
DELETE /links/<linkId>

