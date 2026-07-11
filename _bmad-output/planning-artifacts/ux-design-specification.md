---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
inputDocuments: [
  "index.html",
  "style.css",
  "css/variables.css",
  "css/base.css",
  "css/layout.css",
  "css/components.css",
  "css/responsive.css"
]
lastStep: 14
---

# UX Design Specification — Christian-sCV Mobile App-Like Experience

**Author:** Sally (UX Designer) & Christian
**Date:** 2026-07-11

---

## 1. Executive Summary & Project Vision

### Project Vision
To transform Christian's personal CV website into a premium, app-like mobile experience. The design will mimic a native mobile application (with bottom navigation, sticky headers, and touch-optimized layout patterns) while retaining a clean, professional aesthetic tailored for hiring managers at Maya.

### Target Users
- **Primary Audience:** Hiring managers, recruiters, and R&D team leads at Maya (Fintech/R&D).
- **User Behaviors:** Typically browsing on mobile devices. They need fast navigation, clear readability of technical projects, and easy access to contact information.

### Key Design Challenges
- **Navigation Ergonomics:** Top scrollable navigation on mobile can feel clunky and desktop-oriented.
- **Content Density:** Showing extensive text (like the queueing theory and LP/IP models) on a small screen without overwhelming the user.
- **App-like Feel:** Making a single-page scrolling website feel like a structured mobile app without using heavy JS frameworks.

### Design Opportunities
- **Bottom Navigation Bar:** Placing navigation tabs at the thumb-zone bottom for an instant native app feel.
- **Card UI & Visual Hierarchy:** Using rounded card components with soft shadows and clear visual hierarchy for experiences, skills, and projects.
- **Sticky Actions:** Floating action button (FAB) or sticky header action for quick email/LinkedIn outreach.

---

## 2. Core User Experience

### 2.1 Defining Experience
**Instant Section Switching via Thumb-Optimized Navigation**. The primary visual focus is to shift the user's perception of the mobile site from a standard website to a native app. This is achieved by anchoring a dedicated Bottom Tab Bar to the screen's footer and transforming standard layout dividers into distinct rounded card compartments.

### 2.2 User Mental Model
Hiring managers at Maya are accustomed to mobile banking and productivity apps (Maya, Notion, Slack). They expect to tap icons at the bottom of the screen to move between core views. They also expect summaries with the option to expand details rather than wading through long walls of text.

### 2.3 Success Criteria
- **Zero Lateral Clipping:** All sections fit the viewport precisely.
- **Visual Feedback:** The active navigation tab is visually distinct (highlighted color or bold text).
- **Outreach Velocity:** Getting from the landing state to initiating a call or sending an email takes less than 3 seconds.

### 2.4 Novel UX Patterns
- **HTML5 native details/summary components** styled as custom expandable card blocks on mobile to collapse detailed experience descriptions until clicked. This avoids loading any JS libraries.

### 2.5 Experience Mechanics
1. **Initiation:** User loads the page on mobile and is greeted by a clean sticky app-style header and a bottom navigation menu with clear labels.
2. **Interaction:** Tapping a tab triggers smooth scrolling directly to that section while the bottom menu remains pinned to the bottom.
3. **Feedback:** Tapping a tab highlights the icon/label. Expandable cards expand with smooth CSS transitions when tapped.
4. **Completion:** Contact buttons in the header open mailto/social profiles in their respective native applications.

---

## 3. Desired Emotional Response

### Primary Emotional Goals
- **Confidence & Trust:** Christian should be perceived as a top-tier, details-oriented Applied Research Scientist. The interface should feel structured and precise, reflecting mathematical rigor.
- **Efficiency & Relief:** Recruiter finds the information they want (e.g., "Queueing Theory", "Scheduling Optimization") immediately, without scanning a generic document.

### Emotional Journey Mapping
- **Initial Landing:** Surprise and delight at the app-like visual structure on a mobile phone.
- **Scanning Sections:** Feeling of control and efficiency via clear bottom-navigation tabs.
- **Initiating Contact:** Sense of ease and readiness to connect due to highly visible actions.

### Micro-Emotions
- **Trust vs. Skepticism:** Addressed by high-quality typography, clear section layouts, and professional spacing.
- **Accomplishment vs. Frustration:** Avoid scrolling fatigue by modularizing text into cards and clean hierarchy.

### Design Implications
- **Confidence** → Clean base typography, crisp borders, and a monochromatic color scheme accented by a primary branding color.
- **Efficiency** → Clear typography scaling, sticky header with quick action items.

### Emotional Design Principles
1. **Details Matter:** Alignment, fonts, and micro-padding should look pixel-perfect, conveying research-level precision.
2. **Zero Layout Shifts:** Content should load and settle cleanly without jumping around.
3. **Intentional Transitions:** Simple hover/active states that give physical tactile feedback on mobile tap.

---

## 4. UX Pattern Analysis & Inspiration

### Inspiring Products Analysis
- **Spotify & LinkedIn Mobile:** The bottom tab bar pattern is standard across top-tier mobile interfaces. It is highly ergonomic, keeping all sections within easy reach of the thumb.
- **Notion Mobile:** Content is nested and framed in flat card structures with soft light borders, separating dense textual details neatly.
- **Fintech (Maya/GCash):** Clean rounded modules, simple toggle switches, and a distinct primary brand color to draw the user's eye to high-priority sections.

### Transferable UX Patterns
- **Fixed Tab Bar (Navigation):** Lock a navigation bar to the bottom of the viewport (`position: fixed; bottom: 0`).
- **Collapsible Detail Disclosures (Interactions):** Simple CSS accordion or native `<details>` element for project summaries so that mobile users only read details of what they tap.
- **Soft Border/Elevation Cards (Visuals):** Grouping each experience block into a clean card (`border: 1px solid var(--border); border-radius: 12px`).

### Anti-Patterns to Avoid
- **Top Hamburger Menu:** Hides important links behind a click and requires stretching the thumb to the top corner.
- **Tiny Touch Targets:** Text links close together cause fat-finger errors; we need buttons/tabs that are at least 48px high.
- **Infinite Vertical Wall of Text:** Avoid overwhelming mobile readers; group information logically and use collapses/accords.

### Design Inspiration Strategy
- **Adopt:** Bottom navigation bar for core CV sections; rounded card container layouts.
- **Adapt:** Use HTML `<details>` and `<summary>` tags for expandable section blocks to avoid heavy JS for accordion transitions.
- **Avoid:** Do not hide navigation. Keep bottom nav persistent. Do not use complex overlays that interrupt reading.

---

## 5. Design System Foundation

### 5.1 Design System Choice
**Custom Token-Based Design System (Vanilla CSS Variables & CSS Utility Classes)**.

### Rationale for Selection
- **Sticking with Current Tech Stack:** Eliminates library load overhead (no JS files required) and utilizes the browser's native CSS engine.
- **Uniqueness and Control:** Allows us to craft the exact visual details of the bottom nav and header components.
- **Zero Build Step:** Changes can be applied directly to CSS and HTML files, simplifying deployments.

### Implementation Approach
- Use and expand the existing CSS variables located in `css/variables.css`.
- Define spacing units (`--space-xs`, `--space-sm`, `--space-md`, etc.) and borders/corners (`--radius-sm`, `--radius-md`).
- Define mobile-specific styles in `css/responsive.css` to build bottom nav, sticky header, and card layouts when screen width is under 768px.

### Customization Strategy
- Implement utility class mappings for cards (`.card`), headers, and bottom nav elements.
- Style buttons and anchors to have a minimum touch footprint of `48px` on mobile, aligning with web accessibility standards (WCAG).

---

## 6. Visual Design Foundation

### Color System
We will stick with the existing Notion-inspired color palette for consistency:
- **Primary Text:** Near-black (`#191919`)
- **Body Copy:** Dark gray (`#333333`)
- **Surfaces:** Clean White (`#FFFFFF`) background, warm light gray (`#F7F6F3`) for layout containers and cards.
- **Borders:** Thin light gray (`#E3E2E0`).
- **Accent Active Tab:** Deep charcoal or black background to clearly indicate the selected tab.

### Typography System
Primary font is **Lato** for headings/body, and **Roboto Mono** for badges/skills to maintain high legibility. On mobile:
- **Page Titles / h1:** Rescaled to `24px` for tight screen boundaries.
- **Section Headings / h2:** Rescaled to `18px`.
- **Card Headings / h3:** Rescaled to `15px`.
- **Body Text:** Spanning `14px` with a line height of `1.5` for comfortable reading in mobile views.

### Spacing & Layout Foundation
- **Base Grid:** Built on an 8px grid system.
- **Margins & Paddings:** Standardized mobile container padding of `16px` on the sides, maximizing real estate while keeping text off the edges.
- **Bottom Navigation Height:** Fixed at `60px` to give ample space for touch interactions (thumb-zone) without blocking too much content.

### Accessibility Considerations
- Minimum tap target of `48px` height for all bottom navigation links and buttons.
- Direct contrast ratio compliance of 4.5:1 minimum on all text blocks.
- Screen readers mapping preserved.

---

## 7. Component Strategy & CSS Plan

### 7.1 Component: Sticky App Header
- **Structure:** Pinned to top of viewport (`position: fixed; top: 0; left: 0; width: 100%`) only on screens `< 768px`.
- **Content:** Christian's profile icon, name, and Quick Action buttons (Gmail, LinkedIn, GitHub icons in a compact format).
- **CSS Rules:**
  ```css
  .app-header {
    display: none;
  }
  @media (max-width: 768px) {
    .app-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 56px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0 16px;
      z-index: 1000;
    }
  }
  ```

### 7.2 Component: Pinned Bottom Tab Bar
- **Structure:** Replaces the desktop top navbar (`.site-nav`) on screens `< 768px`. Pinned to the bottom (`position: fixed; bottom: 0; left: 0; width: 100%`).
- **Layout:** Flex layout with evenly distributed items (`flex: 1`).
- **Icons:** Minimal SVG icons for each primary section (Home, Exp, Research, Skills, Projects, Talks).
- **CSS Rules:**
  ```css
  @media (max-width: 768px) {
    .site-nav {
      position: fixed;
      bottom: 0;
      top: auto;
      left: 0;
      width: 100%;
      height: 60px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--border);
      border-bottom: none;
      z-index: 1000;
    }
    .site-nav ul {
      display: flex;
      justify-content: space-around;
      align-items: center;
      height: 100%;
      max-width: none;
      padding: 0;
    }
    .site-nav a {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 10px;
      font-weight: 600;
      padding: 6px 0;
      margin: 0;
      color: var(--text-muted);
    }
    .site-nav a svg {
      width: 20px;
      height: 20px;
      margin-bottom: 2px;
    }
  }
  ```

### 7.3 Component: Expandable Experience & Project Cards
- **Structure:** Wrap the `desc` content inside HTML `<details>` and `<summary>` elements to create collapsible panels on mobile, preserving full text for desktop.
- **CSS Rules:**
  ```css
  @media (max-width: 768px) {
    details summary {
      cursor: pointer;
      list-style: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 700;
      padding: 12px 16px;
      background: var(--bg-secondary);
      border-radius: 8px;
    }
    details summary::-webkit-details-marker {
      display: none;
    }
  }
  ```
