"""
Reddit Scraper for UIUC Course Reviews
Optional module to scrape course discussions from r/UIUC.

Requires Reddit API credentials:
- client_id: from reddit.com/prefs/apps
- client_secret: from reddit.com/prefs/apps
- user_agent: custom identifier
"""

import praw
import pandas as pd
import re
from datetime import datetime


class RedditScraper:
    """Scrapes course-related posts from r/UIUC subreddit."""

    def __init__(self, client_id, client_secret, user_agent):
        """
        Initialize Reddit API connection.

        Args:
            client_id: Reddit API client ID
            client_secret: Reddit API client secret
            user_agent: Custom user agent string
        """
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        self.subreddit = self.reddit.subreddit('UIUC')

    def search_course_posts(self, course_code, limit=100):
        """
        Search for posts mentioning a specific course.

        Args:
            course_code: Course code to search for (e.g., 'CS124')
            limit: Maximum number of posts to retrieve

        Returns:
            List of post dictionaries
        """
        posts = []
        search_query = course_code

        for post in self.subreddit.search(search_query, limit=limit):
            posts.append({
                'title': post.title,
                'text': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc': datetime.fromtimestamp(post.created_utc),
                'url': post.url
            })

        return posts

    def get_course_comments(self, course_code, limit=50):
        """
        Get comments from posts mentioning a specific course.

        Args:
            course_code: Course code to search for
            limit: Maximum number of posts to check

        Returns:
            List of comment dictionaries
        """
        comments = []

        for post in self.subreddit.search(course_code, limit=limit):
            post.comments.replace_more(limit=0)
            for comment in post.comments.list():
                if hasattr(comment, 'body'):
                    comments.append({
                        'course_code': course_code,
                        'text': comment.body,
                        'score': comment.score,
                        'created_utc': datetime.fromtimestamp(comment.created_utc)
                    })

        return comments

    def scrape_multiple_courses(self, course_codes, limit_per_course=50):
        """
        Scrape posts for multiple courses.

        Args:
            course_codes: List of course codes
            limit_per_course: Max posts per course

        Returns:
            DataFrame with all scraped data
        """
        all_data = []

        for code in course_codes:
            print(f"Scraping posts for {code}...")
            posts = self.search_course_posts(code, limit=limit_per_course)

            for post in posts:
                all_data.append({
                    'course_code': code,
                    'course_name': code,  # Will need manual mapping
                    'review': f"{post['title']} {post['text']}",
                    'rating': None,  # Reddit doesn't have ratings
                    'semester': None,
                    'source': 'reddit',
                    'score': post['score']
                })

        df = pd.DataFrame(all_data)
        return df

    def save_to_csv(self, df, output_path='data/reddit_reviews.csv'):
        """Save scraped data to CSV file."""
        df.to_csv(output_path, index=False)
        print(f"Saved {len(df)} reviews to {output_path}")


def main():
    """
    Example usage of the scraper.

    To use this scraper:
    1. Create a Reddit app at https://www.reddit.com/prefs/apps
    2. Get your client_id and client_secret
    3. Replace the placeholders below with your credentials
    """
    print("Reddit Scraper for UIUC Course Reviews")
    print("=" * 50)
    print("\nTo use this scraper, you need Reddit API credentials.")
    print("1. Go to https://www.reddit.com/prefs/apps")
    print("2. Create a new 'script' application")
    print("3. Copy your client_id and client_secret")
    print("\nExample usage:")
    print("""
    scraper = RedditScraper(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='UIUC Course Analyzer 1.0'
    )

    # Scrape posts for specific courses
    courses = ['CS124', 'CS225', 'CS374', 'STAT400']
    df = scraper.scrape_multiple_courses(courses)
    scraper.save_to_csv(df)
    """)


if __name__ == "__main__":
    main()
