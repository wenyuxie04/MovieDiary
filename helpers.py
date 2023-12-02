class diary:
    id: int
    title: str
    genre: str
    review: str

    def __init__(self, id: int, title: str, genre: str, review: str):
        self.id = id
        self.title = title
        self.genre = genre
        self.review = review

    