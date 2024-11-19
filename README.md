# InstaStruct
## Project Overview
InstaStruct is a social media platform that implements core features similar to Instagram, built with a focus on efficient data structures and algorithms. The application provides a robust foundation for social media interactions while maintaining optimal performance.
## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)


### Features

1. **User Profiles**: Allows users to create and manage personal profiles that include a username and bio, enhancing personalization.
2. **Content Posting**: Users can share posts with optional captions, which can receive likes and comments from other users.
3. **Stories**: Users can add temporary stories that disappear after 24 hours, similar to features found on popular social media platforms.
4. **Follow System**: Facilitates social networking by allowing users to follow others, enabling them to see posts from those they follow in their feeds.
5. **Feed Generation**: Automatically generates a personalized feed for users based on their following relationships, showcasing recent posts from followed users.
6. **Commenting**: Encourages interaction by allowing users to comment on each other's posts, fostering community engagement.
7. **Like/Unlike Functionality**: Lets users express appreciation for posts through likes, with the ability to remove likes as well.

## Getting Started


### Prerequisites

- **Python 3**: Ensure you have Python 3 installed on your machine.
- You can download it from [python.org](https://www.python.org/downloads/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mevsaurabh/InstaStruct.git
2.  Navigate to the project directory:
```bash
cd InstaStruct
```

## Usage
Provide examples of how to use your project. Include code snippets if applicable.
```bash
from instagram import Instagram


# Initialize the Instagram system
instagram = Instagram()

# Create a user profile
instagram.create_profile(1, "Ansh", "Photography enthusiast 📸")
```

# Data Structures

## Post Management
```
post_map = defaultdict(list)  # userId -> [count, postId, caption, likes, comments]
```
- Optimized for O(1) post retrieval
- Maintains chronological order


## Social Graph
```
follow_map = defaultdict(set)  # userId -> set of followeeId
```
- Efficient follower relationship management
- O(1) follow/unfollow operations


## Engagement Tracking
```
like_map = defaultdict(set)    # postId -> set of userIds
comment_map = defaultdict(list) # postId -> [userId, comment, timestamp]
```
- Fast like/unlike operations
- Chronological comment ordering

# Performance Characteristics
## Time Complexity

- Post Creation: O(1)
- Feed Generation: O(k log f) where:

- k = posts retrieved
- f = followed users


- Like/Unlike: O(1)
- Follow/Unfollow: O(1)

## Space Complexity
O(U + P + S + L + C) where:

- U = Users
- P = Posts
- S = Stories
- L = Likes
- C = Comments

# Key Benefits

## Scalability

- Efficient data structures for large user bases
- Optimized feed generation algorithm
- Memory-efficient storage


## Performance

- Fast content retrieval
- Efficient social interactions
- Quick feed updates


## Maintainability

- Clear code structure
- Well-documented functions
- Modular design


## Extensibility

- Easy to add new features
- Flexible data structures
- Robust foundation
