# EGATE Talent Center – Cybersecurity Learning Platform

## Project Overview
Build a learning platform for EGATE Talent Center that starts with cybersecurity but is structured to support other departments' learning paths in the future. The platform gives students a central place to practice cybersecurity skills through original CTF challenges, structured learning paths, and AI-assisted hints.

## Objectives
- Build a learning platform for EGATE Center that is not limited to a single format, starting with cybersecurity but structured to support other departments' learning paths in the future.
- Give students a central place to practice cybersecurity skills through original CTF challenges.
- Provide a structured learning path that connects to trusted external platforms rather than duplicating their content.
- Introduce an AI-assisted hint feature to support learners without removing the challenge.
- Track progress and scores to give students visible feedback on their skill development.

## MVP Scope (2-Week Cycle)

### In Scope
- User registration and login
- A dashboard showing points and progress
- 8–10 original CTF challenges across 3–4 categories
- Flag submission with automatic validation
- A simple point-based leaderboard
- A learning path page linking to TryHackMe, picoCTF, and 1–2 additional platforms, organized by topic and difficulty
- An AI-powered hint assistant integrated into the challenge view

### Out of Scope (Future Work)
- Docker-based challenge isolation
- Adaptive AI-driven recommendations
- Detailed skill analytics
- Admin panel
- Public deployment
- Expansion to other EGATE departments

These are documented as future work rather than left unaddressed. They are achievable extensions once the cybersecurity track is stable.

## Technology Stack

| Layer      | Choice                          | Rationale                                      |
|------------|----------------------------------|------------------------------------------------|
| Frontend   | HTML/CSS/JS or lightweight React | Fast to build; no need for heavier tooling     |
| Backend    | Python (Flask)                   | Existing familiarity; fast to set up           |
| Database   | SQLite                           | No server setup required; sufficient for scale |

## Development Timeline (Guideline)

### Week 1: Core Platform
| Day | Focus                 | Key Deliverables |
|-----|-----------------------|------------------|
| 1   | Setup & Planning      | Project structure, repo, spec |
| 2   | Backend               | Flask app, database models |
| 3   | Authentication        | Registration, login, sessions |
| 4   | Challenge Engine      | Challenge model, flag validation |
| 5   | Challenge Content     | 8–10 original challenges |
| 6   | Leaderboard & Points  | Scoring, leaderboard page |
| 7   | Buffer / Catch-Up     | Resolve outstanding issues |
| 8   | AI Hint               | Chat-based hint feature integrated into the challenge view |
| 9   | Learning Path Page    | Curated links to TryHackMe, picoCTF, and other platforms by topic/difficulty |
| 10  | Security Pass         | Input validation, access control checks, password handling review |
| 11  | Buffer / Catch-Up     | Resolve outstanding issues; polish only after core MVP is stable |
| 12  | Testing               | Manual test pass across registration, submissions, leaderboard, hint assistant, and links |
| 13  | Documentation         | README covering setup, features implemented, and future work |
| 14  | Presentation Prep     | Slide deck (8–10 slides) and rehearsed live demo |

### Week 2: AI Hint, Learning Path, Testing, Documentation
(Days 8–14 as above)

## Priority Order

To ensure a working deliverable regardless of pace, features are grouped by priority:

### Must Have
1. Login / registration
2. Challenges with flag submission
3. Points and leaderboard
4. 8–10 original challenges

### Should Have
5. AI hint assistant
6. Learning path / external platform links

### Stretch Goals (Documented as future work if not completed)
7. Docker-based challenge isolation
8. Skill analytics and adaptive recommendations
9. Admin panel
10. Live deployment

## Demonstration Scenario
The final demo will walk through a complete user journey:
A user registers, opens a challenge, submits an incorrect flag, requests a hint from the AI assistant, solves the challenge, and sees their score update on the leaderboard. From there, they visit the learning path page to continue practicing on TryHackMe or picoCTF.

This scenario demonstrates every core feature of the platform in a single, coherent walkthrough.

## Future Work
The following are natural next steps beyond this two-week cycle:
- Expansion to other EGATE departments as additional learning tracks on the same platform
- Docker-based sandboxing for interactive/isolated challenges
- Adaptive challenge recommendations based on performance
- Detailed skill-level analytics and progress visualization
- Administrative interface for managing challenges, tracks, and users
- Public deployment for broader access

## Coding Guidelines for AI Assistant
- Use Python Flask for the backend.
- Use SQLite for the database.
- Use HTML/CSS/JS for the frontend (or lightweight React if needed).
- Keep the code simple, clean, and well-commented.
- Use environment variables for secrets (API keys, session secret).
- Never hardcode passwords or API keys.
- Follow secure coding practices: hash passwords, validate inputs, prevent SQL injection and XSS.
- Build incrementally: implement features one at a time, test after each.
- Do not implement out-of-scope features unless explicitly asked.
- Provide clear instructions for how to run the project after each major change.