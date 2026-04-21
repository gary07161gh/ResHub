# AGENTS.md

This file helps AI coding agents understand the Resolution Hub project.

## Project Overview

Resolution Hub is a single-page web application for managing customer resolution cases. It's built as a standalone HTML file with embedded React code, using CDN libraries for React, Tailwind CSS, and Babel for in-browser JSX compilation.

## Technologies

- React 18 (via CDN)
- Tailwind CSS (via CDN)
- Babel for JSX compilation
- localStorage for data persistence

## Running the Application

Open `Resolution Hub.html` in a modern web browser. No build process or server required.

## Key Features

- Dashboard with KPI cards and donut chart
- Case management with statuses: Open, Customer Responded, Child Resolved, Hold - In Progress, 8 Week Letter Due, Closed
- Categories: Uncategorized, Billing, Technical Issue, Customer Service, Metering
- Search and filter cases
- Table and Kanban views
- Detailed case view with notes, actions, history, subtasks, and links
- Import/export data as JSON
- Dark mode support
- Personal tasks

## Code Structure

The entire application is contained in a single HTML file with inline JavaScript. Key components include:

- App: Main component with state management
- DonutChart: Visual representation of case statuses
- ActionBlock: Reusable component for notes and actions
- Various utility functions for data handling

## Data Model

Cases are stored in localStorage with the following structure:

- id, caseNumber, accountNumber, contactName, contactNumber, email, siteAddress
- status, category, holdUntilDate, creationDate
- notes, latestAction, nextAction
- subTasks, links, history

## Conventions

- Use React hooks for state management
- Memoize expensive computations
- Use localStorage for persistence
- Follow Tailwind CSS classes for styling
- Dark mode support with conditional classes

## Development

Since it's a single file, edit the HTML directly. Changes are reflected immediately on refresh.

No tests or build scripts.</content>
<parameter name="filePath">c:\Users\Gary0\Desktop\Coding\ResHub\AGENTS.md