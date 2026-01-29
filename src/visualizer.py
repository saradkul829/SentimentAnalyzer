"""
UIUC Course Review Visualizer
Generates visualizations from analyzed course reviews.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os


class ReviewVisualizer:
    """Generates visualizations for course review analysis."""

    # Color scheme
    COLORS = {
        'Positive': '#2ecc71',  # Green
        'Neutral': '#95a5a6',   # Gray
        'Negative': '#e74c3c'   # Red
    }

    def __init__(self, data_path='results/analyzed_reviews.csv'):
        """Initialize visualizer with analyzed data."""
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.output_dir = 'visualizations'

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Set style
        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette([self.COLORS['Positive'], self.COLORS['Neutral'], self.COLORS['Negative']])

    def plot_sentiment_distribution(self):
        """Create bar chart of overall sentiment distribution."""
        plt.figure(figsize=(10, 6))

        sentiment_counts = self.df['sentiment_vader'].value_counts()
        colors = [self.COLORS.get(s, '#333333') for s in sentiment_counts.index]

        ax = sentiment_counts.plot(kind='bar', color=colors, edgecolor='black')
        plt.title('Overall Sentiment Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Number of Reviews', fontsize=12)
        plt.xticks(rotation=0)

        # Add value labels on bars
        for i, v in enumerate(sentiment_counts.values):
            ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/sentiment_distribution.png', dpi=300)
        plt.close()
        print("Created: sentiment_distribution.png")

    def plot_course_comparison(self):
        """Create stacked bar chart comparing sentiment across courses."""
        plt.figure(figsize=(12, 6))

        # Calculate sentiment percentages per course
        course_sentiment = pd.crosstab(
            self.df['course_code'],
            self.df['sentiment_vader'],
            normalize='index'
        ) * 100

        # Reorder columns
        cols = ['Positive', 'Neutral', 'Negative']
        course_sentiment = course_sentiment.reindex(columns=[c for c in cols if c in course_sentiment.columns])

        colors = [self.COLORS.get(c, '#333333') for c in course_sentiment.columns]
        course_sentiment.plot(kind='bar', stacked=True, color=colors, edgecolor='black')

        plt.title('Sentiment Distribution by Course', fontsize=14, fontweight='bold')
        plt.xlabel('Course Code', fontsize=12)
        plt.ylabel('Percentage (%)', fontsize=12)
        plt.legend(title='Sentiment', bbox_to_anchor=(1.02, 1), loc='upper left')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/course_comparison.png', dpi=300)
        plt.close()
        print("Created: course_comparison.png")

    def plot_rating_vs_sentiment(self):
        """Create box plot comparing ratings by sentiment."""
        plt.figure(figsize=(10, 6))

        order = ['Positive', 'Neutral', 'Negative']
        colors = [self.COLORS.get(s, '#333333') for s in order if s in self.df['sentiment_vader'].unique()]

        sns.boxplot(
            data=self.df,
            x='sentiment_vader',
            y='rating',
            order=[o for o in order if o in self.df['sentiment_vader'].unique()],
            palette=colors
        )

        plt.title('Rating Distribution by Sentiment', fontsize=14, fontweight='bold')
        plt.xlabel('Sentiment', fontsize=12)
        plt.ylabel('Rating (1-5)', fontsize=12)

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/rating_vs_sentiment.png', dpi=300)
        plt.close()
        print("Created: rating_vs_sentiment.png")

    def plot_course_ratings(self):
        """Create bar chart of average ratings by course."""
        plt.figure(figsize=(12, 6))

        avg_ratings = self.df.groupby('course_code')['rating'].mean().sort_values(ascending=False)

        colors = plt.cm.RdYlGn([(r - 1) / 4 for r in avg_ratings.values])
        ax = avg_ratings.plot(kind='bar', color=colors, edgecolor='black')

        plt.title('Average Rating by Course', fontsize=14, fontweight='bold')
        plt.xlabel('Course Code', fontsize=12)
        plt.ylabel('Average Rating', fontsize=12)
        plt.ylim(0, 5.5)
        plt.axhline(y=avg_ratings.mean(), color='red', linestyle='--', label=f'Overall Avg: {avg_ratings.mean():.2f}')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        # Add value labels
        for i, v in enumerate(avg_ratings.values):
            ax.text(i, v + 0.1, f'{v:.1f}', ha='center', fontsize=9)

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/course_ratings.png', dpi=300)
        plt.close()
        print("Created: course_ratings.png")

    def plot_wordcloud_positive(self):
        """Create word cloud from positive reviews."""
        positive_text = ' '.join(self.df[self.df['sentiment_vader'] == 'Positive']['review'].astype(str))

        if not positive_text.strip():
            print("Skipped: wordcloud_positive.png (no positive reviews)")
            return

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='Greens',
            max_words=100
        ).generate(positive_text)

        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud - Positive Reviews', fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/wordcloud_positive.png', dpi=300)
        plt.close()
        print("Created: wordcloud_positive.png")

    def plot_wordcloud_negative(self):
        """Create word cloud from negative reviews."""
        negative_text = ' '.join(self.df[self.df['sentiment_vader'] == 'Negative']['review'].astype(str))

        if not negative_text.strip():
            print("Skipped: wordcloud_negative.png (no negative reviews)")
            return

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='Reds',
            max_words=100
        ).generate(negative_text)

        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud - Negative Reviews', fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/wordcloud_negative.png', dpi=300)
        plt.close()
        print("Created: wordcloud_negative.png")

    def plot_topic_distribution(self):
        """Create horizontal bar chart of topic frequencies."""
        # Extract all topics
        all_topics = []
        for topics in self.df['topics']:
            if isinstance(topics, list):
                all_topics.extend(topics)
            else:
                try:
                    topics_list = eval(topics)
                    all_topics.extend(topics_list)
                except:
                    pass

        if not all_topics:
            print("Skipped: topic_distribution.png (no topics found)")
            return

        from collections import Counter
        topic_counts = Counter(all_topics)

        plt.figure(figsize=(10, 6))

        topics = list(topic_counts.keys())
        counts = list(topic_counts.values())

        colors = plt.cm.viridis([i / len(topics) for i in range(len(topics))])

        plt.barh(topics, counts, color=colors, edgecolor='black')
        plt.title('Topic Distribution in Reviews', fontsize=14, fontweight='bold')
        plt.xlabel('Number of Mentions', fontsize=12)
        plt.ylabel('Topic', fontsize=12)

        # Add value labels
        for i, v in enumerate(counts):
            plt.text(v + 0.5, i, str(v), va='center')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/topic_distribution.png', dpi=300)
        plt.close()
        print("Created: topic_distribution.png")

    def generate_all(self):
        """Generate all visualizations."""
        print("=" * 60)
        print("Generating Visualizations")
        print("=" * 60)
        print(f"Output directory: {self.output_dir}/\n")

        self.plot_sentiment_distribution()
        self.plot_course_comparison()
        self.plot_rating_vs_sentiment()
        self.plot_course_ratings()
        self.plot_wordcloud_positive()
        self.plot_wordcloud_negative()
        self.plot_topic_distribution()

        print("\n" + "=" * 60)
        print("All visualizations generated successfully!")
        print("=" * 60)


def main():
    """Main function to generate all visualizations."""
    visualizer = ReviewVisualizer()
    visualizer.generate_all()


if __name__ == "__main__":
    main()
