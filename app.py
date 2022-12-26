import os
os.environ["OPENAI_SECRET_KEY"] = "YOUR_API_KEY"

import openai
import panel as pn

# Define the GPT-3 model to use
model_engine = "text-davinci-002"

# Create a Voilà dashboard
app = pn.Column(
    pn.pane.Markdown("# Argumentative Essay Evaluator"),
    pn.pane.Markdown("Enter your essay in the text box below:"),
    pn.widgets.TextArea(value="Enter your essay here...", width=800),
    pn.pane.Markdown("Press the button to receive a score from GPT-3:"),
    pn.widgets.Button(name="Evaluate Essay", width=200),
)


# Define the callback function for the button
def evaluate_essay(event):
    essay = event.widget.parent.objects[1].value

    # Use the GPT-3 API to evaluate the essay
    prompt = (f"Evaluate the argumentative essay:\n{essay}\n")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the score from the GPT-3 response
    score = completions.choices[0].text.strip()

    # Update the Voilà dashboard with the score
    event.widget.parent.objects[2].value = score


# Add the callback function to the button
app[3].on_click(evaluate_essay)

# Display the dashboard
app.show()
