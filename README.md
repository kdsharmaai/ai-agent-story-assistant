# 📚 AI Story Assistant - Interactive Story Generation with LangGraph

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-purple.svg)](https://langchain-ai.github.io/langgraph/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-Apache-yellow.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)

> **Advanced AI Story Assistant powered by LangGraph for interactive story generation with intelligent narrative flow control and collaborative storytelling capabilities.**

## 🚀 Overview

The AI Story Assistant is a sophisticated artificial intelligence system that leverages **LangGraph** to create an interactive storytelling experience. Built with modern web technologies and advanced AI frameworks, this project enables users to collaboratively create stories with an AI that maintains narrative coherence and provides engaging story progression.

### ✨ Key Features

- **📖 Interactive Story Generation**: Create stories collaboratively with AI assistance
- **🧠 Intelligent Narrative Flow**: AI maintains story coherence and progression
- **🎯 Controlled Story Development**: Add 1-2 lines at a time for controlled pacing
- **💬 Real-Time Collaboration**: Seamless interaction between user and AI
- **🎨 Modern Web Interface**: Beautiful, responsive design for optimal storytelling experience
- **⚡ Real-Time Processing**: Instant AI responses with smooth animations
- **🌐 Web-Based Access**: Accessible from any device with a web browser
- **🔄 State Management**: Persistent conversation context and story history

## 🏗️ Architecture

### LangGraph Agentic AI Implementation

This project utilizes **LangGraph**, a powerful framework for building stateful, multi-actor applications with LLMs. The story generation architecture enables:

- **Narrative Control**: Intelligent story progression with controlled line additions
- **State Management**: Persistent story context and conversation history
- **Flow Control**: Conditional routing between story start and continuation
- **Error Recovery**: Graceful handling of API failures and edge cases
- **Scalable Design**: Modular architecture supporting easy extension and customization

### Technology Stack

```
Frontend:
├── HTML5 + CSS3 (Modern Design)
├── Vanilla JavaScript (Interactive UI)
└── Responsive Web Design

Backend:
├── Python 3.10+
├── Flask (Web Framework)
├── LangGraph (Agentic AI)
├── LangChain (LLM Integration)
├── OpenAI GPT-4o-mini (Story Generation)
└── Poetry (Dependency Management)

APIs & Services:
├── OpenAI API (Story generation and narrative control)
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- OpenAI API key
- Internet connection for API access

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/kdsharmaai/ai-agent-story-assistant.git
   cd ai-agent-story-assistant
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   poetry run python main.py
   ```

5. **Access the interface**
   ```
   Open http://localhost:5003/ai-agent-story-assistant in your browser
   ```

## 🎯 Usage Examples

### Starting a New Story
```
User: "Once upon a time, there was a brave knight who lived in a castle on a hill."
AI: "The knight, Sir Aldric, spent his days training with his sword and protecting the nearby village from bandits."
```

### Continuing a Story
```
User: "One day, a mysterious letter arrived at the castle."
AI: "The letter bore an ancient seal and contained a plea for help from a distant kingdom."
```

### Interactive Storytelling
```
User: "The knight decided to embark on a journey to help."
AI: "He packed his armor, sword, and provisions, then set out at dawn the next morning."
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Application Settings
FLASK_ENV=development
DEBUG=True
```

### Customization

The story assistant can be easily extended with additional capabilities:

1. **Story Themes**: Modify the system prompt for different story genres
2. **Narrative Styles**: Adjust the AI's storytelling approach and tone
3. **UI Customization**: Update the interface design and user experience
4. **Story Length Control**: Modify the line limit for different pacing
5. **Character Development**: Add specialized prompts for character-focused stories

## 📊 Project Structure

```
ai-agent-story-assistant/
├── main.py              # Flask application entry point
├── graph.py             # LangGraph story flow definition
├── nodes.py             # LangGraph node implementations
├── pyproject.toml       # Poetry configuration
├── poetry.lock          # Dependency lock file
├── README.md            # Project documentation
├── static/              # Static assets
│   └── favicon-16x16.png
└── templates/           # HTML templates
    └── index.html       # Main story interface
```

## 🤖 AI Story Assistant Capabilities

### Intelligent Story Generation

The AI assistant demonstrates advanced narrative understanding:

- **Context Awareness**: Maintains story coherence and character consistency
- **Controlled Pacing**: Adds exactly 1-2 lines to maintain story flow
- **Genre Adaptation**: Adapts storytelling style based on user input
- **Character Development**: Builds characters naturally through story progression

### Narrative Flow Control

The LangGraph implementation enables sophisticated story management:

1. **Story Start Node**: Initiates new stories with proper setup
2. **Story Continue Node**: Adds controlled progression to existing stories
3. **Flow Control**: Manages transitions between story states
4. **State Management**: Maintains story context and conversation history

### Story Generation Process

The LangGraph implementation enables sophisticated story flow:

```
User Input → Intent Recognition → Story State → AI Generation → Response → Display
```

## 🌟 Features in Detail

### Interactive Story Creation
- **Collaborative Writing**: Users and AI work together to create stories
- **Controlled Progression**: AI adds 1-2 lines at a time for optimal pacing
- **Narrative Coherence**: AI maintains story consistency and logical flow
- **Character Consistency**: Characters develop naturally throughout the story

### User Experience
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern Interface**: Clean, intuitive design focused on storytelling
- **Real-Time Feedback**: Live status indicators and smooth animations
- **Story History**: Complete conversation history with user and AI contributions

### Technical Excellence
- **Stateful Architecture**: Client side maintains story context across interactions
- **Error Handling**: Graceful handling of API failures and edge cases
- **Scalable Design**: Modular architecture for easy extension
- **Performance Optimized**: Fast response times and efficient processing

## 🔍 API Endpoints

### Story API
- **POST** `/api/story` - Handle story interactions and AI responses

## 📄 License

This project is licensed under the Apache License - see the [LICENSE](LICENSE.txt) file for details.

## 🙏 Acknowledgments

- **LangGraph Team**: For the powerful agentic AI framework
- **OpenAI**: For the advanced language model capabilities
- **Flask Community**: For the excellent web framework
- **LangChain Team**: For the comprehensive LLM integration tools

---

<div align="center">

**Built with ❤️ using LangGraph and OpenAI for interactive storytelling**

</div>
