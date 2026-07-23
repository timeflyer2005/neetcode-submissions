class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        result = []
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))
        
        while heap and len(result) < 10:
            negative_time, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)
            previous_index = index - 1
            
            if previous_index >= 0:
                time, previous_tweetId = self.tweets[user][previous_index]
                heapq.heappush(heap, (-time, previous_tweetId, user, previous_index))
            
        return result     
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
