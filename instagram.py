from collections import defaultdict
import heapq
from typing import List, Dict
from datetime import datetime, timedelta

class Instagram:
    def __init__(self):
        # Basic counters
        self.post_count = 0
        self.story_count = 0
        
        # Core data structures
        self.post_map = defaultdict(list)  # userId -> list of [count, postId, caption, likes, comments]
        self.follow_map = defaultdict(set)  # userId -> set of followeeId
        self.story_map = defaultdict(list)  # userId -> list of [count, storyId, timestamp]
        self.like_map = defaultdict(set)    # postId -> set of userIds who liked
        self.comment_map = defaultdict(list) # postId -> list of [userId, comment_text, timestamp]
        self.user_data = defaultdict(dict)  # userId -> user profile info
        
    def create_profile(self, userId: int, username: str, bio: str = "") -> None:
        """Create or update user profile with basic information"""
        self.user_data[userId] = {
            "username": username,
            "bio": bio,
            "post_count": 0,
            "follower_count": 0,
            "following_count": 0
        }
    
    def post_content(self, userId: int, postId: int, caption: str = "") -> None:
        """Create a new post with optional caption"""
        # Add post to user's posts with initial like and comment counts
        self.post_map[userId].append([
            self.post_count,  # For chronological ordering
            postId,
            caption,
            0,  # likes count
            0   # comments count
        ])
        self.user_data[userId]["post_count"] += 1
        self.post_count -= 1  # Decrement for min heap ordering
    
    def add_story(self, userId: int, storyId: int) -> None:
        """Add a story that expires after 24 hours"""
        current_time = datetime.now()
        self.story_map[userId].append([
            self.story_count,
            storyId,
            current_time
        ])
        self.story_count -= 1
    
    def get_stories(self, userId: int) -> List[int]:
        """Get active stories from people user follows"""
        current_time = datetime.now()
        active_stories = []
        
        for followeeId in self.follow_map[userId]:
            # Filter stories less than 24 hours old
            valid_stories = [
                story for story in self.story_map[followeeId]
                if current_time - story[2] < timedelta(hours=24)
            ]
            if valid_stories:
                active_stories.extend([story[1] for story in valid_stories])
        
        return active_stories
    
    def get_feed(self, userId: int) -> List[int]:
        """Get recent posts from followed users"""
        res = []
        min_heap = []
        self.follow_map[userId].add(userId)  # Include user's own posts
        
        # Initialize heap with most recent post from each followed user
        for followeeId in self.follow_map[userId]:
            if followeeId in self.post_map and self.post_map[followeeId]:
                index = len(self.post_map[followeeId]) - 1
                count, postId, caption, likes, comments = self.post_map[followeeId][index]
                heapq.heappush(min_heap, [count, postId, followeeId, index - 1])
        
        # Get 10 most recent posts
        while min_heap and len(res) < 10:
            count, postId, followeeId, index = heapq.heappop(min_heap)
            res.append(postId)
            if index >= 0:
                count, postId, caption, likes, comments = self.post_map[followeeId][index]
                heapq.heappush(min_heap, [count, postId, followeeId, index - 1])
                
        return res
    
    def like_post(self, userId: int, postId: int) -> None:
        """Like a post"""
        self.like_map[postId].add(userId)
        # Update like count in post_map
        for user_posts in self.post_map.values():
            for post in user_posts:
                if post[1] == postId:
                    post[3] = len(self.like_map[postId])
                    break
    
    def unlike_post(self, userId: int, postId: int) -> None:
        """Unlike a post"""
        if userId in self.like_map[postId]:
            self.like_map[postId].remove(userId)
            # Update like count in post_map
            for user_posts in self.post_map.values():
                for post in user_posts:
                    if post[1] == postId:
                        post[3] = len(self.like_map[postId])
                        break
    
    def add_comment(self, userId: int, postId: int, comment_text: str) -> None:
        """Add a comment to a post"""
        self.comment_map[postId].append([userId, comment_text, datetime.now()])
        # Update comment count in post_map
        for user_posts in self.post_map.values():
            for post in user_posts:
                if post[1] == postId:
                    post[4] = len(self.comment_map[postId])
                    break
    
    def get_comments(self, postId: int) -> List[Dict]:
        """Get all comments for a post"""
        return self.comment_map[postId]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        """Follow a user"""
        self.follow_map[followerId].add(followeeId)
        self.user_data[followerId]["following_count"] += 1
        self.user_data[followeeId]["follower_count"] += 1
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Unfollow a user"""
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
            self.user_data[followerId]["following_count"] -= 1
            self.user_data[followeeId]["follower_count"] -= 1
            
