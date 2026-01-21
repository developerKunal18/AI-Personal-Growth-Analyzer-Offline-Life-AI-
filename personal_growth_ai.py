positive_words = [
    "improve", "learn", "progress", "happy", "grateful",
    "confident", "success", "calm", "focus", "positive"
]

negative_words = [
    "stress", "sad", "angry", "fail", "tired",
    "anxious", "fear", "negative", "confused", "frustrated"
]

print("🧠 AI Personal Growth Analyzer \n")

text = input("Write your thoughts for today:\n").lower()

pos_score = sum(word in text for word in positive_words)
neg_score = sum(word in text for word in negative_words)

print("\n📊 Analysis Result")

if pos_score > neg_score:
    print("😊 Overall Mood: Positive")
elif neg_score > pos_score:
    print("😔 Overall Mood: Negative")
else:
    print("😐 Overall Mood: Neutral")

print(f"Positive signals: {pos_score}")
print(f"Negative signals: {neg_score}")

print("\n🧭 Growth Feedback")

if neg_score > pos_score:
    print("• Take breaks and reduce stress")
    print("• Practice gratitude")
    print("• Focus on one task at a time")
elif pos_score > 0:
    print("• Keep building positive habits")
    print("• Continue learning and improving")
    print("• Maintain consistency")
else:
    print("• Try journaling more clearly")
    print("• Reflect on your goals")
