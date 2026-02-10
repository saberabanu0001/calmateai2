# seriousness_detector.py

import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Try to initialize VADER sentiment analyzer.
# If the lexicon isn't available (e.g. on Render), we skip sentiment
# and fall back to keyword-only rules instead of crashing.
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
    analyzer = SentimentIntensityAnalyzer()
except LookupError:
    print("VADER lexicon not found; skipping sentiment analysis.")
    analyzer = None

def get_seriousness_level(user_input, qa_chain_for_llm_check=None):
    """
    Analyzes the user's message to determine a seriousness level.
    Uses keyword matching and sentiment analysis.
    
    Args:
        user_input (str): The text message from the user.
        qa_chain_for_llm_check: (unused) kept for backward compatibility.

    Returns:
        str: The seriousness level ("Low", "Medium", "High", or "Emergency").
    """
    
    # --- Keyword and Pattern Matching (Rule-based) ---
    emergency_keywords = re.compile(
        r'\b(suicide|kill myself|end my life|die|self-harm|harm myself|cutting|overdose|in danger|i need help now)\b',
        re.IGNORECASE
    )
    high_keywords = re.compile(
        r"\b(hopeless|worthless|can't go on|give up|no purpose|can't take it anymore|lost|alone|trapped|scared|crisis|panic attack|anxious|depressed|depression|extreme pain|severe pain|unbearable pain|debilitating pain)\b",
        re.IGNORECASE
    )
    medium_keywords = re.compile(
        r'\b(stress|stressed|anxious|anxiety|sad|unhappy|tired|overwhelmed|struggling|bad day|tough time|feeling down)\b',
        re.IGNORECASE
    )

    if emergency_keywords.search(user_input):
        return "Emergency"
    if high_keywords.search(user_input):
        return "High"
    
    # --- Sentiment Analysis (Nuance-based) ---
    # We only run this if the keywords didn't trigger a High or Emergency level
    if analyzer is not None:
        sentiment = analyzer.polarity_scores(user_input)
        compound_score = sentiment["compound"]
        
        # If the compound sentiment score is very negative, it might be a medium level
        if compound_score <= -0.5:
            return "Medium"
    
    # --- Default Level ---
    # If none of the above conditions are met, default to 'Low'
    return "Low"
