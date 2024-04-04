class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, 'title') and type(value) is str and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, 'name') and type(value) is str and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.magazines()) > 0:
            return [magazine.category for magazine in self.magazines() if len(self.magazines()) > 0]
        else:
            return None
    
    def articles_for_magazine(self, magazine):
        return len([article for article in Article.all if article.magazine == magazine and article.author == self])

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if type(value) is str and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine == self]))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if len(titles) > 0 else None

    def contributing_authors(self):
        answer = [author for author in self.contributors() if author.articles_for_magazine(self) >= 2]
        return answer if len(answer) > 0 else None