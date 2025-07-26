import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyBrNJFN3UriVObZNmEm5x5gL4t0xVSf3rk"

# Configure the API
genai.configure(api_key=API_KEY)

# Use correct model name from supported list
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")


# Sample resume text (replace with actual input or file reading logic)
resume_text = """
Suriya
Final Year B.Tech AI & DS student
SNS College of Engineering
Experienced in Python, ML, DL, Power BI
District-level basketball champion
Looking to pursue MS in Germany
"""

def analyze_resume(text):
    prompt = f"""Analyze the following resume and provide feedback on:
1. Strengths
2. Weaknesses
3. Suggestions for improvement
4. Possible job roles based on skills

Resume:
{text}
"""
    response = model.generate_content(prompt)
    return response.text


# Call the analysis function and print result
if __name__ == "__main__":
    suggestions = analyze_resume(resume_text)
    print("Resume Suggestions:\n")
    print(suggestions)
