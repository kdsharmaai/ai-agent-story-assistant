from flask import Flask, render_template, request, jsonify
from langchain_core.messages import AIMessage, HumanMessage
from graph import web_graph

app = Flask(__name__)

@app.route('/ai-agent-story-assistant')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/story', methods=['POST'])
def story_api():
    """API endpoint to handle story interactions"""
    try:
        data = request.get_json()
        user_input = data.get('user_input', '').strip()
        action = data.get('action', 'continue')
        current_story = data.get('current_story', [])

        if not user_input:
            return jsonify({'error': 'No user input provided'}), 400

        # Convert current story from frontend format to LangGraph format
        story_messages = []
        for line in current_story:
            if line['type'] == 'user':
                story_messages.append(HumanMessage(content=line['content']))
            elif line['type'] == 'ai':
                story_messages.append(AIMessage(content=line['content']))

        # Add the new user input
        story_messages.append(HumanMessage(content=user_input))

        # Determine the control flow based on action
        if action == 'start':
            control = 'start'
        else:
            control = 'user_done'

        # Invoke the web graph with the current state
        result = web_graph.invoke({
            "story": story_messages,
            "control": control
        })

        # Extract the AI response from the result
        ai_response = None
        story_messages = result.get("story", [])

        # Look for the latest AI message in the story
        for message in reversed(story_messages):  # Check from newest to oldest
            if isinstance(message, AIMessage):
                ai_response = message.content
                break

        if ai_response:
            return jsonify({
                'ai_response': ai_response,
                'success': True
            })
        else:
            return jsonify({
                'error': 'No AI response generated',
                'success': False
            }), 500
    except Exception as e:
        print(f"Error in story API: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'success': False
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'AI Story Assistant is running'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5003)