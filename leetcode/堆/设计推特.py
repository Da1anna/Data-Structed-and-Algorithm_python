'''
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-twitter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路：
    数据结构：
        每个用户的推文设计为一个链表，链表节点存储推文id和发布时间（用一个全局整数表示）
        每个用户的关注列表设计为一个哈希set
        然后以上两个都设计为一个字典，键为用户id，值分别为推文和关注列表
    算法：
        难点在于第二个方法
        本质上是k个链表的有序合并，用 堆+链表
        将每个链表入小顶堆，取出堆顶点元素，链表后移，重复这个过程，直到取出目标数量
'''
from collections import defaultdict
import heapq as hp

class Tweet:

    def __init__(self,tweet_id,time):
        self.tweet_id = tweet_id
        self.time = time
        self.next = None

    def __lt__(self, other):    #只定义小于比较符就可以了吗？
        return self.time > other.time

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(lambda:None)      #这个lambda:None怎么用：设置字典中value的默认值，调用为空时，会返回None
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        #链表的头插法
        tweet = Tweet(tweetId,self.time)
        tweet.next = self.tweets[userId]
        self.tweets[userId] = tweet

    def getNewsFeed(self, userId: int) -> [int]:
        tweet_10 = []
        #将满足的链表入堆
        heap = []
        if self.tweets[userId]:
            heap.append(self.tweets[userId])
        for user_id in self.followers[userId]:
            if self.tweets[user_id]:
                heap.append(self.tweets[user_id])
        hp.heapify(heap)
        #取出10前条推文
        while heap and len(tweet_10) < 10:
            tweet = hp.heappop(heap)
            tweet_10.append(tweet.tweet_id)
            if tweet.next:
                hp.heappush(heap, tweet.next)
        return tweet_10

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followers[followerId].discard(followeeId)

#测试
twitter = Twitter()

# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5)

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1)

# // 用户1关注了用户2.
twitter.follow(1, 2)

# // 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6)

# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
res = twitter.getNewsFeed(1)
print(res)
# // 用户1取消关注了用户2.
twitter.unfollow(1, 2)

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1)