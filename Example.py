from instagram import Instagram  # Assuming previous code is saved in instagram.py

def demonstrate_instagram():
    # Initialize Instagram system
    instagram = Instagram()
    
    # Create user profiles
    instagram.create_profile(1, "john_doe", "Photography enthusiast 📸")
    instagram.create_profile(2, "jane_smith", "Travel blogger ✈️")
    instagram.create_profile(3, "mike_jones", "Food lover 🍕")
    
    # Set up following relationships
    instagram.follow(2, 1)  # Jane follows John
    instagram.follow(3, 1)  # Mike follows John
    instagram.follow(1, 2)  # John follows Jane
    
    # Create posts
    print("\n=== Creating Posts ===")
    instagram.post_content(1, 101, "Beautiful sunset at the beach! 🌅")
    instagram.post_content(2, 102, "My morning coffee ☕")
    instagram.post_content(1, 103, "Mountain hiking adventures 🏔️")
    print("Posts created successfully!")
    
    # Add stories
    print("\n=== Adding Stories ===")
    instagram.add_story(1, 201)  # John adds a story
    instagram.add_story(2, 202)  # Jane adds a story
    
    # View stories
    jane_stories = instagram.get_stories(2)
    print(f"Stories visible to Jane: {jane_stories}")
    
    # Interact with posts
    print("\n=== Post Interactions ===")
    # Like posts
    instagram.like_post(2, 101)  # Jane likes John's sunset post
    instagram.like_post(3, 101)  # Mike likes John's sunset post
    instagram.like_post(1, 102)  # John likes Jane's coffee post
    
    # Add comments
    instagram.add_comment(2, 101, "This is gorgeous! Where was this taken? 😍")
    instagram.add_comment(1, 102, "Looks delicious! What blend is this?")
    
    # View feed
    print("\n=== Viewing Feeds ===")
    jane_feed = instagram.get_feed(2)
    print(f"Jane's feed (post IDs): {jane_feed}")
    
    # View comments on a post
    comments = instagram.get_comments(101)
    print("\n=== Comments on Post 101 ===")
    for comment in comments:
        user_id, text, timestamp = comment
        print(f"User {user_id}: {text} at {timestamp}")
    
    # Unlike a post
    print("\n=== Unliking Posts ===")
    instagram.unlike_post(2, 101)
    
    # Unfollow a user
    print("\n=== Unfollowing ===")
    instagram.unfollow(2, 1)
    
    # View updated feed
    updated_jane_feed = instagram.get_feed(2)
    print(f"Jane's updated feed after unfollowing (post IDs): {updated_jane_feed}")

if __name__ == "__main__":
    demonstrate_instagram()