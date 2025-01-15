from typing import Any, Dict

class PromptBuilder:
    """Handles the construction of prompt strings."""

    @staticmethod
    def build_blog_prompt(row: Dict[str, Any]) -> str:
        """
        Constructs the senior editor prompt based on CSV row data.
        """
        topic = row.get('Topic', 'Unknown Topic')
        tone = row.get('Tone', 'Professional')
        audience = row.get('Target Audience', 'General Reader')
        word_limit = row.get('Word Limit', '1000')

        return (
        f"Role: You are a Senior Technical Editor for a world-class technology publication. "
        f"Your goal is to write a blog post about '{topic}' that is authoritative, engaging, and visually structured.\n\n"

        f"### ⚙️ CONTENT SPECIFICATIONS\n"
        f"- **Topic:** {topic}\n"
        f"- **Target Audience:** {audience} (Assume they are smart but busy. Respect their time.)\n"
        f"- **Tone:** {tone} (Professional, yet accessible)\n"
        f"- **Target Word Count:** {word_limit} words\n\n"

        f"### 📝 STRICT MARKDOWN STYLE GUIDE (NON-NEGOTIABLE)\n"
        f"1. **Output Format:** Your response must be pure Markdown. Do NOT include conversational filler like 'Here is the draft'. Start directly with the title.\n"
        f"2. **Headings:** Use `#` for the Title (H1), `##` for Sections (H2), and `###` for Subsections (H3). Never use H4.\n"
        f"3. **Visual Anchors:** You MUST include the following Markdown elements:\n"
        f"   - **Tables:** Use `| Column | Column |` syntax for comparing tools, pros/cons, or data.\n"
        f"   - **Code Blocks:** Use triple backticks with language tags (e.g., ```python) for ALL code or terminal commands.\n"
        f"   - **Callouts:** Use blockquotes (`>`) for 'Pro Tips', 'Warnings', or 'Key Definitions'.\n"
        f"   - **Lists:** Use bullet points (`-`) for readability. Avoid walls of text.\n"
        f"   - **Emphasis:** Use **bold** for key terms and *italics* for nuance.\n\n"

        f"### 🏗️ REQUIRED ARTICLE STRUCTURE\n"
        f"1. **# High-Impact Title:** (Must be catchy and include keywords)\n"
        f"2. **Introduction:** Use the 'Hook-Agitate-Solve' method. State the problem clearly and promise the solution.\n"
        f"3. **Deep Dive Sections (The 'Meat'):** \n"
        f"   - Break the topic into 4-5 logical chapters.\n"
        f"   - **MANDATORY:** Include a Markdown Table in one of these sections.\n"
        f"   - **MANDATORY:** If the topic implies it, include a code snippet or a step-by-step list.\n"
        f"4. **Interactive Summary:** A 'Checklist for Success' or 'Key Takeaways' section.\n"
        f"5. **FAQ:** Answer 3 specific questions real users ask about this topic.\n"
        f"6. **Conclusion:** A brief wrap-up with a strong Call to Action (CTA).\n\n"

        f"### 🚫 WRITING RULES\n"
        f"- No fluff. No 'In today's digital landscape' intros.\n"
        f"- Use active voice.\n"
        f"- Keep paragraphs short (max 3-4 lines).\n\n"

        f"Start writing the content now, beginning strictly with the H1 Title."
        )