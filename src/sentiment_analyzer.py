"""
UIUC Course Review Sentiment Analyzer
Analyzes course reviews using VADER and TextBlob sentiment analysis.
"""

import pandas as pd
import numpy as np
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download required NLTK data
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


class CourseReviewAnalyzer:
    """Analyzes course reviews for sentiment and topic extraction."""

    def __init__(self, data_path='data/sample_reviews.csv'):
        """Initialize the analyzer with data from CSV file."""
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.vader = SentimentIntensityAnalyzer()

        # Topic keywords for extraction
        self.topic_keywords = {
            'difficulty': ['hard', 'difficult', 'easy', 'challenging', 'tough', 'struggle', 'simple'],
            'workload': ['homework', 'assignments', 'projects', 'work', 'time', 'workload', 'labs'],
            'teaching': ['professor', 'instructor', 'lecture', 'teaching', 'explains', 'teacher', 'lectures'],
            'exams': ['exam', 'test', 'midterm', 'final', 'quiz', 'exams', 'tests'],
            'helpful': ['helpful', 'useful', 'practical', 'applicable', 'TAs', 'office hours', 'resources']
        }

    def clean_text(self, text):
        """Clean and preprocess text."""
        if pd.isna(text):
            return ""
        # Convert to lowercase
        text = str(text).lower()
        # Remove special characters but keep spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text

    def analyze_sentiment_vader(self, text):
        """Analyze sentiment using VADER. Returns 'Positive', 'Negative', or 'Neutral'."""
        if not text:
            return 'Neutral'
        scores = self.vader.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            return 'Positive'
        elif compound <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    def analyze_sentiment_textblob(self, text):
        """Analyze sentiment using TextBlob. Returns 'Positive', 'Negative', or 'Neutral'."""
        if not text:
            return 'Neutral'
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            return 'Positive'
        elif polarity < -0.1:
            return 'Negative'
        else:
            return 'Neutral'

    def extract_topics(self, text):
        """Extract topics from text based on keyword matching."""
        if not text:
            return ['general']

        text_lower = text.lower()
        found_topics = []

        for topic, keywords in self.topic_keywords.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    found_topics.append(topic)
                    break

        return found_topics if found_topics else ['general']

    def analyze_all(self):
        """Run complete analysis pipeline on all reviews."""
        print("=" * 60)
        print("UIUC Course Review Sentiment Analyzer")
        print("=" * 60)
        print(f"Loaded {len(self.df)} reviews from {self.data_path}")
        print("\nAnalyzing reviews...")

        # Clean text
        self.df['cleaned_review'] = self.df['review'].apply(self.clean_text)

        # Sentiment analysis
        self.df['sentiment_vader'] = self.df['review'].apply(self.analyze_sentiment_vader)
        self.df['sentiment_textblob'] = self.df['review'].apply(self.analyze_sentiment_textblob)

        # Topic extraction
        self.df['topics'] = self.df['review'].apply(self.extract_topics)

        # Save results
        output_path = 'results/analyzed_reviews.csv'
        self.df.to_csv(output_path, index=False)
        print(f"\nAnalysis complete! Results saved to {output_path}")

        return self.df

    def get_course_summary(self, course_code):
        """Get summary statistics for a specific course."""
        course_df = self.df[self.df['course_code'] == course_code]

        if course_df.empty:
            return None

        summary = {
            'course_code': course_code,
            'course_name': course_df['course_name'].iloc[0],
            'total_reviews': len(course_df),
            'avg_rating': course_df['rating'].mean(),
            'sentiment_distribution': course_df['sentiment_vader'].value_counts().to_dict(),
            'common_topics': self._get_common_topics(course_df)
        }

        return summary

    def _get_common_topics(self, df):
        """Get the most common topics from a dataframe."""
        all_topics = []
        for topics in df['topics']:
            if isinstance(topics, list):
                all_topics.extend(topics)
            else:
                # Handle string representation of list
                try:
                    topics_list = eval(topics)
                    all_topics.extend(topics_list)
                except:
                    pass

        from collections import Counter
        return dict(Counter(all_topics).most_common(5))

    def get_overall_statistics(self):
        """Get overall statistics for all reviews."""
        stats = {
            'total_reviews': len(self.df),
            'total_courses': self.df['course_code'].nunique(),
            'avg_rating': self.df['rating'].mean(),
            'sentiment_distribution': self.df['sentiment_vader'].value_counts().to_dict(),
            'rating_by_sentiment': self.df.groupby('sentiment_vader')['rating'].mean().to_dict()
        }
        return stats

    def print_sample_results(self, n=5):
        """Print sample results."""
        print("\n" + "=" * 60)
        print("SAMPLE RESULTS")
        print("=" * 60)
        print(f"\nFirst {n} analyzed reviews:")
        print(self.df[['course_code', 'course_name', 'rating', 'sentiment_vader', 'topics']].head(n).to_string())

    def print_overall_statistics(self):
        """Print overall statistics."""
        stats = self.get_overall_statistics()
        print("\n" + "=" * 60)
        print("OVERALL STATISTICS")
        print("=" * 60)
        for key, value in stats.items():
            print(f"{key}: {value}")


def main():
    """Main function to run the analyzer."""
    analyzer = CourseReviewAnalyzer()
    analyzer.analyze_all()
    analyzer.print_sample_results()
    analyzer.print_overall_statistics()

    # Print course summaries
    print("\n" + "=" * 60)
    print("COURSE SUMMARIES")
    print("=" * 60)
    for course in analyzer.df['course_code'].unique():
        summary = analyzer.get_course_summary(course)
        if summary:
            print(f"\n{summary['course_code']} - {summary['course_name']}")
            print(f"  Reviews: {summary['total_reviews']}, Avg Rating: {summary['avg_rating']:.2f}")
            print(f"  Sentiment: {summary['sentiment_distribution']}")


if __name__ == "__main__":
    main()
