import random
import string

class Codec:
    
    def __init__(self):
        self.mapping = {}
        
        
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.mapping[shortUrl] = longUrl
        return shortUrl
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.mapping[shortUrl]
